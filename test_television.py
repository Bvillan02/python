import pytest
from television import *

def setup_method(self):
    self.tv1 = Television()

def teardown_method(self):
    del self.tv1
def __init__(self):
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'

def power(self):
    self.tv1.power()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume = 0'

    self.tv1.power()
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'
def mute(self):
    self.tv1.power()
    self.tv1.volume_up()
    self.tv1.mute()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume = 0'

    self.tv1.mute()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume 1'

    self.tv1.power()
    self.tv1.mute()
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'

    self.tv1.mute()
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'


def channel_up(self):
    self.tv1.channel_up()
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.channel_up()
    assert self.tv1__str() == 'Power = True, Channel = 1, Volume = 0'

    self.tv1.channel_up()
    self.tv1.channel_up()
    self.tv1.channel_up()
    assert self.tv1__str() == 'Power = True, Channel = 1, Volume = 0'
def channel_down(self):
    self.tv1.channel_down()
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.channel_down()
    assert self.tv1__str() == 'Power = True, Channel = 3, Volume = 0'
def volume_up(self):
    self.tv1.volume_up()
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.volume_up()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume = 1'

    self.tv1.mute()
    self.tv1.volume_up()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume = 1'

    self.tv.volume_up()
    self.tv1.volume_up()
    self.tv1.volume_up()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume = 3'

def volume_down(self):
    self.tv1.volume_down()
    assert self.tv1__str() == 'Power = False, Channel = 0, Volume = 0'

    self.tv1.power()
    self.tv1.volume_up()
    self.tv1.volume_up()
    self.tv1.volume_up()
    self.tv1.volume_down()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume = 2'

    self.tv1.mute()
    self.tv1.volume_down()
    assert self.tv1__str() == 'Power = True, Channel = 0, Volume = 2'
