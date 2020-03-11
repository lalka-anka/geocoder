#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
"""Блок кода, возвращающий данные в формате json"""


def return_result_json(file, dictionary):
    if file == 'default':
        with open('filename_json', 'a', encoding='utf8') as json_file:
            json.dump(dictionary, json_file, ensure_ascii=False)

        with open('filename_json', 'r') as f:
            for line in f.readlines():
                print(line)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = dir_path + '/filename_json'
        os.remove(file_path)
    else:
        with open(file, 'a', encoding='utf8') as json_file:
            json.dump(dictionary, json_file, ensure_ascii=False)
