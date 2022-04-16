import dataclasses
import typing

RequiredType = typing.TypeVar(name='RequiredType')
CollectionType = typing.TypeVar(name='CollectionType')


def binary_search(collection: list[CollectionType],
                  required: RequiredType,
                  key: typing.Callable[[CollectionType], RequiredType] = lambda x: x
                  ) -> typing.Optional[RequiredType]:

    if not collection:
        return None

    first = 0
    last = len(collection) - 1

    while first <= last:
        mid = int((first + last) / 2)
        guess = key(collection[mid])
        if guess == required:
            return mid
        elif guess < required:
            first = mid + 1
        elif guess > required:
            last = mid - 1
    else:
        return None


# Usage example

@dataclasses.dataclass
class CityTemperature:
    city: str
    temperature: int


cities = [
    CityTemperature(city='Washington', temperature=10),
    CityTemperature(city='Paris', temperature=13),
    CityTemperature(city='Rome', temperature=20),
    CityTemperature(city='Oslo', temperature=0),
    CityTemperature(city='Mexico', temperature=31)
]
key = lambda el: el.temperature
cities.sort(key=key)

assert binary_search([], 123, key=key) is None
assert binary_search(cities, 47, key=key) is None
assert binary_search(cities, -5, key=key) is None
assert binary_search(cities, 15, key=key) is None
assert binary_search(cities, 0, key=key) == 0
assert binary_search(cities, 13, key=key) == 2
assert binary_search(cities, 31, key=key) == 4


