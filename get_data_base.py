#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import get_refs
"""Блок кода вовзращающий центр масс данного адреса и город"""


def create_data_base(file):
    all_str = ''
    city = ''
    city_with_links = dict()
    with open(file, 'r') as f:
        for line in f.readlines():
            all_str += line
            if is_line_city(line):
                city = line[21:-4]
                city_with_links[city] = []
            if is_line_link(line):
                if city is not '':
                    city_with_links[city].append(get_link_lat_lon(line))
        return city_with_links, all_str


def is_line_city(line):
    res = re.findall(r'\s+<tag\sk=\"name\"\sv=\"', line)
    return bool(res)


def is_line_link(line):
    res = re.findall(r'\s+<node\s+id=', line)
    return bool(res)


def count_average(links, base):
    lats = []
    lons = []
    for link in links:
        for value in base.values():
            for v in value:
                if link == v[0]:
                    lats.append(v[1])
                    lons.append(v[2])
    common_lat = 0.0
    common_lon = 0.0
    for l in lats:
        common_lat += float(l)
    res_lat = common_lat/len(lats)
    for l in lons:
        common_lon += float(l)
    res_lon = common_lon/len(lons)
    return res_lat, res_lon


def get_link_lat_lon(line):
    link = (re.findall(r'\d+', line)[0])
    lt = [re.findall(r'\d+', line)[8], re.findall(r'\d+', line)[9]]
    lat = '.'.join(lt)
    ln = [re.findall(r'\d+', line)[10], re.findall(r'\d+', line)[11]]
    lon = '.'.join(ln)
    return link, lat, lon


def get_main_links(data):
    s = ''
    l = []
    for i in data:
        s += str(i)
    links = re.findall(r'<nd ref=\"\d+\"\/>', s)
    for link in links:
        l.append(link[9:-3])
    return l


def get_city(links, base):
    value = []
    link = links[0]
    for b in base.values():
        for v in b:
            if v[0] == link:
                value = b
    return get_key_from_value(base, value)


def get_key_from_value(base, value):
    for i in base.items():
        if i[1] == value:
            return i[0]


def return_result(file, all_str, street, house):
    base = create_data_base(file)[0]
    links = get_refs.return_links(all_str, street, house)
    average = count_average(links, base)
    city = get_city(links, base)
    return average, city
