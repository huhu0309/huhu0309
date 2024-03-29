
"""
File: mxshl.py
作者：胡胡
cron:  0 23 * * *
new Env('明星送好礼');
"""


import os
import requests
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(message)s')
cookies = []
def getCookie():
    global cookies
    try:
        if "JD_COOKIE" in os.environ:
            if len(os.environ["JD_COOKIE"]) > 10:
                cookies.append(os.environ["JD_COOKIE"])
                # logging.info("当前从环境变量获取CK")
                return cookies
    except Exception as e:
        logging.error(f"【getCookie Error】{e}")

host="https://api.m.jd.com/?"
def guanzhu(cookie):
    url = host+"uuid=&client=wh5&area=7_446_453_56899&appid=ProductZ4Brand&functionId=superBrandDoTask&t=1692605705915&body=%7B%22source%22:%22star_gift%22,%22activityId%22:1014124,%22encryptProjectId%22:%223WV2aobWDbvTEYNBHJrYjRw7Reut%22,%22encryptAssignmentId%22:%224Jd5XTB2ismSvkRMPMfS2rZ6sX7c%22,%22assignmentType%22:3,%22itemId%22:%221000396688%22,%22actionType%22:0%7D"
    headers = {
        # "User-Agent": "jdapp;android;12.0.4;;;M/5.0;appBuild/98801;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1690788509997%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJC%3D%22%2C%22ad%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%2C%22od%22%3A%22CQU0DWU5DzU5YzTuDNZwCwUzCzHwZWHsEQVuDWSyDWOzDWYyEWSyCwPuCQDvDzq2YwYyDJVrDNU4EQUnDJuzDG%3D%3D%22%2C%22ov%22%3A%22CzC%3D%22%2C%22ud%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 13; V2217A Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12.0.1; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://prodev.m.jd.com",
        "X-Requested-With": "com.jingdong.app.mall",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://prodev.m.jd.com/mall/active/31GFSKyRbD3ehsHih2rQKArxfb8c/index.html?_ts=1690765991542&utm_user=plusmember&gx=RnAomTM2LVWwrvJT-dYDGRJj5V-Y_g&gxd=RnAox2IPajKNy5Ecq4ByCETF_bPgQ-s&ad_od=share&cu=true&rid=10109&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001695162_&utm_term=551d43b3fb0c4789b36104454b857518&tttparams=oYS7DFeyJhZGRyZXNzSWQiOjE0OTIzNDIxMDQsImRMYXQiOjAsImRMbmciOjAsImdMYXQiOiIzNS4xODciLCJnTG5nIjoiMTEzLjI3MTg3NSIsImdwc19hcmVhIjoiN180NDZfNDUzXzU2OTAxIiwibGF0IjozNS4xOTgzODEsImxuZyI6MTEzLjI2NzY5LCJtb2RlbCI6IlYyMjE3QSIsInBvc0xhdCI6IjM1LjE4NyIsInBvc0xuZyI6IjExMy4yNzE4NzUiLCJwcnN0YXRlIjoiMCIsInVlbXBzIjoiMC0wLTAiLCJ1bl9hcmVhIjoiN180NDZfNDUzXzU2ODk5In60%3D",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        # "Cookie": 'pwdt_id=jd_urdgJLbxpbcJ; retina=1; cid=8; appCode=msc588d6d5; webp=1; visitkey=7216260516063572129; __jdc=122270672; __wga=1689953648535.1689953648535.1689953648535.1689953648535.1.1; sc_width=360; shshshfpa=a23b4f44-51db-b97a-1ab9-28c99c1eecf7-1684824891; shshshfpx=a23b4f44-51db-b97a-1ab9-28c99c1eecf7-1684824891; 3AB9D23F7A4B3C9B=EAJGBXSZ2H37SULAL2J2IUVKN2IVJ2YF7JY5BG36QND2FRQ54FG67SVZ6WWYMWXUKC2DJHREVX3JJU3QXFBG4Q5TEA; b_dw=360; b_dpr=3; b_webp=1; b_avif=1; unionwsws=%7B%22devicefinger%22%3A%22eidA376f8122b2s7qTyuaJnjSo%2BMchAXcOMUQqk8r%2BkctNeaucoXYxs9SLXSnaGZSKmMYkNhO5ZJ6g1XXZjHb%2BwEQJyh%2BvWV96wUk9%2FSXshR4W%2B4X1Jw%22%7D; CCC_SE=; pt_pin=jd_urdgJLbxpbcJ; sid=; RT="z=1&dm=jd.com&si=nnup57ektkq&ss=lkhjwfbk&sl=1&tt=1ad&ld=1az"; share_cpin=; share_open_id=; share_gpin=; channel=; source_module=; erp=; qid_uid=c9553909-cb64-420f-aaf8-b3a70699bd31; qid_fs=1690385939653; TARGET_UNIT=squnit; plusCustomBuryPointToken=1690475977476_4020; shshshfpv=JD012145b9DH09KuGj3n169047611060301XCMiRvCQH7dVHkpJCGC_kHHyuoILaMC20DCWB7WjxjaKJS9byN-H9ZETAI9kFy0_BpIIuLBKx-BP6qD54DgFvA0kxea5r~y0ely6IENsLJ6AV1yyd0tFIltDLkWECvOIwFS6Qajz6HwnFPCFUiOPjc49oC2MFke5tHmYyc9mjh9TNSciVPGvfygz8mTrr9eW6ZZj0QtR5liiIKLnq9winsiAaNLubnq7GnSVAV4FSKeHrBBhsOI-Q; shshshfpb=wI4RehtVbp73sgKv2JJ3fnA; joyya=1690557195.1690557195.51.119eqkn; jcap_dvzw_fp=9P_R1zadhoYvqOfdQp9lMoqZe10q6jma-ZXN_nQpURqaaj2nmhFMsQbq5IG0ji9GKa7p2ug7I3xRo_iVROhDXg==; pt_key=app_openAAJkxgmtADDizQXNjXivavxbbOG3Qcr7VDWu3A_3Mxy3fACdf4lGoC7m579BuAQpC8_JDW6cfwk; wxa_level=1; p-request-id=jd_urdgJLbxpbcJ2023073100qre1k1Gfhe; BT_INDEX_SHOWNOTIFY=false; BT_INDEX_ISCAR=false; BT_INDEX_SHOWRIGHTPAGE=true; qid_ls=1690767763716; qid_ts=1690771946594; qid_vis=6; __jda=122270672.16899536483861133698671.1689953648.1690767765.1690788513.26; pre_session=bP37BBfGovpHa9kPocD4sKxnUb+boLut|6887; pre_seq=2; 3AB9D23F7A4B3CSS=jdd03EAJGBXSZ2H37SULAL2J2IUVKN2IVJ2YF7JY5BG36QND2FRQ54FG67SVZ6WWYMWXUKC2DJHREVX3JJU3QXFBG4Q5TEAAAAAMJVLMUN3YAAAAACPEPQJPDKOCGUIX; _gia_d=1; b_dh=719; mba_sid=4878.13; __jdb=122270672.3.16899536483861133698671|26.1690788513; __jdv=122270672%7Ckong%7Ct_1001695162_%7Cjingfen%7C551d43b3fb0c4789b36104454b857518%7C1690788505916; unpl=JF8EAKhnNSttXE9UUB4ASBBHGFwGW1sBQ0QBaGcEUVhcTgcMHwQfEhl7XlVdXxRKER9tZxRUWVNIXQ4YBysSEHtdVV9dD0MTA2hkNWRdWUpUBBwLGBsSe15Ublw4SxALbmEMXVlZTlAGHQoSGhBPVVBeXDhKJwNnYDVkbVl7VAQbAxMiEktcVV9YDk8TCl8sa1UQWExcBB0LEhYRTllXWFUBQxcHZ2MFVW1Ze1c%7CJF8EAKxnNSttWk9cDRsKSUITHlRUWw8NQ0dWZmcEXV0KGVNSTAcTEUR7XlVdXxRKEB9sYhRUXVNLVw4bASsSFHteVV1ZCkMXA2tvNVRYWENcBR4FKxIVSTNWWVUNSxMFb2JrVF02JVFrKwEbIhF7VVRYXQFDElc9YwZXWA9KXTUaMhITIEtcVV9YDUoTA21uAWRtWXtVNRoyUHwRBlVUWF0BQxJXPWMGV1gPSl01GjIb; __jd_ref_cls=Babel_H5FirstClick; mba_muid=16899536483861133698671.4878.1690788541760'
        "Cookie":cookie
    }
    response = requests.post(url, headers=headers)
    # print(response.status_code)
    # print(response.text)

