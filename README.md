# Shell Scripting Cheat Sheet

Ez a cheat sheet a **shell scripting** alapjait és leggyakoribb parancsait foglalja össze, automatizálás, rendszeradminisztráció és DevOps feladatokhoz.

---

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
