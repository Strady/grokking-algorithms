def quick_sort(collection: list) -> list:
    if len(collection) in (0, 1):
        return collection

    mid = len(collection) // 2
    rest = collection[:mid] + collection[mid + 1:]
    left = [i for i in rest if i < collection[mid]]
    right = [i for i in rest if i >= collection[mid]]

    return quick_sort(left) + [collection[mid]] + quick_sort(right)


# Usage examples and tests

numbers = [1, 5, 3, 7, 11, 9]
assert quick_sort(numbers) == sorted(numbers)

cities = ['New-York', 'Amsterdam', 'Madrid', 'Rome', 'London']
assert quick_sort(cities) == sorted(cities)

assert quick_sort(['whatever']) == sorted(['whatever'])
assert quick_sort([]) == sorted([])