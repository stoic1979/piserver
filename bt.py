#
# script to fetch list of bluetooth devices and connect to them
#

from bluetooth import *


def get_bluetooth_devices():
    names = []
    nearby_devices = discover_devices(lookup_names = True)

    for addr, name in nearby_devices:
        names.append(name)

    return names

if __name__ == "__main__":
    print get_bluetooth_devices()
