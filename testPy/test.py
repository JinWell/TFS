import requests
import base64
import json
from requests_ntlm import HttpNtlmAuth

base_url = 'http://192.168.0.91:91/'

def get_url(url):
    return '/'.join([base_url,url])

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

def loadChildNode(parent):
    parentId = parent.Origin['id']
    # 获取下面的子节点
    res = session.get(get_url('tfs/DefaultCollection/{0}/_apis/wit/queries/{1}?api-version=1.0&%24depth=2&%24expand=minimal').format(project_Id,parentId))
    res_json = res.json();
    res_childs = res_json['children']
    for i,item in enumerate(res_childs):
        node = Node(item['id'],item['name'],item)
        if 'hasChildren' in item:
            loadChildNode(node)
        else:
            team_search_Dict[node.NodeId] = node 
            parent.Childs.append(node)

class Node():
    def __init__(self,id,name,origin):
        self.NodeId = id
        self.NodeName = name
        self.Origin = origin
        self.Childs = []

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
session.auth = HttpNtlmAuth('WIN-8B73S7IKJR2\\chenjinwei','cjw')
login = session.get(get_url('tfs/_signout'))
projects = session.get(get_url('tfs/DefaultCollection/_apis/projects?stateFilter=WellFormed&%24top=500&%24skip=0'))
projects_json = projects.json()['value'] 
project = list_firstOrDefault(lambda x :x["name"]=='RMIS',projects_json)
project_Id = project['id'] 

# 获取团队下的查询
target_project_data = session.get(get_url('tfs/DefaultCollection/{0}/_apis/wit/queries?api-version=1.0&%24depth=1&%24expand=minimal').format(project_Id))
project_rmis_json = target_project_data.json()['value']
team_search_Tree = Node('-1','Root',None)
team_search_Dict = {}
for i,item in enumerate(project_rmis_json):
    node = Node(item['id'],item['name'],item)
    team_search_Tree.Childs.append(node)
    team_search_Dict[node.NodeId] = node
    if 'hasChildren' in item and  item['hasChildren']: 
         loadChildNode(node) 

# 获取详情   
sid = '2d0b4dd1-cb2f-462c-b44b-62437a4dfbf4'
referer = get_url('tfs/DefaultCollection/RMIS/_queries?id={0}&_a=query').format(sid) 
headers = {
    "Referer":referer
}

session.headers.update(headers)
wiq = team_search_Dict[sid]
payload = {'wiql':wiq.Origin["wiql"]}
search_result = session.post(get_url('tfs/DefaultCollection/{0}/_api/_wit/query?__v=5').format(project_Id),json = payload)
search_details = search_result.json()