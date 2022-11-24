from unittest import TestCase
from app.csv_to_json import csv2json_air

import json

class Test_csv2json_air(TestCase):

    def test_json(self):
        outarr , outjson = csv2json_air()
        with open("tests/outdata.json", 'r', encoding='utf-8', newline='') as f:
            testjson = json.load(f)

        self.assertEqual(outjson, testjson)