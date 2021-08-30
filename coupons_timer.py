# -*- coding:utf-8 -*-
import sys
import time
import requests
import json

from datetime import datetime


from meituan_logger import logger
from config import global_config


class CouponsTimer(object):
    def __init__(self, sleep_interval=0.5):
        # '2018-09-28 22:45:50.000'
        # buy_time = 2020-12-22 09:59:59.500
        buy_time_everyday = global_config.getRaw('config', 'coupons_time').__str__()
        localtime = time.localtime(time.time())
        self.buy_time = datetime.strptime(
            localtime.tm_year.__str__() + '-' + localtime.tm_mon.__str__() + '-' + localtime.tm_mday.__str__()
            + ' ' + buy_time_everyday,
            "%Y-%m-%d %H:%M:%S.%f")
        self.buy_time_ms = int(time.mktime(self.buy_time.timetuple()) * 1000.0 + self.buy_time.microsecond / 1000)
        self.sleep_interval = sleep_interval

        self.diff_time = self.local_jd_time_diff()

    def meituan_time(self):
        """
        从美团服务器获取时间毫秒
        :return:
        """
        url = 'https://catfront.dianping.com/batch?v=1&sdk=1.9.5&pageId=owl-b197744d-d914-0786-79a1-b2fc-1630146858328'
        ret = requests.get(url).text

        return int(ret[6:19])

    def local_time(self):

        return int(round(time.time() * 1000))

    def local_jd_time_diff(self):
        """
        计算本地与京东服务器时间差
        :return:
        """
        print('本地时间', self.local_time())
        print('美团时间', self.meituan_time())
        print('购买时间', self.buy_time_ms)
        return self.local_time() - self.meituan_time()

    def start(self):
        logger.info('正在等待到达设定时间:{}，检测本地时间与美团服务器时间误差为【{}】毫秒'.format(self.buy_time, self.diff_time))
        while True:
            # 本地时间减去与美团的时间差，能够将时间误差提升到0.1秒附近
            # 具体精度依赖获取美团服务器时间的网络时间损耗
            if self.local_time() - self.diff_time >= self.buy_time_ms:
                logger.info('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)

    def end(self, local_time):
        # logger.info('正在等待到达设定时间:{}，检测本地时间与京东服务器时间误差为【{}】毫秒'.format(self.buy_time, self.diff_time))
        while True:
            # 本地时间减去与京东的时间差，能够将时间误差提升到0.1秒附近
            # 具体精度依赖获取京东服务器时间的网络时间损耗
            logger.info(local_time)
            if self.local_time() >= local_time + 5000:
                logger.info('时间到达，结束程序……')
                sys.exit(0)
            else:
                break
