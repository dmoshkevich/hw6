import pytest
import iterable_func


@pytest.mark.parametrize("given", [(x for x in range(5)), tuple(x for x in range(5)),list(x for x in range(5))])
def test_ilen_types(given):
    assert iterable_func.ilen(given) == 5


@pytest.mark.parametrize("given", [(x for x in range(5)), tuple(x for x in range(5)),list(x for x in range(5))])
def test_first_types(given):
    assert iterable_func.first(given) == 0


@pytest.mark.parametrize("given", [(x for x in range(5)), tuple(x for x in range(5)),list(x for x in range(5))])
def test_last_types(given):
    assert iterable_func.last(given) == 4


def test_ilen():
    with pytest.raises(TypeError):
        assert iterable_func.ilen()


def test_flatten():
    with pytest.raises(TypeError):
        assert iterable_func.flatten()


def test_distinct():
    with pytest.raises(TypeError):
        assert iterable_func.distinct()


def test_groupby():
    with pytest.raises(TypeError):
        assert iterable_func.groupby()


def test_chunks():
    with pytest.raises(TypeError):
        assert iterable_func.chunks()


def test_first():
    with pytest.raises(TypeError):
        assert iterable_func.first()


def test_last():
    with pytest.raises(TypeError):
        assert iterable_func.last()


def test_groupby_no_key():
    with pytest.raises(KeyError):
        assert iterable_func.groupby('x', [{'y': 'female'}])


def test_flatten_none():
    assert list(iterable_func.flatten(([None, [None, [None, None]]]))) == []

