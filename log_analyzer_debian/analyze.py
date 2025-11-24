#!/usr/bin/env python3
import re
import csv
import subprocess
from datetime import datetime

AUTH_LOG = "auth.log"

# Regexek különféle SSH sikertelen kísérletekhez:
FAILED_PASSWORD = re.compile(
    r"Failed password for (invalid user )?(\S+) from ([0-9\.]+) port (\d+)"
)

INVALID_USER = re.compile(
    r"Invalid user (\S+) from ([0-9\.]+)"
)

PREAUTH = re.compile(
    r"Connection closed by (\S+) port (\d+) \[preauth\]"
)


def generate_auth_log():
    print("[+] auth.log generálása journalból...")
    try:
        subprocess.run(
            ["sudo", "journalctl", "-u", "ssh", "--no-pager"],
            stdout=open(AUTH_LOG, "w"),
            check=True
        )
        print("[+] auth.log kész.")
    except Exception as e:
        print("[!] Hiba journal kiolvasáskor:", e)
        exit(1)


def parse_log():
    print("[+] Log elemzése...")
    results = {}

    with open(AUTH_LOG, "r", errors="ignore") as f:
        for line in f:
            # Timestamp első három mező
            try:
                timestamp_str = " ".join(line.split()[0:3])
                timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
            except:
                continue

            # 1) Failed password
            m1 = FAILED_PASSWORD.search(line)
            if m1:
                ip = m1.group(3)
                results.setdefault(ip, []).append(("Failed password", timestamp))
                continue

            # 2) Invalid user
            m2 = INVALID_USER.search(line)
            if m2:
                ip = m2.group(2)
                results.setdefault(ip, []).append(("Invalid user", timestamp))
                continue

            # 3) Connection closed (preauth)
            m3 = PREAUTH.search(line)
            if m3:
                ip = m3.group(1)
                results.setdefault(ip, []).append(("Connection closed", timestamp))
                continue

    return results


def save_report(results):
    print("[+] Report mentése report.csv néven...")

    with open("report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Attempts", "Last Attempt", "Types"])

        for ip, attempts in results.items():
            last_time = max(a[1] for a in attempts)
            types = ", ".join(set(a[0] for a in attempts))

            writer.writerow([
                ip,
                len(attempts),
                last_time.strftime("%Y-%m-%d %H:%M:%S"),
                types
            ])

    print("[+] Kész!")


def main():
    generate_auth_log()
    results = parse_log()
    save_report(results)

    print(f"[+] Összes gyanús IP: {len(results)}")


if __name__ == "__main__":
    main()
