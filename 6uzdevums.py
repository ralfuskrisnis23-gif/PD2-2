# Label; MountPoint; TotalSize (MB); Used (%)
partitions = [
"System;/;50000;85",
"Data;/home;150000;40",
"Cache;/tmp;5000;10",
"Backup;/mnt/backup;500000;92",
"USB-Drive;/media/usb;16000;0",
"Logs;/var/log;10000;95",
"Database;/var/lib/mysql;80000;70",
"Shared;/mnt/shared;200000;15",
"Win-System;/mnt/win;100000;90",
"Recovery;/recovery;2000;98"
]

def used_mb_report(partitions_list):
    result = []

    for p in partitions_list:
        fields = p.split(";")

        label = fields[0]
        total_mb = int(fields[2])
        used_percent = int(fields[3])

        used_fraction = used_percent / 100
        used_mb = total_mb * used_fraction
        used_mb_int = int(used_mb)

        item = {"Label": label, "UsedMB": used_mb_int}
        result.append(item)

    return result

report = used_mb_report(partitions)

for item in report:
    print(item)

print("Pārbaude Cache (jābūt 500):")
for item in report:
    if item["Label"] == "Cache":
        print(item["UsedMB"])
