# Shell Scripting Cheat Sheet

Ez a cheat sheet a **shell scripting** alapjait és leggyakoribb parancsait foglalja össze.

---
##  Script

```bash
#!/bin/bash
```

* Jelez a rendszernek, hogy a script Bash-ben fusson.

---

## 🗂️ Fájlkezelés

| Parancs | Leírás                                | Példa                                 |
| ------- | ------------------------------------- | ------------------------------------- |
| `ls`    | Könyvtár tartalmának listázása        | `ls -l`                               |
| `cd`    | Könyvtár váltás                       | `cd /elérési/útvonal`                 |
| `pwd`   | Aktuális könyvtár megjelenítése       | `pwd`                                 |
| `cp`    | Fájl/könyvtár másolása                | `cp forras.txt cel.txt`               |
| `mv`    | Fájl mozgatása/átnevezése             | `mv regi.txt uj.txt`                  |
| `rm`    | Fájl/könyvtár törlése                 | `rm fajl.txt`                         |
| `touch` | Fájl létrehozása/időbélyeg frissítése | `touch ujfajl.txt`                    |
| `chmod` | Jogosultságok módosítása              | `chmod 755 script.sh`                 |
| `tar`   | Archiválás/kicsomagolás               | `tar -czvf archiv.tar.gz /elérési/út` |
| `df`    | Lemezhasználat megtekintése           | `df -h`                               |
| `du`    | Könyvtár/fájl méret ellenőrzés        | `du -sh /elérési/út`                  |

---

## ⚙️ Folyamatok és erőforrások

| Parancs | Leírás                       | Példa    |
| ------- | ---------------------------- | -------- |
| `ps`    | Futó folyamatok listázása    | `ps aux` |
| `top`   | Valós idejű folyamatfigyelés | `top`    |

---

## 🌐 Hálózat és adatátvitel

| Parancs | Leírás                         | Példa                             |
| ------- | ------------------------------ | --------------------------------- |
| `curl`  | Adatlekérés API-tól/szerverről | `curl https://api.pelda.com`      |
| `wget`  | Fájl letöltése                 | `wget https://pelda.com/fajl.zip` |

---

## 🔍 Szövegfeldolgozás

| Parancs | Leírás                           | Példa                         |
| ------- | -------------------------------- | ----------------------------- |
| `grep`  | Mintakeresés fájlban             | `grep "keresett" fajl.txt`    |
| `awk`   | Szöveg feldolgozás, mintakeresés | `awk '{ print $1 }' fajl.txt` |
| `sed`   | Szöveg módosítása                | `sed 's/regi/uj/g' fajl.txt`  |

---

## ✏️ Szövegszerkesztők

| Szerkesztő | Leírás                        | Példa             |
| ---------- | ----------------------------- | ----------------- |
| `nano`     | Egyszerű CLI szerkesztő       | `nano script.sh`  |
| `vim`      | Haladó, erőteljes szerkesztő  | `vim script.sh`   |
| `gedit`    | Grafikus szerkesztő GNOME-hoz | `gedit script.sh` |

---

## 🛠️ Haladó shell funkciók

**Változók**

```bash
NAME="Adam"
echo "Hello, $NAME"
```

**Feltételek**

```bash
if [ -f "fajl.txt" ]; then
    echo "A fájl létezik"
fi
```

**Ciklusok**

```bash
for i in 1 2 3; do
    echo "Szám: $i"
done
```

**Függvények**

```bash
greet() {
    echo "Hello, $1"
}
greet "Világ"
```

**Hibakezelés**

```bash
set -e   # Kilép, ha bármelyik parancs hibát jelez
```

---
# PowerShell Cheat Sheet

Ez a cheat sheet a **PowerShell** alapjait és leggyakoribb parancsait foglalja össze.

---

##  Script indítás

Windows rendszeren általában nem szükséges, de `.ps1` fájlok futtatásához:

```powershell
# PowerShell script file: script.ps1
```

* PowerShell promptból futtatható: `.\script.ps1`

---

## 🗂️ Fájlkezelés

