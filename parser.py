import struct
import sys
from os import path


def main(firmware_path):
    if not path.isfile(firmware_path):
        raise FileNotFoundError(firmware_path)

    name, extension = path.splitext(firmware_path)

    with open(firmware_path, "rb") as firmware_file:
        n = firmware_file.read(4)[3]
        partitions = list()

        for _ in range(n):
            address = struct.unpack('<i', firmware_file.read(4))[0]
            size = struct.unpack('<i', firmware_file.read(4))[0]
            partitions.append(dict(address=address, size=size))

        commands = "\
            \npip install esptool\
            \npython -m esptool --port <PORT> erase_flash\
            \npython -m esptool --port <PORT> write_flash"

        for i in range(n):
            partition_path = f"{name}_PART{i}_{hex(partitions[i]["address"])}{extension}"

            with open(partition_path, "wb") as partition_file:
                partition_file.write(firmware_file.read(partitions[i]['size']))
                commands += f" {hex(partitions[i]["address"])} {partition_path}"

        print("To flash your device run set of commands in current directory (replace <PORT> with real one, e.g. COM3):")
        print(commands)


if __name__ == "__main__":
    main(sys.argv[1])
