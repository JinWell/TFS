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
team_search_Tree = Node('-1','TFS查询',None)
team_search_Dict = {}
table_data = []
table_cell = []

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
    'Accept':'application/json;api-version=4.1-preview.1;excludeUrls=true',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

session= requests.session()
session.headers.update(baseHeaders)  

def list_firstOrDefault(lam,data):
    d1 = filter(lam,data)
    d2 = list(d1)
    r = []
    if len(d2):
        r = d2[0]
    else:
        r = None
    return r
    

def login(name,pas):
        session.auth = HttpNtlmAuth('WIN-8B73S7IKJR2\\'+name,pas)
        login = session.get(get_url('tfs/_signout'))
        return login

def  getTeam():
        projects = session.get(get_url('tfs/DefaultCollection/_apis/projects?stateFilter=WellFormed&%24top=500&%24skip=0'))
        projects_json = projects.json()['value']
        return projects_json

def getTfsSearchItem(project_Id):
    target_project_data = session.get(get_url('tfs/DefaultCollection/{0}/_apis/wit/queries?api-version=1.0&%24depth=1&%24expand=minimal').format(project_Id))
    project_rmis_json = target_project_data.json()['value']
    for i,item in enumerate(project_rmis_json):
        node = Node(item['id'],item['name'],item)
        team_search_Tree.Childs.append(node)
        team_search_Dict[node.NodeId] = node
        if 'hasChildren' in item and  item['hasChildren']: 
            loadChildNode(node,project_Id) 

def loadChildNode(parent,project_Id):
    parentId = parent.Origin['id']
    # 获取下面的子节点
    res = session.get(get_url('tfs/DefaultCollection/{0}/_apis/wit/queries/{1}?api-version=1.0&%24depth=2&%24expand=minimal').format(project_Id,parentId))
    res_json = res.json();
    res_childs = res_json['children']
    for i,item in enumerate(res_childs):
        node = Node(item['id'],item['name'],item)

        team_search_Dict[node.NodeId] = node 
        parent.Childs.append(node)

        if 'hasChildren' in item:
            loadChildNode(node,project_Id)
        # else:
        #     team_search_Dict[node.NodeId] = node 
        #     parent.Childs.append(node)


def getTeamUser(projectId):  
    payload = {
        "contributionIds": ["ms.vss-tfs-web.project-members-data-provider"],
        "context": {
            "properties": {
                "pageSource": {
                    "contributionPaths": ["VSS", "VSS/Resources", "q", "knockout", "mousetrap", "mustache", "react", "react-dom", "react-transition-group", "jQueryUI", "jquery", "OfficeFabric", "@uifabric", "VSSUI", "WidgetComponents", "WidgetComponents/Resources", "Charts", "Charts/Resources", "ContentRendering", "ContentRendering/Resources", "TFS", "Notifications", "Presentation/Scripts/marked", "Presentation/Scripts/URI", "Presentation/Scripts/punycode", "Presentation/Scripts/IPv6", "Presentation/Scripts/SecondLevelDomains", "highcharts", "highcharts-more", "highcharts-heatmap", "highcharts-funnel", "highcharts-accessibility"],
                    "diagnostics": {
                        "sessionId": "b14c7085-8ff1-43ca-b4bc-885cb72c13ad",
                        "activityId": "b14c7085-8ff1-43ca-b4bc-885cb72c13ad",
                        "bundlingEnabled":"true",
                        "webPlatformVersion": "M131"
                    },
                    "navigation": {
                        "topMostLevel": "8",
                        "area": "",
                        "currentController": "Apps",
                        "currentAction": "ContributedHub",
                        "commandName": "Project.Overview",
                        "routeId": "ms.vss-tfs-web.project-overview-route",
                        "routeTemplates": ["{project}"],
                        "routeValues": {
                            "project": "RMIS",
                            "controller": "Apps",
                            "action": "ContributedHub"
                        }
                    },
                    "project": {
                        "id": "af272b7e-6207-4c03-a678-536a9c43cc91",
                        "name": "RMIS"
                    },
                    "selectedHubGroupId": "ms.vss-tfs-web.project-team-hidden-hub-group",
                    "selectedHubId": "ms.vss-tfs-web.project-overview-hub",
                    "team": {
                        "id": "23435373-4268-496c-a8f6-2c34d5181789",
                        "name": "RMIS 团队"
                    },
                    "url": "http://192.168.0.91:91/tfs/DefaultCollection/RMIS"
                }
            }
        }
    }
    
    url = get_url('tfs/DefaultCollection/_apis/Contribution/dataProviders/query/project/')
    users = session.post(url,json = payload)
    users_json = users.json()
    members = users_json['data']['ms.vss-tfs-web.project-members-data-provider']['members']
    _members = json.loads(members)
    return users_json