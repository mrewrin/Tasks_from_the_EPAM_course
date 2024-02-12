# This code implements a simple currency converter using magic methods,
# including comparison and addition of currency units for Euro, Dollar and Pound

from __future__ import annotations


class Currency:
    def __init__(self, value=1):
        self.value = value

    def __str__(self):
        return f"{self.value} {self.abbr()}"

    def abbr(self):
        return self.__class__.__name__

    @classmethod
    def course(cls, to_currency):
        return f"{cls.exchange_rate(to_currency)} {to_currency().abbr()} for 1 {cls().abbr()}"

    @classmethod
    def exchange_rate(cls, to_currency):
        return cls(1).to_currency(to_currency).value

    def to_currency(self, to_currency):
        target_value = self.value * self.exchange_rate(to_currency)
        return to_currency(target_value)

    def __add__(self, other):
        converted_value = other.to_currency(self.__class__)
        new_value = self.value + converted_value.value
        return self.__class__(new_value)

    def __lt__(self, other):
        other_value = other.to_currency(self.__class__).value
        return self.value < other_value

    def __gt__(self, other):
        other_value = other.to_currency(self.__class__).value
        return self.value > other_value

    def __eq__(self, other):
        other_value = other.to_currency(self.__class__).value
        return self.value == other_value


class Euro(Currency):
    def abbr(self):
        return "EUR"

    @classmethod
    def exchange_rate(cls, to_currency):
        if to_currency == Dollar:
            return 2.0
        elif to_currency == Pound:
            return 100.0
        else:
            return 1.0


class Dollar(Currency):
    def abbr(self):
        return "USD"

    @classmethod
    def exchange_rate(cls, to_currency):
        if to_currency == Euro:
            return 0.5
        elif to_currency == Pound:
            return 50.0
        else:
            return 1.0


class Pound(Currency):
    def abbr(self):
        return "GBP"

    @classmethod
    def exchange_rate(cls, to_currency):
        if to_currency == Euro:
            return 0.01
        elif to_currency == Dollar:
            return 0.02
        else:
            return 1.0
