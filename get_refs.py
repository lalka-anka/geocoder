#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
"""Блок кода, возвращающий лист со ссылками на строки в общем файле с lat и lon"""


def searching(all_str, street, house):
    pattern = '(<way\s+id=\"\d+\"\s+version=\"\d+\"\s+timestamp=\"\d+-\d+-\w+:\d+:\w+\">\n\s+(<nd\s+ref=\"\d+\"\/>\s+)+<tag\sk=\"addr:housenumber\"\sv=\"\d+\"\/>\s+<tag\sk=\"addr:street\"\s+v=\"\w+\s\w+\"/>)'
    info_about_building = re.findall(pattern, all_str)
    for element in info_about_building:
        flag = 0
        for e in element:
            if find_street(e, street) is not False:
                flag += 1
            if find_house(e, house) is not False:
                flag += 1
        if flag == 2:
            return element
    return None


def get_street(street):
    street1 = 'улица ' + street
    street2 = street + ' улица'
    return street1, street2


def get_link(line):
    row_links = re.findall(r'ref=\"\d+', line)
    links = []
    for r in row_links:
        if r[5:] not in links:
            links.append(r[5:])
    return links


def find_street(line, street):
    res1 = re.findall(r'<tag k=\"addr:street\" v=\"{}\"/>'.format(get_street(street)[0]), line)
    res2 = re.findall(r'<tag k=\"addr:street\" v=\"{}\"/>'.format(get_street(street)[1]), line)
    return bool(res1 or res2)


def find_house(line, house):
    res = re.findall(r'<tag k=\"addr:housenumber\" v=\"{}\"/>'.format(house), line)
    return bool(res)


def return_links(all_str, street, house):
    info = searching(all_str, street, house)[0]
    return get_link(info)
