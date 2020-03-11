#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import get_data_base
import argparse
import return_in_json
"""Блок кода, осуществляющий парсинг, связывающий базу данных и обработчик информации"""


def process_information(file, street, house):
    """Метод, возвращающий результат поиска"""
    all_str = get_data_base.create_data_base(file)[1]
    average = get_data_base.return_result(file, all_str, street, house)[0]
    city = get_data_base.return_result(file, all_str, street, house)[1]
    result = {'Город': city, 'Улица': street, 'Дом': house, 'Широта': average[0], 'Долгота': average[1]}
    return result


def input_and_output(geo_file_from_url):
    """Метод, осуществляющий парсинг и возвращающий результат"""
    parser = argparse.ArgumentParser(description='Geocoder that returns address data')
    parser.add_argument('-st', '--street', type=str, metavar='', help='Search street')
    parser.add_argument('-bld', '--building', type=str, metavar='', help='Search building')
    parser.add_argument('-doc', '--document', type=str, metavar='', help='Document to save the result')
    args = parser.parse_args()
    street = args.street
    building = args.building
    document = args.document
    if street is None and building is None and document is None:
        st = input('Введите улицу для поиска: ')
        bld = input('Введите дом для поиска: ')
        file = 'default'
        dict_res = process_information(geo_file_from_url, st, bld)
        json_res = return_in_json.return_result_json(file, dict_res)

    elif street is not None and building is not None and document is None:
        file = 'default'
        dict_res = process_information(geo_file_from_url, street, building)
        json_res = return_in_json.return_result_json(file, dict_res)

    else:
        dict_res = process_information(geo_file_from_url, street, building)
        json_res = return_in_json.return_result_json(document, dict_res)
    return json_res


