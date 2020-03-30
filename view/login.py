import wx 
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth  
import urllib 
from view.main import *
from host.tfsService import *
 
class Mywin(wx.Frame): 
   def __init__(self, parent, title,name,pas): 
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
      self.nm1.SetValue(name)
      self.nm2.SetValue(pas)
      self.Centre()
   
   def cancelEvent(self,event):
         self.nm1.Clear()
         self.nm2.Clear(); 

   def submitEvent(self, event):
         user = self.nm1.GetValue()
         userPass = self.nm2.GetValue()
         result = login(user,userPass)
         if tryLogin(user,userPass):
            self.Hide()
            showMain()  
      #    soup = BeautifulSoup(res)
      #    print(soup.select("a[tag='ds']"))

def tryLogin(user,userPass):
      result = login(user,userPass)
      if  result.ok:
            return True
      else:
            wx.MessageBox("登陆失败，请核对密码是否正确", "登陆失败",wx.OK | wx.ICON_INFORMATION) 
            return False

def showLogin(name,pas,becomeSilent): 
      win = Mywin(None,  '登录TFS账号',name,pas) 
      if  becomeSilent:
            if tryLogin(name,pas):
                  showMain()
            else:
                  win.Show()
      else:
            win.Show()

      