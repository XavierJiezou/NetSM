from netsm import __version__
from netsm.core import NetSM
from rich.table import Table
from rich.live import Live
from rich import box
import fire


def generate_table() -> Table:
    table = Table(header_style="bold magenta", box=box.SIMPLE_HEAVY)
    columns = ['#', 'NIC', 'IPv4', 'Download', 'Upload']
    styles = ['cyan', 'blue', 'red', 'green', 'yellow']
    for column, style in zip(columns, styles):
        table.add_column(header=column, style=style)
    netsm = NetSM()
    addrs = netsm.addrs
    speed = netsm.speed
    idx = 0
    for nic in addrs:
        speed_sent = speed[nic]['speed_sent']
        speed_recv = speed[nic]['speed_recv']
        if speed_sent == speed_recv == '0.0 KB/s':
            pass
        else:
            table.add_row(
                str(idx),
                nic,
                addrs[nic]['address'],
                f':arrow_down_small: {speed_recv}',
                f':arrow_up_small: {speed_sent}'
            )
            idx += 1
    return table


class NetSMCLI:
    def __init__(self):
        pass

    def show(self) -> None:
        """Shows information about networks.

        Returns:
            str: Information for networks.
        """
        with Live(generate_table()) as live:
            while True:
                try:
                    live.update(generate_table())
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
