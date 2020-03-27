import wx 
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth  
import urllib 

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
         soup = BeautifulSoup(res)
         print(soup.select("a[tag='ds']"))

def showLogin():
    Mywin(None,  '登录TFS账号')