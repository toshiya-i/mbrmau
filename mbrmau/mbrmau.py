# -*- coding: utf-8 -*-

import calendar
from jinja2 import Environment, PackageLoader


class Mbrmau:

    def __init__(self, year, month):
        first_weekday, last_day = calendar.monthrange(year, month)
        days = map(lambda n: n+1, range(last_day))
        weekdays = map(lambda n: (first_weekday+n) % 7, range(last_day))
        workdays = filter(lambda n: n[1] < 5, zip(days, weekdays))
        self.__workdays =\
            list(map(lambda n: '%d/%d/%d' % (year, month, n[0]), workdays))

    def message(self):
        pl = PackageLoader('mbrmau', './', encoding='utf8')
        env = Environment(loader=pl)
        tpl = env.get_template('message.tpl')

        tpl_variables = {
                "days": self.__workdays
                }

        message = tpl.render(tpl_variables)

        return message


if __name__ == '__main__':
    print(Mbrmau(2016, 12).message())
