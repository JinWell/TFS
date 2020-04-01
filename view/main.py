import wx
from host.tfsService import *
import wx.grid

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


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Tree", size=(1500, 600))
        self.Center()
        icon = wx.Icon('Source/fav.ico', wx.BITMAP_TYPE_ICO) 

        swindow = wx.SplitterWindow(parent=self, id=-1)
        left = wx.Panel(parent=swindow)
        right = wx.Panel(parent=swindow)

        # 设置左右布局的分割窗口left和right
        swindow.SplitVertically(left, right, 200)

        # 设置最小窗格大小，左右布局指左边窗口大小
        swindow.SetMinimumPaneSize(80)

        # 创建一棵树 
        self.tree = self.CreateTreeCtrl(left)
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
        grid = wx.grid.Grid(right, -1)
 
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(200, 10)
 
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

        # 获取团队
        teams = getTeam()
        teamsDic = {} 
        
        for i,item in enumerate(teams):
            teamsDic[item['name']] = item['id']

        list_values = [i for i in teamsDic.values()]
        list_keys= [ i for i in teamsDic.keys()]
 
        ch1=wx.ComboBox(right,-1,value='RMIS',choices=list_keys,style=wx.CB_SORT)
        #添加事件处理
        self.Bind(wx.EVT_COMBOBOX,self.on_combobox,ch1)

        #获取团队成员
        # project = list_firstOrDefault(lambda x :x["name"]=='RMIS',teams)
        # users = getTeamUser(project["id"])

        cygl = wx.StaticText(right,-1, style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_MIDDLE,label='成员过滤:')
        list2=["陈金伟","韩小江","姜智林","杨博","邓东林"]
        ch2=wx.ComboBox(right,-1,value='姜智林',choices=list2,style=wx.CB_SORT)
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
        self.st.SetLabel(self.tree.GetItemText(item))
 
    def CreateTreeCtrl(self, parent):
        tree = wx.TreeCtrl(parent)
        # 通过wx.ImageList()创建一个图像列表imglist并保存在树中
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=(16, 16)))
        tree.AssignImageList(imglist)

        # 创建根节点和5个子节点并展开
        root = tree.AddRoot('TreeRoot', image=0)
        item1 = tree.AppendItem(root, 'Item1', 0)
        item2 = tree.AppendItem(root, 'Item2', 0)
        item3 = tree.AppendItem(root, 'Item3', 0)
        item4 = tree.AppendItem(root, 'Item4', 0)
        item5 = tree.AppendItem(root, 'Item5', 0)
        tree.Expand(root)
        tree.SelectItem(root)
 
        # 给item1节点添加5个子节点并展开
        tree.AppendItem(item1, 'file 1', 1)
        tree.AppendItem(item1, 'file 2', 1)
        tree.AppendItem(item1, 'file 3', 1)
        tree.AppendItem(item1, 'file 4', 1)
        tree.AppendItem(item1, 'file 5', 1)
        tree.Expand(item1)
 
        # 给item2节点添加5个子节点并展开
        tree.AppendItem(item2, 'file 1', 1)
        tree.AppendItem(item2, 'file 2', 1)
        tree.AppendItem(item2, 'file 3', 1)
        tree.AppendItem(item2, 'file 4', 1)
        tree.AppendItem(item2, 'file 5', 1)
        tree.Expand(item2)
 
        # 返回树对象
        return tree
 
 
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
     