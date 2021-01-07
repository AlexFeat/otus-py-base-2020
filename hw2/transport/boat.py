#!/usr/bin/env python3

from .base import WaterTransport


class Boat(WaterTransport):
    def beep(self):
        print('Boat says Beeeeeeeeeeeeeeeeeeeeee Beeeeeeeeeeeeeeeeee')
