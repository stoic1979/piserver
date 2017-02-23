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

    Scanning requires root permission to see all the networks.

    Each cell object should have the following attributes:
     + ssid
     + signal
     + quality
     + frequency
     + bitrates
     + encrypted
     + channel
     + address
     + mode
    """
    ssids = []

    try:

        # NOTE: if you cant get list of ssids,
        # probably, you will need to specify appropriate dev name
        cells = Cell.all(dev)

        for cell in cells:
            ssids.append(cell.ssid)

    except Exception as exp:
        print "get_wifis() got exception:", exp

    return ssids

if __name__ == "__main__":
    print get_wifis('wlp3s0') # used this on my laptop
    #print get_wifis()          # used this on pi

