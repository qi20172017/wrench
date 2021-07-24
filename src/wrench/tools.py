#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : tools.py
@Author: crawlSpider
@Address: https://weixin.sogou.com/weixin?type=1&s_from=input&query=%E7%BD%91%E8%99%ABspider&ie=utf8&_sug_=n&_sug_type_=
@Github: https://github.com/qi20172017
@Date  : 2021/7/24 上午8:24
@Desc  :
"""

import time
import datetime
import pytz
import arrow


class Tools:

    @staticmethod
    def now_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    @staticmethod
    def now_data():
        return time.strftime("%Y-%m-%d", time.localtime())

    @staticmethod
    def yesterday_data():
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        return yesterday

    @staticmethod
    def to_timestamp(time_f, millisecond=False):
        """
        标准格式转时间戳 这种格式'2019-1-1 00:00:00'
        :param time_f: 这种格式'2019-1-1 00:00:00'
        :param millisecond: 毫秒级

        :return:
        """
        timestamp = int(time.mktime(time.strptime(time_f, '%Y-%m-%d %H:%M:%S')))
        if millisecond:
            return timestamp * 1000
        else:
            return timestamp

    @staticmethod
    def to_time_format(time_s):
        """
        时间戳转标准格式
        :param time_s:
        :return:
        """
        time_s = int(str(time_s)[:10])
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_s))

    @staticmethod
    def to_time_zone(time_s):
        """
        时间戳转为时区标准格式
        :param time_s:
        :return:
        """
        time_s = int(str(time_s)[:10])
        tz = pytz.timezone('Asia/Shanghai')
        return arrow.get(time_s).astimezone(tz).isoformat()

    @staticmethod
    def safe_get(data, *args):
        """
        用于对多层字典取值
        :param data: 字典类型
        :param args: 从外层依次向里层的参数
        :return:
        """
        assert isinstance(data, dict), "data必须为字典"
        result = None
        for arg in args:
            result = data.get(arg)
            if result:
                data = result
            else:
                break
        return result


if __name__ == '__main__':
    pass
