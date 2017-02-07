#
# Network Utils
# 
# Features
# ==========
# * scan and gets list of available wifi networks
#

from wifi import Cell, Scheme

def get_wifis(dev='wlan0'):
    """
    function scans wifi nws on given device
    and retuns the list of ssids
    """
    ssids = []
    cells = Cell.all(dev)
    for cell in cells:
        ssids.append(cell.ssid)

    return ssids


if __name__ == "__main__":
    print get_wifis('wlp3s0')

