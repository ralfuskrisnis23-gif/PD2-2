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

def get_total_size_mb(lines):
    total = 0
    for line in lines:
        fields = line.strip().split(";")

        # Drošība: ja kāda rinda ir bojāta, to izlaiž
        if len(fields) != 4:
            continue

        size_mb = int(fields[2])
        total += size_mb

    return total

total_mb = get_total_size_mb(partitions)
print(total_mb)