def wanchen(cookie):
    url = host+"uuid=&client=wh5&area=7_446_453_56899&appid=ProductZ4Brand&functionId=superBrandDoTask&t=1692605775926&body=%7B%22source%22:%22star_gift%22,%22activityId%22:1014124,%22encryptProjectId%22:%223WV2aobWDbvTEYNBHJrYjRw7Reut%22,%22encryptAssignmentId%22:%223uQzzP3gpqZaPndMg47nf3oxTy2r%22,%22assignmentType%22:1,%22itemId%22:%222301817939%22,%22actionType%22:0%7D"
    headers = {
        "User-Agent": "jdapp;android;12.0.4;;;M/5.0;appBuild/98801;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1690788509997%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJC%3D%22%2C%22ad%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%2C%22od%22%3A%22CQU0DWU5DzU5YzTuDNZwCwUzCzHwZWHsEQVuDWSyDWOzDWYyEWSyCwPuCQDvDzq2YwYyDJVrDNU4EQUnDJuzDG%3D%3D%22%2C%22ov%22%3A%22CzC%3D%22%2C%22ud%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 13; V2217A Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://prodev.m.jd.com",
        "X-Requested-With": "com.jingdong.app.mall",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://prodev.m.jd.com/mall/active/31GFSKyRbD3ehsHih2rQKArxfb8c/index.html?_ts=1690765991542&utm_user=plusmember&gx=RnAomTM2LVWwrvJT-dYDGRJj5V-Y_g&gxd=RnAox2IPajKNy5Ecq4ByCETF_bPgQ-s&ad_od=share&cu=true&rid=10109&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001695162_&utm_term=551d43b3fb0c4789b36104454b857518&tttparams=oYS7DFeyJhZGRyZXNzSWQiOjE0OTIzNDIxMDQsImRMYXQiOjAsImRMbmciOjAsImdMYXQiOiIzNS4xODciLCJnTG5nIjoiMTEzLjI3MTg3NSIsImdwc19hcmVhIjoiN180NDZfNDUzXzU2OTAxIiwibGF0IjozNS4xOTgzODEsImxuZyI6MTEzLjI2NzY5LCJtb2RlbCI6IlYyMjE3QSIsInBvc0xhdCI6IjM1LjE4NyIsInBvc0xuZyI6IjExMy4yNzE4NzUiLCJwcnN0YXRlIjoiMCIsInVlbXBzIjoiMC0wLTAiLCJ1bl9hcmVhIjoiN180NDZfNDUzXzU2ODk5In60%3D",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie":cookie
    }

    response = requests.post(url, headers=headers)

    # print(response.status_code)
    # print(response.text)

