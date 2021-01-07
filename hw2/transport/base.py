#!/usr/bin/env python3

import random
from abc import ABC, abstractmethod
from typing import Optional
from utils import Passenger, Baggage


def success_or_fail(max_val=100, fail=10):
    val = random.randrange(1, max_val, 1)
    if val <= fail:
        return 0
    return 1


class Transport(ABC):
    '''
        Основной класс транспорта с базовыми методами
        _durability -> оставшийся запас прочности
        _baggage_weight -> текущий вес багажа
        _baggages -> багаж в багажном отделении
        _passengers -> список пассажиров в транспорте
        fuel_size -> размер тпливного бака
        fuel_consumption -> расход топлива
        _fuel_limit -> остаток топлива в баке
        wear -> единица износа транспорта
        can_passenger -> флаг, указывающий на возможность перевозки пассажиров
        can_baggage -> флаг, указывающий на возможность перевозки багажа
        capacity -> объём багажного отделения
        passenger_seats -> количество пассажирских мест
        weight -> вес транспорта
        name -> название транспортного средства
    '''
    # тип транспорта
    _ttype: Optional[str] = None

    def __init__(self, **kwargs):
        # текущий запас прочности
        self._durability: Optional[float] = 100
        # текущий статус загруженности
        self._baggage_weight: float = 0
        # список пассажиров размещённых в транспорте
        self._passengers = dict()
        # список объектов сданных в багаж
        self._baggages = dict()

        # размер бака
        if 'fuel_size' in kwargs and isinstance(kwargs['fuel_size'], (float, int)):
            self._fuel_size: Optional[float] = kwargs['fuel_size']
        else:
            self._fuel_size: Optional[float] = 60
        # расход топлива за поездку
        if 'fuel_consumption' in kwargs and isinstance(kwargs['fuel_consumption'], (float, int)):
            self._fuel_consumption: Optional[float] = kwargs['fuel_consumption']
        else:
            self._fuel_consumption: Optional[float] = 10
        # текущий уровень топлива
        self._fuel_limit: Optional[float] = self._fuel_size

        # количество износа транспорта за одну поездку
        if 'wear' in kwargs and isinstance(kwargs['wear'], (float, int)):
            self._wear: Optional[float] = kwargs['wear']
        else:
            self._wear: Optional[float] = 1
        # может брать пассажиров
        if 'can_passenger' in kwargs and isinstance(kwargs['can_passenger'], bool):
            self._can_passenger: bool = kwargs['can_passenger']
        else:
            self._can_passenger: bool = True
        # может брать багаж
        if 'can_baggage' in kwargs and isinstance(kwargs['can_baggage'], bool):
            self._can_baggage: bool = kwargs['can_baggage']
        else:
            self._can_baggage: bool = True

        # грузовая вместимость
        if 'capacity' in kwargs and isinstance(kwargs['capacity'], (float, int)):
            self._capacity: Optional[float] = kwargs['capacity']
        else:
            self._capacity: Optional[int] = 10
        # кол-во пассажирских мест
        if 'passenger_seats' in kwargs and isinstance(kwargs['passenger_seats'], (float, int)):
            self._passenger_seats: Optional[int] = kwargs['passenger_seats']
        else:
            self._passenger_seats: Optional[int] = 10

        # вес транспорта
        if 'weight' in kwargs and isinstance(kwargs['weight'], (float, int)):
            self._weight: Optional[float] = kwargs['weight']
        else:
            self._weight: Optional[float] = 10

        # название транспорта
        self.name: Optional[str] = self.__class__.__name__
        if 'name' in kwargs and isinstance(kwargs['name'], str):
            self.name: Optional[str] = kwargs['name']

    @property
    def passengers(self):
        return list(self._passengers[pas_id] for pas_id in self._passengers.keys())

    @property
    def baggages(self):
        return list(self._baggages[bag_id] for bag_id in self._baggages.keys())

    def __add__(self, obj):
        if isinstance(obj, Passenger):
            if not self._can_passenger:
                raise Exception(f'Транспорт {self.name} не может брать пассажиров')
            if id(obj) in self._passengers:
                raise Exception(f'Пассажир {obj.name} уже размещён на {self.name}')
            if obj.posted:
                raise Exception(f'Пассажир {obj.name} уже размещён в транспорте {obj.posted}')
            if len(self._passengers.keys()) >= self._passenger_seats:
                raise Exception('Мест нет!')
            baggage_weight = 0
            for bag in obj.get_baggage():
                baggage_weight += bag.weight
            if self._baggage_weight + baggage_weight > self._capacity:
                raise Exception('Багаж пассажира не помещается')
            for bag in obj.get_baggage():
                self + bag
            self._passengers[id(obj)] = obj
            obj.posted = self.name
        elif isinstance(obj, Baggage):
            if not self._can_baggage:
                raise Exception(f'Транспорт {self.name} не может брать багаж')
            if id(obj) in self._baggages:
                raise Exception('Багаж уже размещён в этом транспорте')
            if self._baggage_weight + obj.weight > self._capacity:
                raise Exception('Багаж не помещается')
            self._baggages[id(obj)] = obj
            self._baggage_weight += obj.weight
        else:
            raise Exception('Bad type: only Passenger or Baggage')
        return self

    def __sub__(self, obj):
        if isinstance(obj, Passenger):
            if id(obj) not in self._passengers:
                raise Exception(f'Пассажир {obj.name} не размещён на {self.name}')
            for bag in obj.get_baggage():
                self - bag
            del self._passengers[id(obj)]
            obj.posted = ''
        elif isinstance(obj, Baggage):
            if id(obj) not in self._baggages:
                raise Exception('Багаж не размещён в этом транспорте')
            del self._baggages[id(obj)]
            self._baggage_weight -= obj.weight
        else:
            raise Exception('Bad type: only Passenger or Baggage')
        return self
        pass

    def refuel(self):
        if self._durability > 15 or success_or_fail(100, 15):
            self._fuel_limit = self._fuel_consumption
            return 1
        self._durability = -100
        raise Exception('Заправка не удалась. Транспорт взорвался, так как был изношен!')

    def repair(self):
        if self._durability == -100:
            raise Exception('Ремонт невозможен, транспорт взорвался!')
        elif self._durability <= 5:
            raise Exception('Ремонт невозможен, транспорт сильно изношен!')
        self._durability = 100
        return 1

    def trip(self):
        val_wear = self._wear * 1.25
        if val_wear > self._durability:
            raise Exception('Путешествие невозможно, транспорт слишком изношен!')
        fuel_mul = 1
        if self._capacity - self._baggage_weight <= self._capacity / 2:
            fuel_mul = 2
        val_fuel = self._fuel_consumption * fuel_mul
        if self._fuel_limit - val_fuel < 0:
            raise Exception('Путешествие невозможно, не хватает топлива!')
        self._durability -= val_wear
        self._fuel_limit -= val_fuel
        return 1

    def unloading(self):
        for pas_id, obj in list(self._passengers.items()):
            obj.posted = ''
            del self._passengers[pas_id]
        self._baggage_weight = 0
        self._baggages.clear()
        return 1

    @abstractmethod
    def beep(self):
        pass


