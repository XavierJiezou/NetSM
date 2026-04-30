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
            snicaddrs = netad[nic]
            # Prefer AF_INET; fall back to the first available address
            inet_addr = next(
                (s for s in snicaddrs if s.family.name == 'AF_INET'), None
            )
            chosen = inet_addr if inet_addr is not None else (snicaddrs[0] if snicaddrs else None)
            if chosen is not None:
                addrs[nic]['family'] = chosen.family.name
                addrs[nic]['address'] = chosen.address
        return addrs

    def _format_speed(self, speed: float) -> str:
        speed /= 1024
        if speed < 1e2:
            return f'{speed:.1f} KB/s'
        elif speed < 1e3:
            return f'{int(speed)} KB/s'
        else:
            return f'{speed/1024:.1f} MB/s'

    def speed(self, interval: float = 1.) -> dict:
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

        # Only include NICs present in both snapshots to avoid KeyError when
        # an interface comes up or goes down during the sampling interval.
        common_nics = old_bytes.keys() & new_bytes.keys()
        elapsed = t2 - t1
        result = {
            nic: {
                'speed_sent': self._format_speed(
                    (new_bytes[nic]['bytes_sent'] - old_bytes[nic]['bytes_sent']) / elapsed
                ),
                'speed_recv': self._format_speed(
                    (new_bytes[nic]['bytes_recv'] - old_bytes[nic]['bytes_recv']) / elapsed
                )
            } for nic in common_nics
        }
        return result


if __name__ == '__main__':
    import json
    print(json.dumps(NetSM().speed(), indent=2, ensure_ascii=False))
