import csv
import unittest

import pandas as pd
from bs4 import BeautifulSoup
from solution import process


class Test(unittest.TestCase):

    def check(self, correctcsv, usercsv):
        with open(correctcsv) as correctcsv:
            csv_reader = csv.reader(correctcsv, delimiter=',')
            df = pd.DataFrame([csv_reader], index=None)
            df.head()
        row_count = sum(1 for row in df)
        correctlist = [['3', '4', '7'], ['3', '347', '350'], ['322', '321', '643'], ['333', '32', '365']]

        with open(usercsv) as usercsv:
            csv_reader = csv.reader(usercsv, delimiter=',')
            df = pd.DataFrame([csv_reader], index=None)
            df.head()
        row_count = sum(1 for row in df)
        userlist = []
        for i in range(row_count):
            for li in df[i]:
                new_li = []
                for new_char in li:
                    if new_char != " ":
                        new_li.append(new_char.strip())
                userlist.append(new_li)
        return correctlist == userlist

    def test_sample_1(self):
        process("test1_sample.csv")
        self.assertTrue(self.check("test/correctans.csv", "ans.csv"))
