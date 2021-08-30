# -*- coding: UTF-8 -*-
import requests

from meituan_logger import logger
from coupons_timer import CouponsTimer
from config import global_config
from concurrent.futures import ProcessPoolExecutor
from util import (
    parse_json,
    wait_some_time
)


class Meituan(object):
    def __init__(self):
        self.coupons_timer = CouponsTimer()

    def make_coupons(self):
        global local_time, str, resp_json
        """美团"""
        meituan = 'https://cube.meituan.com/topcube/api/toc/playWay/preSendCoupon?k=84843'
        payload = {
            'callback': 'fetchJSON',
            # 'sku': self.sku_id,
            # '_': str(int(time.time() * 1000)),
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 TitansX/20.0.1.old KNB/1.0 iOS/14.7.1 meituangroup/com.meituan.imeituan/11.12.405 meituangroup/11.12.405 App/10110/11.12.405 iPhone/iPhoneXR WKWebView',
            "Content-Type": 'application/json',
            'Host': 'cube.meituan.com',
            'Referer': 'https://mop.meituan.com/awp/hfe/block/35daf4df68c6/84843/index.html?shark=1&activityId=6&src=group_start_pic&linglongScene=%E6%94%BE%E8%82%86%E5%90%83%E5%96%9D&uuid=000000000000025C2125F5C034EA693AD4F1F90EE3C83A155914936627232000&version_name=11.12.405&utm_term=11.12.405&utm_source=AppStore&utm_content=000000000000025C2125F5C034EA693AD4F1F90EE3C83A155914936627232000&userid=297782217&utm_medium=iphone&lat=39.921832&utm_campaign=AgroupBgroupD200H0&token=7X2QO0HJs9ZqfZNKZ75hmjIBvGsAAAAATQ4AAL3wwqnn5UamIKp7ZFgMT2F8zBdGcSI_Juyr0AQyBIGHFyXnnlxcBiIVjERryneEDA&language=zh-CN&regionid=&lng=116.475296&f=iphone&ci=1&msid=9A12EAA8-DADD-4049-8D4E-88279ED799871630047511212912',
            # 'cookie': '__jdu=16208764115771539430091; areaId=1; ipLoc-djd=1-3065-0-0; shshshfpa=73f33e1e-79c9-fa5f-a2e4-ad8d23722843-1620876412; shshshfpb=qPe52husztho0W2g8nVE2jA%3D%3D; unpl=V2_ZzNtbUZeRxwiCRUAfhkPDWIGRw9LB0UcJgpCB3JJCAM0VhdcclRCFnUUR1BnGVoUZwYZWEtcRxNFCEdkexhdBWYHE1xEVXMXfA5HUnIpbAZnMxNtQlBAFHwOQVF7GVgDYQMWX0pSQRR0AEZkSxlUAlczIl1LX0MQcAlDV3MpXARnAhptQ2cIe3RFRlN4GFUDYAYSXUZRRRVxCk5ReRhdDWczE21B; __jdv=122270672|kong|t_1001050073_387078|jingfen|5858f0be41b944dc8a78b35b8ae7bd40|1621234138504; __jdc=76161171; retina=1; cid=9; webp=1; mba_muid=16208764115771539430091; visitkey=18760757834574002; jcap_dvzw_fp=lhemSFuzpHX8pcrFLvnxQfr0h3dXbasdh4le2QKDKk5Sbu3zKwBuB1RydWCpgMho8OAKUA==; whwswswws=; PPRD_P=UUID.16208764115771539430091; sc_width=1440; 3AB9D23F7A4B3C9B=BZ4GZNB46MAEGBEXXGBOFRWMO4WU2NWC6NNWIUD3A7IU3MXYYDB5ISYR33R2BRSC4P2LY3EE4QO7DYXUXCXFZ7V4FY; __jda=76161171.16208764115771539430091.1620876412.1621433070.1621480007.5; TrackerID=T_5xR-fJiW-GexJNpbDejHrPTqZ4t6QBhFpycREg04WFTxKRyc4P1PX-ygSxdzDf0cW6HSuExxl11YwrMDrjvUzeRr2US3wdX8Qkl6TkamIFXNJO5VaNkRNQ1UqOCb0Q; pt_key=AAJgpdKfADCDO1sqROnutA1Ax_dvo75JQBsK5o8_ZOol2S4BhHBAM4EYNjlKUOhmrXBfIJwyB0o; pt_pin=jd_58c7396bf1d5c; pt_token=3u8ttfet; pwdt_id=jd_58c7396bf1d5c; sfstoken=tk01mde2c1d18a8sMXgyKzIrMSszh+tyu3l4k8EZ8dsNYvH8U5tP2wSNIjjz1VctKBMqVzCLWJ2WdXQNjrrr+yqxS5BC; RT="z=1&dm=jd.com&si=jtri2jl7eht&ss=kowbc24b&sl=1&tt=0&nu=d41d8cd98f00b204e9800998ecf8427e&cl=1qr5&obo=1&ld=1s4h&r=0b28ea838121668d9fe0076f8ba4b475&ul=1s4k&hd=1t0a"; __wga=1621480099364.1621480099364.1621433070268.1621419292139.1.3; shshshfp=51cf1daf073dd46f3a51cb59d480c95e',
            'cookie': '_lxsdk_cuid=17a425b8e06c8-0a0938b9457e01-34647600-13c680-17a425b8e06c8; unpl=v1_ikrjJyKoarlq159nDVkD0OVaT_kxGdyM5R8rBvNPwu4NyeFHzlUya4QptSIEfb-_; _ga=GA1.2.2031100322.1627986515; IJSESSIONID=node01pbmi4oesvmzn178j6daglcmqk10931517; iuuid=8122E0C31D7EFB166EC4113E04010352F31AB52AC7174E6A5A03F6B909F25D89; ci=1; cityname=%E5%8C%97%E4%BA%AC; _lxsdk=8122E0C31D7EFB166EC4113E04010352F31AB52AC7174E6A5A03F6B909F25D89; __utmc=74597006; ci3=1; meishi_ci=1; cityid=1; _hc.v=b372a487-c507-ed72-ef60-00f6fe7cc211.1629425949; wm_order_channel=mtib; utm_source=60030; au_trace_key_net=default; openh5_uuid=8122E0C31D7EFB166EC4113E04010352F31AB52AC7174E6A5A03F6B909F25D89; __utma=74597006.2031100322.1627986515.1629425927.1630142040.2; __utmz=74597006.1630142040.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); backurl=http://i.meituan.com/account/?cevent=imt%2Fft%2Forder; uuid=1cd1c036d5e641518dd3.1630142053.1.0.0; a2h=1; cssVersion=83d2813d; request_source=openh5; channelType={%22mtib%22:%220%22}; channelConfig={%22channel%22:%22default%22%2C%22type%22:0%2C%22fixedReservation%22:{%22reservationTimeStatus%22:0%2C%22startReservationTime%22:0%2C%22endReservationTime%22:0}}; latlng=40.005727,116.564669,1630142063284; i_extend=Gimthomepagecategory122H__a100001__b2; token=evkocTUlatz8y6MTb3Or0ertNDQAAAAAbg4AAIbdWsT2KkMUSGPofdhs6cU9xiyTPTitxsB5JZEEiUOS3-eQvQ98akeheWqRju4NNg; mt_c_token=evkocTUlatz8y6MTb3Or0ertNDQAAAAAbg4AAIbdWsT2KkMUSGPofdhs6cU9xiyTPTitxsB5JZEEiUOS3-eQvQ98akeheWqRju4NNg; oops=evkocTUlatz8y6MTb3Or0ertNDQAAAAAbg4AAIbdWsT2KkMUSGPofdhs6cU9xiyTPTitxsB5JZEEiUOS3-eQvQ98akeheWqRju4NNg; userId=297782217; u=297782217; isid=evkocTUlatz8y6MTb3Or0ertNDQAAAAAbg4AAIbdWsT2KkMUSGPofdhs6cU9xiyTPTitxsB5JZEEiUOS3-eQvQ98akeheWqRju4NNg; _lx_utm=utm_term%3D11.12.405%26utm_source%3DAppStore%26utm_content%3D000000000000025C2125F5C034EA693AD4F1F90EE3C83A155914936627232000%26utm_medium%3Diphone%26utm_campaign%3DAgroupBgroupD200H0; _lxsdk_s=17b8c39bc58-bd1-215-88a%7C%7C142'
        }

        strrr = {"playWaySecrets": "b661905148", "sourceType": "MEI_TUAN", "userId": "297782217",
                 "requestTime": 1630145254522, "nonceRandom": "ccf64bd2-6c15-12ae-8453-332713f301fa",
                 "requestSign": "cGxheVdheVNpZ24sTVRZek1ERTBOVEkxTkRVeU1peGpZMlkyTkdKa01pMDJZekUxTFRFeVlXVXRPRFExTXkwek16STNNVE5tTXpBeFptRT0=",
                 "cubeActivityUrl": "https://mop.meituan.com/awp/hfe/block/35daf4df68c6/84843/index.html?shark=1&activityId=6&src=group_start_pic&linglongScene=%E6%83%85%E4%BE%A3%E7%BA%A6%E4%BC%9A&uuid=000000000000025C2125F5C034EA693AD4F1F90EE3C83A155914936627232000&version_name=11.12.405&utm_term=11.12.405&utm_source=AppStore&utm_content=000000000000025C2125F5C034EA693AD4F1F90EE3C83A155914936627232000&userid=297782217&utm_medium=iphone&lat=40.045968&utm_campaign=AgroupBgroupD200H0&token=7X2QO0HJs9ZqfZNKZ75hmjIBvGsAAAAATQ4AAL3wwqnn5UamIKp7ZFgMT2F8zBdGcSI_Juyr0AQyBIGHFyXnnlxcBiIVjERryneEDA&language=zh-CN&regionid=&lng=116.460565&f=iphone&ci=1&msid=9A12EAA8-DADD-4049-8D4E-88279ED799871630141995916754&userId=297782217&token=evkocTUlatz8y6MTb3Or0ertNDQAAAAAbg4AAIbdWsT2KkMUSGPofdhs6cU9xiyTPTitxsB5JZEEiUOS3-eQvQ98akeheWqRju4NNg",
                 "cubeActivityId": 84843}

        # logger.info(json.loads(str))

        # j = json.dumps(json.loads(strrr))

        while True:
            self.coupons_timer.start()
            while True:
                try:
                    resp = requests.post(url=meituan, headers=headers, json=strrr)
                    resp_json = parse_json(resp.text)
                    logger.info(resp_json)

                except Exception as e:
                    logger.info(e)
                if str(resp_json).find('抢到') != -1:
                    return True

    def coupons(self, work_count=3):
        print('coupons!')
        with ProcessPoolExecutor(work_count) as pool:
            for i in range(work_count):
                pool.submit(self._coupons)

    def _coupons(self):
        """
        抢券
        """
        while True:
            try:
                self.make_coupons()
                break
            except Exception as e:
                logger.info('抢券异常!', e)
            wait_some_time()