| Parancs         | Leírás                          | Példa                                         |
| --------------- | ------------------------------- | --------------------------------------------- |
| `Get-ChildItem` | Könyvtár tartalmának listázása  | `Get-ChildItem -Path C:\Users`                |
| `Set-Location`  | Könyvtár váltás                 | `Set-Location C:\Users`                       |
| `Get-Location`  | Aktuális könyvtár megjelenítése | `Get-Location`                                |
| `Copy-Item`     | Fájl/könyvtár másolása          | `Copy-Item C:\source.txt C:\dest.txt`         |
| `Move-Item`     | Fájl mozgatása/átnevezése       | `Move-Item C:\regi.txt C:\uj.txt`             |
| `Remove-Item`   | Fájl/könyvtár törlése           | `Remove-Item C:\fajl.txt`                     |
| `New-Item`      | Fájl vagy könyvtár létrehozása  | `New-Item -Path C:\ujfajl.txt -ItemType File` |
| `Get-Content`   | Fájl tartalmának megtekintése   | `Get-Content C:\fajl.txt`                     |
| `Set-Content`   | Fájl tartalmának írása          | `Set-Content C:\fajl.txt "Új tartalom"`       |

---

## ⚙️ Folyamatok és erőforrások

| Parancs         | Leírás                    | Példa                          |
| --------------- | ------------------------- | ------------------------------ |
| `Get-Process`   | Futó folyamatok listázása | `Get-Process`                  |
| `Stop-Process`  | Folyamat leállítása       | `Stop-Process -Name notepad`   |
| `Get-Service`   | Szolgáltatások listázása  | `Get-Service`                  |
| `Start-Service` | Szolgáltatás indítása     | `Start-Service -Name wuauserv` |
| `Stop-Service`  | Szolgáltatás leállítása   | `Stop-Service -Name wuauserv`  |

---

## 🌐 Hálózat és adatátvitel

| Parancs             | Leírás                   | Példa                                                                 |
| ------------------- | ------------------------ | --------------------------------------------------------------------- |
| `Invoke-WebRequest` | Fájl vagy adat letöltése | `Invoke-WebRequest -Uri https://pelda.com/fajl.zip -OutFile fajl.zip` |
| `Invoke-RestMethod` | API hívás JSON adatokkal | `Invoke-RestMethod -Uri https://api.pelda.com`                        |
| `Test-Connection`   | Ping parancs             | `Test-Connection google.com`                                          |

---

## 🔍 Szövegfeldolgozás

| Parancs         | Leírás               | Példa                                                 |                                |
| --------------- | -------------------- | ----------------------------------------------------- | ------------------------------ |
| `Select-String` | Mintakeresés fájlban | `Select-String -Pattern "keresett" -Path C:\fajl.txt` |                                |
| `Sort-Object`   | Lista rendezése      | `Get-Process                                          | Sort-Object CPU -Descending`   |
| `Where-Object`  | Feltételes szűrés    | `Get-Process                                          | Where-Object {$_.CPU -gt 100}` |

---

## ✏️ Szövegszerkesztők / Szerkesztés

PowerShell script fájlok szerkeszthetők:

| Eszköz    | Leírás                      | Példa                |
| --------- | --------------------------- | -------------------- |
| `notepad` | Egyszerű szerkesztő         | `notepad script.ps1` |
| `VSCode`  | Haladó, grafikus szerkesztő | `code script.ps1`    |

---

## 🛠️ Haladó PowerShell funkciók

**Változók**

```powershell
$nev = "Adam"
Write-Output "Hello, $nev"
```

**Feltételek**

```powershell
if (Test-Path "C:\fajl.txt") {
    Write-Output "A fájl létezik"
}
```

**Ciklusok**

```powershell
for ($i=1; $i -le 3; $i++) {
    Write-Output "Szám: $i"
}

foreach ($item in 1..3) {
    Write-Output $item
}
```

**Függvények**

```powershell
function Greet($nev) {
    Write-Output "Hello, $nev"
}
Greet "Világ"
```

**Hibakezelés**

```powershell
try {
    Remove-Item "C:\nemletezo.txt"
} catch {
    Write-Output "Hiba történt: $_"
}
```

---
