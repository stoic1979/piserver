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

    # NOTE: if you cant get list of ssids,
    # probably, you will need to specify appropriate dev name
    cells = Cell.all(dev)

    for cell in cells:
        ssids.append(cell.ssid)

    return ssids

if __name__ == "__main__":
    #print get_wifis('wlp3s0') # used this on my laptop
    print get_wifis()          # used this on pi

