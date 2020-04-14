
#!/usr/bin/python
#coding=gbk
#treectrl.py
#http://www.jbxue.com/python/29640.htm
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, 
                          wx.DefaultPosition, wx.Size(450, 350))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(self, -1)
        panel2 = wx.Panel(self, -1)
        
        self.tree = wx.TreeCtrl(panel1, 1, wx.DefaultPosition, (-1, -1), 
                                wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
        root = self.tree.AddRoot('程序员')
        os = self.tree.AppendItem(root, '操作系统',data='2342342342424323')
        pl = self.tree.AppendItem(root, '编程语言')
        tk = self.tree.AppendItem(root, '工具套件')
        self.tree.AppendItem(os, 'Linux')
        self.tree.AppendItem(os, 'FreeBSD')
        self.tree.AppendItem(os, 'OpenBSD')
        self.tree.AppendItem(os, 'NetBSD')
        self.tree.AppendItem(os, 'Solaris')
        cl = self.tree.AppendItem(pl, '编译语言')
        sl = self.tree.AppendItem(pl, '脚本语言')
        self.tree.AppendItem(cl, 'Java')
        self.tree.AppendItem(cl, 'C++')
        self.tree.AppendItem(cl, 'C')
        self.tree.AppendItem(cl, 'Pascal')
        self.tree.AppendItem(sl, 'Ruby')
        self.tree.AppendItem(sl, 'Tcl')
        self.tree.AppendItem(sl, 'PHP')
        self.tree.AppendItem(sl, 'Python')
        self.tree.AppendItem(tk, 'Qt')
        self.tree.AppendItem(tk, 'MFC')
        self.tree.AppendItem(tk, 'wxPython')
        self.tree.AppendItem(tk, 'GTK+')
        self.tree.AppendItem(tk, 'Swing')
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, 
                       self.OnSelChanged, id=1)
        self.display = wx.StaticText(panel2, -1, '', 
                                     (10, 10), style=wx.ALIGN_CENTER)
        vbox.Add(self.tree, 1, wx.EXPAND)
        hbox.Add(panel1, 1, wx.EXPAND)
        hbox.Add(panel2, 1, wx.EXPAND)
        panel1.SetSizer(vbox)
        self.SetSizer(hbox)
        self.Center()
        
    def OnSelChanged(self, event):
        item = event.GetItem()
        self.display.SetLabel(self.tree.GetItemText(item))      
      
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'treectrl.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
    
app = MyApp(0)
app.MainLoop() 