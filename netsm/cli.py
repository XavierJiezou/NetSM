from netsm import __version__
from netsm.core import NetSM
from rich.table import Table
from rich.live import Live
from rich import box
import fire


def generate_table(netsm: NetSM) -> Table:
    table = Table(header_style="bold magenta", box=box.SIMPLE_HEAVY)
    columns = ['#', 'NIC', 'IPv4', 'Download', 'Upload']
    styles = ['cyan', 'blue', 'red', 'green', 'yellow']
    for column, style in zip(columns, styles):
        table.add_column(header=column, style=style)
    addrs = netsm.addrs
    speed = netsm.speed()
    idx = 0
    for nic in addrs:
        nic_speed = speed.get(nic)
        if nic_speed is None:
            continue
        speed_sent = nic_speed['speed_sent']
        speed_recv = nic_speed['speed_recv']
        if speed_sent == speed_recv == '0.0 KB/s':
            continue
        table.add_row(
            str(idx),
            nic,
            addrs[nic].get('address', 'N/A'),
            f':arrow_down_small: {speed_recv}',
            f':arrow_up_small: {speed_sent}'
        )
        idx += 1
    return table


class NetSMCLI:
    def __init__(self):
        """Initialization
        """
        pass

    def show(self, incessant: bool = True) -> None:
        """Shows information about networks.

        Args:
            incessant (bool, optional): Whether it is always displayed on the console. Defaults to True.
        """
        netsm = NetSM()
        table = generate_table(netsm)
        with Live(table) as live:
            if incessant:
                while True:
                    try:
                        live.update(generate_table(netsm))
                    except KeyboardInterrupt:
                        return

    def version(self) -> str:
        """Shows the version of the project.

        Returns:
            str: Version of the project.
        """
        return __version__


def main():
    fire.Fire(NetSMCLI)


if __name__ == '__main__':
    main()
