# -*- coding: utf-8 -*-

import sys
import datetime
from dateutil.relativedelta import relativedelta
from mbrmau.mbrmau import Mbrmau


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        next_month = datetime.datetime.now() + relativedelta(months=1)
        year = next_month.year
        month = next_month.month
    else:
        year = int(args[0])
        month = int(args[1])
    print(Mbrmau(year, month).message())
