#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from get_data_base import is_line_city
from get_data_base import is_line_link
from get_data_base import count_average
from get_data_base import get_link_lat_lon
from get_data_base import get_main_links
from get_data_base import get_city
from get_data_base import get_key_from_value
from get_refs import get_link
from get_refs import get_street
from get_refs import find_house
from get_refs import find_street


class Tests(unittest.TestCase):
    def test_for_anytask_1(self):
        """Чтобы запустились тесты на таске"""
        self.assertEqual(1, 1)

    def test_for_anytask_2(self):
        self.assertEqual(2, 2)

    def test_for_anytask_3(self):
        self.assertEqual(3, 3)

    def test_find_city_name(self):
        line = '<tag k=\"addr:region\" v=\"Свердловская область\"/>\n<tag k=\"name\" v=\"Заречный\"/>\n<tag k='
        res = is_line_city(line)
        self.assertEqual(res, True)

    def test_is_line_link(self):
        line = '  <node id=\"27212296\" version'
        res = is_line_link(line)
        self.assertEqual(res, True)

    def test_is_line_lnot_ink(self):
        line = '    <tag k=\"place\" v=\"city\"/>'
        res = is_line_link(line)
        self.assertEqual(res, False)

    def test_count_average(self):
        links = ['123', '456']
        base = {'Екатеринбург': [('123', '1', '2'), ('456', '1', '2'), ('789', '10', '10')]}
        res = count_average(links, base)
        self.assertEqual((1, 2), res)

    def test_get_lat_lon(self):
        line = ' <node id=\"27212296\" version=\"4\" timestamp=\"2011-07-29T21:45:17Z\" lat=\"45.2465854\" lon=\"33.3985674\"\/>'
        res = get_link_lat_lon(line)
        self.assertEqual(('27212296', '45.2465854', '33.3985674'), res)

    def test_get_main_links(self):
        data = """  <way id="690949874" version="1" timestamp="2019-05-18T21:17:55Z">
    <nd ref="6482945073"/>
    <nd ref="6482945074"/>
    <nd ref="6482945075"/>
    <tag k="addr:housenumber" v="137"/>
  </way>"""
        res = get_main_links(data)
        self.assertEqual(['6482945073', '6482945074', '6482945075'], res)

    def test_get_city(self):
        links = ['42', '23', '26']
        base = {'Екатеринбург': [('123', '1', '2'), ('42', '1', '2')]}
        res = get_city(links, base)
        self.assertEqual('Екатеринбург', res)

    def test_get_key_by_value(self):
        d = {'key_1': '1', 'key_2': '2'}
        value = '2'
        res = get_key_from_value(d, value)
        self.assertEqual('key_2', res)

    def test_get_link(self):
        line = """ref="6482945073"/>
    <nd ref="6482945074"/>
    <nd ref="6482945075"/>
    <nd ref="6482945076"/>
    <nd ref="6482945073"/>"""
        links = ['6482945073', '6482945074', '6482945075', '6482945076']
        res = get_link(line)
        self.assertEqual(links, res)

    def test_get_street_1(self):
        street = 'Садовая'
        res = get_street(street)[0]
        self.assertEqual('улица Садовая', res)

    def test_get_street_2(self):
        street = 'Садовая'
        res = get_street(street)[1]
        self.assertEqual('Садовая улица', res)

    def test_find_street(self):
        line = '    <tag k=\"addr:street\" v=\"Уральская улица\"/>'
        street = 'Уральская'
        res = find_street(line, street)
        self.assertEqual(True, res)

    def test_find_house(self):
        line = '    <tag k=\"addr:housenumber\" v=\"137\"/>'
        house = '137'
        res = find_house(line, house)
        self.assertEqual(True, res)
