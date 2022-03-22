# -*- coding: UTF-8 -*-
import os
import sys
import datetime
import time

import requests

requests.packages.urllib3.disable_warnings()

from coupons_timer import CouponsTimer
from concurrent.futures import ProcessPoolExecutor
from util import (
    parse_json,
    wait_some_time
)


class Caifudao(object):
    def __init__(self):
        self.coupons_timer = CouponsTimer()

    # # 随机ua
    # def ua_random(self):
    #     sys.path.append(os.path.abspath('.'))
    #     global ua
    #     for n in range(3):
    #         try:
    #             from jdUA import jdUA as ua
    #             break
    #         except:
    #             url = 'https://ghproxy.com/https://raw.githubusercontent.com/wuye999/myScripts/main/jd/jdUA.py'
    #             response = requests.get(url)
    #             with open('jdUA.py', "w+", encoding="utf-8") as f:
    #                 f.write(response.text)


    def make_coupons(self):
        global local_time, str, resp_json
        """财富岛"""
        # url ="https://m.jingxi.com/jxbfd/user/ExchangePrize?strZone=jxbfd&bizCode=jxbfd&source=jxbfd&dwEnv=7&_cfd_t=${Date.now()}&ptag=138631.135.2&dwType=3&dwLvl=3&ddwPaperMoney=100000&strPoolName=jxcfd2_exchange_hb_202110&strPgtimestamp=1635495013684&strPhoneID=ab4af355fcf9b9659a829edb6db99dbc125aa321&strPgUUNum=c51bf2105570a8c306833384b57c31aa&_stk=_cfd_t,bizCode,ddwPaperMoney,dwEnv,dwLvl,dwType,ptag,source,strPgUUNum,strPgtimestamp,strPhoneID,strPoolName,strZone&_ste=1&h5st=20211029161013693;7757045245101162;10032;tk01w8e541b0730nc0UaArhpGysmVi+DB+j6rig/IW3G6rJf4Pu2PRcBW2EsHfRm9qlyDv/CAAMiWXGuHFA3bG0RiV0R;a8c85b7b6e49341c3fe189debf9c6565d71b9ed1bddb684ca9f4c13fe414fdbf&_=${Date.now()}&sceneval=2&g_login_type=1&callback=jsonpCBKL&g_ty=ls"
        # url = "https://m.jingxi.com/jxbfd/${fn}?strZone=jxbfd&bizCode=jxbfd&source=jxbfd&dwEnv=7&_cfd_t=${Date.now()}&ptag=7155.9.47&dwLvl=3&ddwPaperMoney=100000&strPoolName=jxcfd2_exchange_hb_202110&strPgtimestamp=${Date.now()}&_stk=${encodeURIComponent(stk)}"
        # url = 'https://m.jingxi.com/jxbfd/user/ExchangePrize?strZone=jxbfd&bizCode=jxbfd&source=jxbfd&dwEnv=7&_cfd_t=1632924011248&ptag=7155.9.47&dwType=3&dwLvl=3&ddwPaperMoney=100000&strPoolName=jxcfd2_exchange_hb_202110&strPgtimestamp=1632924011216&strPhoneID=3f092daf5202a681&strPgUUNum=d18883c067ad1fd1299545f0b0786143&_stk=_cfd_t%2CbizCode%2CddwPaperMoney%2CdwEnv%2CdwLvl%2CdwType%2Cptag%2Csource%2CstrPgUUNum%2CstrPgtimestamp%2CstrPhoneID%2CstrPoolName%2CstrZone&_ste=1&h5st=20210929220011248%3B9225930342578161%3B10032%3Btk01w9b641bbb30nTfJ9PqOZbo7j2qUoj77OqQf4JbpxQFpJGNX0TUHzeZJs0tTkF697FsOBgFlP9%2Fm%2FPMVZwV5pOxwC%3Bb1759a02c174496e076cb0ccfad0ce0a0c5c9aeb22054de4f8c7116fd6a38f05&_=1632924011249&sceneval=2&g_login_type=1&callback=jsonpCBKUUU&g_ty=ls'

        # 29-8
        url = "https://api.m.jd.com/.clientaction?functionId=newBabelAwardCollection&body={%22activityId%22:%223H885vA4sQj6ctYzzPVix4iiYN2P%22,%22scene%22:%221%22,%22args%22:%22key=6102ED3D9BC7C8DFF14D1A36FFA89602070B138DF76D200B6FA411359FBAD50B1FD83787E7C9BEF8843A4631ADF6C792_bingo,roleId=20E136F5EB78E9D323CEA65000B08718_bingo%22}&client=wh5"

         # 10-4
        # url = "https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&body={%22activityId%22:%223H885vA4sQj6ctYzzPVix4iiYN2P%22,%22scene%22:%221%22,%22args%22:%22key=9F77A904F38D9D2EA7968850FE8E4CF8408EF50BCE7C6FF518E48C3F1453D4DDDE2267491E3A0134A4B3422E11261222_bingo,roleId=F922BBE3F2239AD921A7360D331C1010_bingo,strengthenKey=1F8BE8DDD0A23DC1319EDF748BF6ADB85B6A62496F724698639AC28B152C59AE04387D83B0F994E5DFE927C54FEE03D0_bingo%22,%22mitemAddrId%22:%22%22,%22geo%22:{%22lng%22:%22%22,%22lat%22:%22%22}}&client=wh5&clientVersion=1.0.0"
        headers = {
            'Host': 'api.m.jd.com',
            'sec-fetch-mode': 'no-cors',
            'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
            'accept': '*/*',
            'x-requested-with': 'com.jd.pingou',
            'sec-fetch-site': 'same-site',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'pt_key=AAJiGcrcADCldhst6DTuZi4bSDJi4em7GwR1khTbT0_FaNZ_nKGb4QgJizUN2gFCkLQseKDl9nA; pt_pin=jd_58c7396bf1d5c;'
        }

        while True:
            self.coupons_timer.start()
            i = 0
            while True:
                try:
                    resp = requests.get(url=url, headers=headers, verify=False)
                    # i = i + 1
                    # if i > 10:
                    #     break
                    resp_json = parse_json(resp.text)
                    print(resp_json)
                    if "很抱歉" in resp.text or "领取成功" in resp.text:
                        return False
                    # if str(resp_json).find('抢到') != -1:
                    #     return False
                    # time.sleep(0.001)
                    d = datetime.datetime.fromtimestamp(self.coupons_timer.meituan_time() / 1000)
                    # 精确到毫秒
                    str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
                    print(str1)
                except Exception as e:
                    print(e)


    def coupons(self, work_count=10):
        print('财富岛!')
        with ProcessPoolExecutor(work_count) as pool:
            for i in range(work_count):
                time.sleep(0.050)
                pool.submit(self._coupons)

    def _coupons(self):
        """
        抢券
        """
        while True:
            try:
                # self.ua_random()
                self.make_coupons()
                break
            except Exception as e:
                print('抢券异常!', e)