def linqu(cookie):
    url = host+"uuid=&client=wh5&area=7_446_453_56899&appid=ProductZ4Brand&functionId=superBrandDoTask&t=1692605762462&body=%7B%22source%22:%22star_gift%22,%22activityId%22:1014124,%22encryptProjectId%22:%223WV2aobWDbvTEYNBHJrYjRw7Reut%22,%22encryptAssignmentId%22:%223uQzzP3gpqZaPndMg47nf3oxTy2r%22,%22assignmentType%22:1,%22itemId%22:%222301817939%22,%22actionType%22:1%7D"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "jdapp;android;12.0.4;;;M/5.0;appBuild/98801;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1690788509997%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJC%3D%22%2C%22ad%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%2C%22od%22%3A%22CQU0DWU5DzU5YzTuDNZwCwUzCzHwZWHsEQVuDWSyDWOzDWYyEWSyCwPuCQDvDzq2YwYyDJVrDNU4EQUnDJuzDG%3D%3D%22%2C%22ov%22%3A%22CzC%3D%22%2C%22ud%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 13; V2217A Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Origin": "https://prodev.m.jd.com",
        "X-Requested-With": "com.jingdong.app.mall",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://prodev.m.jd.com/mall/active/31GFSKyRbD3ehsHih2rQKArxfb8c/index.html?_ts=1690765991542&utm_user=plusmember&gx=RnAomTM2LVWwrvJT-dYDGRJj5V-Y_g&gxd=RnAox2IPajKNy5Ecq4ByCETF_bPgQ-s&ad_od=share&cu=true&rid=10109&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001695162_&utm_term=551d43b3fb0c4789b36104454b857518&tttparams=oYS7DFeyJhZGRyZXNzSWQiOjE0OTIzNDIxMDQsImRMYXQiOjAsImRMbmciOjAsImdMYXQiOiIzNS4xODciLCJnTG5nIjoiMTEzLjI3MTg3NSIsImdwc19hcmVhIjoiN180NDZfNDUzXzU2OTAxIiwibGF0IjozNS4xOTgzODEsImxuZyI6MTEzLjI2NzY5LCJtb2RlbCI6IlYyMjE3QSIsInBvc0xhdCI6IjM1LjE4NyIsInBvc0xuZyI6IjExMy4yNzE4NzUiLCJwcnN0YXRlIjoiMCIsInVlbXBzIjoiMC0wLTAiLCJ1bl9hcmVhIjoiN180NDZfNDUzXzU2ODk5In60%3D",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie":cookie

    }
    response = requests.post(url, headers=headers)

    # print(response.status_code)
    # print(response.text)

