# -*- coding: UTF-8 -*-
#python tkinter menu
#python version 3.3.2
#EN = Window 7


from tkinter import *
import tkinter as tk
from tkinter  import ttk  
import FileDialog
#import Autotest
import sys
import os
'''
    在python 3.3.2中，tkinter模块可以创建一个窗口控件，如Java中的Swing
    功能描述：
        根据Python 3.3.2 IDEL的菜单，创建出一个tkinter窗口
        File-Exit    :  退出功能完成
        Help-About IDEL     ： 打印相应信息
        其他的菜单项，当点击时，会打印出相应菜单项的名称
'''

__author__ = 'Chenfufeng'
MENU_ITEMS = ['File', 'Edit', 'Format', 'Run', 'Options', 'Windows', 'Help']
#菜单File中的选项
MENU_FILE_ITEMS = ['New Test      Ctrl+N      ',
                   'Open...         Ctrl+O      ',
                   'Recent Files                ',
                   'Open Module...  Alt+M       ',
                   'Class Browser   Alt+C       ',
                   'Path Browser                ',
                   'Save            Ctrl+S      ',
                   'Save As...      Ctrl+Shift+S',
                   'Save Copy As... Ctrl+Alt+S  ',
                   'Print Window    Ctrl+P      ',
                   'Close           Alt+F4      ',
                   'Exit            Ctrl+Q      ']
#菜单Edit中的选项
MENU_EDIT_ITEMS = ['Undo                     Ctrl+Z        ',
                   'Redo                     Ctrl+Shift+Z  ',
                   'Cut                      Ctrl+X        ',
                   'Copy                     Ctrl+C        ',
                   'Paste                    Ctrl+V        ',
                   'Select All               Ctrl+A        ',
                   'Find...                  Ctrl+F        ',
                   'Find Again               Ctrl+G        ',
                   'Find Selections          Ctrl+F3       ',
                   'Find in Files            Alt+F3        ',
                   'Replace...               Ctrl+H        ',
                   'Go to Line               Alt+G         ',
                   'Expend Word              Alt+/         ',
                   'Show call tip            Ctrl+backslash',
                   'Show surerounding parens Ctrl+0        ',
                   'Show Completions         Ctrl+space    ']
#菜单Format中的选项
MENU_FORMAT_ITEMS = ['Check Module        Alt+X   ',
                   'Ident Region        Ctrl+]  ',
                   'Dedent Region       Ctrl+[  ',
                   'Commemt Out Region  Alt+3   ',
                   'Uncomment Region    Alt+4   ',
                   'Tabify Region       Alt+5   ',
                   'Untabify Region     Alt+6   ',
                   'Toggle Tabs         Alt+T   ',
                   'New Ident Width     Alt+U   ',
                   'Format Paragraph    Alt+Q   ',
                   'Strip trailing whitespace   ']
#菜单Run中的选项
MENU_RUN_ITEMS = [ 'Python Shell                ',
                   'Check Module    Alt+X       ',
                   'Run Module      F5          ']
#菜单Options中的选项
MENU_OPTIONS_ITEMS = ['Config IDEL...              ',
                   'Code Context                ']
#菜单Windows中的选项
MENU_WINDOWS_ITEMS = ['Zoom Height     Alt+2       ']
#菜单Help中的选项
MENU_HELP_ITEMS = ['About IDEL                  ',
                   'IDEL Help                   ',
                   'Python Docs     F1          ']
#help-About IDEL
ABOUT_MESSAGE = '''
    Author       : chenfufeng
    Author_email : chenfufeng@ruijie.com.cn    
    Created      : 2018-04-24
    Version      : 1.0    
    '''  


def menu_file(menubar):
    '''定义菜单File'''
    filemenu = Menu(menubar, tearoff=1)
    filemenu.add_command(label=MENU_FILE_ITEMS[0], command=lambda:addNewConnect(root))
    filemenu.add_command(label=MENU_FILE_ITEMS[1], command=lambda:print(MENU_FILE_ITEMS[1]))
    filemenu.add_command(label=MENU_FILE_ITEMS[2], command=lambda:print(MENU_FILE_ITEMS[2]))
    
    filemenu.add_command(label=MENU_FILE_ITEMS[3], command=lambda:print(MENU_FILE_ITEMS[3]))
    filemenu.add_command(label=MENU_FILE_ITEMS[4], command=lambda:print(MENU_FILE_ITEMS[4]))
    filemenu.add_command(label=MENU_FILE_ITEMS[5], command=lambda:print(MENU_FILE_ITEMS[5]))
    filemenu.add_separator()
    filemenu.add_command(label=MENU_FILE_ITEMS[6], command=lambda:print(MENU_FILE_ITEMS[6]))
    filemenu.add_command(label=MENU_FILE_ITEMS[7], command=lambda:print(MENU_FILE_ITEMS[7]))
    filemenu.add_command(label=MENU_FILE_ITEMS[8], command=lambda:print(MENU_FILE_ITEMS[8]))
    filemenu.add_separator()
    filemenu.add_command(label=MENU_FILE_ITEMS[9], command=lambda:print(MENU_FILE_ITEMS[9]))
    filemenu.add_separator()
    filemenu.add_command(label=MENU_FILE_ITEMS[10], command=lambda:print(MENU_FILE_ITEMS[10]))
    filemenu.add_command(label=MENU_FILE_ITEMS[11], command=root.destroy)
    menubar.add_cascade(label=MENU_ITEMS[0], menu=filemenu)

