#!/usr/bin/env python3

from random import randrange
from utils import Passenger, Baggage
from transport import Boat, Fairchild, Motorcycle

if __name__ == '__main__':
    print('Start')

    baggage_list = []
    for wght in range(200):
        baggage_list.append(
            Baggage(
                weight=wght+1,
                width=randrange(15, 30, 1),
                height=randrange(7, 37, 1)))

    oliver = Passenger(name='Oliver', gender='male', age=randrange(18, 60, 1))
    oliver + baggage_list[0] + baggage_list[1] + baggage_list[2] + baggage_list[3]
    oliver - baggage_list[3]

    olivia = Passenger(name='Olivia', gender='female', age=randrange(17, 52, 1))
    olivia + baggage_list[3] + baggage_list[4] + baggage_list[5] + baggage_list[6]

    freya = Passenger(name='Freya', gender='female', age=randrange(14, 40, 1))
    (freya + baggage_list[7]) / 0

    lily = Passenger(name='Lily', gender='female', age=randrange(10, 35, 1))
    alfred = Passenger(name='Alfred', gender='male', age=randrange(10, 70, 1))
    chester = Passenger(name='Chester', gender='male', age=randrange(10, 28, 1))

    moto = Motorcycle(
        passenger_seats=2,
        fuel_size=32,
        fuel_consumption=3.6,
        wear=10.2,
        capacity=2,
        weight=3.5,
        name='Урал')

    boat = Boat(
        passenger_seats=1,
        fuel_size=24,
        fuel_consumption=1.4,
        wear=8,
        capacity=2,
        weight=2.5,
        name='Suzuki')

    moto + chester + alfred
    try:
        moto + lily
    except Exception as e:
        boat + lily
        print(f'{lily.name} решила поплыть на {boat.name}, так как на "{moto.name}" {e}')
    print(f'В "{moto.name}" сейчас находятся', list(pas.name for pas in moto.passengers))

    moto - chester
    try:
        moto + oliver
    except Exception as e:
        print(f'{oliver.name} придётся идти пешком: {e}')

    try:
        moto + lily
    except Exception as e:
        print(f'{lily.name} не поехала на "{moto.name}", так как {e}')

    print(f'В "{moto.name}" сейчас находятся', list(pas.name for pas in moto.passengers))

    while 1:
        try:
            moto.trip()
            moto.beep()
        except Exception as e:
            print(f'На "{moto.name}" больше не поездить так как {e}')
            break

    try:
        moto.refuel()
    except Exception as e:
        print(f'На "{moto.name}" больше не поездить так как {e}')
    try:
        moto.repair()
    except Exception as e:
        print(f'На "{moto.name}" больше не поездить так как {e}')


    moto.unloading()
    print(f'В "{moto.name}" сейчас находятся', list(pas.name for pas in moto.passengers))

    print('<<<')

    boxcar = Fairchild(
        name='C-119 Flying Boxcar',
        fuel_size=925,
        fuel_consumption=50.6,
        wear=8.5,
        capacity=1300,
        weight=317.73,
        can_passenger=False)

    for i in range(100, 200):
        try:
            boxcar + baggage_list[i]
        except Exception as e:
            print(f'{boxcar.name} больше не может вместить багаж: {e}')
            break

    try:
        boxcar + oliver
    except Exception as e:
        print(f'{oliver.name} не может воспользоваться {boxcar.name} так как {e}')

    boxcar.beep()
    boxcar.trip()
    print(boxcar)
