#!/usr/bin/env python3

from .baggage import Baggage
from pprint import pprint


class Passenger:
    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age
        self._posted = ''
        self._baggages = dict()

    @property
    def posted(self) -> str:
        return self._posted

    @posted.setter
    def posted(self, val):
        self._posted = val

    def view_baggage(self):
        pprint(self.get_baggage())

    def get_baggage(self):
        return list(val for val in self._baggages.values())

    def add_baggage(self, baggage):
        if isinstance(baggage, Baggage):
            return self + baggage
        else:
            raise Exception('Bad type')

    def remove_baggage(self, baggage):
        return self - baggage

    def drop_baggage(self, baggage):
        return self / 0

    def __add__(self, baggage):
        if id(baggage) not in self._baggages:
            self._baggages[id(baggage)] = baggage
        return self

    def __sub__(self, baggage):
        if id(baggage) in self._baggages:
            del self._baggages[id(baggage)]
        return self

    def __truediv__(self, val):
        if val == 0:
            self._baggages.clear()
        else:
            raise Exception('Bad params')
        return self
