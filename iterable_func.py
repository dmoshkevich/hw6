from collections.abc import Iterable


def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    counter = 0
    for _ in iterable:
        counter += 1
    return counter


def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for elem in iterable:
        if isinstance(elem, (list, set, tuple)):
            yield from flatten(elem)
        elif isinstance(elem, (int, str, float, bool)):
            yield elem


def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    unq = []
    for val in iterable:
        if val not in unq:
            unq.append(val)
            yield val


def groupby(key, iterable: Iterable):
    """
    >>> users = [{'gender': 'female', 'age': 23},{'gender': 'male', 'age': 20},{'gender': 'female', 'age': 21}]
    >>> groupby('gender', users)
    {'female': [{'gender': 'female', 'age': 23}, {'gender': 'female', 'age': 21}], 'male': [{'gender': 'male', 'age': 20}]}
    """
    group = {}
    for elem in iterable:
        if elem[key] not in group:
            group[elem[key]] = []
        group[elem[key]].append(elem)
    return group


def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4, 5, 6]))
    [[0, 1, 2], [3, 4, 5], [6, None, None]]
    """
    part = []
    for elem in iterable:
        part.append(elem)
        if len(part) == size:
            yield part
            part = []
    val = size - len(part)
    for i in range(val):
        part.append(None)
    yield part


def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> print(first(range(0)))
    None
    """
    return next(iter(iterable), None)


def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> print(last(range(0)))
    None
    """
    elem = None
    for elem in iterable:
        pass
    return elem
