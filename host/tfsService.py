import requests
import base64
import json
from requests_ntlm import HttpNtlmAuth

class Node():
    def __init__(self,id,name,origin):
        self.NodeId = id
        self.NodeName = name
        self.Origin = origin
        self.Childs = []

team_search_Tree = Node('-1','Root',None)
team_search_Dict = {}
host = ''
session = {}

base_url = 'http://192.168.0.91:91/'

def get_url(url):
    return '/'.join([base_url,url])

baseHeaders = {
    'Host': '192.168.0.91:91',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin':base_url,
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

session= requests.session()
session.headers.update(baseHeaders)  


def login(name,pas):
        session.auth = HttpNtlmAuth('WIN-8B73S7IKJR2\\'+name,pas)
        login = session.get(get_url('tfs/_signout'))
        return login

def  getTeam():
    projects = session.get(get_url('tfs/DefaultCollection/_apis/projects?stateFilter=WellFormed&%24top=500&%24skip=0'))
    projects_json = projects.json()['value']
    return projects_json