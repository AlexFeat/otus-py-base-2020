#!/usr/bin/env python3

from .base import AirTransport


class Fairchild(AirTransport):
    def beep(self):
        print(f"{self.name} beeps, but you can't hear")

    def __str__(self):
        fields = [self.name]
        s = ''
        if self._can_passenger or self._can_baggage:
            s += '{} имеет на борту '
            if self._can_passenger:
                s += '{} пассажиров '
                fields.append(len(self.passengers)),
                if self._can_baggage:
                    s += 'и '
            if self._can_baggage:
                s += '{} предметов багажа общим весом {} из допустимого {}. '
                fields.extend((
                    len(self.baggages),
                    self._baggage_weight,
                    self._capacity))
        s += 'Текущий уровень топлива {} из {}. '
        s += 'Текущий уровень прочности {} из 100.'
        fields.extend((
            self._fuel_limit,
            self._fuel_size,
            self._durability))
        return s.format(*fields)
