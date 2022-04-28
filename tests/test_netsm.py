from netsm import __version__
from netsm.core import NetSM
import toml


def test_version():
    data = toml.load('pyproject.toml')
    version = data['tool']['poetry']['version']
    assert __version__ == version


def test_netsm():
    netsm = NetSM()
    speed = netsm.speed
    addrs = netsm.addrs
    assert len(speed) == len(addrs)


def test_format():
    netsm = NetSM()
    for i in range(100):
        speed = 1024*i
        assert 8 <= len(netsm.__format__(speed)) <= 9
    for i in range(100, 1000):
        speed = 1024*i
        assert len(netsm.__format__(speed)) == 8
    for i in range(1000, int(1e5)):
        speed = 1024*i
        assert 'M' in netsm.__format__(speed)