class WaterTransport(Transport):
    '''
        Базовый класс для водного транспорта
    '''
    _ttype = 'water'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # количество турбин у водногшо транспорта
        if 'turbine_count' in kwargs and isinstance(kwargs['turbine_count'], int):
            self._turbine_count: int = kwargs['turbine_count']
        else:
            self._turbine_count: int = 0

        def beep(self):
            print('Bloo Bloo')


class AirTransport(Transport):
    '''
        Базовый класс для воздушного транспорта
    '''
    _ttype = 'air'
    propeller_count: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # количество пропеллеров у воздушного транспорта
        if 'propeller_count' in kwargs and isinstance(kwargs['propeller_count'], int):
            self._propeller_count: int = kwargs['propeller_count']
        else:
            self._propeller_count: int = 0

    def beep(self):
        print('Vroo Vroo')


class EarthTransport(Transport):
    '''
        Базовый класс для наземного транспорта
    '''
    _ttype = 'earth'
    wheel_count: int = 0
    door_count: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # количество колёс у наземного транспорта
        if 'wheel_count' in kwargs and isinstance(kwargs['wheel_count'], int):
            self._wheel_count: int = kwargs['wheel_count']
        else:
            self._wheel_count: int = 0
        # количество дверей у наземного транспорта
        if 'door_count' in kwargs and isinstance(kwargs['door_count'], int):
            self._door_count: int = kwargs['door_count']
        else:
            self._door_count: int = 0

    def beep(self):
        print('Bee Bee')
