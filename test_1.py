import pytest
import logging

def test_create_tuple_structure():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ СОЗДАНИЯ ТИПА ДАННЫХ TUPLE')
    logging.debug('Создаем структуру данных типа tuple')
    a = tuple()
    logging.debug('Проверяем получившейся тип данных')
    assert f"{type(a)}" == "<class 'tuple'>", logging.error('FAILED')
    logging.info('PASSED')

def test_converting_list_to_tuple():
    tpl = (2, 4, 6, 8, 10)
    lst = list(tpl)
    assert f"{type(lst)}" == "<class 'list'>", logging.error('FAILED')

def test_converting_tuple_to_list():
    lst = [1, 2, 3, 4, 5]
    tpl = tuple(lst)
    assert f"{type(tpl)}" == "<class 'tuple'>", logging.error('FAILED')


def test_zero_division_float_structure():