def menu_edit(menubar):
    '''定义菜单Edit'''
    edit_menu = Menu(menubar, tearoff=1)
    edit_menu.add_command(label=MENU_EDIT_ITEMS[0], command=lambda:print(MENU_EDIT_ITEMS[0]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[1], command=lambda:print(MENU_EDIT_ITEMS[1]))
    edit_menu.add_separator()
    edit_menu.add_command(label=MENU_EDIT_ITEMS[2], command=lambda:print(MENU_EDIT_ITEMS[2]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[3], command=lambda:print(MENU_EDIT_ITEMS[3]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[4], command=lambda:print(MENU_EDIT_ITEMS[4]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[5], command=lambda:print(MENU_EDIT_ITEMS[5]))
    edit_menu.add_separator()
    edit_menu.add_command(label=MENU_EDIT_ITEMS[6], command=lambda:print(MENU_EDIT_ITEMS[6]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[7], command=lambda:print(MENU_EDIT_ITEMS[7]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[8], command=lambda:print(MENU_EDIT_ITEMS[8]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[9], command=lambda:print(MENU_EDIT_ITEMS[9]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[10], command=lambda:print(MENU_EDIT_ITEMS[10]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[11], command=lambda:print(MENU_EDIT_ITEMS[11]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[12], command=lambda:print(MENU_EDIT_ITEMS[12]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[13], command=lambda:print(MENU_EDIT_ITEMS[13]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[14], command=lambda:print(MENU_EDIT_ITEMS[14]))
    edit_menu.add_command(label=MENU_EDIT_ITEMS[15], command=lambda:print(MENU_EDIT_ITEMS[15]))
    menubar.add_cascade(label=MENU_ITEMS[1], menu=edit_menu)

def menu_format(menubar):
    '''定义菜单Format'''
    format_menu = Menu(menubar, tearoff=1)
    format_menu.add_command(label=MENU_FORMAT_ITEMS[0], command=lambda:print(MENU_FORMAT_ITEMS[0]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[1], command=lambda:print(MENU_FORMAT_ITEMS[1]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[2], command=lambda:print(MENU_FORMAT_ITEMS[2]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[3], command=lambda:print(MENU_FORMAT_ITEMS[3]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[4], command=lambda:print(MENU_FORMAT_ITEMS[4]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[5], command=lambda:print(MENU_FORMAT_ITEMS[5]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[6], command=lambda:print(MENU_FORMAT_ITEMS[6]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[7], command=lambda:print(MENU_FORMAT_ITEMS[7]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[8], command=lambda:print(MENU_FORMAT_ITEMS[8]))
    format_menu.add_command(label=MENU_FORMAT_ITEMS[9], command=lambda:print(MENU_FORMAT_ITEMS[9]))
    format_menu.add_separator()
    format_menu.add_command(label=MENU_FORMAT_ITEMS[10], command=lambda:print(MENU_FORMAT_ITEMS[10]))
    menubar.add_cascade(label=MENU_ITEMS[2], menu=format_menu)

def menu_run(menubar):
    '''定义菜单Run'''
    run_menu = Menu(menubar, tearoff=1)
    run_menu.add_command(label=MENU_RUN_ITEMS[0], command=lambda:print(MENU_RUN_ITEMS[0]))
    run_menu.add_separator()
    run_menu.add_command(label=MENU_RUN_ITEMS[1], command=lambda:print(MENU_RUN_ITEMS[1]))
    run_menu.add_command(label=MENU_RUN_ITEMS[2], command=lambda:print(MENU_RUN_ITEMS[2]))
    menubar.add_cascade(label=MENU_ITEMS[-4], menu=run_menu)

def meun_options(menubar):
    '''定义菜单Options'''
    options_menu = Menu(menubar, tearoff=1)
    options_menu.add_command(label=MENU_OPTIONS_ITEMS[0], command=lambda:print(MENU_OPTIONS_ITEMS[0]))
    options_menu.add_separator()
    options_menu.add_command(label=MENU_OPTIONS_ITEMS[1], command=lambda:print(MENU_OPTIONS_ITEMS[1]))
    menubar.add_cascade(label=MENU_ITEMS[-3], menu=options_menu)

def menu_windows(menubar):
    '''定义菜单Windows'''
    windows_menu = Menu(menubar, tearoff=1)
    windows_menu.add_command(label=MENU_WINDOWS_ITEMS[0], command=lambda:print(MENU_WINDOWS_ITEMS[0]))
    windows_menu.add_separator()
    menubar.add_cascade(label=MENU_ITEMS[-2], menu=windows_menu)

def meun_help(menubar):
    '''定义菜单Help'''
    help_menu = Menu(menubar, tearoff=1)
    help_menu.add_command(label=MENU_HELP_ITEMS[0], command=about_idel)
    help_menu.add_separator()
    help_menu.add_command(label=MENU_HELP_ITEMS[1], command=lambda:print(MENU_HELP_ITEMS[1]))
    help_menu.add_command(label=MENU_HELP_ITEMS[2], command=lambda:print(MENU_HELP_ITEMS[2]))
    menubar.add_cascade(label=MENU_ITEMS[-1], menu=help_menu)

def about_idel():
    '''Help-About IDEL function'''
    label = Label(root, text=ABOUT_MESSAGE, fg='blue')
    label.pack(side='top')

def init_menu_bar(menubar):
    '''初始化菜单条'''
    menu_file(menubar)     #file
    menu_edit(menubar)     #edit
    menu_format(menubar)   #format
    menu_run(menubar)      #run
    meun_options(menubar)  #options
    menu_windows(menubar)  #windows
    meun_help(menubar)     #help

def get_tk():
    '''获取一个Tk对象'''
    return Tk()

def set_tk_title(tk, title):
    '''给窗口定义title'''
    if title is not None and title != '':
        tk.title(title)
    else:
        tk.title('chenfufeng v1.0')

def set_tk_geometry(tk, size):
    '''设置窗口大小，size的格式为：widthxheight,如：size = '200x100'.'''
    if size is not None and size != '':
        tk.geometry(size)
    else:
        tk.geometry('670x600')

def get_menu(tk):
    '''获取一个菜单条'''
    return Menu(tk)

class addNewConnect(object):
  """docstring for ClassName"""
  def __init__(self, root):
    #super(ClassName, self).__init__()
    self.root = root
    self.SelectSerial()
    self.SelectTestCase()
    
  def SelectSerial(self):
      L1 = ttk.Label(self.root, text="选择串口")
      L1.pack(side=TOP,pady = 2)
      comvalue=tk.StringVar()#窗体自带的文本，新建一个值  
      #comvalue = "COM1"
      self.comboxlist=ttk.Combobox(self.root,textvariable=comvalue) #初始化  
      self.comboxlist["values"]=("COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10","COM11","COM12","COM13","COM14","COM15")  
      self.comboxlist.current(0)  #选择第一个  
      self.comboxlist.bind("<<ComboboxSelected>>",self.comboxlist.get())  #绑定事件,(下拉列表框被选中时，绑定go()函数)  
      self.comboxlist.pack(side=TOP)
      return self.comboxlist

  def startTest(self):   # 当acction被点击时,该函数则生效
      #action.configure()     # 设置button显示的内容
      #action.configure(state='disabled')      # 将按钮设置为灰色状态，不可使用状态  "/Serial COM11 /BAUD 115200"
      COM = "/Serial " + self.comboxlist.get() + " /BAUD 115200"
      #fd = FileDialog.LoadPathDialog(self.root)
      #loadfile = fd.go()
      print(COM)
      cmd = "SecureCRT /SCRIPT Autotest.py %s" %(COM)
      os.system(cmd)
      # button被点击之后会被执行

  def SelectTestCase(self):
      action = ttk.Button(root, text="选择并执行", command=self.startTest)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
      action.pack(side=TOP,pady = 0)




def function():
    global menubar
    global root
    #获得窗口对象
    root = Tk()
    #设置窗口大小
    set_tk_geometry(root, '')
    #设置窗口title
    set_tk_title(root, '物联网自动化测试工具 v1.0')
    #获取菜单对象
    menubar = get_menu(root)
    #初始化菜单
    init_menu_bar(menubar)
    #加载菜单配置
    root.config(menu=menubar)

    #connet = addNewConnect(root)
    
    mainloop()
    pass


#app = Select(root)
#root.withdraw()
#fd = FileDialog.LoadPathDialog(root)
#loadfile = fd.go()
#fd = SaveFileDialog(root)
#savefile = fd.go(key="test")
#print (loadfile)



if __name__ == '__main__':
    function()