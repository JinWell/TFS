import wx
import wx.adv
import datetime
from datetime import timedelta

class Page1(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        v_box_sizer = wx.BoxSizer(wx.VERTICAL)
        v_box_sizer.Add(wx.StaticText(self,label='Page One Line1'), proportion=0, flag=wx.EXPAND)
        v_box_sizer.Add(wx.StaticText(self,label='Page One Line2'), proportion=1, flag=wx.EXPAND)

        self.SetSizer(v_box_sizer)

class Page2(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self,label='Page Two2')
 

if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame(None, title="TFS统计", size=(1500,800))
    panel = wx.Panel(frame) 
    vbox = wx.BoxSizer(wx.VERTICAL) 

    #本周第一天和最后一天
    now = datetime.datetime.now()
    this_week_start = now - timedelta(days=now.weekday())
    this_week_end = now + timedelta(days=6-now.weekday())
    
    day1 = this_week_start.day
    day2 = this_week_end.day

    title = '{0} - {1}'.format(str(day1), str(day2))
    nb = wx.Notebook(panel,size=(1500,600))
    nb.AddPage(Page1(nb),title+" 任务列表")
    nb.AddPage(Page2(nb),title+" 计划列表")  

    # hbox0 = wx.BoxSizer(wx.HORIZONTAL)

    # start = wx.StaticText(panel, -1, '开始')
    # startDate = wx.adv.DatePickerCtrl(panel, id = -1,style=wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY)
    
    # startDate.SetValue(this_week_start)
    # end = wx.StaticText(panel, -1, '结束', pos=(50, 40))
    # endDate = wx.adv.DatePickerCtrl(panel, id = -1,style=wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY)
    # endDate.SetValue(this_week_end)
    # button = wx.Button(panel, -1, "统计")

    # hbox0.Add(start, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    # hbox0.Add(startDate, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    # hbox0.Add(end, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    # hbox0.Add(endDate, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    # hbox0.Add(button, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    # vbox.Add(hbox0) 
 
    hbox1 = wx.BoxSizer(wx.HORIZONTAL)
    hbox1.Add(nb, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    vbox.Add(hbox1) 

    # hbox2 = wx.BoxSizer(wx.VERTICAL) 
    # tj = wx.StaticText(panel, -1, "统计信息:") 
    # hbox2.Add(tj, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    # vbox.Add(hbox2) 

    # hbox3 = wx.BoxSizer(wx.VERTICAL) 
    # tjxq = wx.TextCtrl(panel,size = (1500,100),style = wx.TE_MULTILINE) 
    # hbox2.Add(tjxq, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
    # vbox.Add(hbox3)

    panel.SetSizer(vbox) 

    frame.Show()
    app.MainLoop()