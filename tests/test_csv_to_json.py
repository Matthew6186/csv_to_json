from unittest import TestCase
from app.csv_to_json import csv2json

import json

class Test_csv2json(TestCase):

    def test_json(self):
        outjson = csv2json()
        with open("tests/outdata.json", 'r', encoding='utf-8', newline='') as f:
            testjson = json.load(f)

        self.assertEqual(outjson, testjson)