def liulan1(cookie):
    url = host+"uuid=&client=wh5&area=7_446_453_56899&appid=ProductZ4Brand&functionId=superBrandDoTask&t=1692605940910&body=%7B%22source%22:%22star_gift%22,%22activityId%22:1014124,%22encryptProjectId%22:%223WV2aobWDbvTEYNBHJrYjRw7Reut%22,%22encryptAssignmentId%22:%222DzzS4iHDNAh5WGMmAPGzYBQPQ5X%22,%22assignmentType%22:1,%22itemId%22:%22100056452802%22,%22actionType%22:0%7D"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "jdapp;android;12.0.4;;;M/5.0;appBuild/98801;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1690788509997%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJC%3D%22%2C%22ad%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%2C%22od%22%3A%22CQU0DWU5DzU5YzTuDNZwCwUzCzHwZWHsEQVuDWSyDWOzDWYyEWSyCwPuCQDvDzq2YwYyDJVrDNU4EQUnDJuzDG%3D%3D%22%2C%22ov%22%3A%22CzC%3D%22%2C%22ud%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 13; V2217A Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Origin": "https://prodev.m.jd.com",
        "X-Requested-With": "com.jingdong.app.mall",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://prodev.m.jd.com/mall/active/31GFSKyRbD3ehsHih2rQKArxfb8c/index.html?_ts=1690765991542&utm_user=plusmember&gx=RnAomTM2LVWwrvJT-dYDGRJj5V-Y_g&gxd=RnAox2IPajKNy5Ecq4ByCETF_bPgQ-s&ad_od=share&cu=true&rid=10109&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001695162_&utm_term=551d43b3fb0c4789b36104454b857518&tttparams=oYS7DFeyJhZGRyZXNzSWQiOjE0OTIzNDIxMDQsImRMYXQiOjAsImRMbmciOjAsImdMYXQiOiIzNS4xODciLCJnTG5nIjoiMTEzLjI3MTg3NSIsImdwc19hcmVhIjoiN180NDZfNDUzXzU2OTAxIiwibGF0IjozNS4xOTgzODEsImxuZyI6MTEzLjI2NzY5LCJtb2RlbCI6IlYyMjE3QSIsInBvc0xhdCI6IjM1LjE4NyIsInBvc0xuZyI6IjExMy4yNzE4NzUiLCJwcnN0YXRlIjoiMCIsInVlbXBzIjoiMC0wLTAiLCJ1bl9hcmVhIjoiN180NDZfNDUzXzU2ODk5In60%3D",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie":cookie

    }

    response = requests.post(url, headers=headers)
    # print(response.status_code)
    # print(response.text)
