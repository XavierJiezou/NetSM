import psutil
import time


class NetSM:
    def __init__(self):
        pass

    @property
    def addrs(self):
        addrs = {}
        netad = psutil.net_if_addrs()
        for nic in netad:
            addrs[nic] = {}
            if len(netad[nic]) == 1:
                addrs[nic]['family'] = netad[nic][0].family.name
                addrs[nic]['address'] = netad[nic][0].address
            else:
                for snicaddr in netad[nic]:
                    if snicaddr.family.name == 'AF_INET':
                        addrs[nic]['family'] = snicaddr.family.name
                        addrs[nic]['address'] = snicaddr.address
                        break
        return addrs

    def __format__(self, speed: float):
        speed /= 1024
        if speed < 1e2:
            return f'{speed:.1f} KB/s'
        elif speed < 1e3:
            return f'{int(speed)} KB/s'
        else:
            return f'{speed/1024:.1f} MB/s'

    @property
    def speed(self, interval: float = 1.):
        t1 = time.time()
        netio = psutil.net_io_counters(pernic=True)
        old_bytes = {
            nic: {
                'bytes_sent': netio[nic].bytes_sent,
                'bytes_recv': netio[nic].bytes_recv
            } for nic in netio
        }

        time.sleep(interval)

        t2 = time.time()
        netio = psutil.net_io_counters(pernic=True)
        new_bytes = {
            nic: {
                'bytes_sent': netio[nic].bytes_sent,
                'bytes_recv': netio[nic].bytes_recv
            } for nic in netio
        }

        speed = {
            nic: {
                'speed_sent': self.__format__((new_bytes[nic]['bytes_sent']-old_bytes[nic]['bytes_sent'])/(t2-t1)),
                'speed_recv': self.__format__((new_bytes[nic]['bytes_recv']-old_bytes[nic]['bytes_recv'])/(t2-t1))
            } for nic in new_bytes
        }
        return speed


if __name__ == '__main__':
    import json
    print(json.dumps(NetSM().speed, indent=2, ensure_ascii=False))
