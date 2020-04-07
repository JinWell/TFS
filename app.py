from view.login import *
import configparser
import os
import re   #引入正则表达式对象
import urllib   #用于对URL进行编解码 
from host.tfsService import *

cf=configparser.ConfigParser()
cf.read(os.getcwd()+"/app.conf")
userName = cf.get("db","user")
userPass = cf.get("db","pass")
host = cf.get("ssh","host")
becomeSilent = cf.get("config","becomeSilent")
app = wx.App()  
showLogin(userName,userPass,becomeSilent)
app.MainLoop()       