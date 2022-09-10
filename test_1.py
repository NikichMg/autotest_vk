import pytest
import logging

def test_create_tuple_structure():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ СОЗДАНИЯ ТИПА ДАННЫХ TUPLE')
    logging.debug('Создаем структуру данных типа tuple')
    a = tuple()
    logging.debug('Проверяем получившейся тип данных(должен принадлежать:tuple)')
    assert f"{type(a)}" == "<class 'tuple'>", logging.error('FAILED')
    logging.info('PASSED')

def test_add_new_items_tuple_structure():
    logging.info('ТЕСТ НА КОРРЕКТНОСТЬ ДОБОВЛЕНИЯ НОВЫХ ЭЛЕМЕНТОВ В КАРТЕЖ')
    logging.debug('Создаем структуру данных типа tuple')
