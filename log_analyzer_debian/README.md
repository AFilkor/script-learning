# SSH Log Analyzer

Ez a Python script segít elemezni a Linux SSH naplókat, hogy könnyen áttekintsd a sikertelen bejelentkezési próbálkozásokat.

## Mit csinál?

* Lekéri az SSH naplókat a systemd journalból:

  ```bash
  sudo journalctl -u ssh > auth.log
  ```
* Keres a naplóban hibás bejelentkezéseket:

  * "Failed password"
  * "Invalid user"
  * "Connection closed by ... [preauth]"
* Összesíti a próbálkozásokat IP-címek szerint
* Kimenetet ment CSV formátumban (`report.csv`)

## Fájlstruktúra

```
.
├── analyze.py      # A fő Python script
└── README.md       # Ez a dokumentum
```

## Használat

1. Klónozd a repót:

```bash
git clone https://github.com/<user>/ssh-log-analyzer.git
cd ssh-log-analyzer
```

2. Futtasd a scriptet:

```bash
python3 analyze.py
```

Ez létrehozza az `auth.log` fájlt és a `report.csv` riportot.

3. Nézd meg az eredményt:

```bash
column -s, -t < report.csv
```

## Példa a riportból

```
IP               Attempts   Last Attempt           Types
192.168.100.19    3        2025-08-26 19:48:52   Connection closed
5.188.10.33      12        2025-08-26 04:21:11   Failed password, Invalid user
```

## Követelmények

* Python 3.8+
* Linux (Debian/Ubuntu ajánlott)
* journalctl elérhető legyen

##
