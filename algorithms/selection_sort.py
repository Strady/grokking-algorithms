import dataclasses
import typing

ElementType = typing.TypeVar('ElementType')


def find_smallest_index(collection: typing.Sequence,
                        key: typing.Callable = lambda el: el
                        ) -> int:
    if not collection:
        raise ValueError('Empty collection are not allowed')
    smallest = 0
    for i in range(1, len(collection)):
        if key(collection[i]) < key(collection[smallest]):
            smallest = i
    return smallest


def selection_sort(collection: typing.Sequence[ElementType],
                   key: typing.Callable = lambda el: el
                   ) -> typing.List[ElementType]:
    temp: typing.List[ElementType] = []
    _collection = list(collection)
    for _ in range(len(collection)):
        index = find_smallest_index(collection=_collection, key=key)
        temp.append(_collection[index])
        _collection.pop(index)
    return temp


# Usage example

@dataclasses.dataclass
class Song:
    band: str
    name: str
    duration: str


songs = (
    Song(band='Green Day', name='Whatsername', duration='4.17'),
    Song(band='Billy Idol', name='Bitter Taste', duration='4.26'),
    Song(band='Pink', name='Try', duration='4.07'),
    Song(band='Sum 41', name='War', duration='3.29'),
    Song(band='Imagine Dragons', name='Believer', duration='3.24'),
)

for song in selection_sort(songs, key=lambda s: s.duration):
    print(f'{song.band} - {song.name} - {song.duration}')
