
"""
File: ww_red.py
作者：胡胡
新手上路，当前版本只能填一个ck兑换
每隔0.5秒并发抢三次，抢3秒共计16次
export ww_ck="需要兑换红包的完整ck"
export ww_red="需要兑换的红包金额，只能是3或者10" #未设置ww_red,默认查询账户余额
cron:  0 0 * * *
new Env('ww_red');
"""


import os
import sys
import requests
import concurrent.futures
import time


def send_request3():
   start_time1 = time.time()
   url = "https://api.m.jd.com"
   headers = {
    "Host": "api.m.jd.com",
    "Connection": "keep-alive",
    # "Content-Length": "444",
    # "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/x-www-form-urlencoded",
    # "Origin": "https://h5platform.jd.com",
    # "X-Requested-With": "com.jd.jdlite",
    # "Sec-Fetch-Site": "same-site",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Dest": "empty",
    # "User-Agent":"jdltapp;android;4.8.2;;;appBuild/2385;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1676203082208%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJS%3D%22%2C%22ad%22%3A%22YWO1Ztc5DtdsYtDrCtSzZK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22CzO%3D%22%2C%22ud%22%3A%22YWO1Ztc5DtdsYtDrCtSzZK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jd.jdlite%22%7D;Mozilla/5.0 (Linux; Android 12; V1981A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
    "User-Agent": "jdapp;iPhone;10.1.2;15.0;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
    "Referer": "https://h5platform.jd.com/",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": ww_ck
}
   data = {
    "functionId": "runningPrizeDraw",
    "body": '{"linkId":"L-sOanK_5RJCz7I314FpnQ","type":1,"level":2}',
    "t": "1676203113895",
    "appid": "activities_platform",
    # "client": "android",
    # "clientVersion": "4.8.2",
    # "cthr": "1",
    # "uuid": "1616536673936373-2626331623233346",
    # "build": "2385",
    # "screen": "360*803",
    # "networkType": "UNKNOWN",
    # "d_brand": "vivo",
    # "d_model": "V1981A",
    # "lang": "zh_CN",
    # "osVersion": "12",
    # "partner": "vivo",
    # "eid": "eidA24a2812335s6GtkpcKjHQnS3xUl8PRUd5BrZKvbuRCyPxjieOSAGndnPE%2B6nTsH0NVVuYlNfClwfMnTQGk5MTuu9oAV4KoAQyQKTmw4KOK9lZllL"
}
   response = requests.post(url, headers=headers, data=data)
   print(response.text)
   print("Start time1: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time1)))
   # print(ww_ck)


def send_request10():
    start_time2 = time.time()
    url = "https://api.m.jd.com/"

    headers = {
        "Connection": "keep-alive",
        "Content-Length": "326",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "jdapp;iPhone;10.1.2;15.0;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://h5platform.jd.com",
        "X-Requested-With": "com.jd.jdlite",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://h5platform.jd.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": ww_ck
    }

    data = {
        "functionId": "runningPrizeDraw",
        "body": "{\"linkId\":\"L-sOanK_5RJCz7I314FpnQ\",\"type\":1,\"level\":3}",
        "t": "1676613114449",
        "appid": "activities_platform",
        "client": "android",
        "clientVersion": "4.8.2",
        "cthr": "1",
        "uuid": "1616536673936373-2626331623233346",
        "build": "2385",
        "screen": "360*803",
        "networkType": "UNKNOWN",
        "d_brand": "vivo",
        "d_model": "V1981A",
        "lang": "zh_CN",
        "osVersion": "12",
        "partner": "vivo",
        "eid": ""
    }

    response2 = requests.post(url, headers=headers, data=data)

    print(response2.text)
    print("Start time2: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time2)))
    # print(ww_ck)
def check():
    url = "https://api.m.jd.com/?functionId=runningMyPrize&body={%22linkId%22:%22L-sOanK_5RJCz7I314FpnQ%22,%22pageSize%22:10,%22time%22:null,%22ids%22:null}&t=1676617870980&appid=activities_platform&client=android&clientVersion=4.8.2&cthr=1&uuid=1616536673936373-2626331623233346&build=2385&screen=360*803&networkType=UNKNOWN&d_brand=vivo&d_model=V1981A&lang=zh_CN&osVersion=12&partner=vivo&eid="

    headers = {
        "User-Agent": "jdapp;iPhone;10.1.2;15.0;network/wifi;Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1",
        "Origin": "https://h5platform.jd.com",
        "X-Requested-With": "com.jd.jdlite",
        "Referer": "https://h5platform.jd.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": ww_ck
    }

    res = requests.get(url=url, headers=headers).json()
    # print(res)
    print("剩余金额"+str(res["data"]["rewardAmount"]))
if __name__ == '__main__':
  print("大赢家提现软，偷ck小工具，提取ck软等更多，详情QQ群:538546575")
  start_time = time.time()
  print("Start time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
  ww_ck = os.environ.get('ww_ck', "")
  ww_ck=str(ww_ck)
  if ww_ck == "":
      print('您尚未设置变量 ww_ck="pt_key=xxx;pt_pin=xxx"')
      sys.exit()
  try:
      ww_pin = ww_ck.split('&')
  except:
      print("ww_ck 变量设置错误，ww_ck='pt_key=xxx;pt_pin=xxx'")
      sys.exit()
  ww_red = os.environ.get('ww_red', "")
  if ww_red == "":
      print('您尚未设置变量 ww_red,只能是3或者10')
      check()
      sys.exit()
  else:
      print(ww_red)
      ww_red=int(ww_red)

  if ww_red==3:
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = [executor.submit(send_request3) for _ in range(3)]
        time.sleep(0.5)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results1 = [executor.submit(send_request3) for _ in range(3)]
        time.sleep(0.5)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results2 = [executor.submit(send_request3) for _ in range(3)]
        time.sleep(0.5)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results3 = [executor.submit(send_request3) for _ in range(3)]
        time.sleep(0.5)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results4 = [executor.submit(send_request3) for _ in range(3)]
        time.sleep(0.5)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results5 = [executor.submit(send_request3) for _ in range(3)]
        time.sleep(0.5)

    end_time = time.time()

    # print("Start time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print("End time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print("Total running time: ", end_time - start_time, "seconds")
  elif ww_red==10:
      print("10元红包")
      with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
          results = [executor.submit(send_request10) for _ in range(3)]
          time.sleep(0.5)
      with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
          results1 = [executor.submit(send_request10) for _ in range(3)]
          time.sleep(0.5)
      with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
          results2 = [executor.submit(send_request10) for _ in range(3)]
          time.sleep(0.5)
      with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
          results3 = [executor.submit(send_request10) for _ in range(3)]
          time.sleep(0.5)
      with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
          results4 = [executor.submit(send_request10) for _ in range(3)]
          time.sleep(0.5)
      with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
          results5 = [executor.submit(send_request10) for _ in range(3)]
          time.sleep(0.5)

      end_time = time.time()

      # print("Start time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
      print("End time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))
      print("Total running time: ", end_time - start_time, "seconds")
  else:
      print("请设置正确的红包数，3或者10")