def liulan2(cookie):
    url = host+"uuid=&client=wh5&area=7_446_453_56899&appid=ProductZ4Brand&functionId=superBrandDoTask&t=1692605974402&body=%7B%22source%22:%22star_gift%22,%22activityId%22:1014124,%22encryptProjectId%22:%223WV2aobWDbvTEYNBHJrYjRw7Reut%22,%22encryptAssignmentId%22:%222DzzS4iHDNAh5WGMmAPGzYBQPQ5X%22,%22assignmentType%22:1,%22itemId%22:%22100029082004%22,%22actionType%22:0%7D"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "jdapp;android;12.0.4;;;M/5.0;appBuild/98801;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1690788509997%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJC%3D%22%2C%22ad%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%2C%22od%22%3A%22CQU0DWU5DzU5YzTuDNZwCwUzCzHwZWHsEQVuDWSyDWOzDWYyEWSyCwPuCQDvDzq2YwYyDJVrDNU4EQUnDJuzDG%3D%3D%22%2C%22ov%22%3A%22CzC%3D%22%2C%22ud%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 13; V2217A Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Origin": "https://prodev.m.jd.com",
        "X-Requested-With": "com.jingdong.app.mall",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://prodev.m.jd.com/mall/active/31GFSKyRbD3ehsHih2rQKArxfb8c/index.html?_ts=1690765991542&utm_user=plusmember&gx=RnAomTM2LVWwrvJT-dYDGRJj5V-Y_g&gxd=RnAox2IPajKNy5Ecq4ByCETF_bPgQ-s&ad_od=share&cu=true&rid=10109&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001695162_&utm_term=551d43b3fb0c4789b36104454b857518&tttparams=oYS7DFeyJhZGRyZXNzSWQiOjE0OTIzNDIxMDQsImRMYXQiOjAsImRMbmciOjAsImdMYXQiOiIzNS4xODciLCJnTG5nIjoiMTEzLjI3MTg3NSIsImdwc19hcmVhIjoiN180NDZfNDUzXzU2OTAxIiwibGF0IjozNS4xOTgzODEsImxuZyI6MTEzLjI2NzY5LCJtb2RlbCI6IlYyMjE3QSIsInBvc0xhdCI6IjM1LjE4NyIsInBvc0xuZyI6IjExMy4yNzE4NzUiLCJwcnN0YXRlIjoiMCIsInVlbXBzIjoiMC0wLTAiLCJ1bl9hcmVhIjoiN180NDZfNDUzXzU2ODk5In60%3D",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }

    response = requests.post(url, headers=headers)

    # print(response.status_code)
    # print(response.text)


def liulan3(cookie):
    url = host+"uuid=&client=wh5&area=7_446_453_56899&appid=ProductZ4Brand&functionId=superBrandDoTask&t=1692606007139&body=%7B%22source%22:%22star_gift%22,%22activityId%22:1014124,%22encryptProjectId%22:%223WV2aobWDbvTEYNBHJrYjRw7Reut%22,%22encryptAssignmentId%22:%222DzzS4iHDNAh5WGMmAPGzYBQPQ5X%22,%22assignmentType%22:1,%22itemId%22:%22100060880861%22,%22actionType%22:0%7D"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "jdapp;android;12.0.4;;;M/5.0;appBuild/98801;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1690788509997%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJC%3D%22%2C%22ad%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%2C%22od%22%3A%22CQU0DWU5DzU5YzTuDNZwCwUzCzHwZWHsEQVuDWSyDWOzDWYyEWSyCwPuCQDvDzq2YwYyDJVrDNU4EQUnDJuzDG%3D%3D%22%2C%22ov%22%3A%22CzC%3D%22%2C%22ud%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 13; V2217A Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Origin": "https://prodev.m.jd.com",
        "X-Requested-With": "com.jingdong.app.mall",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://prodev.m.jd.com/mall/active/31GFSKyRbD3ehsHih2rQKArxfb8c/index.html?_ts=1690765991542&utm_user=plusmember&gx=RnAomTM2LVWwrvJT-dYDGRJj5V-Y_g&gxd=RnAox2IPajKNy5Ecq4ByCETF_bPgQ-s&ad_od=share&cu=true&rid=10109&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001695162_&utm_term=551d43b3fb0c4789b36104454b857518&tttparams=oYS7DFeyJhZGRyZXNzSWQiOjE0OTIzNDIxMDQsImRMYXQiOjAsImRMbmciOjAsImdMYXQiOiIzNS4xODciLCJnTG5nIjoiMTEzLjI3MTg3NSIsImdwc19hcmVhIjoiN180NDZfNDUzXzU2OTAxIiwibGF0IjozNS4xOTgzODEsImxuZyI6MTEzLjI2NzY5LCJtb2RlbCI6IlYyMjE3QSIsInBvc0xhdCI6IjM1LjE4NyIsInBvc0xuZyI6IjExMy4yNzE4NzUiLCJwcnN0YXRlIjoiMCIsInVlbXBzIjoiMC0wLTAiLCJ1bl9hcmVhIjoiN180NDZfNDUzXzU2ODk5In60%3D",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }

    response = requests.post(url, headers=headers)
    # print(response.status_code)
    # print(response.text)
