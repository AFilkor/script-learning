#!/usr/bin/env python3
import subprocess
from datetime import datetime
import shutil
import re

REPORT_FILE = "server-health-report.txt"


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return ""


def get_disk_usage():
    return run("df -h --output=source,size,used,avail,pcent,target")


def get_smart_status():
    smart_data = {}
    disks = run("lsblk -nd --output NAME,TYPE").strip().split("\n")

    for line in disks:
        parts = line.split()
        if len(parts) != 2:
            continue
        name, dtype = parts
        if dtype != "disk":
            continue

        dev = f"/dev/{name}"
        info = run(f"sudo smartctl -H {dev}")
        attrs = run(f"sudo smartctl -A {dev}")

        status_match = re.search(r"SMART overall-health self-assessment test result: (.*)", info)
        status = status_match.group(1) if status_match else "Unknown"

        # Try multiple possible SMART temperature fields
        # Match RAW_VALUE temperature (last number before optional parenthesis)
        temp_match = re.search(r"Temperature_Celsius.*?(\d+)\s*(?:\(|$)", attrs) or \
                      re.search(r"Airflow_Temperature_Cel.*?(\d+)", attrs) or \
                      re.search(r"Temperature.*?(\d+)", attrs)
        temp = temp_match.group(1) + " °C" if temp_match else "N/A"

        reall_match = re.search(r"Reallocated_Sector_Ct.*?(\d+)", attrs)
        realloc = reall_match.group(1) if reall_match else "N/A"

        smart_data[dev] = {
            "status": status,
            "temperature": temp,
            "reallocated": realloc,
        }

    return smart_data


def get_temperatures():
    return run("sensors")


def get_cpu_load():
    return run("uptime")


def get_memory():
    return run("free -h")


def write_report(content):
    with open(REPORT_FILE, "w") as f:
        f.write(content)


def generate_report():
    report = []

    report.append("SERVER HEALTH REPORT")
    report.append(f"Generated: {datetime.now()}\n")

    report.append("=== Disk Usage ===")
    report.append(get_disk_usage())

    report.append("=== CPU Load ===")
    report.append(get_cpu_load())

    report.append("=== Memory Usage ===")
    report.append(get_memory())

    report.append("=== HDD / SSD SMART Status ===")
    smart = get_smart_status()
    if not smart:
        report.append("No SMART data available or smartctl missing.\n")
    else:
        for disk, data in smart.items():
            report.append(f"Drive: {disk}")
            report.append(f"  Status: {data['status']}")
            report.append(f"  Temperature: {data['temperature']}")
            report.append(f"  Reallocated sectors: {data['reallocated']}\n")

    report.append("=== Sensors (Temperatures) ===")
    report.append(get_temperatures())

    final = "\n".join(report)
    write_report(final)

    print("[*] Report generated:", REPORT_FILE)


if __name__ == "__main__":
    generate_report()
