import wx
from host.tfsService import *
import wx.grid
import time
import datetime

global project
project = {}

global _init
_init = True

global grid
grid = {}

class GridFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
 
        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)
 
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(100, 10)
 
        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)
 
        # And set grid cell contents as strings
        grid.SetCellValue(0, 0, 'wxGrid is good')
 
        # We can specify that some cells are read.only
        grid.SetCellValue(0, 3, 'This is read.only')
        grid.SetReadOnly(0, 3)
 
        # Colours can be specified for grid cell contents
        grid.SetCellValue(3, 3, 'green on grey')
        grid.SetCellTextColour(3, 3, wx.GREEN)
        grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)
 
        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        grid.SetColFormatFloat(5, 6, 2)
        grid.SetCellValue(0, 6, '3.1415')
 
        self.Show()

def  Empty():
    return "                         |"

def is_valid_date(str_date):
    if str_date == None:
        return ''

    str_date = str_date.replace('/Date(','').replace(')/','') 
    str_date1 =  str_date[0:10]+'.'+ str_date[-3:] 
    timeArray = time.localtime(float(str_date1))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    return otherStyleTime
    # '''判断是否是一个有效的日期字符串'''
    # try:
    #     time.strptime(str_date, "%Y-%m-%d")
    # except Exception:
    #     # traceback.print_exc()
    #     raise Exception("时间参数错误 near : {}".format(str_date)) 

