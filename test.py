windows_io = {
    'Panda': {'bytes_sent': 0, 'bytes_recv': 0}, 
    '以太网': {'bytes_sent': 68003377, 'bytes_recv': 352952835}, 
    'WLAN': {'bytes_sent': 0, 'bytes_recv': 0}, 
    '本地连接* 1': {'bytes_sent': 0, 'bytes_recv': 0}, 
    '以太网 2': {'bytes_sent': 0, 'bytes_recv': 0}, 
    '本地连接* 2': {'bytes_sent': 190998357, 'bytes_recv': 46033570}, 
    'Loopback Pseudo-Interface 1': {'bytes_sent': 0, 'bytes_recv': 0}
}

windows_ad = {
    'Panda': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-FF-26-4B-57-9B', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.20.165', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::972:354d:f9e2:14a5', netmask=None, broadcast=None, ptp=None)], 
    '以太网': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='84-A9-3E-3C-D4-B5', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='10.160.130.113', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::1030:9cb0:1fa9:6a18', netmask=None, broadcast=None, ptp=None)], 
    'WLAN': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='30-24-32-FB-A2-E3', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.205.242', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::4dd7:7deb:bcdf:cdf2', netmask=None, broadcast=None, ptp=None)], 
    '本地连接* 1': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='30-24-32-FB-A2-E4', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.14.22', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::28b9:7d4d:2b24:e16', netmask=None, broadcast=None, ptp=None)], 
    '以太网 2': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-FF-BF-47-87-8C', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.143.144', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::b4d7:81a5:586c:8f90', netmask=None, broadcast=None, ptp=None)], 
    '本地连接* 2': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='32-24-32-FB-A2-E3', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.137.1', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::8cf1:1f6b:8c2f:eb84', netmask=None, broadcast=None, ptp=None)], 
    'Loopback Pseudo-Interface 1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)]
}


linux_io = {
    'eno1': snetio(bytes_sent=84525208237, bytes_recv=165781129476, packets_sent=523417389, packets_recv=610344268, errin=0, errout=0, dropin=0, dropout=0), 
    'eno2': snetio(bytes_sent=1136457649734, bytes_recv=7151087545582, packets_sent=2405570569, packets_recv=5801648446, errin=0, errout=0, dropin=7813580, dropout=0), 
    'lo': snetio(bytes_sent=5033099648848, bytes_recv=5033099648848, packets_sent=778000917, packets_recv=778000917, errin=0, errout=0, dropin=0, dropout=0), 
    'ens4f0': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 
    'ens4f1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 
    'ib1': snetio(bytes_sent=1064538410663, bytes_recv=7022304303140, packets_sent=4618435490, packets_recv=6330419776, errin=0, errout=0, dropin=0, dropout=0), 
    'ib0': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 
    'enp0s20f0u1u6': snetio(bytes_sent=1860848482, bytes_recv=1986393439, packets_sent=16954476, packets_recv=17782707, errin=0, errout=0, dropin=0, dropout=0)
}

linux_ad = {
    'lo': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 10>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:00:00:00:00', netmask=None, broadcast=None, ptp=None)], 
    'eno1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.20.1', netmask='255.255.255.0', broadcast='192.168.20.255', ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::3a68:ddff:fe31:e5f0%eno1', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='38:68:dd:31:e5:f0', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)], 
    'eno2': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='111.115.201.25', netmask='255.255.255.0', broadcast='111.115.201.255', ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::3a68:ddff:fe31:e5f1%eno2', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='38:68:dd:31:e5:f1', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)], 
    'enp0s20f0u1u6': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.95.120', netmask='255.255.255.0', broadcast='169.254.95.255', ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::3868:ddff:fe31:e5f7%enp0s20f0u1u6', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='3a:68:dd:31:e5:f7', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)], 
    'ib1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='172.10.10.1', netmask='255.255.255.0', broadcast='172.10.10.255', ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::e42:a103:60:90a1%ib1', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:19:07:fe:80:00:00:00:00:00:00:0c:42:a1:03:00:60:90:a1', netmask=None, broadcast='00:ff:ff:ff:ff:12:40:1b:ff:ff:00:00:00:00:00:00:ff:ff:ff:ff', ptp=None)], 
    'ens4f0': [snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='b0:26:28:f8:97:6c', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)], 
    'ens4f1': [snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='b0:26:28:f8:97:6d', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)], 
    'ib0': [snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:11:07:fe:80:00:00:00:00:00:00:0c:42:a1:03:00:60:90:a0', netmask=None, broadcast='00:ff:ff:ff:ff:12:40:1b:ff:ff:00:00:00:00:00:00:ff:ff:ff:ff', ptp=None)]
}