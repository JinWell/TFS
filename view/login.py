import wx 
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth 
# from requests_ntlm import HttpNtlmAuth
# from requests.auth import HTTPDigestAuth
import urllib

# from  tools.httpClientService import *  
# from toolPackage.httpClientService import http_Post

 
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title)   
      icon = wx.Icon('Source/fav.ico', wx.BITMAP_TYPE_ICO) 
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      nm = wx.StaticBox(panel, -1, '账户信息') 
      nmSizer = wx.StaticBoxSizer(nm, wx.VERTICAL) 
      nmbox = wx.BoxSizer(wx.HORIZONTAL) 
      fn = wx.StaticText(panel, -1, "账户:") 
      self.nm1 = wx.TextCtrl(panel, -1, style = wx.ALIGN_LEFT) 
      self.nm2 = wx.TextCtrl(panel, -1, style = wx.TE_PASSWORD) 
      ln = wx.StaticText(panel, -1, "密码") 
      nmbox.Add(fn, 0, wx.ALL|wx.CENTER, 5) 
      nmbox.Add(self.nm1, 0, wx.ALL|wx.CENTER, 5)
      nmbox.Add(ln, 0, wx.ALL|wx.CENTER, 5) 
      nmbox.Add(self.nm2, 0, wx.ALL|wx.CENTER, 5) 
      nmSizer.Add(nmbox, 0, wx.ALL|wx.CENTER, 10)   
      sbox = wx.StaticBox(panel, -1, '操作') 
      sboxSizer = wx.StaticBoxSizer(sbox, wx.VERTICAL)  
      hbox = wx.BoxSizer(wx.HORIZONTAL) 
      okButton = wx.Button(panel, -1, '登录')  
      hbox.Add(okButton, 0, wx.ALL|wx.LEFT, 10) 
      cancelButton = wx.Button(panel, -1, '重置')   
      hbox.Add(cancelButton, 0, wx.ALL|wx.LEFT, 10) 
      sboxSizer.Add(hbox, 0, wx.ALL|wx.LEFT, 10)  
      vbox.Add(nmSizer,0, wx.ALL|wx.CENTER, 5) 
      vbox.Add(sboxSizer,0, wx.ALL|wx.CENTER, 5)  
      panel.SetSizer(vbox) 
      panel.Fit()
      self.SetIcon(icon) 
      self.Bind(wx.EVT_BUTTON,self.cancelEvent,cancelButton)
      self.Bind(wx.EVT_BUTTON,self.submitEvent,okButton)
      self.Centre()  
      self.Show()  
   
   def cancelEvent(self,event): 
         self.nm1.Clear()
         self.nm2.Clear(); 

   def submitEvent(self, event):
         user = self.nm1.GetValue()
         userPass = self.nm2.GetValue();  
         res = http_Get("http://192.168.0.91:91/tfs/DefaultCollection/RMIS/_queries",{})
        #  res = updateIP()
        #  t = res.status_code 
         soup = BeautifulSoup(res)
         print(soup.select("a[tag='ds']"))

def showLogin():
    Mywin(None,  '登录TFS账号')


def http_Post(url,dic):
    headers = {}
    res = requests.post(url =url,data = dic,json=True,headers=headers,auth=('chenjinwei','cjw'))
    return res.json()
 

def http_Get(url,dic): 
    headers = { 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.5",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"Keep-Alive",
        "Host":"192.168.0.91:91",
        "Authorization": "Basic MTExMTExOjQ0NDQ0NDQ0NDQ0"
     } 
    surl = "http://192.168.0.91:91/tfs/DefaultCollection/RMIS/_queries?hostname=WIN-8B73S7IKJR2"
    # passman = urllib.request.HTTPPasswordMgrWithDefaultRealm() #创建域验证对象
    # passman.add_password(None,surl, "chenjinwei", "cjw")
    # auth_handler = urllib.request.HTTPBasicAuthHandler(passman) #生成处理与远程主机的身份验证的处理程序
    # opener = urllib.request.build_opener(auth_handler) #返回一个openerDirector实例
    # urllib.request.install_opener(opener) #安装一个openerDirector实例作为默认的开启者。
    # response = urllib.request.urlopen(surl) #打开URL链接，返回Response对象
    # resContent = response.read() #读取响应内容 

    # res2 = requests.get(url,auth=('WIN-8B73S7IKJR2\\chenjinwei','cjw'),headers = headers); 
    # res1 = requests.get(url,auth=HTTPDigestAuth('WIN-8B73S7IKJR2\\chenjinwei', 'cjw'),headers = headers); 
    res = requests.get(surl,auth=HttpNtlmAuth('WIN-8B73S7IKJR2\\chenjinwei','cjw'),headers = headers)
    # x = requests.get("http://ntlm_protected_site.com",auth=HttpNtlmAuth('domain\\username','password'))
    # res.encoding = 'utf-8';
    return response

# def updateIP():  
#     url = "http://192.168.0.91:91/tfs/DefaultCollection/RMIS/_queries"
#     try:
#         pwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#         pwdmgr.add_password(None,'http://192.168.0.91:91', 'chenjinwei','cjw')
#         auth_handler = urllib.request.HTTPDigestAuthHandler(pwdmgr)
#         opener = urllib.request.build_opener(auth_handler)
#         response = opener.open(url)
#         result = response.read().decode('utf-8')
#         result = str.strip(result) 
#         return True
#     except BaseException as e: 
#         return False

 