class GridData(wx.grid.PyGridTableBase):
    _cols = []
    _data = []

    def __init__(self,task):
        super(GridData,self).__init__()
        dts = task['payload']
        oldColumns = task['columns']
        showColumns = []
        rows = dts['rows']

        for k,v in  enumerate(dts['columns']): 
            item = list_firstOrDefault(lambda x :v==x['name'],oldColumns)
            if (item is None) == False:
                showColumns.append(item['text'])
            else:
                showColumns.append('● [ 未知 ]')

        global grid

        grid.ClearGrid()

        for j,p in enumerate(showColumns):
            grid.SetColLabelValue(j, p)

        # 表格数据
        for k,v in enumerate(rows):
            # 表格列
            for j,p in enumerate(showColumns):
                text = str(v[j]) 
                if p == '创建者' or p == '指派给': 
                    text = text.split('<')[0]

                elif p == '完成日期' or p == '开始日期' or p == '截止日期': 
                    text = is_valid_date(v[j])
                
                elif p == '初始估计' or p == '已完成工作':
                    if text == 'None':
                       text = ' '
                else:
                    if text == 'None':
                       text = ' '
                       
                grid.SetCellValue(k, j,text)

        self._cols = showColumns
        self._data = rows
 
    _highlighted = set()

    def GetColLabelValue(self, col):
        return self._cols[col]

    def GetNumberRows(self):
        return len(self._data)

    def GetNumberCols(self):
        return len(self._cols)

    def GetValue(self, row, col):
        return self._data[row][col]

    def SetValue(self, row, col, val):
        self._data[row][col] = val

    def GetAttr(self, row, col, kind):
        attr = wx.grid.GridCellAttr()
        attr.SetBackgroundColour(wx.GREEN if row in self._highlighted else wx.WHITE)
        return attr

    def set_value(self, row, col, val):
        self._highlighted.add(row)
        self.SetValue(row, col, val)

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="TFS查询 - V1.0.0", size=(1500, 600))
        self.Center()
        icon = wx.Icon('Source/fav.ico', wx.BITMAP_TYPE_ICO) 

        # 获取团队
        teams = getTeam()
        teamsDic = {} 
        
        for i,item in enumerate(teams):
            teamsDic[item['name']] = item['id']

        list_values = [i for i in teamsDic.values()]
        list_keys= [ i for i in teamsDic.keys()]
  
        #获取团队成员
        global project
        project = list_firstOrDefault(lambda x :x["name"]=='RMIS',teams)
        # users = getTeamUser(project["id"])

        swindow = wx.SplitterWindow(parent=self, id=-1)
        left = wx.Panel(parent=swindow)
        right = wx.Panel(parent=swindow)

        # 设置左右布局的分割窗口left和right
        swindow.SplitVertically(left, right, 200)

        # 设置最小窗格大小，左右布局指左边窗口大小
        swindow.SetMinimumPaneSize(80)

        # 创建一棵树 
        self.tree = self.CreateTreeCtrl(left,project['id'])
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_click, self.tree)

        # 为left面板设置一个布局管理器
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        left.SetSizer(vbox1)  
        vbox1.Add(self.tree, 1, flag=wx.EXPAND | wx.ALL, border=5)

        # 为right面板设置一个布局管理器
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        right.SetSizer((vbox2))

        # frame = GridFrame(right) 
        # Create a wxGrid object
        global grid
        grid = wx.grid.Grid(right, -1)
 
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(200, 30)
 
        # We can set the sizes of individual rows and columns
        # in pixels
        # grid.SetRowSize(0, 60)
        # grid.SetColSize(0, 120)
 
        # And set grid cell contents as strings
        # grid.SetCellValue(0, 0, 'wxGrid is good') 

        # We can specify that some cells are read.only
        # grid.SetCellValue(0, 3, 'This is read.only')
        # grid.SetReadOnly(0, 3)
 
        # Colours can be specified for grid cell contents
        # grid.SetCellValue(3, 3, 'green on grey')
        # grid.SetCellTextColour(3, 3, wx.GREEN)
        # grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)
 
        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        # grid.SetColFormatFloat(5, 6, 2)
        # grid.SetCellValue(0, 6, '3.1415')

        # 标题
        lbl = wx.StaticText(right,-1,style = wx.ALIGN_CENTER) 
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
        lbl.SetFont(font) 
        lbl.SetLabel('统计信息') 
        vbox2.Add(lbl, 3, wx.EXPAND)

        # 操作
        h_box_sizer = wx.BoxSizer(wx.HORIZONTAL)

        v_box_sizer = wx.BoxSizer(wx.VERTICAL)

        gs = wx.StaticText(right,-1, style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_MIDDLE,label='工时：') 
        # gsNum = wx.TextCtrl(right, -1, style = wx.ALIGN_LEFT) 
        sc = wx.SpinCtrl(right, -1, "", (30, 20), (80, -1))  
        sc.SetRange(1,100)  
        sc.SetValue(40)  

        btn = wx.Button(right,-1,"统计",style = wx.ALIGN_LEFT,size=(60,27))
        btn1 = wx.Button(right,-1,"导出Excel",style = wx.ALIGN_LEFT,size=(100,27))

        # xztd = wx.StaticText(right,-1, style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_MIDDLE,label='选择团队:') 
        xztd = wx.StaticText(right, wx.ID_ANY, "选择团队:", (10,10), (100,27),wx.ALIGN_CENTER)
        xztd.SetForegroundColour("White")
        xztd.SetBackgroundColour("Black")
        # font1=wx.Font(-10,wx.SCRIPT,wx.NORMAL,wx.NORMAL,False,)
        # xztd.SetFont(font)

        ch1=wx.ComboBox(right,-1,value='RMIS',choices=list_keys,style=wx.CB_SORT)
        #添加事件处理
        self.Bind(wx.EVT_COMBOBOX,self.on_combobox,ch1)

        cygl = wx.StaticText(right,-1, style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_MIDDLE,label='成员过滤:')
        list2=["全部","陈金伟","韩小江","姜智林","杨博","邓东林"]
        ch2=wx.ComboBox(right,-1,value='全部',choices=list2,style=wx.CB_SORT)
        #添加事件处理
        self.Bind(wx.EVT_COMBOBOX,self.on_combobox,ch2)

        h_box_sizer.Add(xztd)
        h_box_sizer.Add((10,-1))
        h_box_sizer.Add(ch1)
        h_box_sizer.Add((10,-1))
        h_box_sizer.Add(cygl)
        h_box_sizer.Add((10,-1))
        h_box_sizer.Add(ch2)
        h_box_sizer.Add((10,-1))
        h_box_sizer.Add(gs)
        h_box_sizer.Add((10,-1))
        h_box_sizer.Add(sc)
        h_box_sizer.Add((10,-1))
        h_box_sizer.Add(btn)
        h_box_sizer.Add((10,-1))
        h_box_sizer.Add(btn1)  
        v_box_sizer.Add(h_box_sizer, proportion=0, flag=wx.EXPAND)
        vbox2.Add(v_box_sizer, -1, wx.EXPAND) 
        vbox2.Add((-1,15))

        # 统计信息
        lbl1 = wx.StaticText(right,-1, style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_MIDDLE) 
        lbl1.SetLabel('张三') 
        lbl1.SetForegroundColour((255,0,0)) 
        lbl1.SetBackgroundColour((0,0,0))   
 
        vbox2.Add(lbl1, -1, wx.EXPAND) 
        vbox2.Add(grid, -1, flag=wx.EXPAND, border=5) 
        
        self.SetIcon(icon)
 
    def on_combobox(self,event):
        print("选择{0}".format(event.GetString()))
    
    def on_click(self, event):
        item = event.GetItem()  
        selId = self.tree.GetItemData(item)   
        fItem = team_search_Dict[selId]
 
        if fItem == '':
            return False

        if (('isFolder' in fItem.Origin) and (fItem.Origin['isFolder'] == True)):
            return False

        # 获取查询项ID
        item_id = fItem.NodeId 

        # 获取数据
        tasks = getTaskDetails(project['id'],item_id)
        self.data = GridData(tasks)
        # self.grid = wx.grid.Grid(self)
        # grid.ClearGrid()
        # global _init

        # if _init == True: 
        #     _init = False
        #     grid.SetTable(self.data)


        # grid.AutoSize()
        # self.data.set_value(1, 0, "x")
        grid.Refresh()
 
    def CreateTreeCtrl(self, parent,project_Id):
        tree = wx.TreeCtrl(parent,style=wx.TR_HAS_BUTTONS|wx.TR_LINES_AT_ROOT|wx.TR_TWIST_BUTTONS)

        # 获取查询列表
        getTfsSearchItem(project_Id)

        # 通过wx.ImageList()创建一个图像列表imglist并保存在树中
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=(16, 16)))
        tree.AssignImageList(imglist)

        # 创建根节点和5个子节点并展开
        root = tree.AddRoot('RMIS团队查询', image=0)
 
        for i,item in enumerate(team_search_Tree.Childs):
            treeNode = tree.AppendItem(root,item.NodeName, 0,data=item.NodeId)
            if  len(item.Origin['children']) >0:
                loadChild(tree,treeNode,item) 
                tree.Expand(treeNode) 

        tree.Expand(root) 
        # tree.SelectItem(root)
   
        # 返回树对象
        return tree
 

def loadChild(tree,treeNode,parentItem):
     for i,item in enumerate(parentItem.Childs):
            if  len(item.Childs) > 0:
                node = tree.AppendItem(treeNode, item.NodeName, 0,data = item.NodeId) 
                loadChild(tree,node,item)
                # tree.Expand(node)
            else:
                node = tree.AppendItem(treeNode, item.NodeName,1,data = item.NodeId)

class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True
 
    def OnExit(self):
        print("应用程序退出")
        return 0

def showMain():
    app = App()
    app.MainLoop()
     