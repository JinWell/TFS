import requests 
import json

def http_Get(url,dic):
    res = requests.get(url,dic);
    res.encoding = 'utf-8';
    return res.text;

def http_Post(url,dic):
    headers = {}
    res = requests.post(url =url,data = dic,json=True,headers=headers);
    return res.json();



