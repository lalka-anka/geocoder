#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
import os.path
import shutil
import process_info
"""Блок кода, скачивающий картографические данные"""


def launch():
    os.mkdir('dir_for_database')
    links_for_russia = {'central': 'https://download.geofabrik.de/russia/central-fed-district-latest-free.shp.zip',
                        'crimean': 'https://download.geofabrik.de/russia/crimean-fed-district-latest-free.shp.zip',
                        'far_eastern': 'https://download.geofabrik.de/russia/far-eastern-fed-district-latest-free.shp.zip',
                        'north_causus': 'https://download.geofabrik.de/russia/north-caucasus-fed-district-latest-free.shp.zip',
                        'northwestern': 'https://download.geofabrik.de/russia/northwestern-fed-district-latest-free.shp.zip',
                        'siberian': 'https://download.geofabrik.de/russia/siberian-fed-district-latest-free.shp.zip',
                        'south': 'https://download.geofabrik.de/russia/south-fed-district-latest-free.shp.zip',
                        'ural': 'https://download.geofabrik.de/russia/ural-fed-district-latest-free.shp.zip',
                        'volga': 'https://download.geofabrik.de/russia/volga-fed-district-latest-free.shp.zip'}

    links_for_training = {
        'first_file': 'https://drive.google.com/uc?export=download&id=1VZXzUcVzLTjaQF9nTSPlP6tcdwdOFsWq',
        'second_file': 'https://drive.google.com/uc?export=download&id=1ooF-5-CDq7jRYTtrvtStCvKZq-Sp3nWP'}
    for value in links_for_training.items():
        LINK = value[1]
        urlretrieve(LINK, os.path.join('dir_for_database', value[0]))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = dir_path + '/dir_for_database/' + value[0]
        process_info.input_and_output(file_path)

    shutil.rmtree('dir_for_database', ignore_errors=True)


if __name__ == '__main__':
    launch()
