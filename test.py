import requests
import base64
import json
from requests_ntlm import HttpNtlmAuth

test_url = 'http://192.168.0.91:91/tfs/DefaultCollection/RMIS'

def get_url(url):
    return '/'.join([test_url,url])

def baseAuthorization(username, password):
    temp_str = username + ':' + password 
    bytesString = temp_str.encode(encoding="utf-8") 
    encodestr = base64.b64encode(bytesString) 
    #decodestr = base64.b64decode(encodestr) 
    return 'Basic ' + encodestr.decode()

def print_keyvalue_by_key(input_json, key):
    key_value = ''
    if isinstance(input_json, dict):
        for json_result in input_json.values():
            if key in input_json.keys():
                key_value = input_json.get(key)
            else:
                print_keyvalue_by_key(json_result, key)
    elif isinstance(input_json, list):
        for json_array in input_json:
            print_keyvalue_by_key(json_array, key)
    if key_value != '':
        print(str(key) + " = " + str(key_value)) 

# surl = get_url('_queries') 

# 程序登录
# res = requests.get('http://192.168.0.91:91/tfs/_signout',auth=HttpNtlmAuth('WIN-8B73S7IKJR2\\chenjinwei','cjw'))
# authorization = res.request.headers["Authorization"]

# cookies = r.cookies.get_dict()   #  获取登录之后 cookie
# localReadConfig.set_headers("cookies", str(cookies))   #把cookie存到配置文件里面去
# authorization = response.request.headers["Authorization"]
# 获取数据
# referer = 'http://192.168.0.91:91/tfs/DefaultCollection/RMIS/_queries?id=2834e47d-3e45-4e95-ba63-35c5d881000e&_a=query'
# headers = { 
#             # 'Host':"192.168.0.91:91", 
#             # "Connection":"keep-alive",
#             # "Content-Length":'1717', 
#             # "Accept":"application/json, text/javascript, */*; q=0.01",
#             # "X-Requested-With":"XMLHttpRequest",
#             # "X-TFS-Session":"c2057770-975e-4f48-abc7-9f995ece784b",
#             # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#             # 'Content-Type': 'application/json',
#             # 'Origin': 'http://192.168.0.91:91',
#             'Referer': referer,
#             # 'Accept-Encoding':'gzip, deflate',
#             # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
#      } 
# session.headers.update(headers)
# rs = session.get(referer)
# hr = {
# 'Host': '192.168.0.91:91',
# 'Connection': 'keep-alive',
# 'Authorization': 'NTLM TlRMTVNTUAADAAAAGAAYAIoAAABIAUgBogAAAAAAAABYAAAAFAAUAFgAAAAeAB4AbAAAAAAAAADqAQAABYKIogoAukcAAAAPJA8m/rCdt+2PjN0buEfMwWMAaABlAG4AagBpAG4AdwBlAGkAUwBDAC0AMgAwADEAOQAxADAAMgA3ADEANAAxADYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1ufvc0V8ZwePRTjUcB0djQEBAAAAAAAAKtxVnwz+1QGDj4BcBe5AmwAAAAACAB4AVwBJAE4ALQA4AEIANwAzAFMANwBJAEsASgBSADIAAQAeAFcASQBOAC0AOABCADcAMwBTADcASQBLAEoAUgAyAAQAHgBXAEkATgAtADgAQgA3ADMAUwA3AEkASwBKAFIAMgADAB4AVwBJAE4ALQA4AEIANwAzAFMANwBJAEsASgBSADIABwAIACrcVZ8M/tUBBgAEAAIAAAAIADAAMAAAAAAAAAAAAAAAADAAAB8Jm+ygf+Lu4YaKrdAS72oBxStA3Uz+trJboTwKpx8LCgAQAAAAAAAAAAAAAAAAAAAAAAAJACgASABUAFQAUAAvADEAOQAyAC4AMQA2ADgALgAwAC4AOQAxADoAOQAxAAAAAAAAAAAAAAAAAA==',
# 'Content-Length': '1717',
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
# 'X-Requested-With': 'XMLHttpRequest',
# 'X-TFS-Session': 'c20577c0-975e-4f48-abc7-9f995ece784b',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
# 'Content-Type': 'application/json',
# 'Origin': 'http://192.168.0.91:91',
# 'Referer': 'http://192.168.0.91:91/tfs/DefaultCollection/RMIS/_queries?id=2834e47d-3e45-4e95-ba63-35c5d881000e&_a=query',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
# 'Cookie': '__RequestVerificationToken_L3Rmcw2=NUw2qXgmYD9KL3tiIQG3bloL4dN1-qgOAQrqZec9JcJRtGpx3sGQfzbyXBZMkDQvi_748a2kHaQd7_CwJK-QEeYfowo1; __RequestVerificationToken27d56a928-328f-4adf-bc6f-78f269d7affb=NUw2qXgmYD9KL3tiIQG3bloL4dN1-qgOAQrqZec9JcJRtGpx3sGQfzbyXBZMkDQvi_748a2kHaQd7_CwJK-QEeYfowo1'
# }

def list_where(lam,data):
    d1 = filter(lam,data)
    d2=list(d1)
    r = []
    if len(d2):
        r = d2
    else:
        r = []
    return r

def list_firstOrDefault(lam,data):
    d1 = filter(lam,data)
    d2 = list(d1)
    r = []
    if len(d2):
        r = d2[0]
    else:
        r = None
    return r
  
session= requests.session()
session.auth = HttpNtlmAuth('WIN-8B73S7IKJR2\\chenjinwei','cjw')
login = session.get('http://192.168.0.91:91/tfs/_signout')
projects = session.get('http://192.168.0.91:91/tfs/DefaultCollection/_apis/projects?stateFilter=WellFormed&%24top=500&%24skip=0')
projects_json = projects.json()['value']
rmis = filter(lambda x :x["name"]=='RMIS',projects_json)
rmisId = list(rmis)[0]['id']
# x = list_firstOrDefault(lambda x :x["name"]=='RMIS',projects_json)
project_rmis = session.get('http://192.168.0.91:91/tfs/DefaultCollection/{0}/_apis/wit/queries?api-version=1.0&%24depth=1&%24expand=minimal'.format(rmisId));
project_rmis_json = project_rmis.json()
# 将所有的查询整合在一起
print('ok')
# print(r.status_code)
# # print(r.text)
# print(r.request.headers)
# print(r)
# # print(base64.b64decode('Y2hlbmppbndlaTpjanc='))

 
