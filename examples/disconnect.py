# win32wifi - Windows Native Wifi Api Python library.
# Copyright (C) 2016 - Shaked Gitelman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Shaked Gitelman   (almondg)   <shaked.dev@gmail.com>
#

import sys


from win32wifi.Win32Wifi import getWirelessInterfaces
from win32wifi.Win32Wifi import getWirelessAvailableNetworkList
from win32wifi.Win32Wifi import disconnect

if __name__ == "__main__":
    ifaces = getWirelessInterfaces()
    print(ifaces)
    print(len(ifaces))
    for iface in ifaces:
        disconnect(iface)
        print(iface)
        guid = iface.guid
        networks = getWirelessAvailableNetworkList(iface)
        print()
        for network in networks:
            print(network)
            print("-" * 20)
        print()
