#!/usr/bin/env python3

from pydantic import BaseModel


class Baggage(BaseModel):
    weight: float = None  # вес багажа
    width: float = None  # ширина
    height: float = None  # высота
    items: list = []  # TODO: содержимое багажа
