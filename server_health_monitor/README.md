# Server Health Monitor

Ez egy egyszerű, saját használatra készült Python alapú rendszerfigyelő eszköz Debian (és más Linux) szerverekhez.
A script gyorsan lefut, jól áttekinthető információkat ad, és igény szerint cronból is futtatható.

A cél: **egy könnyű, telepítés nélkül használható szerverállapot-jelentés**, amely megmutatja a gép legfontosabb paramétereit.

---

## Mit mér a script?

### **1. Lemezhasználat**

A `df -h` segítségével listázza:

* partíciók
* foglalt / szabad hely
* százalékos terhelés

### **2. HDD / SSD állapot (SMART)**

A `smartctl` kimenete alapján:

* SMART összegző állapot (PASSED / WARNING / FAILED)
* újraelosztott szektorok (`Reallocated_Sector_Ct`)
* pending / offline uncorrectable szektorok
* power-on hours
* brand és modell információk

### **3. Hőmérsékletek**

Két forrásból:

* HDD/SSD RAW hőmérséklet (`smartctl -A`)
* CPU / alaplap hőmérsékletek (`sensors`, ha elérhető)

### **4. CPU és memória**

* load average (1 / 5 / 15 perc)
* memóriahasználat a `free -h` alapján

### **5. Egyszerű riport generálása**

A futtatás végén elkészül egy jól olvasható szöveges file:

```
server-health-report.txt
```

---

## Telepítési követelmények

A szükséges Linux csomagok:

```
sudo apt install smartmontools lm-sensors
sudo sensors-detect
```

A Python modulok mind beépítettek:

* subprocess
* shutil
* re
* datetime

Nincs szükség pip-es telepítésre.

---

## Használat

Futtatás:

```
python3 monitor.py
```

A script:

* kiír mindent a terminálba
* létrehozza a friss `server-health-report.txt` fájlt

---

## Automatizálás (cron)

Naponta egyszeri futtatáshoz:

```
crontab -e
```

Majd:

```
0 6 * * * /usr/bin/python3 /home/user/server-health-monitor/monitor.py
```

---

## Fájlstruktúra

```
.
├── monitor.py
└── README.md
```

---
