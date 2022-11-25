from unittest import TestCase
from app.csv_to_json import csv2json

import json
import argparse

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--filename', help='input csv filepath', type=str, required=True)
    args = parser.parse_args(["--filename","./sample.csv"])
    return args
class Test_csv2json(TestCase):


    def test_json(self):
        args = argparser()

        outjson = csv2json(args)
        with open("tests/outdata.json", 'r', encoding='utf-8', newline='') as f:
            testjson = json.load(f)

        self.assertEqual(outjson, testjson)