def choujiang(cookie):
    url = host+"uuid=&client=wh5&area=7_446_453_56899&appid=ProductZ4Brand&functionId=superBrandTaskLottery&t=1692606033541&body=%7B%22source%22:%22star_gift%22,%22activityId%22:1014124,%22encryptProjectId%22:%223WV2aobWDbvTEYNBHJrYjRw7Reut%22%7D"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "jdapp;android;12.0.4;;;M/5.0;appBuild/98801;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1690788509997%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJC%3D%22%2C%22ad%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%2C%22od%22%3A%22CQU0DWU5DzU5YzTuDNZwCwUzCzHwZWHsEQVuDWSyDWOzDWYyEWSyCwPuCQDvDzq2YwYyDJVrDNU4EQUnDJuzDG%3D%3D%22%2C%22ov%22%3A%22CzC%3D%22%2C%22ud%22%3A%22EJO3CJq5DQVtDJSyDQYmEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 13; V2217A Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046247 Mobile Safari/537.36",
        "Origin": "https://prodev.m.jd.com",
        "X-Requested-With": "com.jingdong.app.mall",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://prodev.m.jd.com/mall/active/31GFSKyRbD3ehsHih2rQKArxfb8c/index.html?_ts=1690765991542&utm_user=plusmember&gx=RnAomTM2LVWwrvJT-dYDGRJj5V-Y_g&gxd=RnAox2IPajKNy5Ecq4ByCETF_bPgQ-s&ad_od=share&cu=true&rid=10109&utm_source=kong&utm_medium=jingfen&utm_campaign=t_1001695162_&utm_term=551d43b3fb0c4789b36104454b857518&tttparams=oYS7DFeyJhZGRyZXNzSWQiOjE0OTIzNDIxMDQsImRMYXQiOjAsImRMbmciOjAsImdMYXQiOiIzNS4xODciLCJnTG5nIjoiMTEzLjI3MTg3NSIsImdwc19hcmVhIjoiN180NDZfNDUzXzU2OTAxIiwibGF0IjozNS4xOTgzODEsImxuZyI6MTEzLjI2NzY5LCJtb2RlbCI6IlYyMjE3QSIsInBvc0xhdCI6IjM1LjE4NyIsInBvc0xuZyI6IjExMy4yNzE4NzUiLCJwcnN0YXRlIjoiMCIsInVlbXBzIjoiMC0wLTAiLCJ1bl9hcmVhIjoiN180NDZfNDUzXzU2ODk5In60%3D",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie
    }

    response = requests.post(url, headers=headers).json()

    # print(response.status_code)
    # print(response.text)
    # logging.info(response)
    if response["data"]["bizMsg"]=="任务已完成":
        logging.info(response["data"]["bizMsg"])
    elif response["data"]["bizMsg"]=="任务成功":
        if response["data"]["result"]["rewards"] is None:
            logging.info("未获得奖励")
        else:
            logging.info("获取京豆"+str(response["data"]["result"]["rewards"][0]["beanNum"])+"个")
    else:
        logging.info(response)
data = getCookie()
if data:
    data_str = str(data[0])
    variable_list = data_str.split('&')
    logging.info("【【收留京东ck，自助上车：https://k557e25139.goho.co】】")
    logging.info("=====================总共"+str(len(variable_list))+"个账号===========================")
    for i in range(len(variable_list)):
        logging.info(f"【第{i+1}个账号】"+variable_list[i])
        try:
            guanzhu(variable_list[i])
            linqu(variable_list[i])
            logging.info("等待8秒完成任务")
            time.sleep(8)
            wanchen(variable_list[i])
            liulan1(variable_list[i])
            liulan2(variable_list[i])
            liulan3(variable_list[i])
            choujiang(variable_list[i])
        except:
            logging.info("ck失效或未知错误")
        time.sleep(2)
else:
    logging.error("未获取到Cookie信息")
