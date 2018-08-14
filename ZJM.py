from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *
import tkinter.colorchooser
import tkinter.filedialog
import tkinter as tk
import HS

canva_W = 0
canva_H = 0

flag_CK_GuDing = FALSE

canva_X = 60
canva_Y = 50

WangGe_KuanDu = 20
WangGe_ShuMu_X = 0
WangGe_ShuMu_Y = 0

scal_X_Zhi = 0
scal_Y_Zhi = 0

# 全局滚轮屏幕坐标
Event_GunLun_x = 0
Event_GunLun_y = 0

# 全局 Canvas 坐标
Event_Canvas_x = 0
Event_Canvas_y = 0

# 滚轮参数
flag_GunLun_Gun = FALSE
flag_GunLun_Shang = FALSE
GL_Yuan_canva_X = 60
GL_Yuan_canva_Y = 50

# 记录字典
Button1 = {}
Canvas1 = {}
Checkbutton1 = {}
Combobox1 = {}
Entry1 = {}
Frame1 = {}
Label1 = {}
LabelFrame1 = {}
Listbox1 = {}
Message1 = {}
PanedWindow1 = {}
Radiobutton1 = {}
Scale1_X = {}
Scale1_Y = {}
Scrollbar1_X = {}
Scrollbar1_Y = {}
Spinbox1 = {}
Text1 = {}
Toplevel1 = {}
tkMessageBox1 = {}

Menu1 = {}
Menu1_ListCode = {}
Menu1_Delete_Num = []
Menu1_Son_Len = {}
zi_menu1_num_i = 0

# 画控件标志
KJBZ = ''

# 画控件数目标志
button1_i = 0
canvas1_i = 0
checkbutton1_i = 0
combobox1_i = 0
entry1_i = 0
frame1_i = 0
label1_i = 0
labelFrame1_i = 0
listbox1_i = 0
menu1_i = 0
message1_i = 0
panedWindow1_i = 0
radiobutton1_i = 0
scale1_x_i = 0
scale1_y_i = 0
scrollbar1_x_i = 0
scrollbar1_y_i = 0
spinbox1_i = 0
text1_i = 0
toplevel1_i =  0
tkMessageBox1_i = 0

# 记录各个部件类型删除的成员的 列表
Button1_List_Num = []
Canvas1_List_Num = []
Checkbutton1_List_Num = []
Combobox1_List_Num = []
Entry1_List_Num = []
Frame1_List_Num = []
Label1_List_Num = []
LabelFrame1_List_Num = []
Listbox1_List_Num = []
Message1_List_Num = []
PanedWindow1_List_Num = []
Radiobutton1_List_Num = []
Scale1_List_Num_X = []
Scale1_List_Num_Y = []
Spinbox1_List_Num = []
Text1_List_Num = []

# 事件字典
SJ_button_press_1 = {}
SJ_button_release_1 = {}
SJ_button_press_right_1 = {}
SJ_button_press_left_2 = {}
SJ_button_press_right_2 = {}
SJ_button_press_middle_1 = {}
SJ_button_press_middle_2 = {}
SJ_button_press_left_move = {}
SJ_cursor_enter = {}
SJ_cursor_leave = {}
SJ_get_key_focus = {}
SJ_lose_key_focus = {}
SJ_press_a_key = {}
SJ_press_enter_key = {}
SJ_when_control_change = {}
SJ_press_space_key = {}
SJ_shift_mouseWheel = {}
SJ_press_combinatorial_key = {}

# 当前控件名
DangQian_KJ_name = ''

# Menu 参数
flag_Menu_Kai = FALSE
D_ZhuMenu = {}
zi_menu1_sum = 0
DQ_ZhuMenu_ZiXiang_Num_i = 0
DQ_Zong_Len = 0
AnXia_Menu_Btn_Num = 0

# Hua_Radiobutton 参数
Radiobutton_i = 0  # 每一组当前的 Radiobutton 编号
flag_RadBtn_Zu = FALSE

# 编译 Text 参数
flag_BianYi_Text = FALSE
flag_Canva_Hide = FALSE

# Canvas 项目处理参数
# 选择参数
background_XiangMu_XuanDing = 'red'
foreground_XiangMu_XuanDing = 'white'

XuanZhong = {}
XuanZhong_sum = 0

# 属性框参数
flag_ShuXing_Tan = FALSE

# 部件编辑参数
flag_ZuJian_Move = TRUE

# 右键编辑选择
each_YouJian = ''
flag_TanChuan_BianJian = FALSE

# 完成时选框
XuanKuang_X0 = 0
XuanKuang_Y0 = 0
XuanKuang_X1 = 0
XuanKuang_Y1 = 0

# 窗口位置
win_X = 0
win_Y = 0

# 属性面板全局参数
lab_ControlType = ''
ent_ControlName = ''
ent_X0 = 0
ent_Y0 = 0
ent_width = 0
ent_height = 0
ent_length = 0
ent_fontSize = 0
combt_fontType = ''
combt_foreground = ''
combt_background = ''
combt_anchor = ''
combt_justify = ''
ent_text = ''
combt_state = ''
combt_relief = ''
combt_highlightcolor = ''
combt_highlightbackground = ''
combt_bitmap = ''
ent_image = ''
combt_padx = 0
combt_pady = 0
combt_takefocus = ''
combt_cursor = ''
ent_container = ''
ent_command = ''

# 窗口设置窗口变量
ck_name = ''
ck_init_x = ''
ck_init_y = ''
ck_is_width_not_change = 1
ck_is_height_not_change = 1
ck_is_minsize = 1
ck_init_minsize_w = 0
ck_init_minsize_h = 0
ck_is_maxsize = 1
ck_init_maxsize_w = 0
ck_init_maxsize_h = 0
ck_is_toolwindow = 0
ck_is_topmost = 1
ck_is_zoomed = 1
ck_set_icon = ''
ck_set_grid = 0
ck_is_transparency = 1
ck_scal_transparency = 1
ck_is_son_win = 1

Str_BianYi = ''
Str_BianYi_End = ''
Str_Menu = ''

# 定义空格tap
tap = "    "

# 窗口重要参数
bar_W = 30
bar_menu_W = 30
Distance = 0

# class of Main interface
class PyDraw(Tk):
    # Main interface Define
    def __init__(self):
        super().__init__()
        # Main interface parameter setting
        w = 1000
        h = 700
        self.minsize(w, h)  # 最小化固定

        S_width = self.winfo_screenwidth()
        S_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2, (S_height - h) / 2 - 30)
        self.geometry(size)

        self.state('zoomed')
        self.title('PyDraw')
        self.BiaoTi_Text = 'PyDraw'
        self.BiaoTi_Text_YanSe = 'black'
        self.ChuangKou_JiXia_YanSe = 'black'
        self.ChuangKou_BianTiLan_YanSe = 'white'
        self.ChuangKou_BeiJing_YanSe = 'white'

        # Scale setting
        self.Sca_JiZhi_X = 1000
        self.Sca_JiZhi_Y = 1000

        # parameter setting
        self.ChuangKou_BianYan_YanSe = 'black'
        self.ChuangKou_BiaoTiLan_YanSe = 'green'

        # Control component initial parameter setting
        # Button parameter
        self.Button_H = 50
        self.Button_W = 100
        self.Button_NO = 0
        self.Button_YanSe = 'gray'
        self.Button_Text_YanSe = 'white'

        # Boolean value setting
        global flag_CK_GuDing
        flag_CK_GuDing = FALSE
        self.flag_WangGe = FALSE
        self.flag_SongKai = FALSE
        self.flag_BuJian_YinCang = FALSE

        # Original canvas parameter
        self.Yuan_canva_H = 600  # height 对应 Y
        self.Yuan_canva_W = 800  # width  对应 X

        # Canvas parameter
        global canva_H
        global canva_W
        canva_H = self.Yuan_canva_H
        canva_W = self.Yuan_canva_W
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        # Canvas position
        global canva_X
        global canva_Y
        global GL_Yuan_canva_X
        global GL_Yuan_canva_Y
        global bar_W
        canva_X = 60
        canva_Y = 50

        GL_Yuan_canva_X = 60
        GL_Yuan_canva_Y = 50

        # Frame parameter
        self.fram_H = canva_H  # height 对应 Y
        self.fram_W = canva_W  # width  对应 X

        # Menu bar width
        self.bar_W = bar_W

        # Grid width parameter
        global WangGe_KuanDu
        WangGe_KuanDu = 20
        self.WangGe_YanSe = 'gray'

        # 编译 Text 参数初始化
        global flag_BianYi_Text
        global flag_Canva_Hide
        global XuanZhong_sum
        XuanZhong_sum = 0
        flag_Canva_Hide = FALSE
        flag_BianYi_Text = FALSE

        # 属性框参数
        global flag_ShuXing_Tan
        flag_ShuXing_Tan = FALSE

        self.V_Scal_Y1 = StringVar()
        self.V_Scal_Y2 = StringVar()

        # 设置画布的放大调节及参数定义设置
        self.vy = StringVar()
        self.vx = StringVar()
        self.vx_Text_font = StringVar()

        self.ent_y = StringVar()
        self.ent_x = StringVar()

        self.GuDing_Text = StringVar()
        self.GuDing_Text.set('Lock')

        self.Btn_WG_Text = StringVar()
        self.Btn_WG_Text.set('Grid')

        self.Btn_YinCang_Text = StringVar()
        self.Btn_YinCang_Text.set('Hide')

        self.Btn_ShuXing_Text = StringVar()
        self.Btn_ShuXing_Text.set('<=')

        self.Tv_BianYi_Text = StringVar()
        self.Tv_BianYi_Text.set('Text')

        self.Tv_Canva_Hide = StringVar()
        self.Tv_Canva_Hide.set('Paint')

        # 网格参数设定
        global WangGe_ShuMu_X
        global WangGe_ShuMu_Y
        WangGe_ShuMu_X = (canva_H - self.bar_W) / WangGe_KuanDu
        WangGe_ShuMu_Y = canva_W / WangGe_KuanDu

        # 全局屏幕坐标
        global Event_GunLun_x
        global Event_GunLun_y
        Event_GunLun_x = 0
        Event_GunLun_y = 0

        # Switch to the main interface UI setting
        self.Set_UI()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Set_UI(self):
        global canva_X
        global canva_Y
        global canva_W
        global canva_H

        # Set Canvas
        self.canva = Canvas(bg='white', width=canva_W, height=canva_H)  # scrollregion=(0, 0, 1000, 1000))  # 创建canva
        self.canva.place(x=canva_X, y=canva_Y)  # 放置canva的位置

        # 画 Menu
        self.it_Menu = self.canva.create_rectangle(0, 0, 0, 0)

        # 画外边框
        self.it1 = self.canva.create_rectangle(2, canva_H - 1, canva_W - 1, 2,
                                               fil=self.ChuangKou_BeiJing_YanSe)
        # 画标题栏
        self.it2 = self.canva.create_rectangle(2, self.bar_W, canva_W - 1, self.bar_W,
                                               fil=self.ChuangKou_BiaoTiLan_YanSe)

        # 画标题
        self.it_BiaoTi = self.canva.create_text(43, 16, text=self.BiaoTi_Text,
                                                font=('Consol', 11),
                                                fill=self.BiaoTi_Text_YanSe)

        # 画标题栏按钮
        self.it_BiaoTi_AnNiu_ZuiXiao = self.canva.create_text(canva_W - 116, 16, text='—',
                                                              font=('Consol', 11),
                                                              fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_ZuiDa = self.canva.create_text(canva_W - 70, 16, text='□',
                                                            font=('Consol', 11),
                                                            fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_GuanBi = self.canva.create_text(canva_W - 28, 16, text='X',
                                                             font=('Helvetica', 11),
                                                             fill=self.BiaoTi_Text_YanSe)

        self.Menubar = Menu(self)
        # 定义下拉菜单栏
        FileMenu = Menu(self.Menubar, tearoff=0)
        FileMenu.add_command(label='Compile', command=self.BianYi)
        FileMenu.add_command(label='Generate', command=self.BianYi)
        FileMenu.add_command(label='Copy', command=self.BianYi)
        FileMenu.add_separator()
        FileMenu.add_command(label='Quit', command=self.quit)
        self.Menubar.add_cascade(label='File', menu=FileMenu)

        # 定义控件菜单栏
        KongJianMenu = Menu(self.Menubar, tearoff=0)
        KongJianMenu.add_command(label='Button', command=self.Hua_Button)
        KongJianMenu.add_command(label='Canvas', command=self.Hua_Canvas)
        KongJianMenu.add_command(label='Checkbutton', command=self.Hua_Checkbutton)
        KongJianMenu.add_command(label='Combobox', command=self.Hua_Combobox)
        KongJianMenu.add_command(label='Entry', command=self.Hua_Entry)
        KongJianMenu.add_command(label='Frame', command=self.Hua_Frame)
        KongJianMenu.add_command(label='Label', command=self.Hua_Label)
        KongJianMenu.add_command(label='LabelFrame', command=self.Hua_LabelFrame)
        KongJianMenu.add_command(label='Listbox', command=self.Hua_Listbox)
        KongJianMenu.add_command(label='Menu', command=self.Hua_Menu)
        KongJianMenu.add_command(label='Message', command=self.Hua_Message)
        KongJianMenu.add_command(label='PanedWindow', command=self.Hua_PanedWindow)
        KongJianMenu.add_command(label='Radiobutton', command=self.Hua_Radiobutton)
        KongJianMenu.add_command(label='Scale_X', command=self.Hua_Scale_X)
        KongJianMenu.add_command(label='Scale_Y', command=self.Hua_Scale_Y)
        KongJianMenu.add_command(label='Spinbox', command=self.Hua_Spinbox)
        KongJianMenu.add_command(label='Text', command=self.Hua_Text)
        self.Menubar.add_cascade(label='Control', menu=KongJianMenu)

        # 定义自画控件菜单栏
        SheZhiMenu = Menu(self.Menubar, tearoff=0)
        SheZhiMenu.add_command(label='System Setup', command=HS.hello)
        self.Menubar.add_cascade(label='Setup', menu=SheZhiMenu)


        # 定义窗口菜单栏
        ChuangKouMenu = Menu(self.Menubar, tearoff=0)
        ChuangKouMenu.add_command(label='New son_win', command=HS.hello)
        ChuangKouMenu.add_command(label='Current win set', command=HS.hello)
        ChuangKouMenu.add_command(label='Win control information', command=HS.hello)
        self.Menubar.add_cascade(label='Win', menu=ChuangKouMenu)

        # 定义对话框菜单栏
        DuiHuaKuangMenu = Menu(self.Menubar, tearoff=0)
        DuiHuaKuangMenu.add_command(label='New news dialog', command=HS.hello)
        DuiHuaKuangMenu.add_command(label='New flie dialog', command=HS.hello)
        DuiHuaKuangMenu.add_command(label='New colour dialog', command=HS.hello)
        self.Menubar.add_cascade(label='Dialog', menu=DuiHuaKuangMenu)

        # 定义帮助菜单栏
        BangZhuMenu = Menu(self.Menubar, tearoff=0)
        BangZhuMenu.add_command(label='About', command=HS.hello)
        self.Menubar.add_cascade(label='Help', menu=BangZhuMenu)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 定义右键菜单
        # 新建控件右键菜单
        self.New_kj_menu = Menu(self.Menubar, tearoff=0)
        self.New_kj_menu.add_command(label='Button', command=self.Hua_Button)
        self.New_kj_menu.add_command(label='Canvas', command=self.Hua_Canvas)
        self.New_kj_menu.add_command(label='Checkbutton', command=self.Hua_Checkbutton)
        self.New_kj_menu.add_command(label='Combobox', command=self.Hua_Combobox)
        self.New_kj_menu.add_command(label='Entry', command=self.Hua_Entry)
        self.New_kj_menu.add_command(label='Frame', command=self.Hua_Frame)
        self.New_kj_menu.add_command(label='Label', command=self.Hua_Label)
        self.New_kj_menu.add_command(label='LabelFrame', command=self.Hua_LabelFrame)
        self.New_kj_menu.add_command(label='Listbox', command=self.Hua_Listbox)
        self.New_kj_menu.add_command(label='Menu', command=self.Hua_Menu)
        self.New_kj_menu.add_command(label='Message', command=self.Hua_Message)
        self.New_kj_menu.add_command(label='PanedWindow', command=self.Hua_PanedWindow)
        self.New_kj_menu.add_command(label='Radiobutton', command=self.Hua_Radiobutton)
        self.New_kj_menu.add_command(label='Scale_X', command=self.Hua_Scale_X)
        self.New_kj_menu.add_command(label='Scale_Y', command=self.Hua_Scale_Y)
        self.New_kj_menu.add_command(label='Spinbox', command=self.Hua_Spinbox)
        self.New_kj_menu.add_command(label='Text', command=self.Hua_Text)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 编辑控件右键菜单
        self.BianJi_kj_menu = Menu(self.Menubar, tearoff=0)
        self.BianJi_kj_menu.add_command(label='OK', command=self.BianJi_OK)
        self.BianJi_kj_menu.add_command(label='Move', command=self.BianJi_Move)
        self.BianJi_kj_menu.add_command(label='Design', command=self.BianJi_Design)
        self.BianJi_kj_menu.add_command(label='Delete', command=self.BianJi_Delete)
        self.BianJi_kj_menu.add_command(label='Cancel', command=self.BianJi_Cancel)

        # 展示主菜单
        self.config(menu=self.Menubar)

        # X:横向  Y:纵向 设置部件
        self.Lab1 = Label(text='Y:', font=('Consol', '26', 'bold'), foreground='DarkBlue')
        self.Lab1.place(x=0, y=0)

        self.Lab2 = Label(text='X:', font=('Consol', '26', 'bold'), foreground='DarkBlue')
        self.Lab2.place(x=60, y=0)

        self.Lab_CK_X_len = Label(text='X length', font=('Consol', '12'), foreground='DarkBlue')
        self.Lab_CK_X_len.place(x=623, y=0)

        self.Lab_CK_Y_len = Label(text='Y length', font=('Consol', '12'), foreground='DarkBlue')
        self.Lab_CK_Y_len.place(x=623, y=26)

        self.Lab_font_size = Label(text='font size', font=('Consol', '12'), foreground='DarkBlue')
        self.Lab_font_size.place(x=1250, y=760)
        self.Lab_font_size.lower()

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Btn_CK_ZhuanDao = Button(text='To win', font=('Consol', 9), foreground='DarkBlue', width=8, height=1,
                      command=self.ChuangKouZhuan)
        self.Btn_CK_ZhuanDao.place(x=762, y=0)  # 要想以后修改Btn_CK_ZhuanDao，必须先定义后摆放！

        self.Btn_CK_FuWei = Button(text='Reset win', font=('Consol', 9), foreground='DarkBlue', width=8, height=1,
                      command=self.FuWeiKouZhuan)
        self.Btn_CK_FuWei.place(x=762, y=26)

        self.Btn_CK_Set = Button(text='Win_Set', font=('Consol', 9), foreground='DarkBlue', width=8, height=1,
                                   command=self.Set_KouZhuan)
        self.Btn_CK_Set.place(x=826, y=26)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Hide or Show 键
        self.Btn_YinCang = Button(textvariable=self.Btn_YinCang_Text, font=('Consol', 10), foreground='DarkBlue', width=6, height=1,
                           command=self.YinCang)
        self.Btn_YinCang.place(x=1482, y=0)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Update 键
        self.Btn_Update = Button(text='Update', font=('Consol', 10), foreground='DarkBlue',
                                  width=6, height=1,
                                  command=self.UI_Ban_Btn_OK)
        self.Btn_Update.place(x=2000, y=26)
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        #  属性键
        self.Btn_ShuXing = Button(textvariable=self.Btn_ShuXing_Text, font=('Consol', 10), foreground='DarkBlue',
                                  width=6, height=1,
                                  command=self.ShuXing_Zhan)
        self.Btn_ShuXing.place(x=1482, y=26)

        self.Btn_BianYi = Button(text='Compi', font=('Consol', 10), foreground='black', width=5, height=2,
                           command=self.BianYi)
        self.Btn_BianYi.place(x=6, y=600)
        self.Btn_BianYi.lower()

        self.Btn_BianYi_FuZhi = Button(text='Copy', font=('Consol', 10), foreground='black', width=5, height=2,
                                 command=self.BianYi_Color_Green)
        self.Btn_BianYi_FuZhi.place(x=6, y=650)
        self.Btn_BianYi_FuZhi.lower()

        self.Btn_BianYi_ShengCheng = Button(text='Gener', font=('Consol', 10), foreground='black', width=5, height=2,
                                 command=self.BianYi_Color_Green)
        self.Btn_BianYi_ShengCheng.place(x=6, y=700)
        self.Btn_BianYi_ShengCheng.lower()

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 下排按钮
        self.Btn_BianYi_Text = Button(textvariable=self.Tv_BianYi_Text, font=('华文行楷', 12), foreground='red', width=5, height=1,
                                      command=self.BianYi_Text)
        self.Btn_BianYi_Text.place(x=60, y=746)
        self.Btn_BianYi_Text.lower()

        self.Btn_Canva_Hide = Button(textvariable=self.Tv_Canva_Hide, font=('华文行楷', 12), foreground='DarkBlue', width=5,
                                      height=1,
                                      command=self.Canva_Hide)
        self.Btn_Canva_Hide.place(x=120, y=746)
        self.Btn_Canva_Hide.lower()

        self.Btn_BianYi_Color_White = Button(text='Color', font=('华文行楷', 12), foreground='black', background='white', width=5, height=1,
                                      command=self.BianYi_Color_White)
        self.Btn_BianYi_Color_White.place(x=180, y=746)
        self.Btn_BianYi_Color_White.lower()

        self.Btn_BianYi_Color_Black = Button(text='Color', font=('华文行楷', 12), foreground='white', background='black', width=5, height=1,
                                       command=self.BianYi_Color_Black)
        self.Btn_BianYi_Color_Black.place(x=240, y=746)
        self.Btn_BianYi_Color_Black.lower()

        self.Btn_BianYi_Color_YangPiZhi = Button(text='Color', font=('华文行楷', 12), foreground='black', background='LemonChiffon', width=5, height=1,
                                       command=self.BianYi_Color_YangPiZhi)
        self.Btn_BianYi_Color_YangPiZhi.place(x=300, y=746)
        self.Btn_BianYi_Color_YangPiZhi.lower()

        self.Btn_BianYi_Color_Green = Button(text='Color', font=('华文行楷', 12), foreground='white', background='green', width=5, height=1,
                                       command=self.BianYi_Color_Green)
        self.Btn_BianYi_Color_Green.place(x=360, y=746)
        self.Btn_BianYi_Color_Green.lower()

        self.Btn_WangGe = Button(textvariable=self.Btn_WG_Text, font=('华文行楷', 13), foreground='DarkBlue',
                                 width=5, height=1, command=self.QiYong_WangGe)
        self.Btn_WangGe.place(x=420, y=746)
        self.Btn_WangGe.lower()

        self.GuDing = Button(textvariable=self.GuDing_Text, font=('华文行楷', 13),foreground='DarkBlue', width=5, height=1,
                             command=self.GuDingChuangKou)
        self.GuDing.place(x=0, y=746)
        self.GuDing.lower()

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Ent_X = Entry(textvariable=self.ent_x, width=5, font=('Consol', '12', 'bold'), foreground='Darkblue')
        self.Ent_X.place(x=703, y=0)

        self.Ent_Y = Entry(textvariable=self.ent_y, width=5, font=('Consol', '12', 'bold'), foreground='Darkblue')
        self.Ent_Y.place(x=703, y=26)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Sca_Y = Scale(from_=0, to=self.Sca_JiZhi_Y, orient=VERTICAL, variable=self.vy, length=500,
                      resolution=1, command=self.HuaBuFangDa_Y)
        self.Sca_Y.place(x=0, y=40)

        self.Sca_X = Scale(from_=0, to=self.Sca_JiZhi_X, orient=HORIZONTAL, variable=self.vx, length=500,
                      resolution=1, command=self.HuaBuFangDa_X)
        self.Sca_X.place(x=100, y=0)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 字体调节滚动条
        self.Sca_Text_front = Scale(from_=8, to=50, orient=HORIZONTAL, variable=self.vx_Text_font, length=200,
                           resolution=1, command=self.Text_font)
        self.Sca_Text_front.set(16)
        self.Sca_Text_front.place(x=1328, y=739)
        self.Sca_Text_front.lower()

        self.ent_x.set(canva_W)
        self.ent_y.set(canva_H)

        self.PanedWin_X1 = PanedWindow(width=1480, height=690, sashwidth=6,  sashrelief=SUNKEN)
        self.PanedWin_X1.place(x=2000, y=50)
        self.PanedWin_X1.lower()

        self.Text_BianYi = ScrolledText(self.PanedWin_X1, width=74, height=22, font=('Consolas', '20'), insertbackground='black')
        self.PanedWin_X1.add(self.Text_BianYi)
        self.Text_BianYi.lower()

        self.PanedWin_Y1 = PanedWindow(self.PanedWin_X1, orient=VERTICAL, sashwidth=6,  sashrelief=SUNKEN)
        self.PanedWin_X1.add(self.PanedWin_Y1)

        self.Paned_Frame_Y1 = Frame(self.PanedWin_Y1,  width=300, height=380, bg='red')
        self.PanedWin_Y1.add(self.Paned_Frame_Y1)

        self.Paned_Frame_Y2 = Frame(self.PanedWin_Y1, width=330, height=300, bg='green')
        self.PanedWin_Y1.add(self.Paned_Frame_Y2)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.PanedF_Canvas_Y1 = Canvas(self.Paned_Frame_Y1, bg='white', width=300, height=1700)
        self.PanedF_Canvas_Y1.place(x=48, y=0)

        self.Scal_Y1 = Scale(self.Paned_Frame_Y1, from_=0, to=100, fg='white', bg='white', resolution=2, length=380,
                             variable=self.V_Scal_Y1, command=self.V_P_Scal_Y1)
        self.Scal_Y1.pack(side=LEFT, fill=Y)

        self.PanedF_Canvas_Y2 = Canvas(self.Paned_Frame_Y2, bg='white', width=300, height=1700)
        self.PanedF_Canvas_Y2.place(x=48, y=0)

        self.Scal_Y2 = Scale(self.Paned_Frame_Y2, from_=0, to=100, fg='white', bg='white', resolution=2, length=380,
                             variable=self.V_Scal_Y2, command=self.V_P_Scal_Y2)
        self.Scal_Y2.pack(side=LEFT, fill=Y)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 上属性框部件设置
        self.lab_ControlType = StringVar()
        self.ent_ControlName = StringVar()
        self.ent_X0 = IntVar()
        self.ent_Y0 = IntVar()
        self.ent_width = IntVar()
        self.ent_height = IntVar()
        self.ent_length = IntVar()
        self.ent_fontSize = IntVar()
        self.combt_fontType = StringVar()
        self.combt_foreground = StringVar()
        self.combt_background = StringVar()
        self.combt_anchor = StringVar()
        self.combt_justify = StringVar()
        self.ent_text = StringVar()
        self.combt_state = StringVar()
        self.combt_relief = StringVar()
        self.combt_highlightcolor = StringVar()
        self.combt_highlightbackground = StringVar()
        self.combt_bitmap = StringVar()
        self.ent_image = StringVar()
        self.combt_padx = IntVar()
        self.combt_pady = IntVar()
        self.combt_takefocus = StringVar()
        self.combt_cursor = StringVar()
        self.ent_container = StringVar()
        self.ent_command = StringVar()

        global lab_ControlType
        global ent_ControlName
        global ent_X0
        global ent_Y0
        global ent_width
        global ent_height
        global ent_length
        global ent_fontSize
        global combt_fontType
        global combt_foreground
        global combt_background
        global combt_anchor
        global combt_justify
        global ent_text
        global combt_state
        global combt_relief
        global combt_highlightcolor
        global combt_highlightbackground
        global combt_bitmap
        global ent_image
        global combt_padx
        global combt_pady
        global combt_takefocus
        global combt_cursor
        global ent_container
        global ent_command

        # 上属性框部件设置
        self.lab_ControlType.set(lab_ControlType)
        self.ent_ControlName.set(ent_ControlName)
        self.ent_X0.set(ent_X0)
        self.ent_Y0.set(ent_Y0)
        self.ent_width.set(ent_width)
        self.ent_height.set(ent_height)
        self.ent_length.set(ent_length)
        self.ent_fontSize.set(ent_fontSize)
        self.combt_fontType.set(combt_fontType)
        self.combt_foreground.set(combt_foreground)
        self.combt_background.set(combt_background)
        self.combt_anchor.set(combt_anchor)
        self.combt_justify.set(combt_justify)
        self.ent_text.set(ent_text)
        self.combt_state.set(combt_state)
        self.combt_relief.set(combt_relief)
        self.combt_highlightcolor.set(combt_highlightcolor)
        self.combt_highlightbackground.set(combt_highlightbackground)
        self.combt_bitmap.set(combt_bitmap)
        self.ent_image.set(ent_image)
        self.combt_padx.set(combt_padx)
        self.combt_pady.set(combt_pady)
        self.combt_takefocus.set(combt_takefocus)
        self.combt_cursor.set(combt_cursor)
        self.ent_container.set(ent_container)
        self.ent_command.set(ent_command)

        self.JG_Y=70
        self.JG_X=6
        self.FuDong=6
        self.FuDong_Scal_Y=30

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Control Type

        self.l = Label(self.PanedF_Canvas_Y1, text='control type', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 0 + self.FuDong)

        self.Ent_ControlType = Label(self.PanedF_Canvas_Y1, textvariable=self.lab_ControlType, width=20, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_ControlType.place(x=self.JG_X + 120, y=self.JG_Y * 0 + self.FuDong)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Control Name

        self.l = Label(self.PanedF_Canvas_Y1, text='control name', bg='white')
        self.l.place(x=self.JG_X, y=40)

        self.Ent_ControlName = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_ControlName, width=16, bg='LightGreen',
                            foreground='black')
        self.Ent_ControlName.place(x=self.JG_X + 120, y=40)

        self.Btn_Ok_ControlName = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                         , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_ControlName.place(x=self.JG_X + 241, y=40)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # X0

        self.l = Label(self.PanedF_Canvas_Y1, text='X0', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y*1 + self.FuDong)

        self.Ent_X0 = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_X0, width=16, bg='DeepSkyBlue',
                          foreground='Darkblue')
        self.Ent_X0.place(x=self.JG_X + 120, y=self.JG_Y*1 + self.FuDong)

        self.Btn_Ok_X0 = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                         , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_X0.place(x=self.JG_X + 241, y=self.JG_Y*1 + self.FuDong)

        self.Sca_X0 = Scale(self.PanedF_Canvas_Y1, from_=0, to=1800, orient=HORIZONTAL, variable=self.ent_X0,
                     length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_X0.place(x=self.JG_X, y=self.JG_Y*1 + self.FuDong_Scal_Y)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # Y0

        self.l = Label(self.PanedF_Canvas_Y1, text='Y0', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 2 + self.FuDong)

        self.Ent_Y0 = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_Y0, width=16, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_Y0.place(x=self.JG_X + 120, y=self.JG_Y * 2 + self.FuDong)

        self.Btn_Ok_Y0 = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_Y0.place(x=self.JG_X + 241, y=self.JG_Y * 2 + self.FuDong)

        self.Sca_Y0 = Scale(self.PanedF_Canvas_Y1, from_=0, to=1600, orient=HORIZONTAL, variable=self.ent_Y0,
                       length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_Y0.place(x=self.JG_X, y=self.JG_Y * 2 + self.FuDong_Scal_Y)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # width

        self.l = Label(self.PanedF_Canvas_Y1, text='width', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 3 + self.FuDong)

        self.Ent_width = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_width, width=16, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_width.place(x=self.JG_X + 120, y=self.JG_Y * 3 + self.FuDong)

        self.Btn_Ok_width = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_width.place(x=self.JG_X + 241, y=self.JG_Y * 3 + self.FuDong)

        self.Sca_width = Scale(self.PanedF_Canvas_Y1, from_=0, to=300, orient=HORIZONTAL, variable=self.ent_width,
                            length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_width.place(x=self.JG_X, y=self.JG_Y * 3 + self.FuDong_Scal_Y)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # height

        self.l = Label(self.PanedF_Canvas_Y1, text='height', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 4 + self.FuDong)

        self.Ent_height = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_height, width=16, bg='DeepSkyBlue',
                            foreground='Darkblue')
        self.Ent_height.place(x=self.JG_X + 120, y=self.JG_Y * 4 + self.FuDong)

        self.Btn_Ok_height = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                   , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_height.place(x=self.JG_X + 241, y=self.JG_Y * 4 + self.FuDong)

        self.Sca_height = Scale(self.PanedF_Canvas_Y1, from_=0, to=100, orient=HORIZONTAL, variable=self.ent_height,
                            length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_height.place(x=self.JG_X, y=self.JG_Y * 4 + self.FuDong_Scal_Y)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # length
        len_scal = 16
        D = 18
        self.l = Label(self.PanedF_Canvas_Y1, text='length', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * len_scal - D)

        self.Ent_length = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_length, width=16, bg='DeepSkyBlue',
                                foreground='Darkblue')
        self.Ent_length.place(x=self.JG_X + 120, y=self.JG_Y * len_scal - D)

        self.Btn_Ok_length = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_length.place(x=self.JG_X + 241, y=self.JG_Y * len_scal - D)

        self.Sca_length = Scale(self.PanedF_Canvas_Y1, from_=0, to=2000, orient=HORIZONTAL, variable=self.ent_length,
                                length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_length.place(x=self.JG_X, y=self.JG_Y * len_scal + self.FuDong_Scal_Y - 6 - D)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # fontSize

        self.l = Label(self.PanedF_Canvas_Y1, text='fontSize', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 5 + self.FuDong)

        self.Ent_fontSize = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_fontSize, width=16, bg='DeepSkyBlue',
                                foreground='Darkblue')
        self.Ent_fontSize.place(x=self.JG_X + 120, y=self.JG_Y * 5 + self.FuDong)

        self.Btn_Ok_fontSize = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_fontSize.place(x=self.JG_X + 241, y=self.JG_Y * 5 + self.FuDong)

        self.Sca_fontSize = Scale(self.PanedF_Canvas_Y1, from_=1, to=100, orient=HORIZONTAL, variable=self.ent_fontSize,
                                length=260, width=10, resolution=1, bg='white', command=self.UI_Ban)
        self.Sca_fontSize.place(x=self.JG_X, y=self.JG_Y * 5 + self.FuDong_Scal_Y)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # fontType

        self.l = Label(self.PanedF_Canvas_Y1, text='fontType', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 6 + self.FuDong)

        self.comb_FontType_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_fontType)
        self.comb_FontType_Chose['values'] = \
            (
                'TkDefaultFont','Consolas', 'Arial', 'Algerian', 'Arial Rounded MT Bold', 'Bell MT', 'Bauhaus 93', 'BankGothic Md BT'
                , 'Bradley Hand ITC', 'CASTELLAR', 'Elephant', 'French Script MT', 'Helvetica', 'Palace Script MT'
                , 'MS UI Gothic', 'MingLiU_HKSCS-ExtB', 'Vineta BT', 'Swis721 BlkEx BT', '微软雅黑', '华文宋体'
                , '华文行楷', '华文隶书', '华文新魏', '华文楷体', '华文细黑', '华文中宋', '华文彩云', '华文琥珀'
                , '方正舒体', '方正姚体', '楷体', '宋体', '隶书', '幼圆', '新宋体'
            )
        self.comb_FontType_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 6 + self.FuDong)
        self.comb_FontType_Chose.current(0)

        self.Btn_Ok_fontSize = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                      , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_fontSize.place(x=self.JG_X + 241, y=self.JG_Y * 6 + self.FuDong)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # foreground

        self.l = Label(self.PanedF_Canvas_Y1, text='foreground', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 - 20)

        self.Btn_foreground = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1, font=('Consol', '9'),
                                     command=self.More_foreground)
        self.Btn_foreground.place(x=self.JG_X+215, y=self.JG_Y * 7 - 20)

        self.Btn_Ok_foreground = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                      , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_foreground.place(x=self.JG_X + 241, y=self.JG_Y * 7 - 20)

        self.comb_foreground_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15, textvariable=self.combt_foreground)
        self.comb_foreground_Chose['values'] = \
            (
                'SystemButtonText','black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
                , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet','Beige'
                , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue','Aqua'
                , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
                , 'SlateGray', 'LightSlateGray', 'CadetBlue','DodgerBlue'
            )
        self.comb_foreground_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 - 20)
        self.comb_foreground_Chose.current(0)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # background

        self.l = Label(self.PanedF_Canvas_Y1, text='background', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 20)

        self.Btn_background = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1, font=('Consol', '9'),
                                     command=self.More_background)
        self.Btn_background.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 20)

        self.Btn_Ok_background = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                        , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_background.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 20)

        self.comb_background_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15, textvariable=self.combt_background)
        self.comb_background_Chose['values'] = \
            (
                'SystemButtonFace','black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
                , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet', 'Beige'
                , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue', 'Aqua'
                , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
                , 'SlateGray', 'LightSlateGray', 'CadetBlue', 'DodgerBlue'
            )
        self.comb_background_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 20)
        self.comb_background_Chose.current(0)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # anchor
        self.l = Label(self.PanedF_Canvas_Y1, text='anchor', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 60)

        self.combt_anchor_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_anchor)
        self.combt_anchor_Chose['values'] = \
            (
               'center', 'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'
            )
        self.combt_anchor_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 60)
        self.combt_anchor_Chose.current(0)

        self.Btn_Ok_anchor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                        , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_anchor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 60)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # justify

        self.l = Label(self.PanedF_Canvas_Y1, text='justify', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 100)  # y 方向每 40一间隔

        self.combt_justify_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_justify)
        self.combt_justify_Chose['values'] = \
            (
                'center', 'left', 'right'
            )
        self.combt_justify_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 100)
        self.combt_justify_Chose.current(0)

        self.Btn_Ok_justify = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_justify.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 100)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # text

        self.l = Label(self.PanedF_Canvas_Y1, text='text', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 140)  # y 方向每 40一间隔

        self.Ent_text = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_text, width=26, bg='LightCyan',
                                foreground='Darkblue')
        self.Ent_text.place(x=self.JG_X+50, y=self.JG_Y * 7 + 140)

        self.Btn_Ok_text = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                     , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_text.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 140)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # state

        self.l = Label(self.PanedF_Canvas_Y1, text='state', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 180)  # y 方向每 40一间隔

        self.combt_state_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_state)
        self.combt_state_Chose['values'] = \
            (
                'normal', 'active', 'disabled'
            )
        self.combt_state_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 180)
        self.combt_state_Chose.current(0)

        self.Btn_Ok_state = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                  , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_state.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 180)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # relief

        self.l = Label(self.PanedF_Canvas_Y1, text='relief', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 220)  # y 方向每 40一间隔

        self.combt_relief_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_relief)
        self.combt_relief_Chose['values'] = \
            (
                'raised', 'sunken', 'flat', 'ridge', 'solid', 'groove'
            )
        self.combt_relief_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 220)
        self.combt_relief_Chose.current(0)

        self.Btn_Ok_relief = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                   , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_relief.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 220)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # highlightcolor

        self.l = Label(self.PanedF_Canvas_Y1, text='highlight', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 260)

        self.Btn_highlightcolor = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1, font=('Consol', '9'),
                                         command=self.More_highlightcolor)
        self.Btn_highlightcolor.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 260)

        self.Btn_Ok_highlightcolor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_highlightcolor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 260)

        self.comb_highlightcolor_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15,
                                                      textvariable=self.combt_highlightcolor)
        self.comb_highlightcolor_Chose['values'] = \
            (
                'SystemWindowFrame', 'black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
                , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet', 'Beige'
                , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue', 'Aqua'
                , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
                , 'SlateGray', 'LightSlateGray', 'CadetBlue', 'DodgerBlue'
            )
        self.comb_highlightcolor_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 260)
        self.comb_highlightcolor_Chose.current(0)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # highlightbackground

        self.l = Label(self.PanedF_Canvas_Y1, text='highlight_B', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 300)

        self.Btn_highlightbackground = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1,
                                              font=('Consol', '9'), command=self.More_highlightbackground)
        self.Btn_highlightbackground.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 300)

        self.Btn_Ok_highlightcolor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                            , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_highlightcolor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 300)

        self.comb_highlightbackground_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=15,
                                                           textvariable=self.combt_highlightbackground)
        self.comb_highlightbackground_Chose['values'] = \
            (
                'SystemButtonFace', 'black', 'white', 'blue', 'red', 'green', 'yellow', 'gray', 'DarkBlue', 'DeepSkyBlue'
                , 'LightGreen', 'Pink', 'LightPink', 'DeepPink', 'Purple', 'Violet', 'BLueViolet', 'Beige'
                , 'GreenYellow', 'Ivory', 'LightYellow', 'LightCyan', 'LightBlue', 'LightSkyBlue', 'Aqua'
                , 'Lime', 'LawnGreen', 'ForestGreen', 'Olive', 'Azure', 'SpringGreen', 'PaleGreen'
                , 'SlateGray', 'LightSlateGray', 'CadetBlue', 'DodgerBlue'
            )
        self.comb_highlightbackground_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 300)
        self.comb_highlightbackground_Chose.current(0)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # bitmap

        self.l = Label(self.PanedF_Canvas_Y1, text='bitmap', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 340)  # y 方向每 40一间隔

        self.comb_bitmap_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19,
                                                           textvariable=self.combt_bitmap)
        self.comb_bitmap_Chose['values'] = \
            (
                '', 'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question', 'warning'
            )
        self.comb_bitmap_Chose.place(x=self.JG_X + 53, y=self.JG_Y * 7 + 340)
        self.comb_bitmap_Chose.current(0)

        self.Btn_bitmap = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1,
                                              font=('Consol', '9'),
                                              command=self.More_bitmap)
        self.Btn_bitmap.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 340)

        self.Btn_Ok_bitmap = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_bitmap.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 340)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # image

        self.l = Label(self.PanedF_Canvas_Y1, text='image', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 380)  # y 方向每 40一间隔

        self.Ent_image = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_image, width=22, bg='LightCyan',
                                foreground='Darkblue')
        self.Ent_image.place(x=self.JG_X + 53, y=self.JG_Y * 7 + 380)

        self.Btn_image = Button(self.PanedF_Canvas_Y1, text='...', width=2, height=1,
                                 font=('Consol', '9'),
                                 command=self.More_image)
        self.Btn_image.place(x=self.JG_X + 215, y=self.JG_Y * 7 + 380)

        self.Btn_Ok_image = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_image.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 380)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # padx

        self.l = Label(self.PanedF_Canvas_Y1, text='padx', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 420)  # y 方向每 40一间隔

        self.combt_padx_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_padx)
        self.combt_padx_Chose['values'] = \
            (
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
            )
        self.combt_padx_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 420)
        self.combt_padx_Chose.current(0)

        self.Btn_Ok_padx = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                   , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_padx.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 420)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # pady

        self.l = Label(self.PanedF_Canvas_Y1, text='pady', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 460)  # y 方向每 40一间隔

        self.combt_pady_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_pady)
        self.combt_pady_Chose['values'] = \
            (
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
            )
        self.combt_pady_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 460)
        self.combt_pady_Chose.current(0)

        self.Btn_Ok_pady = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                  , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_pady.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 460)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # takefocus

        self.l = Label(self.PanedF_Canvas_Y1, text='takefocus', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 500)  # y 方向每 40一间隔

        self.combt_takefocus_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_takefocus,
                                                  state='readonly')
        self.combt_takefocus_Chose['values'] = \
            (
                '', 0, 1
            )
        self.combt_takefocus_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 500)
        self.combt_takefocus_Chose.current(0)

        self.Btn_Ok_takefocus = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                  , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_takefocus.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 500)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # cursor

        self.l = Label(self.PanedF_Canvas_Y1, text='cursor', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 540)  # y 方向每 40一间隔

        self.combt_cursor_Chose = ttk.Combobox(self.PanedF_Canvas_Y1, width=19, textvariable=self.combt_cursor)
        self.combt_cursor_Chose['values'] = \
            (
                '', 'arrow', 'based_arrow_up', 'based_arrow_down', 'boat', 'bogosity', 'bottom_left_corner ', 'bottom_right_corner', 'bottom_side',
                'bottom_tee', 'box_spiral', 'center_ptr', 'circle', 'clock', 'coffee_mug', 'cross', 'cross_reverse', 'crosshair',
                'diamond_cross', 'dot', 'dotbox', 'double_arrow', 'draft_large', 'draft_small', 'draped_box', 'exchange',
                'fleur', 'gobbler', 'gumby', 'hand1', 'hand2', 'heart', 'icon', 'iron_cross', 'left_ptr', 'left_side', 'left_tee',
                'leftbutton', 'll_angle', 'lr_angle', 'man', 'middlebutton', 'mouse', 'pencil', 'pirate', 'plus', 'question_arrow',
                'right_ptr', 'right_side', 'right_tee', 'rightbutton', 'rtl_logo', 'sailboat', 'sb_down_arrow',
                'sb_h_double_arrow', 'sb_left_arrow', 'sb_right_arrow', 'sb_up_arrow', 'sb_v_double_arrow', 'shuttle',
                'sizing', 'spider', 'spraycan', 'star', 'target', 'tcross', 'top_left_arrow', 'top_left_corner', 'top_right_corner',
                'top_side', 'top_tee', 'trek', 'ul_angle', 'umbrella', 'ur_angle', 'watch', 'xterm', 'X_cursor'
            )
        self.combt_cursor_Chose.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 540)
        self.combt_cursor_Chose.current(0)

        self.Btn_Ok_cursor = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                       , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_cursor.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 540)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # container

        self.l = Label(self.PanedF_Canvas_Y1, text='container', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 7 + 580)  # y 方向每 40一间隔

        self.Ent_container = Entry(self.PanedF_Canvas_Y1, textvariable=self.ent_container, width=22, bg='LightCyan',
                                foreground='Darkblue')
        self.Ent_container.place(x=self.JG_X + 80, y=self.JG_Y * 7 + 580)

        self.Btn_Ok_container = Button(self.PanedF_Canvas_Y1, text='=>', width=2, height=1, font=('Consol', '9')
                                    , command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_container.place(x=self.JG_X + 241, y=self.JG_Y * 7 + 580)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 下事件框事件设置

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # command

        self.l = Label(self.PanedF_Canvas_Y2, text='command', bg='white')
        self.l.place(x=self.JG_X, y=self.JG_Y * 0 + 6)  # y 方向每 40一间隔

        self.Ent_command = Entry(self.PanedF_Canvas_Y2, textvariable=self.ent_command, width=22, bg='LightCyan',
                                   foreground='Darkblue')
        self.Ent_command.place(x=self.JG_X + 80, y=6)

        self.Btn_Ok_command = Button(self.PanedF_Canvas_Y2, text='=>', width=2, height=1, font=('Consol', '9'),
                                     command=self.UI_Ban_Btn_OK)
        self.Btn_Ok_command.place(x=246, y=6)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_press_1
        self.ent_button_press_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Click left mouse button once', bg='white')
        self.l.place(x=self.JG_X, y=6 + 40)  # y 方向每 40一间隔

        self.Btn_button_press_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1, font=('Consol', '10'),
                                         command=self.SJ_button_press_1)
        self.Btn_button_press_1.place(x=220, y=6 + 40)


        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_release_1
        self.ent_button_release_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Release left mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 80)  # y 方向每 40一间隔

        self.Btn_button_release_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1, font=('Consol', '10'),
                                         command=self.SJ_button_release_1)
        self.Btn_button_release_1.place(x=220, y=6 + 80)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_press_right_1
        self.ent_button_press_right_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Click right mouse button once', bg='white')
        self.l.place(x=self.JG_X, y=6 + 120)  # y 方向每 40一间隔

        self.Btn_button_press_right_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1, font=('Consol', '10'),
                                         command=self.SJ_button_press_right_1)
        self.Btn_button_press_right_1.place(x=220, y=6 + 120)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_press_left_2
        self.ent_button_press_left_2 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click left mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 160)  # y 方向每 40一间隔

        self.Btn_button_press_left_2 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                               font=('Consol', '10'),
                                               command=self.SJ_button_press_left_2)
        self.Btn_button_press_left_2.place(x=220, y=6 + 160)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_press_right_2
        self.ent_button_press_right_2 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click right mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 160)  # y 方向每 40一间隔

        self.Btn_button_press_right_2 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                              font=('Consol', '10'),
                                              command=self.SJ_button_press_right_2)
        self.Btn_button_press_right_2.place(x=220, y=6 + 160)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_press_middle_1
        self.ent_button_press_middle_1 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Click middle mouse button once', bg='white')
        self.l.place(x=self.JG_X, y=6 + 200)  # y 方向每 40一间隔

        self.Btn_button_press_middle_1 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                               font=('Consol', '10'),
                                               command=self.SJ_button_press_middle_1)
        self.Btn_button_press_middle_1.place(x=220, y=6 + 200)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_press_middle_2
        self.ent_button_press_middle_2 = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click right mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 240)  # y 方向每 40一间隔

        self.Btn_button_press_middle_2 = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                                font=('Consol', '10'),
                                                command=self.SJ_button_press_middle_2)
        self.Btn_button_press_middle_2.place(x=220, y=6 + 240)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # button_press_left_move
        self.ent_button_press_left_move = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Double click right mouse button', bg='white')
        self.l.place(x=self.JG_X, y=6 + 240)  # y 方向每 40一间隔

        self.Btn_button_press_left_move = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                                font=('Consol', '10'),
                                                command=self.SJ_button_press_left_move)
        self.Btn_button_press_left_move.place(x=220, y=6 + 240)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # cursor_enter
        self.combt_cursor_enter = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Cursor enter the control area', bg='white')
        self.l.place(x=self.JG_X, y=6 + 280)  # y 方向每 40一间隔

        self.Btn_cursor_enter = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                                 font=('Consol', '10'),
                                                 command=self.SJ_cursor_enter)
        self.Btn_cursor_enter.place(x=220, y=6 + 280)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # cursor_leave
        self.combt_cursor_leave = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Cursor the leave control area', bg='white')
        self.l.place(x=self.JG_X, y=6 + 320)  # y 方向每 40一间隔

        self.Btn_cursor_leave = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                       font=('Consol', '10'),
                                       command=self.SJ_cursor_leave)
        self.Btn_cursor_leave.place(x=220, y=6 + 320)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # get_key_focus
        self.ent_get_key_focus = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Get the focus of the keyboard', bg='white')
        self.l.place(x=self.JG_X, y=6 + 360)  # y 方向每 40一间隔

        self.Btn_get_key_focus = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                       font=('Consol', '10'),
                                       command=self.SJ_get_key_focus)
        self.Btn_get_key_focus.place(x=220, y=6 + 360)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # press_a_key
        self.ent_press_a_key = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Press a key of the keyboard', bg='white')
        self.l.place(x=self.JG_X, y=6 + 400)  # y 方向每 40一间隔

        self.Btn_press_a_key = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                        font=('Consol', '10'),
                                        command=self.SJ_press_a_key)
        self.Btn_press_a_key.place(x=220, y=6 + 400)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # press_enter_key
        self.ent_press_enter_key = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Press the enter key', bg='white')
        self.l.place(x=self.JG_X, y=6 + 440)  # y 方向每 40一间隔

        self.Btn_press_enter_key = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                      font=('Consol', '10'),
                                      command=self.SJ_press_enter_key)
        self.Btn_press_enter_key.place(x=220, y=6 + 440)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # when_control_change
        self.ent_when_control_change = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='When the control change', bg='white')
        self.l.place(x=self.JG_X, y=6 + 480)  # y 方向每 40一间隔

        self.Btn_when_control_change = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                          font=('Consol', '10'),
                                          command=self.SJ_when_control_change)
        self.Btn_when_control_change.place(x=220, y=6 + 480)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # control_mouseWheel
        self.ent_control_mouseWheel = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text='Press control and mouse_wheel', bg='white')
        self.l.place(x=self.JG_X, y=6 + 520)  # y 方向每 40一间隔

        self.control_mouseWheel = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                              font=('Consol', '10'),
                                              command=self.SJ_control_mouseWheel)
        self.control_mouseWheel.place(x=220, y=6 + 520)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # shift_mouseWheel
        self.ent_shift_mouseWheel = StringVar()

        self.l = Label(self.PanedF_Canvas_Y2, text="Press shift and mouse_wheel", bg='white')
        self.l.place(x=self.JG_X, y=6 + 560)  # y 方向每 40一间隔

        self.Btn_shift_mouseWheel = Button(self.PanedF_Canvas_Y2, text='Add...', width=6, height=1,
                                          font=('Consol', '10'),
                                          command=self.SJ_shift_mouseWheel)
        self.Btn_shift_mouseWheel.place(x=220, y=6 + 560)


        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # canva 事件绑定
        self.canva.bind("<ButtonPress-1>", self.HuoQu_Canvas_ZuoBiao)  # 绑定获取 Canvas 坐标事件
        self.canva.bind("<ButtonPress-3>", self.Button3_Press)  # 绑定获取 Canvas 坐标事件

        self.Text_BianYi.bind("<Control-MouseWheel>", self.Text_Wheel)  # 绑定获取 Text_BianYi 滚轮事件
        # 组合键之间用 - 连接，只能同时使用

        self.Scal_Y1.bind("<MouseWheel>", self.Y1_win_Wheel)
        self.Scal_Y2.bind("<MouseWheel>", self.Y2_win_Wheel)

        # 窗口位置改变事件
        self.bind("<Configure>", self.Win_Change)  # 绑定事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 编译
    def BianYi(self):
        global Str_BianYi

        # 编译文本先清空
        self.Text_BianYi.delete(1.0, END)

        self.Text_BianYi.insert(END, Str_BianYi)
        hua = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        hua.Hua_BianYi()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 设置 设计UI窗口参数
    def Set_KouZhuan(self):
        global canva_W
        global canva_H
        ck = SetCK_D(self)


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def UI_Ban(self, value):
        pass
        global XuanZhong
        Len = len(XuanZhong)
        self.UI_2_QuanJu()
        if Len != 0:
            self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
            self.a.UI_Ban_Design()
            print('UI_Ban')

    def UI_Ban_Btn_OK(self):
        pass
        global XuanZhong
        Len = len(XuanZhong)
        self.UI_2_QuanJu()
        if Len != 0:
            self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
            self.a.UI_Ban_Design()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 窗口位置改变
    def Win_Change(self, event):
        global win_X
        global win_Y
        win_X = self.winfo_x()
        win_Y = self.winfo_y()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 全局 to UI
    def QuanJu_2_UI(self):
        # 使用全局变量更新
        global lab_ControlType
        global ent_ControlName
        global ent_X0
        global ent_Y0
        global ent_width
        global ent_height
        global ent_length
        global ent_fontSize
        global combt_fontType
        global combt_foreground
        global combt_background
        global combt_anchor
        global combt_justify
        global ent_text
        global combt_state
        global combt_relief
        global combt_highlightcolor
        global combt_highlightbackground
        global combt_bitmap
        global ent_image
        global combt_padx
        global combt_pady
        global combt_takefocus
        global combt_cursor
        global ent_container
        global ent_command

        # 上属性框部件设置
        self.lab_ControlType.set(lab_ControlType)
        self.ent_ControlName.set(ent_ControlName)
        self.ent_X0.set(ent_X0)
        self.ent_Y0.set(ent_Y0)
        self.ent_width.set(ent_width)
        self.combt_background.set(combt_background)
        self.ent_container.set(ent_container)

        if ent_height != "":
            self.ent_height.set(ent_height)
        else:
            self.ent_height.set(0)

        if ent_length != "":
            self.ent_length.set(ent_length)
        else:
            self.ent_length.set(0)

        if ent_fontSize != "":
            self.ent_fontSize.set(ent_fontSize)
        else:
            self.ent_fontSize.set(0)

        if combt_fontType != "":
            self.combt_fontType.set(combt_fontType)
        else:
            self.combt_fontType.set("")

        if combt_foreground != "":
            self.combt_foreground.set(combt_foreground)
        else:
            self.combt_foreground.set(0)

        if combt_anchor != "":
            self.combt_anchor.set(combt_anchor)
        else:
            self.combt_anchor.set("")

        if combt_justify != "":
            self.combt_justify.set(combt_justify)
        else:
            self.combt_justify.set("")

        if ent_text != "":
            self.ent_text.set(ent_text)
        else:
            self.ent_text.set("")

        if combt_state != "":
            self.combt_state.set(combt_state)
        else:
            self.combt_state.set("")

        if combt_relief != "":
            self.combt_relief.set(combt_relief)
        else:
            self.combt_relief.set("")

        if combt_highlightcolor != "":
            self.combt_highlightcolor.set(combt_highlightcolor)
        else:
            self.combt_highlightcolor.set("")

        if combt_highlightbackground != "":
            self.combt_highlightbackground.set(combt_highlightbackground)
        else:
            self.combt_highlightbackground.set("")

        if combt_bitmap != "":
            self.combt_bitmap.set(combt_bitmap)
        else:
            self.combt_bitmap.set("")

        if ent_image != "":
            self.ent_image.set(ent_image)
        else:
            self.ent_image.set("")

        if combt_padx != "":
            self.combt_padx.set(combt_padx)
        else:
            self.combt_padx.set(0)

        if combt_pady != "":
            self.combt_pady.set(combt_pady)
        else:
            self.combt_pady.set(0)

        if combt_takefocus != "":
            self.combt_takefocus.set(combt_takefocus)
        else:
            self.combt_takefocus.set("")

        if combt_cursor != "":
            self.combt_cursor.set(combt_cursor)
        else:
            self.combt_cursor.set("")

        if ent_command != "":
            self.ent_command.set(ent_command)
        else:
            self.ent_command.set("")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 全局 to UI
    def UI_2_QuanJu(self):
        # 使用全局变量更新
        global lab_ControlType
        global ent_ControlName
        global ent_X0
        global ent_Y0
        global ent_width
        global ent_height
        global ent_length
        global ent_fontSize
        global combt_fontType
        global combt_foreground
        global combt_background
        global combt_anchor
        global combt_justify
        global ent_text
        global combt_state
        global combt_relief
        global combt_highlightcolor
        global combt_highlightbackground
        global combt_bitmap
        global ent_image
        global combt_padx
        global combt_pady
        global combt_takefocus
        global combt_cursor
        global ent_container
        global ent_command

        # 上属性框部件设置
        lab_ControlType = self.lab_ControlType.get()
        ent_ControlName = self.ent_ControlName.get()
        ent_X0 = self.ent_X0.get()
        ent_Y0 = self.ent_Y0.get()
        ent_width = self.ent_width.get()
        ent_height = self.ent_height.get()
        ent_length = self.ent_length.get()
        ent_fontSize = self.ent_fontSize.get()
        combt_fontType = self.combt_fontType.get()
        combt_foreground = self.combt_foreground.get()
        combt_background = self.combt_background.get()
        combt_anchor = self.combt_anchor.get()
        combt_justify = self.combt_justify.get()
        ent_text = self.ent_text.get()
        combt_state = self.combt_state.get()
        combt_relief = self.combt_relief.get()
        combt_highlightcolor = self.combt_highlightcolor.get()
        combt_highlightbackground = self.combt_highlightbackground.get()
        combt_bitmap = self.combt_bitmap.get()
        ent_image = self.ent_image.get()
        combt_padx = self.combt_padx.get()
        combt_pady = self.combt_pady.get()
        combt_takefocus = self.combt_takefocus.get()
        combt_cursor = self.combt_cursor.get()
        ent_container = self.ent_container.get()
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        ent_command = self.ent_command.get()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def BianJi_OK(self):
        global each_YouJian
        each_YouJian = 'OK'
        print(each_YouJian)
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.OK()


    def BianJi_Move(self):
        global each_YouJian
        each_YouJian = 'Move'
        print(each_YouJian)
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.Move()


    def BianJi_Delete(self):
        global each_YouJian
        each_YouJian = 'Delete'
        print(each_YouJian)
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.Delete()


    def BianJi_Design(self):
        global each_YouJian
        self.BianYi_Text_Design()
        each_YouJian = 'Design'
        self.QuanJu_2_UI()


    def BianJi_Cancel(self):
        global each_YouJian
        each_YouJian = 'Cancel'
        self.a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        self.a.Cancel()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 属性框处理函数
    # 滚动处理
    def Y1_win_Wheel(self, event):
        i = self.Scal_Y1.get()
        if event.delta > 0:  # 滚轮上滚
            i = i - 10
            print('i= ', i)
            self.Scal_Y1.set(i)
        else:  # 滚轮下滚
            i = i + 10
            print('i= ', i)
            self.Scal_Y1.set(i)

    def Y2_win_Wheel(self, event):
        i = self.Scal_Y2.get()
        if event.delta > 0:  # 滚轮上滚
            i = i - 5
            self.Scal_Y2.set(i)
        else:  # 滚轮下滚
            i = i + 5
            self.Scal_Y2.set(i)

    # 添加前景色
    def More_foreground(self):
        global combt_foreground
        a = Choose_Color()
        b = a.Color_Choose()
        combt_foreground = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加背景色
    def More_background(self):
        global combt_background
        a = Choose_Color()
        b = a.Color_Choose()
        combt_background = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加 highlightcolor
    def More_highlightcolor(self):
        global combt_highlightcolor
        a = Choose_Color()
        b = a.Color_Choose()
        combt_highlightcolor = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加 highlightbackground
    def More_highlightbackground(self):
        global combt_highlightbackground
        a = Choose_Color()
        b = a.Color_Choose()
        combt_highlightbackground = b[1]
        self.QuanJu_2_UI()
        self.UI_Ban_Btn_OK()

    # 添加 bitmap
    def More_bitmap(self):
        global combt_bitmap
        a = Get_File_Name_XBM()
        b = a.Get_Name()
        combt_bitmap = b
        self.QuanJu_2_UI()

    # 添加 image
    def More_image(self):
        global ent_image
        a = Get_File_Name_GIF()
        b = a.Get_Name()
        ent_image = b
        self.QuanJu_2_UI()

    # 打开事件 button_press_1
    def SJ_button_press_1(self):
        # def SJ_Dict(self, str_SJ):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_1")

    # 打开事件 button_release_1
    def SJ_button_release_1(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_release_1")

    # 打开事件 button_press_right_1
    def SJ_button_press_right_1(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_right_1")

    def SJ_button_press_left_2(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_left_2")

    def SJ_button_press_right_2(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_right_2")

    def SJ_button_press_middle_1(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_middle_1")

    def SJ_button_press_middle_2(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_middle_2")

    def SJ_button_press_left_move(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("button_press_left_move")

    def SJ_cursor_enter(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("cursor_enter")

    def SJ_cursor_leave(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("cursor_leave")

    def SJ_get_key_focus(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("get_key_focus")

    def SJ_lose_key_focus(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("lose_key_focus")

    def SJ_press_a_key(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("press_a_key")

    def SJ_press_enter_key(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("press_enter_key")

    def SJ_when_control_change(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("when_control_change")

    def SJ_control_mouseWheel(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("control_mouseWheel")

    def SJ_shift_mouseWheel(self):
        sj_dict = SJ_Dictionary()
        sj_dict.SJ_Dict("shift_mouseWheel")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 属性框展开函数
    def V_P_Scal_Y1(self, value):
        self.PanedF_Canvas_Y1.place(x=48, y=0-int(value)*10)


    def V_P_Scal_Y2(self, value):
        self.PanedF_Canvas_Y2.place(x=48, y=0-int(value)*10)


    def ShuXing_Zhan(self):
        global flag_ShuXing_Tan
        if flag_ShuXing_Tan == FALSE:
            self.Btn_ShuXing_Text.set('=>')
            self.PanedWin_X1.place(x=1196, y=50)
            self.PanedWin_X1.paneconfig(self.Text_BianYi, after=self.PanedWin_Y1)
            flag_ShuXing_Tan = TRUE
            self.Btn_Update.place(x=1420, y=26)
        else:
            self.Btn_ShuXing_Text.set('<=')
            self.PanedWin_X1.place(x=2000, y=50)
            self.PanedWin_X1.paneconfig(self.Text_BianYi, before=self.PanedWin_Y1)
            flag_ShuXing_Tan = FALSE
            self.Btn_Update.place(x=2000, y=26)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 编译文本框展开函数
    def BianYi_Text(self):
        global flag_BianYi_Text
        if flag_BianYi_Text == FALSE:
            self.Tv_BianYi_Text.set('Hide')
            self.PanedWin_X1.place(x=60, y=50)
            self.PanedWin_X1.paneconfig(self.Text_BianYi, before=self.PanedWin_Y1)
            flag_BianYi_Text = TRUE
            self.Btn_Update.place(x=1420, y=26)

        elif flag_BianYi_Text == TRUE:
            self.Tv_BianYi_Text.set('Text')
            self.PanedWin_X1.place(x=2000, y=50)
            flag_BianYi_Text = FALSE
            self.Btn_Update.place(x=2000, y=26)

    def BianYi_Text_Design(self):
        global flag_BianYi_Text
        self.Tv_BianYi_Text.set('Hide')
        self.PanedWin_X1.place(x=60, y=50)
        self.PanedWin_X1.paneconfig(self.Text_BianYi, before=self.PanedWin_Y1)
        self.Btn_Update.place(x=1420, y=26)
        flag_BianYi_Text = TRUE

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Canvas 隐藏函数
    def Canva_Hide(self):
        global flag_Canva_Hide
        global canva_X
        global canva_Y
        if flag_Canva_Hide == FALSE:
            self.Tv_Canva_Hide.set('Hide')
            self.canva.place(x=canva_X, y=canva_Y)
            flag_Canva_Hide = TRUE

        elif flag_Canva_Hide == TRUE:
            self.Tv_Canva_Hide.set('Paint')
            self.canva.place(x=2000, y=50)
            flag_Canva_Hide = FALSE

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Text 背景颜色设定函数

    def BianYi_Color_White(self):
        self.Text_BianYi.config(fg='black', bg='white', insertbackground='black')

    def BianYi_Color_Black(self):
        self.Text_BianYi.config(fg='white', bg='black', insertbackground='white')

    def BianYi_Color_Green(self):
        self.Text_BianYi.config(fg='white', bg='green', insertbackground='white')

    def BianYi_Color_YangPiZhi(self):
        self.Text_BianYi.config(fg='black', bg='LemonChiffon', insertbackground='black')


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Text 字体大小调节函数
    def Text_font(self, value):
        Font=('Consolas',str(value))
        self.Text_BianYi.config(font=Font)

    # Text_BianYi 滚轮事件
    def Text_Wheel(self, event):
        i = self.Sca_Text_front.get()
        if event.delta > 0:  # 滚轮上滚
            i = i + 1
            self.Sca_Text_front.set(i)
        else:  # 滚轮下滚
            i = i - 1
            self.Sca_Text_front.set(i)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 右键菜单
    def Button3_Press(self, event):
        self.New_kj_menu.post(event.x_root, event.y_root)  # 必须为 (event.x_root, event.y_root) 才精准出现在点击点

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def HuoQu_Canvas_ZuoBiao(self, event):
        global Event_Canvas_x
        global Event_Canvas_y
        Event_GunLun_x = event.x
        Event_GunLun_y = event.y
        print('Event_GunLun_x = ', Event_GunLun_x)
        print('Event_GunLun_y = ', Event_GunLun_y)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 定义画布放伸缩函数
    def HuaBuFangDa_Y(self, value):
        global canva_W
        global canva_H
        global scal_Y_Zhi

        scal_Y_Zhi = value

        self.ZhuChuangKou_BianYan_ShanChu()

        canva_H = self.fram_H + int(value)
        self.canva.config(width=canva_W, height=canva_H)

        self.ent_y.set(canva_H)
        self.ZhuChuangKou_BianYan()
        if self.flag_WangGe == TRUE:
            self.WG_Kai()

    def HuaBuFangDa_X(self, value):
        global canva_W
        global canva_H
        global scal_X_Zhi

        scal_X_Zhi = value

        self.ZhuChuangKou_BianYan_ShanChu()

        canva_W = self.fram_W + int(value)

        self.canva.config(width=canva_W, height=canva_H)

        self.ent_x.set(canva_W)
        self.ZhuChuangKou_BianYan()
        if self.flag_WangGe == TRUE:
            self.WG_Kai()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 转到窗口
    def ChuangKouZhuan(self):
        global canva_W
        global canva_H

        self.ZhuChuangKou_BianYan_ShanChu()

        self.ScZhi_X = int(self.ent_y.get()) - self.Yuan_canva_H  # ScZhi_X 为 X方向的范围条的值
        self.ScZhi_Y = int(self.ent_x.get()) - self.Yuan_canva_W  # ScZhi_Y 为 Y方向的范围条的值

        self.vy.set(self.ScZhi_X)  # vy is the value of Sca_Y
        self.vx.set(self.ScZhi_Y)  # vx is the value of Sca_X

        canva_H = int(self.ent_y.get())
        canva_W = int(self.ent_x.get())

        self.canva.config(width=canva_W, height=canva_H)


        self.ZhuChuangKou_BianYan()
        if self.flag_WangGe == TRUE:
            self.WG_Kai()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 复位窗口
    def FuWeiKouZhuan(self):
        # 定义画布复位
        global canva_X
        global canva_Y
        canva_X = 60
        canva_Y = 50
        self.ZhuChuangKou_BianYan_ShanChu()
        self.canva.place(x=canva_X, y=canva_Y)  # 此句用于复位
        self.ZhuChuangKou_BianYan()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 隐藏窗口
    def YinCang(self):
        if self.flag_BuJian_YinCang == FALSE:
            self.flag_BuJian_YinCang= TRUE
            self.Btn_YinCang_Text.set('Show')
            D = -600
            self.Lab1.place(x=D, y=0)
            self.Lab2.place(x=D, y=0)
            self.Lab_CK_X_len.place(x=D, y=0)
            self.Lab_CK_Y_len.place(x=D, y=26)
            self.Lab_font_size.place(x=D, y=760)

            self.Btn_CK_ZhuanDao.place(x=D, y=0)
            self.Btn_CK_FuWei.place(x=D, y=0)
            self.GuDing.place(x=D, y=0)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.Btn_WangGe.place(x=D, y=746)
            self.Btn_BianYi.place(x=D, y=600)
            self.Btn_BianYi_FuZhi.place(x=D, y=650)
            self.Btn_BianYi_ShengCheng.place(x=D, y=700)
            self.Btn_BianYi_Text.place(x=D, y=746)
            self.Btn_Canva_Hide.place(x=D, y=746)
            self.Btn_BianYi_Color_White.place(x=D, y=746)
            self.Btn_BianYi_Color_Black.place(x=D, y=746)
            self.Btn_BianYi_Color_YangPiZhi.place(x=D, y=746)
            self.Btn_BianYi_Color_Green.place(x=D, y=746)
            self.Btn_CK_Set.place(x=D, y=26)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            self.Ent_X.place(x=D, y=0)
            self.Ent_Y.place(x=D, y=26)

            self.Sca_Y.place(x=D, y=40)
            self.Sca_X.place(x=D, y=0)
            self.Sca_Text_front.place(x=D, y=739)

        else:
            self.flag_BuJian_YinCang = FALSE
            self.Btn_YinCang_Text.set('Hide')
            self.Lab1.place(x=0, y=0)
            self.Lab2.place(x=60, y=0)
            self.Lab_CK_X_len.place(x=620, y=0)
            self.Lab_CK_Y_len.place(x=620, y=26)
            self.Lab_font_size.place(x=1250, y=760)

            self.Btn_CK_ZhuanDao.place(x=762, y=0)
            self.Btn_CK_FuWei.place(x=762, y=26)
            self.GuDing.place(x=0, y=746)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.Btn_WangGe.place(x=420, y=746)
            self.Btn_BianYi.place(x=6, y=600)
            self.Btn_BianYi_FuZhi.place(x=6, y=650)
            self.Btn_BianYi_ShengCheng.place(x=6, y=700)
            self.Btn_BianYi_Text.place(x=60, y=746)
            self.Btn_Canva_Hide.place(x=120, y=746)
            self.Btn_BianYi_Color_White.place(x=180, y=746)
            self.Btn_BianYi_Color_Black.place(x=240, y=746)
            self.Btn_BianYi_Color_YangPiZhi.place(x=300, y=746)
            self.Btn_BianYi_Color_Green.place(x=360, y=746)
            self.Btn_CK_Set.place(x=826, y=26)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$

            self.Ent_X.place(x=710, y=0)
            self.Ent_Y.place(x=710, y=26)

            self.Sca_Y.place(x=0, y=40)
            self.Sca_X.place(x=100, y=0)
            self.Sca_Text_front.place(x=1328, y=739)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 固定窗口
    def GuDingChuangKou(self):
        global flag_CK_GuDing
        if flag_CK_GuDing == FALSE:
            flag_CK_GuDing = TRUE
            self.GuDing_Text.set('Unluck')
        else:
            flag_CK_GuDing = FALSE
            self.GuDing_Text.set('Luck')

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 网格开
    def WG_Kai(self):
        # 参数设定
        global WangGe_ShuMu_X
        global WangGe_ShuMu_Y
        global WangGe_KuanDu
        global canva_H
        global canva_W

        WangGe_ShuMu_X = (canva_H - self.bar_W) / WangGe_KuanDu
        WangGe_ShuMu_Y = canva_W / WangGe_KuanDu

        # 下面画网格
        for i in range(0, int(WangGe_ShuMu_X), 1):
            self.it_WangGe = self.canva.create_line(0, self.bar_W + WangGe_KuanDu * i, canva_W,
                                               self.bar_W + WangGe_KuanDu * i,
                                               fill=self.WangGe_YanSe, width=0.1)
            self.canva.itemconfig(self.it_WangGe, tags='WG')
            self.canva.lower(self.it_WangGe)

        for i in range(0, int(WangGe_ShuMu_Y), 1):
            self.it_WangGe = self.canva.create_line(WangGe_KuanDu + WangGe_KuanDu * i, self.bar_W,
                                               WangGe_KuanDu + WangGe_KuanDu * i, canva_H,
                                               fill=self.WangGe_YanSe, width=0.1)
            self.canva.itemconfig(self.it_WangGe, tags='WG')
            self.canva.lower(self.it_WangGe)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 网格关
    def WG_Gun(self):
        self.canva.delete('WG')  # 删除所有具有标签'WG'的项目

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 启用网格
    def QiYong_WangGe(self):
        if self.flag_WangGe == FALSE:
            self.flag_WangGe = TRUE
            self.Btn_WG_Text.set('G_Off')
            self.WG_Kai()

        else:
            self.flag_WangGe = FALSE
            self.Btn_WG_Text.set('G_On')
            self.WG_Gun()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 画主窗口边沿
    def ZhuChuangKou_BianYan(self):
        global canva_W
        global canva_H
        global flag_Menu_Kai

        # 画外边框
        self.it1 = self.canva.create_rectangle(2, canva_H - 1, canva_W - 1, 2)
        # 画标题栏框
        self.it2 = self.canva.create_rectangle(2, self.bar_W, canva_W - 1, self.bar_W,
                                               fil=self.ChuangKou_BiaoTiLan_YanSe)
        # 画标题
        self.it_BiaoTi = self.canva.create_text(43, 16, text=self.BiaoTi_Text,
                                                font=('Consol', 11),
                                                fill=self.BiaoTi_Text_YanSe)

        # 画标题栏按钮
        self.it_BiaoTi_AnNiu_ZuiXiao = self.canva.create_text(canva_W - 116, 16, text='—',
                                                              font=('Consol', 11),
                                                              fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_ZuiDa = self.canva.create_text(canva_W - 70, 16, text='□',
                                                            font=('Consol', 11),
                                                            fill=self.BiaoTi_Text_YanSe)
        self.it_BiaoTi_AnNiu_GuanBi = self.canva.create_text(canva_W - 28, 16, text='X',
                                                             font=('Helvetica', 11),
                                                             fill=self.BiaoTi_Text_YanSe)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 删除主窗口边沿
    def ZhuChuangKou_BianYan_ShanChu(self):
        if flag_Menu_Kai == TRUE:
            self.canva.delete(self.it_Menu)

        self.canva.delete(self.it1)
        self.canva.delete(self.it2)
        self.canva.delete(self.it_BiaoTi)
        self.canva.delete(self.it_BiaoTi_AnNiu_ZuiXiao)
        self.canva.delete(self.it_BiaoTi_AnNiu_ZuiDa)
        self.canva.delete(self.it_BiaoTi_AnNiu_GuanBi)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 画布移动
    def HuaBu_YiDong(self):
        # 鼠标中键按下事件
        def paint1(event):
            self.x1 = event.x
            self.y1 = event.y
            self.flag_SongKai = FALSE
            self.canva.config(cursor='fleur')

        # 鼠标中键松开事件
        def paint2(event):
            self.flag_SongKai = TRUE
            self.canva.config(cursor='arrow')

        # 鼠标中键按下并移动事件
        def paint3(event):
            self.x2 = event.x
            self.y2 = event.y
            if self.flag_SongKai == FALSE:
                if flag_CK_GuDing == FALSE:
                    global canva_X
                    global canva_Y

                    self.canva.place(x=canva_X + (self.x2 - self.x1), y=canva_Y + (self.y2 - self.y1))
                    # 重新定义画布位置
                    canva_X = canva_X + (self.x2 - self.x1)
                    canva_Y = canva_Y + (self.y2 - self.y1)


        # 画布控件与鼠标左键进行绑定
        self.canva.bind("<ButtonPress-2>", paint1)  # 绑定鼠标按下事件
        self.canva.bind("<ButtonRelease - 2>", paint2)  # 绑定鼠标松开事件
        self.canva.bind("<B2-Motion>", paint3)  # 绑定鼠标移动事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 主菜单功能函数定义
    def Hua_Button(self):
        global button1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Button ' + str( button1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('button1')
        a.Hua_Button()

    def Hua_Canvas(self):
        global canvas1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Canvas ' + str(canvas1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('canvas1')
        a.Hua_Canvas()


    def Hua_Checkbutton(self):
        global checkbutton1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Checkbutton ' + str(checkbutton1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('checkbutton1')
        a.Hua_Checkbutton()


    def Hua_Combobox(self):
        global combobox1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Combobox ' + str(combobox1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('combobox1')
        a.Hua_Combobox()


    def Hua_Entry(self):
        global entry1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Entry ' + str(entry1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('entry1')
        a.Hua_Entry()


    def Hua_Frame(self):
        global frame1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Frame ' + str(frame1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('frame1')
        a.Hua_Frame()


    def Hua_Label(self):
        global label1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Label ' + str(label1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('label1')
        a.Hua_Label()


    def Hua_LabelFrame(self):
        global labelFrame1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'LabelFrame ' + str(labelFrame1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('labelFrame1')
        a.Hua_LabelFrame()


    def Hua_Listbox(self):
        global listbox1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Listbox ' + str(listbox1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('listbox1')
        a.Hua_Listbox()


    def Hua_Menu(self):
        global menu1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Menu ' + str(menu1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('menu1')
        a.Hua_Menu()


    def Hua_Message(self):
        global message1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Message ' + str(message1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('message1')
        a.Hua_Message()


    def Hua_PanedWindow(self):
        global panedWindow1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'PanedWindow ' + str(frame1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('panedWindow1')
        a.Hua_PanedWindow()


    def Hua_Radiobutton(self):
        global radiobutton1_i
        global Radiobutton_i
        global flag_RadBtn_Zu
        global DangQian_KJ_name

        flag_RadBtn_Zu = FALSE

        Radiobutton_i = 0
        DangQian_KJ_name = 'Radiobutton ' + str(radiobutton1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('radiobutton1')
        a.Hua_Radiobutton()


    def Hua_Scale_X(self):
        global scale1_x_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Scale_X ' + str(scale1_x_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('scale1_x')
        a.Hua_Scale_X()


    def Hua_Scale_Y(self):
        global scale1_y_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Scale_Y ' + str(scale1_y_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('scale1_y')
        a.Hua_Scale_Y()


    def Hua_Spinbox(self):
        global spinbox1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Spinbox ' + str(spinbox1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('spinbox1')
        a.Hua_Spinbox()


    def Hua_Text(self):
        global text1_i
        global DangQian_KJ_name
        DangQian_KJ_name = 'Text ' + str(text1_i + 1)

        a = Hua(self.canva, self.BianJi_kj_menu, self.Text_BianYi)
        a.Set_KJBZ('text1')
        a.Hua_Text()


    def Hua_Toplevel(self):
        pass

    def Hua_tkMessageBox(self):
        pass


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 画基本图形类
class Hua:
    def __init__(self, Canva_1, Menu_1, Text_1):
        self.Text_1 = Text_1
        self.BianJi_kj_menu = Menu_1
        self.canva = Canva_1
        self.front_BiLi = 20
        self.Text_YanSe = 'black'
        self.fill_YanSe = 'white'
        self.OutLine_YanSe = 'Aqua'
        self.Kuan_width = 2
        self.flag_WanCheng1 = FALSE
        self.flag_FuZuKuang = FALSE

        self.bg_Canvas_YanSe = 'LightCyan'
        self.bg_Entry_YanSe = 'Aqua'
        self.bg_Spinbox_YanSe = 'Aqua'
        self.bg_Listbox_YanSe = 'AquaMarine'

        self.bg_Canvas_YanSe = 'LightCyan'
        self.bg_Text_YanSe = 'LightCyan'

        self.list_name = StringVar()

        global bar_W
        self.bar_W = bar_W
        self.Zi_Menu_Shu = 0

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Hua_Button(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Button = Button(self.canva, text=DangQian_KJ_name, font=('TkDefaultFont', 10), width=7, height=1)
                self.it_Button.place(x=self.X0, y=self.Y0)
                # self.it_Button.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Button.config(width=W, height=H)

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 50
                    self.Y1 = self.Y0 + 20
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Canvas(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Canva = Canvas(self.canva, bg=self.bg_Canvas_YanSe, width=100, height=80)
                self.it_Canva.place(x=self.X0, y=self.Y0)

                self.it_Canva_name_Text = self.it_Canva.create_text(30, 10, text=DangQian_KJ_name, fill='DeepSkyBlue')

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                global DangQian_KJ_name
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Canva.config(width=W, height=H)

                self.it_Canva_name_Text = self.it_Canva.create_text(30, 10, text=DangQian_KJ_name, fill='DeepSkyBlue')

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 80

                self.it_Canva.delete(self.it_Canva_name_Text)
                self.it_Canva_name_Text = self.it_Canva.create_text(30, 10, text=DangQian_KJ_name, fill='DeepSkyBlue')
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Checkbutton(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Checkbutton = Checkbutton(self.canva, text=DangQian_KJ_name, font=('TkDefaultFont', 10),
                                                  width=12, height=1)

                self.it_Checkbutton.place(x=self.X0, y=self.Y0)

                self.it_Checkbutton.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.3)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Checkbutton.config(width=W, height=H)
                # self.it_Checkbutton.place(x=self.X1, y=self.Y1)

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 20
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Combobox(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                list_name = StringVar()
                self.it_Combobox = ttk.Combobox(self.canva, text=list_name, font=('TkDefaultFont', 10),  width=12, height=2)
                self.it_Combobox["values"] = ('Combobox', 1)
                self.it_Combobox.current(0)
                self.it_Combobox.place(x=self.X0, y=self.Y0)
                self.it_Combobox.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.6)
                H = int(abs(self.Y1 - self.Y0)/15.26)

                self.it_Combobox.config(width=W, height=H)
                self.it_Combobox.place(x=self.X0, y=self.Y0)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 90
                    self.Y1 = self.Y0 + 5

                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Entry(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                entry_Text = StringVar()
                entry_Text.set(DangQian_KJ_name)
                self.it_Entry = Entry(self.canva, text=DangQian_KJ_name, font=('TkDefaultFont', 10), width=10, bg=self.bg_Entry_YanSe)
                self.it_Entry.place(x=self.X0, y=self.Y0)
                self.it_Entry.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)

                self.it_Entry.config(width=W)
                self.it_Entry.place(x=self.X0, y=self.Y0)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 70
                    self.Y1 = self.Y0 + 20

                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Frame(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Frame = Frame(self.canva,  width=100, height=60)
                self.it_Frame.place(x=self.X0, y=self.Y0)
                self.it_Frame.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Frame.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 60
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Label(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Label = Label(self.canva, text=DangQian_KJ_name, font=('TkDefaultFont', 10), width=0, height=0)
                self.it_Label.place(x=self.X0, y=self.Y0)
                self.it_Label.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                global DangQian_KJ_name
                self.Text = DangQian_KJ_name

                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Label.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 40
                    self.Y1 = self.Y0 + 10

                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_LabelFrame(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name

                self.X0 = event.x
                self.Y0 = event.y

                self.canva.config(cursor='crosshair')

                # LabelFrame 无 textvariable 属性
                self.it_LabelFrame = LabelFrame(self.canva, text=DangQian_KJ_name, font=('TkDefaultFont', 10), width=100, height=60)
                self.it_LabelFrame.place(x=self.X0, y=self.Y0)
                self.it_LabelFrame.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                global DangQian_KJ_name
                self.Text = DangQian_KJ_name

                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_LabelFrame.config(width=W, height=H)

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 60
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Listbox(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                # Listbox 无 textvariable 或 text 属性
                self.it_Listbox = Listbox(self.canva, bg=self.bg_Listbox_YanSe, font=('TkDefaultFont', 10), width=12, height=3)
                self.it_Listbox.place(x=self.X0, y=self.Y0)
                self.it_Listbox.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                global DangQian_KJ_name
                self.Text = DangQian_KJ_name

                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/14)

                self.it_Listbox.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 60
                    self.Y1 = self.Y0 + 60
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Hua_Menu_Tuo(self):

        self.list_name.set('')
        self.btn_name.set('')
        self.it_ShuRu_Entry.place(x=3, y=2)
        self.it_List_ShuRu_Entry.place(x=180, y=2)

        def X_add():
            global D_ZhuMenu
            global Menu1
            global DQ_Zong_Len
            global zi_menu1_sum  # 子 Menu的总数
            global DQ_ZhuMenu_ZiXiang_Num_i
            global Menu1_Son_Len
            global zi_menu1_num_i  # 子 Menu的序号

            self.Ent_X = StringVar()

            if zi_menu1_sum != 0:
                YinChang_List(zi_menu1_sum)

            if self.btn_name.get() != '':  # Entry 空时用 '' 表示

                zi_menu1_num_i = zi_menu1_num_i + 1
                zi_menu1_sum = zi_menu1_sum + 1

                DQ_ZhuMenu_ZiXiang_Num_i = zi_menu1_num_i

                self.Ent_X.set(self.btn_name.get())

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                num = zi_menu1_num_i # 华文琥珀  微软雅黑
                self.it_X_add_Btn_New = Button(self.frame, textvariable=self.Ent_X, relief=FLAT, height=1,
                                               font=('TkDefaultFont', 8), command=lambda: XianShi_ListBox(num_i=num))
                self.it_X_add_Btn_New.grid(row=1, column=zi_menu1_num_i + 1)
                self.it_X_add_Btn_New.lift()

                width = int((self.it_X_add_Btn_New.winfo_reqwidth()))

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                DQ_Zong_Len = 0
                if zi_menu1_num_i > 1:
                    for i in range(1, zi_menu1_num_i, 1):
                        if i not in Menu1_Delete_Num:
                            len_name = "Len" + str(i)
                            DQ_Zong_Len = DQ_Zong_Len + Menu1_Son_Len[len_name][1]
                else:
                    DQ_Zong_Len = 0

                self.it_Y_add_Listbox_new = Listbox(self.canva, bg='SystemButtonFace')
                self.it_Y_add_Listbox_new.place(x=3 + DQ_Zong_Len, y=self.bar_W + 20)  # 画布坐标是控件的 7 倍
                self.it_Y_add_Listbox_new.lift()

                len_name = "Len" + str(zi_menu1_num_i)
                Menu1_Son_Len[len_name] = (zi_menu1_num_i, width)
                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                # 设置字典
                # 0： self.it_X_add_Btn_New      菜单标题按钮
                # 1： zi_menu1_num_i               菜单标题按钮的 序号
                # 2： self.it_Y_add_Listbox_new  菜单标题按钮对应的下拉列表
                # 3： self.Ent_X.get()           菜单标题按钮的 输入标题

                D_Menu_Btn_name = 'Menu_Btn' + str(zi_menu1_num_i)
                D_ZhuMenu[D_Menu_Btn_name] = (self.it_X_add_Btn_New, zi_menu1_num_i, self.it_Y_add_Listbox_new,
                                              self.Ent_X.get())

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                # 录入代码
                Menubar = "Menubar"

                zi_menu_name = "zi_menu_name" + str(zi_menu1_num_i)
                Menu1[zi_menu_name] = (str(self.Ent_X.get()) + "_menu").strip()

                zi_menu_tearoff_name = "zi_menu_tearoff_name" + str(zi_menu1_num_i)
                zi_menu_add_cascade_name = "zi_menu_add_cascade_name" + str(zi_menu1_num_i)

                Menu_Code1 = str(Menu1[zi_menu_name]) + " = Menu(" + Menubar + ", tearoff=0)"
                Menu_Code2 = Menubar + ".add_cascade(label='" + str(self.Ent_X.get()) + "', menu=" + str(Menu1[zi_menu_name]) + ")"

                Menu1[zi_menu_tearoff_name] = (Menu_Code1, zi_menu1_num_i)
                Menu1[zi_menu_add_cascade_name] = (Menu_Code2, zi_menu1_num_i)

                print(Menu1[zi_menu_tearoff_name][0])
                print(Menu1[zi_menu_add_cascade_name][0])

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                # 屏蔽之前的 List
                if zi_menu1_num_i > 1:
                    for i in range(1, zi_menu1_num_i, 1):
                        if i not in Menu1_Delete_Num:
                            a = D_ZhuMenu['Menu_Btn' + str(i)]
                            a[2].place(x=-600, y=self.bar_W + 30)

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                # 清空以备下次输入
                self.btn_name.set('')

        def XianShi_ListBox(num_i):
            global D_ZhuMenu
            global DQ_ZhuMenu_ZiXiang_Num_i
            global DQ_Zong_Len
            global zi_menu1_sum
            global Menu1_Delete_Num

            DQ_ZhuMenu_ZiXiang_Num_i = num_i   # 定义当前按下的子按钮标号
            L = 0

            # len_name = "Len" + str(zi_menu1_num_i)
            # Menu1_Son_Len[len_name] = (zi_menu1_num_i, width)
            for i in range(1, num_i, 1):
                if i not in Menu1_Delete_Num:
                    len_name = "Len" + str(i)
                    L = L + Menu1_Son_Len[len_name][1]
                    print("L = ", L)

            name_menu = 'Menu_Btn' + str(num_i)

            print("num_i = ", num_i)

            a = D_ZhuMenu[name_menu]
            # 重新复位
            a[2].place(x=3 + L, y=self.bar_W + 20)  # 字典内的列表下表由 0 开始

            print("zi_menu1_sum = ", zi_menu1_sum)

            for i_Num in range(1, zi_menu1_num_i+1, 1):
                if (i_Num != num_i) and (i_Num not in Menu1_Delete_Num):
                    name1 = 'Menu_Btn' + str(i_Num)
                    a = D_ZhuMenu[name1]
                    a[2].place(x=-600, y=self.bar_W + 30)


        def X_delet():
            global D_ZhuMenu
            global DQ_ZhuMenu_ZiXiang_Num_i
            global zi_menu1_sum
            global DQ_Zong_Len
            global Menu1_Delete_Num  # Menu1_Delete_Num[]

            if zi_menu1_sum != 0:
                if DQ_ZhuMenu_ZiXiang_Num_i == zi_menu1_sum:
                    DQ_ZhuMenu_ZiXiang_Num_i = DQ_ZhuMenu_ZiXiang_Num_i - 1

                # D_Menu_Btn_name = 'Menu_Btn' + str(zi_menu1_sum)
                D_Menu_Btn_name = 'Menu_Btn' + str(DQ_ZhuMenu_ZiXiang_Num_i)
                a = D_ZhuMenu[D_Menu_Btn_name]

                Menu1_Delete_Num.append(DQ_ZhuMenu_ZiXiang_Num_i)

                a[0].destroy()  # 0： self.it_X_add_Btn_New  菜单标题按钮
                a[2].destroy()  # 2： self.it_Y_add_Listbox_new  菜单标题按钮对应的下拉列表

                del D_ZhuMenu[D_Menu_Btn_name]
                zi_menu1_sum = zi_menu1_sum - 1


        def YinChang_List(i):
            global D_ZhuMenu
            global Menu1_Delete_Num
            if i not in Menu1_Delete_Num:
                name1 = 'Menu_Btn' + str(i)
                a = D_ZhuMenu[name1]
                a[2].place(x=-600, y=self.bar_W + 30)


        def YinChang_Entry():
            self.it_ShuRu_Entry.place(x=-600, y=0)
            self.it_List_ShuRu_Entry.place(x=-600, y=0)


        def YinChang_All():
            global DQ_ZhuMenu_ZiXiang_Num_i
            YinChang_List(DQ_ZhuMenu_ZiXiang_Num_i)
            YinChang_Entry()


        def Y_add(flag):
            global D_ZhuMenu
            global Menu1
            global Menu1_ListCode
            global DQ_Zong_Len
            global zi_menu1_sum
            global DQ_ZhuMenu_ZiXiang_Num_i  # 当前按下的标题按钮标号

            Str_Insert = ''
            global tap

            if flag == "text":
                Str_Insert = tap + str(self.list_name.get())
            elif flag == "separator":
                Str_Insert = '-----------------------------------------------------------------------------'

            if zi_menu1_sum != 0:
                D_Menu_Btn_name = 'Menu_Btn' + str(DQ_ZhuMenu_ZiXiang_Num_i)
                a = D_ZhuMenu[D_Menu_Btn_name]

                DQ_Listbox = a[2]
                zong = DQ_Listbox.size()

                if zong == 0:
                    DQ_Listbox.insert(END, Str_Insert)
                if zong > 0:
                    if a[2].curselection() == ():
                        DQ_Listbox.insert(END, Str_Insert)
                    else:
                        DQ_i = a[2].curselection()
                        DQ_Listbox.insert(DQ_i, Str_Insert)

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                # 录入代码
                zi_menu_name = "zi_menu_name" + str(DQ_ZhuMenu_ZiXiang_Num_i)
                Code_Insert = ''
                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                if flag == "text":
                    Code_Insert = str(Menu1[zi_menu_name]) + ".add_command(label='" + \
                                  str(self.list_name.get()) + "', command='')"
                elif flag == "separator":
                    Code_Insert = str(Menu1[zi_menu_name]) + ".add_separator()"

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

                if zong == 0:
                    menu_list_code_name = str(Menu1[zi_menu_name]) + "_list_" + str(1)
                    Menu1_ListCode[menu_list_code_name] = (Code_Insert, DQ_ZhuMenu_ZiXiang_Num_i, 1)
                    print(Menu1_ListCode[menu_list_code_name][0])

                if zong > 0:
                    if a[2].curselection() == ():
                        menu_list_code_name = str(Menu1[zi_menu_name]) + "_list_" + str(zong + 1)
                        Menu1_ListCode[menu_list_code_name] = (Code_Insert, DQ_ZhuMenu_ZiXiang_Num_i, zong + 1)
                        print(Menu1_ListCode[menu_list_code_name][0])

                    else:
                        # 按下后当前选定选项向后偏移一个
                        A = a[2].curselection()  # a[3].curselection() 是一个单值元组 为 (索引值,)
                        DQ_Listbox_i = A[0]   # A[0] 从 0 开始

                        # for 循环重新排列大于 int(DQ_Listbox_i) 项对应代码
                        # listbox 可以 get() 不能 set()
                        # *****************************************************************************************
                        D = {}  # 备用记录字典
                        for i in range(1, zong+1, 1):  # range(a, b, i) 从 a 开始到 b前为止，间隔为 i, 包括 a不包括 b
                            name = str(Menu1[zi_menu_name]) + "_list_" + str(i)
                            D[str(i)] = Menu1_ListCode[name]

                        for i in range(int(DQ_Listbox_i)+1, zong+2, 1):
                            name = str(Menu1[zi_menu_name]) + "_list_" + str(i)
                            Menu1_ListCode[name] = D[str(i-1)]

                        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                        # 关键代码
                        menu_list_code_name = str(Menu1[zi_menu_name]) + "_list_" + str(int(DQ_Listbox_i))
                        Menu1_ListCode[menu_list_code_name] = (Code_Insert, zi_menu1_sum, int(DQ_Listbox_i))

                        print(Menu1_ListCode[menu_list_code_name][0])
                        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                        for i in range(1, zong + 2, 1):
                            name = str(Menu1[zi_menu_name]) + "_list_" + str(i)
                            print('Menu1[name] = ', Menu1[name][0], 'i = ', i)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        def Y_delet():
            global D_ZhuMenu
            global D_ZhuMenu_List  # 标题按钮下拉列表字典
            global DQ_Zong_Len
            global Menu1
            global Menu1_ListCode
            global zi_menu1_sum
            global DQ_ZhuMenu_ZiXiang_Num_i  # 当前按下的标题按钮标号

            D_Menu_Btn_name = 'Menu_Btn' + str(DQ_ZhuMenu_ZiXiang_Num_i)
            a = D_ZhuMenu[D_Menu_Btn_name]
            DQ_Listbox = a[2]
            zong = DQ_Listbox.size()

            if zong > 0:
                # 录入代码
                zi_menu_name = "zi_menu_name" + str(DQ_ZhuMenu_ZiXiang_Num_i)
                if zong == 0:
                    DQ_Listbox.delete(END)

                    menu_list_code_name = str(Menu1[zi_menu_name]) + "_list_" + str(zong)
                    del Menu1_ListCode[menu_list_code_name]

                if zong > 0:
                    if a[2].curselection() == ():
                        DQ_Listbox.delete(END)

                        menu_list_code_name = str(Menu1[zi_menu_name]) + "_list_" + str(zong)
                        del Menu1_ListCode[menu_list_code_name]
                        print('del Menu1[menu_list_code_name] **************************')

                    else:
                        DQ_i = a[2].curselection()  # a[3].curselection() 是一个单值元组 为 (索引值,)
                        DQ_Listbox_i = DQ_i[0]  # A[0] 从 0 开始
                        DQ_Listbox.delete(DQ_i)  # 删除选定列表项

                        print('D = {}  # 备用记录字典')
                        D = {}  # 备用记录字典
                        # range(a, b, i) 从 a 开始到 b前为止，间隔为 i, 包括 a不包括 b
                        for i in range(1, zong + 1, 1):
                            name = str(Menu1[zi_menu_name]) + "_list_" + str(i)
                            D[str(i)] = Menu1_ListCode[name]

                        for i in range(int(DQ_Listbox_i)+1, zong, 1):
                            name = str(Menu1[zi_menu_name]) + "_list_" + str(i)
                            Menu1_ListCode[name] = D[str(i + 1)]

                        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                        # # 关键代码
                        menu_list_code_name = str(Menu1[zi_menu_name]) + "_list_" + str(zong)
                        del Menu1_ListCode[menu_list_code_name]
                        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

                for i in range(1, zong, 1):
                    name = str(Menu1[zi_menu_name]) + "_list_" + str(i)
                    print('Menu1[name] = ', Menu1_ListCode[name], 'i = ', i)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        Font = ('TkDefaultFont', 8)
        if self.YiCi == FALSE:
            self.it_Y_add_Btn = Button(self.frame, text='+Y', width=3, bg='yellow', fg='blue',
                                       font=Font, command=lambda: Y_add(flag="text"))

            self.it_Y_delet_Btn = Button(self.frame, text='-Y', width=3, bg='red', fg='white',
                                       font=Font,  command=Y_delet)

            self.it_X_add_Btn = Button(self.frame, text='+X', width=3, bg='yellow', fg='blue',
                                       font=Font, command=X_add)

            self.it_X_delet_Btn = Button(self.frame, text='-X', width=3, bg='red', fg='white',
                                       font=Font,  command=X_delet)

            self.Separator_Btn = Button(self.frame, text='----', width=3, bg='lightblue', fg='white',
                                       font=Font, command=lambda: Y_add(flag="separator"))

            self.YinCang_Btn = Button(self.frame, text='C', width=3, bg='blue', fg='white',
                                       font=Font, command=YinChang_All)
            self.YiCi = TRUE

        self.it_X_add_Btn.grid(row=1, column=1001)
        self.it_X_delet_Btn.grid(row=1, column=1002)
        self.it_Y_add_Btn.grid(row=1, column=1003)
        self.it_Y_delet_Btn.grid(row=1, column=1005)
        self.Separator_Btn.grid(row=1, column=1004)
        self.YinCang_Btn.grid(row=1, column=1006)

        self.it_X_add_Btn.lift()
        self.it_X_delet_Btn.lift()
        self.it_Y_add_Btn.lift()
        self.it_Y_delet_Btn.lift()
        self.YinCang_Btn.lift()
        self.Separator_Btn.lift()
        # self.it_Y_add_Btn.place(x=3, y=self.bar_W + 2 + 28)

    def Hua_Menu(self):
        if self.flag_WanCheng1 == FALSE:
            def paint_AnXia(event):
                global DangQian_KJ_name
                global canva_W
                global flag_Menu_Kai

                self.YiCi = FALSE

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                if flag_Menu_Kai == FALSE:

                    self.frame = Frame(self.canva, width=380, height=28)
                    self.frame.place(x=3, y=self.bar_W + 2)

                    self.btn_name = StringVar()
                    self.btn_name.set('Menu title input')

                    self.list_name = StringVar()
                    self.list_name.set('Title list input')

                    self.it_ShuRu_Entry = Entry(self.canva, textvariable=self.btn_name, font=('微软雅黑', 10),
                                                bg='DeepSkyBlue', width=20)

                    self.it_List_ShuRu_Entry = Entry(self.canva, textvariable=self.list_name, font=('微软雅黑', 10),
                                                bg='LightBlue', width=20)

                    self.it_Button_Menu = Button(self.frame, text='Edit', width=6, bg='LightGreen',
                                                 font=('TkDefaultFont', 8), command=self.Hua_Menu_Tuo)  # 此处调用函数时，不要加()，加()后，是调用+执行

                    self.it_Button_Menu.grid(row=1, column=100)
                    self.it_ShuRu_Entry.place(x=3, y=2)
                    self.it_List_ShuRu_Entry.place(x=180, y=2)

                    self.it_Button_Menu.lift()
                    flag_Menu_Kai = TRUE

            def paint_YiDong(event):
                global DangQian_KJ_name
                self.Text = DangQian_KJ_name

            def paint_ShiFang(event):
                self.X0 = 0
                self.Y0 = 0
                self.X1 = 0
                self.Y1 = 0
                self.canva.delete('Hua_Kuang_ing')
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Message(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                # 再引入 tkinter.messagebox 后，Message定义前面要加上 tk. ，避免冲突
                self.it_Message = tk.Message(self.canva, text=DangQian_KJ_name, font=('TkDefaultFont', 10), width=100)
                self.it_Message.place(x=self.X0, y=self.Y0)
                self.it_Message.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y
                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                # H = int(abs(self.Y1 - self.Y0))  # Message 无 height属性

                self.it_Message.config(width=W)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 80
                    self.Y1 = self.Y0 + 10
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_PanedWindow(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_PanedWindow = PanedWindow(self.canva, width=100, height=60)
                self.it_PanedWindow.place(x=self.X0, y=self.Y0)
                self.it_PanedWindow.lower()

                self.flag_DanJi = TRUE


            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_PanedWindow.config(width=W, height=H)


            def paint_ShiFang(event):
                self.X1 = self.X0 + 100
                self.Y1 = self.Y0 + 65

                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Radiobutton(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global Radiobutton_i
                global flag_RadBtn_Zu

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                if flag_RadBtn_Zu == FALSE:
                    self.varInt = IntVar()
                    self.varInt.set(0)
                    flag_RadBtn_Zu = TRUE


                print('varInt = ', self.varInt)
                self.it_Radiobutton = Radiobutton(self.canva, variable=self.varInt, text='Radiobutton',
                                                  font=('TkDefaultFont', 10), value=Radiobutton_i)

                self.it_Radiobutton.place(x=self.X0, y=self.Y0)
                self.it_Radiobutton.lower()

                print('Radiobutton_i = ', Radiobutton_i)
                Radiobutton_i = Radiobutton_i + 1

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.6)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Radiobutton.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 90
                    self.Y1 = self.Y0 + 20
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Scale_X(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Scale_X = Scale(self.canva, orient=HORIZONTAL, font=('TkDefaultFont', 10))
                self.it_Scale_X.place(x=self.X0, y=self.Y0)
                self.it_Scale_X.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Scale_X.config(width=H-23, length=W)

                # ******************************************************************************************
                if self.flag_FuZuKuang == TRUE:
                    self.canva.itemconfig(self.it_Kuan, tags='Hua_Kuang_ing')
                # ******************************************************************************************

            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 100
                    self.Y1 = self.Y0 + 40
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Scale_Y(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Scale_Y = Scale(self.canva, font=('TkDefaultFont', 10))
                self.it_Scale_Y.place(x=self.X0, y=self.Y0)
                self.it_Scale_Y.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0))
                H = int(abs(self.Y1 - self.Y0))

                self.it_Scale_Y.config(width=W-26, length=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 50
                    self.Y1 = self.Y0 + 100
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Spinbox(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Spinbox = Spinbox(self.canva, values=(DangQian_KJ_name, 1, 2, 3), font=('TkDefaultFont', 10),
                                          bg=self.bg_Spinbox_YanSe)
                self.it_Spinbox.place(x=self.X0, y=self.Y0)
                self.it_Spinbox.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7.2)
                # H = int(abs(self.Y1 - self.Y0))

                self.it_Spinbox.config(width=W)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 200
                    self.Y1 = self.Y0 + 20
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Hua_Text(self):
        if self.flag_WanCheng1 == FALSE:
            self.flag_DanJi = FALSE  # 用于处理单击时，self.X1， self.Y1 为 0的情况
            def paint_AnXia(event):
                global DangQian_KJ_name

                self.X0 = event.x
                self.Y0 = event.y
                self.canva.config(cursor='crosshair')

                self.it_Text = Text(self.canva, bg=self.bg_Text_YanSe, font=('TkDefaultFont', 10), width=20, height=6)
                self.it_Text.insert(END, DangQian_KJ_name)
                self.it_Text.place(x=self.X0, y=self.Y0)
                self.it_Text.lower()

                self.flag_DanJi = TRUE

            def paint_YiDong(event):
                self.X1 = event.x
                self.Y1 = event.y

                self.flag_DanJi = FALSE

                W = int(abs(self.X1 - self.X0)/7)
                H = int(abs(self.Y1 - self.Y0)/13)

                self.it_Text.config(width=W, height=H)


            def paint_ShiFang(event):
                if self.flag_DanJi == TRUE:
                    self.X1 = self.X0 + 145
                    self.Y1 = self.Y0 + 80
                self.canva.config(cursor='arrow')
                self.LuRu_Dict()
                self.WanCheng()

            self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
            self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # 完成后
    def WanCheng(self):
        global background_XiangMu_XuanDing
        global foreground_XiangMu_XuanDing


        self.flag_WanCheng1 = TRUE

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        def paint_AnXia(event):
            global XuanZhong
            global XuanZhong_sum

            global Event_Canvas_x
            global Event_Canvas_y

            global XuanKuang_X0
            global XuanKuang_Y0

            self.Yanse_HuiFu()  # 每次按下颜色都要恢复到原来的状态

            XuanZhong.clear()
            XuanZhong_sum = 0

            Event_Canvas_x = event.x
            Event_Canvas_y = event.y

            XuanKuang_X0 = event.x
            XuanKuang_Y0 = event.y

            self.Yanse_HuiFu()


        def paint_YiDong(event):
            global flag_TanChuan_BianJian
            flag_TanChuan_BianJian = TRUE

            global XuanKuang_X0
            global XuanKuang_Y0
            global XuanKuang_X1
            global XuanKuang_Y1

            XuanKuang_X1 = event.x
            XuanKuang_Y1 = event.y

            self.canva.delete('Xuan_Kuang_ing')

            self.it_Kuan1 = self.canva.create_line(XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1, XuanKuang_Y0, fill='DeepSkyBlue', width=2)
            self.it_Kuan2 = self.canva.create_line(XuanKuang_X0, XuanKuang_Y0, XuanKuang_X0, XuanKuang_Y1, fill='DeepSkyBlue', width=2)
            self.it_Kuan3 = self.canva.create_line(XuanKuang_X0, XuanKuang_Y1, XuanKuang_X1, XuanKuang_Y1, fill='DeepSkyBlue', width=2)
            self.it_Kuan4 = self.canva.create_line(XuanKuang_X1, XuanKuang_Y0, XuanKuang_X1, XuanKuang_Y1, fill='DeepSkyBlue', width=2)

            # ******************************************************************************************
            self.canva.itemconfig(self.it_Kuan1, tags='Xuan_Kuang_ing')
            self.canva.itemconfig(self.it_Kuan2, tags='Xuan_Kuang_ing')
            self.canva.itemconfig(self.it_Kuan3, tags='Xuan_Kuang_ing')
            self.canva.itemconfig(self.it_Kuan4, tags='Xuan_Kuang_ing')

        def paint_ShiFang(event):
            global XuanKuang_X0
            global XuanKuang_Y0
            global XuanKuang_X1
            global XuanKuang_Y1

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            global Distance
            global bar_W
            global bar_menu_W

            if zi_menu1_sum == 0:
                Distance = bar_W
            else:
                Distance = bar_W + bar_menu_W

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            XuanKuang_X1 = event.x
            XuanKuang_Y1 = event.y

            XuanKuang_Y0 = XuanKuang_Y0 - Distance
            XuanKuang_Y1 = XuanKuang_Y1 - Distance

            self.canva.delete('Xuan_Kuang_ing')

            global XuanZhong_sum
            global XuanZhong
            # 收索
            # 控件字典
            # $$$$$$$$$$$$$$$$$$$
            global Button1
            global Canvas1
            global Checkbutton1
            global Combobox1
            global Entry1
            global Frame1
            global Label1
            global LabelFrame1
            global Listbox1
            global Message1
            global PanedWindow1
            global Radiobutton1
            global Scale1_X
            global Scale1_Y
            global Scrollbar1_X
            global Scrollbar1_Y
            global Spinbox1
            global Text1
            # $$$$$$$$$$$$$$$$$$$$
            global button1_i
            global canvas1_i
            global checkbutton1_i
            global combobox1_i
            global entry1_i
            global frame1_i
            global label1_i
            global labelFrame1_i
            global listbox1_i
            global message1_i
            global panedWindow1_i
            global radiobutton1_i
            global scale1_x_i
            global scale1_y_i
            global scrollbar1_x_i
            global scrollbar1_y_i
            global spinbox1_i
            global text1_i


            # for 循环逐个判断
            for i in range(1, button1_i + 1, 1):
                if i not in Button1_List_Num:
                    # BuJian_ChuLi(self, i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_Lei, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1, XuanKuang_Y1):
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Button', 'button', Button1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1, XuanKuang_Y1)

            for i in range(1, canvas1_i + 1, 1):
                if i not in Canvas1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Canvas', 'canvas', Canvas1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, checkbutton1_i + 1, 1):
                if i not in Checkbutton1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Checkbutton', 'checkbutton', Checkbutton1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, combobox1_i + 1, 1):
                if i not in Combobox1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Combobox', 'combobox', Combobox1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, entry1_i + 1, 1):
                if i not in Entry1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Entry', 'entry', Entry1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, frame1_i + 1, 1):
                if i not in Frame1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Frame', 'frame', Frame1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, label1_i + 1, 1):
                if i not in Label1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Label', 'label', Label1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, labelFrame1_i + 1, 1):
                if i not in LabelFrame1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'LabelFrame', 'labelFrame', LabelFrame1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, listbox1_i + 1, 1):
                if i not in Listbox1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Listbox', 'listbox', Listbox1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, message1_i + 1, 1):
                if i not in Message1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Message', 'message', Message1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, panedWindow1_i + 1, 1):
                if i not in PanedWindow1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'PanedWindow', 'panedWindow', PanedWindow1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, radiobutton1_i + 1, 1):
                if i not in Radiobutton1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Radiobutton', 'radiobutton', Radiobutton1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, scale1_x_i + 1, 1):
                if i not in Scale1_List_Num_X:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Scale_X', 'scale_x', Scale1_X, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, scale1_y_i + 1, 1):
                if i not in Scale1_List_Num_Y:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Scale_Y', 'scale_y', Scale1_Y, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, spinbox1_i + 1, 1):
                if i not in Spinbox1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Spinbox', 'spinbox', Spinbox1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            for i in range(1, text1_i + 1, 1):
                if i not in Text1_List_Num:
                    xuan_ding = XuanDing()
                    xuan_ding.BuJian_ChuLi(i, 'Text', 'text', Text1, XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1,
                                           XuanKuang_Y1)

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.Design()
            self.TanChuang()
            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

        self.canva.bind("<B1-Motion>", paint_YiDong)  # 绑定鼠标移动事件
        self.canva.bind("<ButtonPress-1>", paint_AnXia)  # 绑定鼠标按下事件
        self.canva.bind("<ButtonRelease-1>", paint_ShiFang)  # 绑定鼠标释放事件



    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def TanChuang(self):
        global canva_X
        global canva_Y
        global win_X
        global win_Y
        global flag_TanChuan_BianJian
        global XuanKuang_X1
        global XuanKuang_Y1

        if flag_TanChuan_BianJian == TRUE:
            self.BianJi_kj_menu.post(XuanKuang_X1+canva_X+win_X, XuanKuang_Y1+canva_Y+win_Y)
            flag_TanChuan_BianJian = FALSE


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def OK(self):
        global flag_ZuJian_Move
        flag_ZuJian_Move = FALSE

        print('OK, $$$$$$$$$$$$$$$$$$$$$$$$$$$$$   flag_ZuJian_Move = ', flag_ZuJian_Move)

        self.WanCheng()
        self.Yanse_HuiFu()
        self.Clear_XuanZhong()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Design(self):
            global XuanZhong_sum
            global XuanZhong

            # Design_bujian(self, XuanZhong_Object):
            design_buJian = Design_BuJian()

            Len = len(XuanZhong)
            if Len == 1:
                name = "XuanZhong" + str(1)
                a = XuanZhong[name]
                design_buJian.Design_bujian(a)


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def UI_Ban_Design(self):
        global XuanZhong_sum
        global XuanZhong

        Len = len(XuanZhong)
        if Len == 1:
            name = "XuanZhong" + str(1)
            a = XuanZhong[name]

            BuJian_LeiXing_DaXie = a[1]
            BuJian_LeiXing_XiaoXie = a[2]
            BuJian_NO_i = a[3]
            BuJian_Lei = a[4]

            # name = "XuanZhong" + str(XuanZhong_sum)
            # XuanZhong[name] = (Button1[KJ], 'Button', 'button', Num_i, Button1)
            design_new = Design_New()
            design_new.BuJian_New(BuJian_LeiXing_DaXie, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei)

            # name
            # KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
            # BuJian_Lei[KJ_name] = ent_ControlName
            sj_chu_li = SJ_ChuLi()
            sj_chu_li.SJ_New(BuJian_LeiXing_XiaoXie, BuJian_NO_i, BuJian_Lei)


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Move(self):
        global flag_ZuJian_Move
        # $$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$
        global XuanZhong_sum
        global XuanZhong
        # $$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$
        global Button1
        global Canvas1
        global Checkbutton1
        global Combobox1
        global Entry1
        global Frame1
        global Label1
        global LabelFrame1
        global Listbox1
        global Message1
        global PanedWindow1
        global Radiobutton1
        global Scale1_X
        global Scale1_Y
        global Scrollbar1_X
        global Scrollbar1_Y
        global Spinbox1
        global Text1

        Len = len(XuanZhong)
        # $$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$
        # name = "XuanZhong" + str(XuanZhong_sum)
        # XuanZhong[name] = (Button1[KJ], 'Button', 'button', Num_i, Button1)

        if 1:
        # if flag_ZuJian_Move == TRUE:
            # 鼠标左键按下事件
            def paint1(event):
                self.ZuJian_x1 = event.x
                self.ZuJian_y1 = event.y
                self.canva.config(cursor='fleur')

                self.Line = self.canva.create_line(self.ZuJian_x1, self.ZuJian_y1, self.ZuJian_x1, self.ZuJian_y1,
                                                   fill="DeepSkyBlue", width=1.6)

            # 鼠标左键按下并移动事件
            def paint2(event):
                self.ZuJian_x2 = event.x
                self.ZuJian_y2 = event.y

                self.Move_X = self.ZuJian_x2 - self.ZuJian_x1
                self.Move_Y = self.ZuJian_y2 - self.ZuJian_y1
                # 绘制移动基线
                self.canva.coords(self.Line, self.ZuJian_x1, self.ZuJian_y1, self.ZuJian_x2, self.ZuJian_y2)

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                for i in range(1, Len + 1, 1):
                    name = "XuanZhong" + str(i)
                    a = XuanZhong[name]
                    if a[1] == 'Button':
                        num_i = a[3]
                        KJ = 'Button' + str(a[3])
                        name_coords = 'button_coords' + str(num_i)
                        a = Button1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Button1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Canvas':
                        num_i = a[3]
                        KJ = 'Canvas' + str(a[3])
                        name_coords = 'canvas_coords' + str(num_i)
                        a = Canvas1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Canvas1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Checkbutton':
                        num_i = a[3]
                        KJ = 'Checkbutton' + str(a[3])
                        name_coords = 'checkbutton_coords' + str(num_i)
                        a = Checkbutton1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Checkbutton1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Combobox':
                        num_i = a[3]
                        KJ = 'Combobox' + str(a[3])
                        name_coords = 'combobox_coords' + str(num_i)
                        a = Combobox1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Combobox1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Entry':
                        num_i = a[3]
                        KJ = 'Entry' + str(a[3])
                        name_coords = 'entry_coords' + str(num_i)
                        a = Entry1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Entry1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Frame':
                        num_i = a[3]
                        KJ = 'Frame' + str(a[3])
                        name_coords = 'frame_coords' + str(num_i)
                        a = Frame1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Frame1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Label':
                        num_i = a[3]
                        KJ = 'Label' + str(a[3])
                        name_coords = 'label_coords' + str(num_i)
                        a = Label1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Label1[KJ].place(x=X, y=Y)

                    elif a[1] == 'LabelFrame':
                        num_i = a[3]
                        KJ = 'LabelFrame' + str(a[3])
                        name_coords = 'labelFrame_coords' + str(num_i)
                        a = LabelFrame1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        LabelFrame1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Listbox':
                        num_i = a[3]
                        KJ = 'Listbox' + str(a[3])
                        name_coords = 'listbox_coords' + str(num_i)
                        a = Listbox1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Listbox1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Message':
                        num_i = a[3]
                        KJ = 'Message' + str(a[3])
                        name_coords = 'message_coords' + str(num_i)
                        a = Message1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Message1[KJ].place(x=X, y=Y)

                    elif a[1] == 'PanedWindow':
                        num_i = a[3]
                        KJ = 'PanedWindow' + str(a[3])
                        name_coords = 'panedWindow_coords' + str(num_i)
                        a = PanedWindow1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        PanedWindow1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Radiobutton':
                        num_i = a[3]
                        KJ = 'Radiobutton' + str(a[3])
                        name_coords = 'radiobutton_coords' + str(num_i)
                        a = Radiobutton1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Radiobutton1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Scale_X':
                        num_i = a[3]
                        KJ = 'Scale_X' + str(a[3])
                        name_coords = 'scale_x_coords' + str(num_i)
                        a = Scale1_X[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Scale1_X[KJ].place(x=X, y=Y)

                    elif a[1] == 'Scale_Y':
                        num_i = a[3]
                        KJ = 'Scale_Y' + str(a[3])
                        name_coords = 'scale_y_coords' + str(num_i)
                        a = Scale1_Y[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Scale1_Y[KJ].place(x=X, y=Y)

                    elif a[1] == 'Spinbox':
                        num_i = a[3]
                        KJ = 'Spinbox' + str(a[3])
                        name_coords = 'spinbox_coords' + str(num_i)
                        a = Spinbox1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Spinbox1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Text':
                        num_i = a[3]
                        KJ = 'Text' + str(a[3])
                        name_coords = 'text_coords' + str(num_i)
                        a = Text1[name_coords]
                        X0 = a[0]
                        Y0 = a[1]
                        X = X0 + self.Move_X
                        Y = Y0 + self.Move_Y
                        Text1[KJ].place(x=X, y=Y)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            # 鼠标左键松开事件
            def paint3(event):
                global canva_X
                global canva_Y
                global win_X
                global win_Y

                self.ZuJian_x2 = event.x
                self.ZuJian_y2 = event.y

                self.canva.delete(self.Line)
                self.canva.config(cursor='arrow')
                self.BianJi_kj_menu.post(self.ZuJian_x2 + canva_X + win_X, self.ZuJian_y2 + canva_Y + win_Y)

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                for i in range(1, Len + 1, 1):
                    name = "XuanZhong" + str(i)
                    a = XuanZhong[name]
                    if a[1] == 'Button':
                        num_i = a[3]
                        KJ = 'Button' + str(a[3])
                        name_coords = 'button_coords' + str(num_i)
                        a = Button1[name_coords]

                        # name_coords = 'button_coords' + str(BuJian_NO_i)
                        # Zhi = (self.X0, self.Y0, self.X1, self.Y1, BuJian_NO_i)

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y


                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Button1[name_coords] = Zhi
                        # # Button1[KJ].place(x=X, y=Y)

                    elif a[1] == 'Canvas':
                        num_i = a[3]
                        KJ = 'Canvas' + str(a[3])
                        name_coords = 'canvas_coords' + str(num_i)
                        a = Canvas1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Canvas1[name_coords] = Zhi


                    elif a[1] == 'Checkbutton':
                        num_i = a[3]
                        KJ = 'Checkbutton' + str(a[3])
                        name_coords = 'checkbutton_coords' + str(num_i)
                        a = Checkbutton1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Checkbutton1[name_coords] = Zhi


                    elif a[1] == 'Combobox':
                        num_i = a[3]
                        KJ = 'Combobox' + str(a[3])
                        name_coords = 'combobox_coords' + str(num_i)
                        a = Combobox1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Combobox1[name_coords] = Zhi


                    elif a[1] == 'Entry':
                        num_i = a[3]
                        KJ = 'Entry' + str(a[3])
                        name_coords = 'entry_coords' + str(num_i)
                        a = Entry1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Entry1[name_coords] = Zhi


                    elif a[1] == 'Frame':
                        num_i = a[3]
                        KJ = 'Frame' + str(a[3])
                        name_coords = 'frame_coords' + str(num_i)
                        a = Frame1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Entry1[name_coords] = Zhi



                    elif a[1] == 'Label':
                        num_i = a[3]
                        KJ = 'Label' + str(a[3])
                        name_coords = 'label_coords' + str(num_i)
                        a = Label1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Label1[name_coords] = Zhi


                    elif a[1] == 'LabelFrame':
                        num_i = a[3]
                        KJ = 'LabelFrame' + str(a[3])
                        name_coords = 'labelFrame_coords' + str(num_i)
                        a = LabelFrame1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        LabelFrame1[name_coords] = Zhi


                    elif a[1] == 'Listbox':
                        num_i = a[3]
                        KJ = 'Listbox' + str(a[3])
                        name_coords = 'listbox_coords' + str(num_i)
                        a = Listbox1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Listbox1[name_coords] = Zhi


                    elif a[1] == 'Message':
                        num_i = a[3]
                        KJ = 'Message' + str(a[3])
                        name_coords = 'message_coords' + str(num_i)
                        a = Message1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Message1[name_coords] = Zhi


                    elif a[1] == 'PanedWindow':
                        num_i = a[3]
                        KJ = 'PanedWindow' + str(a[3])
                        name_coords = 'panedWindow_coords' + str(num_i)
                        a = PanedWindow1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        PanedWindow1[name_coords] = Zhi


                    elif a[1] == 'Radiobutton':
                        num_i = a[3]
                        KJ = 'Radiobutton' + str(a[3])
                        name_coords = 'radiobutton_coords' + str(num_i)
                        a = Radiobutton1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Radiobutton1[name_coords] = Zhi


                    elif a[1] == 'Scale_X':
                        num_i = a[3]
                        KJ = 'Scale_X' + str(a[3])
                        name_coords = 'scale_x_coords' + str(num_i)
                        a = Scale1_X[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Scale1_X[name_coords] = Zhi


                    elif a[1] == 'Scale_Y':
                        num_i = a[3]
                        KJ = 'Scale_Y' + str(a[3])
                        name_coords = 'scale_y_coords' + str(num_i)
                        a = Scale1_Y[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Scale1_Y[name_coords] = Zhi


                    elif a[1] == 'Spinbox':
                        num_i = a[3]
                        KJ = 'Spinbox' + str(a[3])
                        name_coords = 'spinbox_coords' + str(num_i)
                        a = Spinbox1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Spinbox1[name_coords] = Zhi


                    elif a[1] == 'Text':
                        num_i = a[3]
                        KJ = 'Text' + str(a[3])
                        name_coords = 'text_coords' + str(num_i)
                        a = Text1[name_coords]

                        X0 = a[0]
                        Y0 = a[1]
                        X1 = a[2]
                        Y1 = a[3]

                        XX0 = X0 + self.Move_X
                        YY0 = Y0 + self.Move_Y
                        XX1 = X1 + self.Move_X
                        YY1 = Y1 + self.Move_Y

                        Zhi = (XX0, YY0, XX1, YY1, a[4])
                        Text1[name_coords] = Zhi

                        print('Text1 = \n', Text1[KJ])
                        print('Text1_coords = \n', Text1[name_coords])


                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            # 画布控件与鼠标左键进行绑定
            self.canva.bind("<ButtonPress-1>", paint1)  # 绑定鼠标按下事件
            self.canva.bind("<B1-Motion>", paint2)  # 绑定鼠标移动事件
            self.canva.bind("<ButtonRelease-1>", paint3)  # 绑定鼠标松开事件


    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Delete(self):
        global XuanZhong
        global XuanZhong_sum

        if askyesno('Delete', 'Is going to delete Selected？'):
            Len = len(XuanZhong)

            for i in range(1, Len + 1, 1):
                name = "XuanZhong" + str(i)
                a = XuanZhong[name]

                XuanZhong_Object = a
                delete_buJian = Delete_BuJian()
                delete_buJian.Delete(XuanZhong_Object)

            # 清空选中
            self.Clear_XuanZhong()

        # 如果不清空则恢复原来颜色
        else:
            self.Yanse_HuiFu()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Cancel(self):
        self.Yanse_HuiFu()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Clear_XuanZhong(self):
        global XuanZhong_sum
        global XuanZhong
        XuanZhong_sum = 0
        XuanZhong.clear()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Yanse_HuiFu(self):
        global XuanZhong_sum
        global XuanZhong
        # name = "XuanZhong" + str(XuanZhong_sum)
        # XuanZhong[name] = (Button1[KJ], 'Button', 'button', Num_i, Button1)

        Len = len(XuanZhong)
        if len != 0:
            for i in range(1, Len + 1, 1):
                name = "XuanZhong" + str(i)
                a = XuanZhong[name]

                BuJian_Lei = a[4]
                BuJian_LeiXing_DaXie = a[1]
                BuJian_LeiXing_XiaoXie = a[2]
                Num_i = a[3]

                # Color_Restore(self, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, Num_i):
                color_handle = Color_Handle()
                color_handle.Color_Restore(BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, Num_i)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # 设置控件标志
    def Set_KJBZ(self, str):
        global KJBZ
        KJBZ = str

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def Hua_BianYi(self):
        global XuanZhong_sum
        global XuanZhong
        # 收索
        # 控件字典
        # $$$$$$$$$$$$$$$$$$$
        global Button1
        global Canvas1
        global Checkbutton1
        global Combobox1
        global Entry1
        global Frame1
        global Label1
        global LabelFrame1
        global Listbox1
        global Message1
        global PanedWindow1
        global Radiobutton1
        global Scale1_X
        global Scale1_Y
        global Scrollbar1_X
        global Scrollbar1_Y
        global Spinbox1
        global Text1
        # $$$$$$$$$$$$$$$$$$$$
        global button1_i
        global canvas1_i
        global checkbutton1_i
        global combobox1_i
        global entry1_i
        global frame1_i
        global label1_i
        global labelFrame1_i
        global listbox1_i
        global message1_i
        global panedWindow1_i
        global radiobutton1_i
        global scale1_x_i
        global scale1_y_i
        global scrollbar1_x_i
        global scrollbar1_y_i
        global spinbox1_i
        global text1_i

        # 记录各个部件类型删除的成员的 列表
        global Button1_List_Num
        global Canvas1_List_Num
        global Checkbutton1_List_Num
        global Combobox1_List_Num
        global Entry1_List_Num
        global Frame1_List_Num
        global Label1_List_Num
        global LabelFrame1_List_Num
        global Listbox1_List_Num
        global Menu1_List_Num
        global Message1_List_Num
        global PanedWindow1_List_Num
        global Radiobutton1_List_Num
        global Scale1_List_Num_X
        global Scale1_List_Num_Y
        global Spinbox1_List_Num
        global Text1_List_Num

        # 标注注释
        global tap
        global ck_name
        if ck_name != "":
            str_code = tap + tap + "# Control Define" + "\n\n"
            self.Text_1.insert(END, str_code)

        # Menu
        if zi_menu1_sum != 0:
            str_code = tap + tap + "# Menu Define" + "\n"
            self.Text_1.insert(END, str_code)

            menu_str = Menu_Str()
            str_Menu = menu_str.Menu_Str()
            self.Text_1.insert(END, str_Menu)

        if ck_name != "":
            str_code = tap + tap + "# Other Control Define" + "\n\n"
            self.Text_1.insert(END, str_code)

        # for 循环逐个判断
        for i in range(1, button1_i + 1, 1):
            if i not in Button1_List_Num:
                KJ = 'Button' + str(i)
                # Record_Code(self, BuJian, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
                dictionary = Dictionary()
                dictionary.Record_Code(Button1[KJ], Button1, 'Button', 'button', i)

                name_Code = 'button' + '_Code' + str(i)
                str_code = Button1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, canvas1_i + 1, 1):
            if i not in Canvas1_List_Num:
                KJ = 'Canvas' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Canvas1[KJ], Canvas1, 'Canvas', 'canvas', i)

                name_Code = 'canvas' + '_Code' + str(i)
                str_code = Canvas1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, checkbutton1_i + 1, 1):
            if i not in Checkbutton1_List_Num:
                KJ = 'Checkbutton' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Checkbutton1[KJ], Checkbutton1, 'Checkbutton', 'checkbutton', i)

                name_Code = 'checkbutton' + '_Code' + str(i)
                str_code = Checkbutton1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, combobox1_i + 1, 1):
            if i not in Combobox1_List_Num:
                KJ = 'Combobox' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Combobox1[KJ], Combobox1, 'ttk.Combobox', 'combobox', i)

                name_Code = 'combobox' + '_Code' + str(i)
                str_code = Combobox1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, entry1_i + 1, 1):
            if i not in Entry1_List_Num:
                KJ = 'Entry' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Entry1[KJ], Entry1, 'Entry', 'entry', i)

                name_Code = 'entry' + '_Code' + str(i)
                str_code = Entry1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, frame1_i + 1, 1):
            if i not in Frame1_List_Num:
                KJ = 'Frame' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Frame1[KJ], Frame1, 'Frame', 'frame', i)

                name_Code = 'frame' + '_Code' + str(i)
                str_code = Frame1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, label1_i + 1, 1):
            if i not in Label1_List_Num:
                KJ = 'Label' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Label1[KJ], Label1, 'Label', 'label', i)

                name_Code = 'label' + '_Code' + str(i)
                str_code = Label1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, labelFrame1_i + 1, 1):
            if i not in LabelFrame1_List_Num:
                KJ = 'LabelFrame' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(LabelFrame1[KJ], LabelFrame1, 'LabelFrame', 'labelFrame', i)

                name_Code = 'labelFrame' + '_Code' + str(i)
                str_code = LabelFrame1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, listbox1_i + 1, 1):
            if i not in Listbox1_List_Num:
                KJ = 'Listbox' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Listbox1[KJ], Listbox1, 'Listbox', 'listbox', i)

                name_Code = 'listbox' + '_Code' + str(i)
                str_code = Listbox1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, message1_i + 1, 1):
            if i not in Message1_List_Num:
                KJ = 'Message' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Message1[KJ], Message1, 'tk.Message', 'message', i)

                name_Code = 'message' + '_Code' + str(i)
                str_code = Message1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, panedWindow1_i + 1, 1):
            if i not in PanedWindow1_List_Num:
                KJ = 'PanedWindow' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(PanedWindow1[KJ], PanedWindow1, 'PanedWindow', 'panedWindow', i)

                name_Code = 'panedWindow' + '_Code' + str(i)
                str_code = PanedWindow1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, radiobutton1_i + 1, 1):
            if i not in Radiobutton1_List_Num:
                KJ = 'Radiobutton' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Radiobutton1[KJ], Radiobutton1, 'Radiobutton', 'radiobutton', i)

                name_Code = 'radiobutton' + '_Code' + str(i)
                str_code = Radiobutton1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, scale1_x_i + 1, 1):
            if i not in Scale1_List_Num_X:
                KJ = 'Scale_X' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Scale1_X[KJ], Scale1_X, 'Scale_X', 'scale_x', i)

                name_Code = 'scale_x' + '_Code' + str(i)
                str_code = Scale1_X[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, scale1_y_i + 1, 1):
            if i not in Scale1_List_Num_Y:
                KJ = 'Scale_Y' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Scale1_Y[KJ], Scale1_Y, 'Scale_Y', 'scale_y', i)

                name_Code = 'scale_y' + '_Code' + str(i)
                str_code = Scale1_Y[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, spinbox1_i + 1, 1):
            if i not in Spinbox1_List_Num:
                KJ = 'Spinbox' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Spinbox1[KJ], Spinbox1, 'Spinbox', 'spinbox', i)

                name_Code = 'spinbox' + '_Code' + str(i)
                str_code = Spinbox1[name_Code]
                self.Text_1.insert(END, str_code)

        for i in range(1, text1_i + 1, 1):
            if i not in Text1_List_Num:
                KJ = 'Text' + str(i)
                dictionary = Dictionary()
                dictionary.Record_Code(Text1[KJ], Text1, 'Text', 'text', i)

                name_Code = 'text' + '_Code' + str(i)
                str_code = Text1[name_Code]
                self.Text_1.insert(END, str_code)

        if ck_name != "":
            event_code = tap + tap + "# Event Define" + "\n\n"
            self.Text_1.insert(END, event_code)

        # def Judge_If_Delete(self, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
        sj_chu_li = SJ_ChuLi()
        sj_chu_li.SJ_Bian_Yi(SJ_button_press_1, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_button_release_1, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_button_press_right_1, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_button_press_left_2, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_button_press_right_2, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_button_press_middle_1, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_button_press_middle_2, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_button_press_left_move, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_cursor_enter, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_cursor_leave, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_get_key_focus, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_lose_key_focus, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_press_a_key, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_press_enter_key, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_when_control_change, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_press_space_key, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_shift_mouseWheel, self.Text_1)
        sj_chu_li.SJ_Bian_Yi(SJ_press_combinatorial_key, self.Text_1)

        # 结尾
        global Str_BianYi_End
        if ck_name != "":
            self.Text_1.insert(END, Str_BianYi_End)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # 录入字典
    def LuRu_Dict(self):
        global KJBZ
        global DangQian_KJ_name
        global Distance
        global bar_W
        global bar_menu_W
        global zi_menu1_sum

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        if zi_menu1_sum == 0:
            Distance = bar_W
        else:
            Distance = bar_W + bar_menu_W

        self.Y0 = self.Y0 - Distance
        self.Y1 = self.Y1 - Distance
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        if KJBZ == 'button1':
            global Button1
            global button1_i

            button1_i = button1_i + 1

            DangQian_KJ_name = 'Button ' + str(button1_i)
            self.it_Button.config(text=DangQian_KJ_name)
            BuJian_NO_i = button1_i

            # Record_Dict(self, BuJian, BuJian_Lei, BuJian_NO_i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie,
            #             self_X0, self_Y0, self_X1, self_Y1):
            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Button, Button1, BuJian_NO_i, 'Button', 'button',
                        self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'canvas1':
            global Canvas1
            global canvas1_i

            canvas1_i = canvas1_i + 1
            DangQian_KJ_name = 'Canvas ' + str(canvas1_i)
            BuJian_NO_i = canvas1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Canva, Canvas1, BuJian_NO_i, 'Canvas', 'canvas',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'checkbutton1':
            global Checkbutton1
            global checkbutton1_i

            checkbutton1_i = checkbutton1_i + 1

            DangQian_KJ_name = 'Checkbutton ' + str(checkbutton1_i)
            self.it_Checkbutton.config(text=DangQian_KJ_name)
            BuJian_NO_i = checkbutton1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Checkbutton, Checkbutton1, BuJian_NO_i, 'Checkbutton', 'checkbutton',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'combobox1':
            global Combobox1
            global combobox1_i

            combobox1_i = combobox1_i + 1

            DangQian_KJ_name = 'Combobox ' + str(combobox1_i )

            self.it_Combobox["values"] = ('Combobox', DangQian_KJ_name)
            self.it_Combobox.current(1)
            BuJian_NO_i = combobox1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Combobox, Combobox1, BuJian_NO_i, 'Combobox', 'combobox',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'entry1':
            global Entry1
            global entry1_i

            entry1_i = entry1_i + 1

            DangQian_KJ_name = 'Entry ' + str(entry1_i)
            # self.it_Entry.config(text=DangQian_KJ_name)
            self.it_Entry.insert(1, DangQian_KJ_name)
            BuJian_NO_i = entry1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Entry, Entry1, BuJian_NO_i, 'Entry', 'entry',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'frame1':
            global Frame1
            global frame1_i

            frame1_i = frame1_i + 1

            DangQian_KJ_name = 'Frame ' + str(frame1_i + 1)
            BuJian_NO_i = frame1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Frame, Frame1, BuJian_NO_i, 'Frame', 'frame',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'label1':
            global Label1
            global label1_i

            label1_i = label1_i + 1

            DangQian_KJ_name = 'Label ' + str(label1_i + 1)
            self.it_Label.config(text=DangQian_KJ_name)
            BuJian_NO_i = label1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Label, Label1, BuJian_NO_i, 'Label', 'label',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'labelFrame1':
            global LabelFrame1
            global labelFrame1_i

            labelFrame1_i = labelFrame1_i + 1

            DangQian_KJ_name = 'LabelFrame ' + str(labelFrame1_i + 1)
            self.it_LabelFrame.config(text=DangQian_KJ_name)
            BuJian_NO_i = labelFrame1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_LabelFrame, LabelFrame1, BuJian_NO_i, 'LabelFrame', 'labelFrame',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'listbox1':
            global Listbox1
            global listbox1_i

            listbox1_i = listbox1_i + 1
            DangQian_KJ_name = 'Listbox ' + str(listbox1_i + 1)
            BuJian_NO_i = listbox1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Listbox, Listbox1, BuJian_NO_i, 'Listbox', 'listbox',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'menu1':
            global Menu1
            global menu1_i

            menu1_i = menu1_i + 1

            DangQian_KJ_name = 'Menu ' + str(menu1_i + 1)

       # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'message1':
            global Message1
            global message1_i

            message1_i = message1_i + 1

            DangQian_KJ_name = 'Message ' + str(message1_i)
            self.it_Message.config(text=DangQian_KJ_name)
            BuJian_NO_i = message1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Message, Message1, BuJian_NO_i, 'Message', 'message',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'panedWindow1':
            global PanedWindow1
            global panedWindow1_i

            panedWindow1_i = panedWindow1_i + 1

            DangQian_KJ_name = 'PanedWindow ' + str(panedWindow1_i + 1)
            BuJian_NO_i = panedWindow1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_PanedWindow, PanedWindow1, BuJian_NO_i, 'PanedWindow', 'panedWindow',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'radiobutton1':
            global Radiobutton1
            global radiobutton1_i

            radiobutton1_i = radiobutton1_i + 1

            DangQian_KJ_name = 'Radiobutton ' + str(radiobutton1_i)
            self.it_Radiobutton.config(text=DangQian_KJ_name)
            BuJian_NO_i = radiobutton1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Radiobutton, Radiobutton1, BuJian_NO_i, 'Radiobutton', 'radiobutton',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'scale1_x':
            global Scale1_X
            global scale1_x_i

            scale1_x_i = scale1_x_i + 1

            DangQian_KJ_name = 'Scale_X ' + str(scale1_x_i + 1)
            BuJian_NO_i = scale1_x_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Scale_X, Scale1_X, BuJian_NO_i, 'Scale_X', 'scale_x',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'scale1_y':
            global Scale1_Y
            global scale1_y_i

            scale1_y_i = scale1_y_i + 1

            DangQian_KJ_name = 'Scale_Y ' + str(scale1_y_i + 1)
            BuJian_NO_i = scale1_y_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Scale_Y, Scale1_Y, BuJian_NO_i, 'Scale_Y', 'scale_y',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'scrollbar1_x':
            global Scrollbar1_X
            global scrollbar1_x_i

            scrollbar1_i = scrollbar1_x_i + 1

            DangQian_KJ_name = 'Scrollbar_X ' + str(scrollbar1_i + 1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'scrollbar1_y':
            global Scrollbar1_Y
            global scrollbar1_y_i

            scrollbar1_i = scrollbar1_y_i + 1

            DangQian_KJ_name = 'Scrollbar_Y ' + str(scrollbar1_i + 1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'text1':
            global Text1
            global text1_i

            text1_i = text1_i + 1

            DangQian_KJ_name = 'Text ' + str(text1_i + 1)
            BuJian_NO_i = text1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Text, Text1, BuJian_NO_i, 'Text', 'text',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'spinbox1':
            global Spinbox1
            global spinbox1_i

            spinbox1_i = spinbox1_i + 1

            DangQian_KJ_name = 'Spinbox ' + str(spinbox1_i + 1)
            BuJian_NO_i = spinbox1_i

            dictionary = Dictionary()
            dictionary.Record_Dict(self.it_Spinbox, Spinbox1, BuJian_NO_i, 'Spinbox', 'spinbox',
                                   self.X0, self.Y0, self.X1, self.Y1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'toplevel1':
            global Toplevel1
            global toplevel1_i

            toplevel1_i = toplevel1_i + 1
            DangQian_KJ_name = 'Toplevel ' + str(toplevel1_i + 1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        elif KJBZ == 'tkMessageBox1':
            global tkMessageBox1
            global tkMessageBox1_i

            tkMessageBox1_i = tkMessageBox1_i + 1
            DangQian_KJ_name = 'tkMessageBox1_i ' + str(tkMessageBox1_i + 1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 对话框类



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 字符串处理类
class Str_ChuLi:

    def FenDuan(self, str1):
        self.str = str(str1)
        L = len(self.str)
        for i in range(1, L, 1):
            if self.str[i] == ' ':
                self.falg_FenDuan = True
                self.a = self.str[0:i]
                self.ab = self.str[i:L]
                break
            else:
                self.falg_FenDuan = False

        if self.falg_FenDuan == True:
            L = len(self.ab)
            for i in range(1, L + 1, 1):
                if self.ab[i] != ' ':
                    self.b = self.ab[i:L]
                    break
            print(self.a)
            print(self.b)
            return (self.a, self.b)
        else:
            return (self.str, '')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 颜色选择框类
class Choose_Color:
    def Color_Choose(self):
        col = tkinter.colorchooser.askcolor(color='green', title="Choose the Colour")
        print(col)
        return col

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 获取文件名类
class Get_File_Name_GIF:
    def Get_Name(self):
        file_name = tkinter.filedialog.askopenfilename(filetypes=[("*.gif", "gif")])
        return file_name

class Get_File_Name_XBM:
    def Get_Name(self):
        file_name = tkinter.filedialog.askopenfilename(filetypes=[("*.xbm", "xbm")])
        return file_name

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Bitmap 图像处理类
class BitMap:
    def BitMap_ChuLi(self, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):
        global combt_bitmap
        name_bitmap = str(BuJian_LeiXing_XiaoXie) + '_bitmap' + str(BuJian_NO_i)
        list = (
        'error', 'gray75', 'gray50', 'gray25', 'gray12', 'hourglass', 'info', 'questhead', 'question', 'warning')
        Zhi = combt_bitmap
        flag_bitmap_list = FALSE
        for i in list:
            if i == Zhi:
                flag_bitmap_list = TRUE
                BuJian.config(bitmap=Zhi)

        if (flag_bitmap_list == FALSE) and (Zhi != ''):
            bitmap_photo = tkinter.BitmapImage(file=Zhi)
            BuJian.config(bitmap=bitmap_photo)

        BuJian_Lei[name_bitmap] = "" + Zhi + ""

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Image 图像处理类
class Image_ChuLi:
    def Image_ChuLi(self, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):
        global ent_image
        name_image = str(BuJian_LeiXing_XiaoXie) + '_image' + str(BuJian_NO_i)
        Zhi = ent_image
        if Zhi != '':
            BuJian_Lei[name_image] = Zhi
            image_photo = PhotoImage(file=Zhi)
            BuJian.config(image=image_photo)
        elif Zhi == '':
            BuJian.config(image='')


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 设计更新类
class Design_New:
    def BuJian_New(self, BuJian_LeiXing_DaXie, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei):
        global lab_ControlType
        global ent_ControlName
        global ent_X0
        global ent_Y0
        global ent_width
        global ent_height
        global ent_length
        global ent_fontSize
        global combt_fontType
        global combt_foreground
        global combt_background
        global combt_anchor
        global combt_justify
        global ent_text
        global combt_state
        global combt_relief
        global combt_highlightcolor
        global combt_highlightbackground
        global combt_bitmap
        global ent_image
        global combt_padx
        global combt_pady
        global combt_takefocus
        global combt_cursor
        global ent_container
        global ent_command

        # if a[1] == 'Button':
        BuJian_NO_i = BuJian_NO_i

        lab_ControlType = BuJian_LeiXing_DaXie

        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        global Distance
        global bar_W
        global bar_menu_W

        if zi_menu1_sum == 0:
            Distance = bar_W
        else:
            Distance = bar_W + bar_menu_W
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        # 字典更新及设计窗口更新

        # name = "XuanZhong" + str(XuanZhong_sum)
        # XuanZhong[name] = (Button1[KJ], 'Button', 'button', Num_i, Button1)

        judge = Judge_Property()

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 通用属性 container, name, cusor, width, background, coords

        # container
        name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        Zhi = ent_container
        BuJian_Lei[name_container] = Zhi

        # name
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        BuJian_Lei[KJ_name] = ent_ControlName
        judge_Property = Judge_Property()
        if (judge_Property.Is_In_text(BuJian_LeiXing_DaXie) == TRUE) and ent_text == '':
            BuJian_Lei[KJ].config(text=ent_ControlName)

        # coords and width
        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)
        Zhi = (ent_X0, ent_Y0, ent_width, ent_height, BuJian_NO_i)
        BuJian_Lei[name_coords] = Zhi

        BuJian_Lei[KJ].place(x=ent_X0, y=ent_Y0 + Distance)
        BuJian_Lei[KJ].config(width=int(ent_width))

        # cursor
        name_cursor = str(BuJian_LeiXing_XiaoXie) + '_cursor' + str(BuJian_NO_i)
        Zhi = combt_cursor
        BuJian_Lei[name_cursor] = Zhi
        BuJian_Lei[KJ].config(cursor=Zhi)

        # background
        name_background = str(BuJian_LeiXing_XiaoXie) + '_background' + str(BuJian_NO_i)
        Zhi = combt_background
        BuJian_Lei[name_background] = Zhi
        BuJian_Lei[KJ].config(background=Zhi)


        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 部分属性

        # height
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            name_height = str(BuJian_LeiXing_XiaoXie) + '_height' + str(BuJian_NO_i)
            Zhi = int(ent_height)
            BuJian_Lei[name_height] = Zhi
            BuJian_Lei[KJ].config(height=Zhi)

        # length
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            name_length = str(BuJian_LeiXing_XiaoXie) + '_length' + str(BuJian_NO_i)
            Zhi = int(ent_length)
            BuJian_Lei[name_length] = Zhi
            BuJian_Lei[KJ].config(length=Zhi)

        # font
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            name_font = str(BuJian_LeiXing_XiaoXie) + '_font' + str(BuJian_NO_i)
            Zhi = (str(combt_fontType), ent_fontSize)
            BuJian_Lei[name_font] = Zhi
            BuJian_Lei[KJ].config(font=Zhi)

        # foreground
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = str(BuJian_LeiXing_XiaoXie) + '_foreground' + str(BuJian_NO_i)
            Zhi = combt_foreground
            BuJian_Lei[name_foreground] = Zhi
            BuJian_Lei[KJ].config(foreground=Zhi)

        # anchor
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            name_anchor = str(BuJian_LeiXing_XiaoXie) + '_anchor' + str(BuJian_NO_i)
            Zhi = combt_anchor
            BuJian_Lei[name_anchor] = Zhi
            BuJian_Lei[KJ].config(anchor=Zhi)

        # justify
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            name_justify = str(BuJian_LeiXing_XiaoXie) + '_justify' + str(BuJian_NO_i)
            Zhi = combt_justify
            BuJian_Lei[name_justify] = Zhi
            BuJian_Lei[KJ].config(justify=Zhi)

        # state
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            name_state = str(BuJian_LeiXing_XiaoXie) + '_state' + str(BuJian_NO_i)
            Zhi = combt_state
            BuJian_Lei[name_state] = Zhi
            BuJian_Lei[KJ].config(state=Zhi)

        # relief
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            name_relief = str(BuJian_LeiXing_XiaoXie) + '_relief' + str(BuJian_NO_i)
            Zhi = combt_relief
            BuJian_Lei[name_relief] = Zhi
            BuJian_Lei[KJ].config(relief=Zhi)


        # highlightcolor and highlightbackground
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            name_highlightcolor = str(BuJian_LeiXing_XiaoXie) + '_highlightcolor' + str(BuJian_NO_i)
            Zhi = combt_highlightcolor
            BuJian_Lei[name_highlightcolor] = Zhi
            BuJian_Lei[KJ].config(highlightcolor=Zhi)

            name_highlightbackground = str(BuJian_LeiXing_XiaoXie) + '_highlightbackground' + str(BuJian_NO_i)
            Zhi = combt_highlightbackground
            BuJian_Lei[name_highlightbackground] = Zhi
            BuJian_Lei[KJ].config(highlightbackground=Zhi)


        # bitmap
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            a = BitMap()
            a.BitMap_ChuLi(BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian_Lei[KJ])
            # BitMap_ChuLi(BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):

        # image
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            a = Image_ChuLi()
            a.Image_ChuLi(BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian_Lei[KJ])
            # Image_ChuLi(self, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei, BuJian):


        # padx and pady
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            name_padx = str(BuJian_LeiXing_XiaoXie) + '_padx' + str(BuJian_NO_i)
            Zhi = combt_padx
            BuJian_Lei[name_padx] = Zhi
            BuJian_Lei[KJ].config(padx=Zhi)

            name_pady = str(BuJian_LeiXing_XiaoXie) + '_pady' + str(BuJian_NO_i)
            Zhi = combt_pady
            BuJian_Lei[name_pady] = Zhi
            BuJian_Lei[KJ].config(pady=Zhi)


        # text
        if (judge.Is_In_takefocus(BuJian_LeiXing_DaXie)) == TRUE and (ent_text != ''):
            name_text = str(BuJian_LeiXing_XiaoXie) + '_text' + str(BuJian_NO_i)
            Zhi = ent_text
            BuJian_Lei[name_text] = Zhi
            BuJian_Lei[KJ].config(text=Zhi)

        # takefocus
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            name_takefocus = str(BuJian_LeiXing_XiaoXie) + '_takefocus' + str(BuJian_NO_i)
            Zhi = combt_takefocus
            BuJian_Lei[name_takefocus] = Zhi
            BuJian_Lei[KJ].config(takefocus=Zhi)

        # command
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            name_command = str(BuJian_LeiXing_XiaoXie) + '_command' + str(BuJian_NO_i)
            Zhi = ent_command
            BuJian_Lei[name_command] = Zhi
            BuJian_Lei[KJ].config(command=Zhi)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 判断属性类
# 每个控件都有的属性 container, cusor, width, background
class Judge_Property:
    def Is_In_anchor(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Label', 'tk.Message', 'Radiobutton')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_font(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'LabelFrame', 'Listbox', 'tk.Message', 'Radiobutton',
                'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_bitmap(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Label', 'Radiobutton')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_justify(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'Listbox', 'tk.Message', 'Radiobutton', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_image(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Label', 'Radiobutton')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE



    def Is_In_height(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                'PanedWindow', 'Radiobutton', 'Text')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_length(self, BuJian_LeiXing_DaXie):
        list = ('Scale_X', 'Scale_Y')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_foreground(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'LabelFrame', 'Listbox', 'tk.Message',
                'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')

        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_padx_or_pady(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Frame', 'Label', 'LabelFrame', 'tk.Message', 'Radiobutton', 'Text')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_relief(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                'tk.Message', 'PanedWindow', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_text(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Entry', 'Label', 'LabelFrame', 'tk.Message', 'Radiobutton', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_state(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Label', 'Listbox',
                'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_takefocus(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                'tk.Message', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_highlightcolor_or_highlightbackground(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox', 'tk.Message',
                'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE


    def Is_In_command(self, BuJian_LeiXing_DaXie):
        list = ('Button', 'Checkbutton', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Spinbox')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE

    def Is_In_orient(self, BuJian_LeiXing_DaXie):
        list = ('Scale_X', 'Scale_Y')
        if BuJian_LeiXing_DaXie in list:
            return TRUE
        else:
            return FALSE

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# BuJian_New(self, BuJian_LeiXing_DaXie, BuJian_NO_i, BuJian_LeiXing_XiaoXie, BuJian_Lei)
# 颜色恢复处理类
class Color_Handle:
    # XuanZhong[name] = (Button1[KJ], 'Button', 'button', Num_i, Button1)
    def Color_Restore(self, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, Num_i):
        num_i = Num_i
        KJ = BuJian_LeiXing_DaXie + str(Num_i)

        if self.Judge_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = BuJian_LeiXing_XiaoXie + '_foreground' + str(num_i)
            BuJian_Lei[KJ].config(foreground=BuJian_Lei[name_foreground])

        if self.Judge_background(BuJian_LeiXing_DaXie) == TRUE:
            name_background = BuJian_LeiXing_XiaoXie + '_background' + str(num_i)
            BuJian_Lei[KJ].config(background=BuJian_Lei[name_background])

        if self.Judge_state(BuJian_LeiXing_DaXie) == TRUE:
            BuJian_Lei[KJ].configure(state='normal')

    # 判断是否具有 foreground or background or state
    def Judge_foreground(self, BuJian_LeiXing_DaXie):
        foreground_list = ('Button', 'Checkbutton', 'Entry', 'Label', 'LabelFrame', 'Listbox', 'tk.Message',
                           'Radiobutton', 'Scale_X', 'Scale_Y', 'Spinbox', 'Text')
        if BuJian_LeiXing_DaXie in foreground_list:
            return TRUE
        else:
            return FALSE

    def Judge_background(self, BuJian_LeiXing_DaXie):
        background_list = ('Button', 'Canvas', 'Checkbutton', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox',
                           'tk.Message', 'PanedWindow', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Spinbox', 'Text')
        if BuJian_LeiXing_DaXie in background_list:
            return TRUE
        else:
            return FALSE

    def Judge_state(self, BuJian_LeiXing_DaXie):   # 注意此处为颜色恢复
        state_list = ('Combobox')
        if BuJian_LeiXing_DaXie in state_list:
            return TRUE
        else:
            return FALSE

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 完成后，选定处理类
class XuanDing:
    def BuJian_ChuLi(self, i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_Lei,
                     XuanKuang_X0, XuanKuang_Y0, XuanKuang_X1, XuanKuang_Y1):

        global XuanZhong
        global XuanZhong_sum

        name = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(i)
        a = BuJian_Lei[name]
        xx0 = a[0]
        yy0 = a[1]
        xx1 = a[2]
        yy1 = a[3]
        Num_i = a[4]

        if ((XuanKuang_X0 <= xx0) and (XuanKuang_Y0 <= yy0) and (XuanKuang_X1 >= xx1) and (XuanKuang_Y1 >= yy1)) \
                and (XuanKuang_X1 != XuanKuang_X0) and (XuanKuang_Y1 != XuanKuang_Y0):
            KJ = str(BuJian_LeiXing_DaXie) + str(i)

            color_handle = Color_Handle()

            if color_handle.Judge_foreground(BuJian_LeiXing_DaXie) == TRUE:
                BuJian_Lei[KJ].config(foreground=foreground_XiangMu_XuanDing)
            if color_handle.Judge_background(BuJian_LeiXing_DaXie) == TRUE:
                BuJian_Lei[KJ].config(background=background_XiangMu_XuanDing)
            if color_handle.Judge_state(BuJian_LeiXing_DaXie) == TRUE:
                BuJian_Lei[KJ].config(state='disabled')

            XuanZhong_sum = XuanZhong_sum + 1
            name = "XuanZhong" + str(XuanZhong_sum)
            XuanZhong[name] = (BuJian_Lei[KJ], str(BuJian_LeiXing_DaXie), str(BuJian_LeiXing_XiaoXie), Num_i, BuJian_Lei)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Design 部件类
class Design_BuJian:
    def Design_bujian(self, XuanZhong_Object):
        global lab_ControlType
        global ent_ControlName
        global ent_X0
        global ent_Y0
        global ent_width
        global ent_height
        global ent_length
        global ent_fontSize
        global combt_fontType
        global combt_foreground
        global combt_background
        global combt_anchor
        global combt_justify
        global ent_text
        global combt_state
        global combt_relief
        global combt_highlightcolor
        global combt_highlightbackground
        global combt_bitmap
        global ent_image
        global combt_padx
        global combt_pady
        global combt_takefocus
        global combt_cursor
        global ent_container
        global ent_command

        a = XuanZhong_Object
        lab_ControlType = a[1]
        BuJian_LeiXing_DaXie = a[1]
        BuJian_LeiXing_XiaoXie = a[2]
        BuJian_NO_i = a[3]
        BuJian_Lei = a[4]

        # 每个控件都有的属性 name, coords, container, cusor, width, background
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 共有属性修改

        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        ent_ControlName = BuJian_Lei[KJ_name]

        name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        ent_container = BuJian_Lei[name_container]

        name_cursor = str(BuJian_LeiXing_XiaoXie) + '_cursor' + str(BuJian_NO_i)
        combt_cursor = BuJian_Lei[name_cursor]

        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)
        a = BuJian_Lei[name_coords]
        ent_X0 = a[0]
        ent_Y0 = a[1]

        name_width = str(BuJian_LeiXing_XiaoXie) + '_width' + str(BuJian_NO_i)
        ent_width = BuJian_Lei[name_width]

        name_background = str(BuJian_LeiXing_XiaoXie) + '_background' + str(BuJian_NO_i)
        combt_background = BuJian_Lei[name_background]

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 部分属性
        judge = Judge_Property()

        # height
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            name_height = str(BuJian_LeiXing_XiaoXie) + '_height' + str(BuJian_NO_i)
            ent_height = BuJian_Lei[name_height]

        # length
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            name_length = str(BuJian_LeiXing_XiaoXie) + '_length' + str(BuJian_NO_i)
            ent_length = BuJian_Lei[name_length]

        # font
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            name_font = str(BuJian_LeiXing_XiaoXie) + '_font' + str(BuJian_NO_i)
            font = BuJian_Lei[name_font]
            combt_fontType = font[0]
            ent_fontSize = font[1]

        # foreground
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = str(BuJian_LeiXing_XiaoXie) + '_foreground' + str(BuJian_NO_i)
            combt_foreground = BuJian_Lei[name_foreground]

        # anchor
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            name_anchor = str(BuJian_LeiXing_XiaoXie) + '_anchor' + str(BuJian_NO_i)
            combt_anchor = BuJian_Lei[name_anchor]

        # justify
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            name_justify = str(BuJian_LeiXing_XiaoXie) + '_justify' + str(BuJian_NO_i)
            combt_justify = BuJian_Lei[name_justify]

        # state
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            name_state = str(BuJian_LeiXing_XiaoXie) + '_state' + str(BuJian_NO_i)
            combt_state = BuJian_Lei[name_state]

        # relief
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            name_relief = str(BuJian_LeiXing_XiaoXie) + '_relief' + str(BuJian_NO_i)
            combt_relief = BuJian_Lei[name_relief]

        # highlightcolor and highlightbackground
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            name_highlightcolor = str(BuJian_LeiXing_XiaoXie) + '_highlightcolor' + str(BuJian_NO_i)
            combt_highlightcolor = BuJian_Lei[name_highlightcolor]

            name_highlightbackground = str(BuJian_LeiXing_XiaoXie) + '_highlightbackground' + str(BuJian_NO_i)
            combt_highlightbackground = BuJian_Lei[name_highlightbackground]

        # bitmap
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            name_bitmap = str(BuJian_LeiXing_XiaoXie) + '_bitmap' + str(BuJian_NO_i)
            combt_bitmap = BuJian_Lei[name_bitmap]

        # image
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            name_image = str(BuJian_LeiXing_XiaoXie) + '_image' + str(BuJian_NO_i)
            ent_image = BuJian_Lei[name_image]

        # padx and pady
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            name_padx = str(BuJian_LeiXing_XiaoXie) + '_padx' + str(BuJian_NO_i)
            combt_padx = BuJian_Lei[name_padx]

            name_pady = str(BuJian_LeiXing_XiaoXie) + '_pady' + str(BuJian_NO_i)
            combt_pady = BuJian_Lei[name_pady]

        # takefocus
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            name_takefocus = str(BuJian_LeiXing_XiaoXie) + '_takefocus' + str(BuJian_NO_i)
            combt_takefocus = BuJian_Lei[name_takefocus]

        # command
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            name_command = str(BuJian_LeiXing_XiaoXie) + '_command' + str(BuJian_NO_i)
            ent_command = BuJian_Lei[name_command]


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Delete 部件类
class Delete_BuJian:
    def Delete(self, XuanZhong_Object):
        # 记录各个部件类型删除的成员的 列表
        global Button1_List_Num
        global Canvas1_List_Num
        global Checkbutton1_List_Num
        global Combobox1_List_Num
        global Entry1_List_Num
        global Frame1_List_Num
        global Label1_List_Num
        global LabelFrame1_List_Num
        global Listbox1_List_Num
        global Menu1_List_Num
        global Message1_List_Num
        global PanedWindow1_List_Num
        global Radiobutton1_List_Num
        global Scale1_List_Num_X
        global Scale1_List_Num_Y
        global Spinbox1_List_Num
        global Text1_List_Num

        a = XuanZhong_Object
        BuJian_LeiXing_DaXie = a[1]
        BuJian_NO_i = a[3]
        BuJian_Lei = a[4]

        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)
        BuJian_Lei[KJ].destroy()

        if BuJian_LeiXing_DaXie == 'Button':
            Button1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Canvas':
            Canvas1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Checkbutton':
            Checkbutton1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Combobox':
            Combobox1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Entry':
            Entry1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Frame':
            Frame1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Label':
            Label1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'LabelFrame':
            LabelFrame1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Listbox':
            Listbox1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Message':
            Message1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'PanedWindow':
            PanedWindow1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'PanedWindow':
            PanedWindow1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Radiobutton':
            Radiobutton1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Scale_X':
            Scale1_List_Num_X.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Scale_Y':
            Scale1_List_Num_Y.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'PanedWindow':
            PanedWindow1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Spinbox':
            Spinbox1_List_Num.append(BuJian_NO_i)

        elif BuJian_LeiXing_DaXie == 'Text':
            Text1_List_Num.append(BuJian_NO_i)

 # ('Button', 'Canvas', 'Checkbutton', 'Combobox', 'Entry', 'Frame', 'Label', 'LabelFrame', 'Listbox', 'Message', 'PanedWindow', 'Radiobutton', 'Scale_X', 'Scale_Y', 'Text', 'Spinbox')


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 录入字典类
class Dictionary:
    def Record_Dict(self, BuJian, BuJian_Lei, BuJian_NO_i, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie,
                    self_X0, self_Y0, self_X1, self_Y1):
        global DangQian_KJ_name
        X0 = self_X0
        Y0 = self_Y0
        X1 = self_X1
        Y1 = self_Y1

        DangQian_KJ_name = str(BuJian_LeiXing_DaXie) + ' ' + str(BuJian_NO_i)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 将控件录入字典
        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        BuJian_Lei[KJ] = BuJian
        BuJian_Lei[KJ_name] = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 具体参数录入
        # 通用属性
        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)
        Zhi = (X0, Y0, X1, Y1, BuJian_NO_i)
        BuJian_Lei[name_coords] = Zhi

        name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        Zhi = 'root'
        BuJian_Lei[name_container] = Zhi

        name_cursor = str(BuJian_LeiXing_XiaoXie) + '_cursor' + str(BuJian_NO_i)
        Zhi = BuJian.cget('cursor')
        BuJian_Lei[name_cursor] = Zhi

        name_width = str(BuJian_LeiXing_XiaoXie) + '_width' + str(BuJian_NO_i)
        Zhi = BuJian.cget('width')
        BuJian_Lei[name_width] = Zhi

        name_background = str(BuJian_LeiXing_XiaoXie) + '_background' + str(BuJian_NO_i)
        Zhi = BuJian.cget('background')
        BuJian_Lei[name_background] = Zhi

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 部分属性
        judge = Judge_Property()

        # length
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            name_length = str(BuJian_LeiXing_XiaoXie) + '_length' + str(BuJian_NO_i)
            Zhi = BuJian.cget('length')
            BuJian_Lei[name_length] = Zhi

        # height
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            name_height = str(BuJian_LeiXing_XiaoXie) + '_height' + str(BuJian_NO_i)
            Zhi = BuJian.cget('height')
            BuJian_Lei[name_height] = Zhi

        # font
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            name_font = str(BuJian_LeiXing_XiaoXie) + '_font' + str(BuJian_NO_i)
            str1 = BuJian.cget('font')
            a = Str_ChuLi()
            b = a.FenDuan(str1)
            BuJian_Lei[name_font] = b

        # foreground
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            name_foreground = str(BuJian_LeiXing_XiaoXie) + '_foreground' + str(BuJian_NO_i)
            Zhi = BuJian.cget('foreground')
            BuJian_Lei[name_foreground] = Zhi

        # anchor
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            name_anchor = str(BuJian_LeiXing_XiaoXie) + '_anchor' + str(BuJian_NO_i)
            Zhi = BuJian.cget('anchor')
            BuJian_Lei[name_anchor] = Zhi

        # justify
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            name_justify = str(BuJian_LeiXing_XiaoXie) + '_justify' + str(BuJian_NO_i)
            Zhi = BuJian.cget('justify')
            BuJian_Lei[name_justify] = Zhi

        # state
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            name_state = str(BuJian_LeiXing_XiaoXie) + '_state' + str(BuJian_NO_i)
            Zhi = BuJian.cget('state')
            BuJian_Lei[name_state] = Zhi

        # relief
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            name_relief = str(BuJian_LeiXing_XiaoXie) + '_relief' + str(BuJian_NO_i)
            Zhi = BuJian.cget('relief')
            BuJian_Lei[name_relief] = Zhi

        # highlightcolor and highlightbackground
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            name_highlightcolor = str(BuJian_LeiXing_XiaoXie) + '_highlightcolor' + str(BuJian_NO_i)
            Zhi = BuJian.cget('highlightcolor')
            BuJian_Lei[name_highlightcolor] = Zhi

            name_highlightbackground = str(BuJian_LeiXing_XiaoXie) + '_highlightbackground' + str(BuJian_NO_i)
            Zhi = BuJian.cget('highlightbackground')
            BuJian_Lei[name_highlightbackground] = Zhi

        # bitmap
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            name_bitmap = str(BuJian_LeiXing_XiaoXie) + '_bitmap' + str(BuJian_NO_i)
            Zhi = BuJian.cget('bitmap')
            BuJian_Lei[name_bitmap] = Zhi

        # image
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            name_image = str(BuJian_LeiXing_XiaoXie) + '_image' + str(BuJian_NO_i)
            Zhi = BuJian.cget('image')
            BuJian_Lei[name_image] = Zhi

        # padx and pady
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            name_padx = str(BuJian_LeiXing_XiaoXie) + '_padx' + str(BuJian_NO_i)
            Zhi = BuJian.cget('padx')
            BuJian_Lei[name_padx] = Zhi

            name_pady = str(BuJian_LeiXing_XiaoXie) + '_pady' + str(BuJian_NO_i)
            Zhi = BuJian.cget('pady')
            BuJian_Lei[name_pady] = Zhi

        # text
        if judge.Is_In_text(BuJian_LeiXing_DaXie) == TRUE:
            name_text = str(BuJian_LeiXing_XiaoXie) + '_text' + str(BuJian_NO_i)
            Zhi = BuJian.cget('text')
            BuJian_Lei[name_text] = Zhi
            # 组件名显示
            BuJian.config(text=DangQian_KJ_name)

        # takefocus
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            name_takefocus = str(BuJian_LeiXing_XiaoXie) + '_takefocus' + str(BuJian_NO_i)
            Zhi = BuJian.cget('takefocus')
            BuJian_Lei[name_takefocus] = Zhi

        # command
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            name_command = str(BuJian_LeiXing_XiaoXie) + '_command' + str(BuJian_NO_i)
            Zhi = BuJian.cget('command')
            BuJian_Lei[name_command] = Zhi

        # orient
        if judge.Is_In_orient(BuJian_LeiXing_DaXie) == TRUE:
            name_orient = str(BuJian_LeiXing_XiaoXie) + '_orient' + str(BuJian_NO_i)
            Zhi = BuJian.cget('orient')
            BuJian_Lei[name_orient] = Zhi

        self.Record_Code(BuJian, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_NO_i)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def Record_Code(self, BuJian, BuJian_Lei, BuJian_LeiXing_DaXie, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
        # 录入代码
        judge = Judge_Property()
        KJ = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        BuJian_Lei[KJ] = BuJian

        # global ent_ControlName
        # if ent_ControlName != '':
        #     BuJian_Lei[KJ_name] = ent_ControlName
        # else:
        # BuJian_Lei[KJ_name] = str(BuJian_LeiXing_DaXie) + str(BuJian_NO_i)

        # 通用属性
        # name_container = str(BuJian_LeiXing_XiaoXie) + '_container' + str(BuJian_NO_i)
        name_coords = str(BuJian_LeiXing_XiaoXie) + '_coords' + str(BuJian_NO_i)

        if BuJian.cget('cursor') != '':
            cursor_str = str(BuJian.cget('cursor'))
            cursor_str_head = "cursor='"
            cursor_str_tail = "', "
        else:
            cursor_str = ""
            cursor_str_head = ""
            cursor_str_tail = ""

        if BuJian.cget('background') != '':
            background_str = str(BuJian.cget('background'))
            background_str_head = "background='"
            background_str_tail = "', "
        else:
            background_str = ""
            background_str_head = ""
            background_str_tail = ""

        if BuJian.cget('width') != '':
            width_str = str(BuJian.cget('width'))
            width_str_head = "width="
            width_str_tail = ", "
        else:
            width_str = ""
            width_str_head = ""
            width_str_tail = ""

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 部分属性

        # height
        height_str = ""
        height_str_head = ""
        height_str_tail = ""
        if judge.Is_In_height(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('height') != '':
                height_str = str(BuJian.cget('height'))
                height_str_head = "height="
                height_str_tail = ", "

        # length
        length_str = ""
        length_str_head = ""
        length_str_tail = ""
        if judge.Is_In_length(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('length') != '':
                length_str = str(BuJian.cget('length'))
                length_str_head = "length="
                length_str_tail = ", "

        # font
        font_str = ""
        font_str_head = ""
        font_str_tail = ""
        if judge.Is_In_font(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('font') != '':
                str2 = BuJian.cget('font')
                a = Str_ChuLi()
                b = a.FenDuan(str2)
                font_str = "('" + str(b[0]) + "', " + str(b[1]) + ")"
                font_str_head = "font="
                font_str_tail = ", "

        # foreground
        foreground_str = ""
        foreground_str_head = ""
        foreground_str_tail = ""
        if judge.Is_In_foreground(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('foreground') != '':
                foreground_str = str(BuJian.cget('foreground'))
                foreground_str_head = "foreground='"
                foreground_str_tail = "', "

        # anchor
        anchor_str = ""
        anchor_str_head = ""
        anchor_str_tail = ""
        if judge.Is_In_anchor(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('anchor') != '':
                anchor_str = str(BuJian.cget('anchor'))
                anchor_str_head = "anchor='"
                anchor_str_tail = "', "

        # justify
        justify_str = ""
        justify_str_head = ""
        justify_str_tail = ""
        if judge.Is_In_justify(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('justify') != '':
                justify_str = str(BuJian.cget('justify'))
                justify_str_head = "justify='"
                justify_str_tail = "', "

        # state
        state_str = ""
        state_str_head = ""
        state_str_tail = ""
        if judge.Is_In_state(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('state') != '':
                state_str = str(BuJian.cget('state'))
                state_str_head = "state='"
                state_str_tail = "', "

        # relief
        relief_str = ""
        relief_str_head = ""
        relief_str_tail = ""
        if judge.Is_In_relief(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('relief') != '':
                relief_str = str(BuJian.cget('relief'))
                relief_str_head = "relief='"
                relief_str_tail = "', "

        # highlightcolor and highlightbackground
        highlightcolor_str = ""
        highlightbackground_str = ""
        highlightcolor_str_head = ""
        highlightcolor_str_tail = ""
        highlightbackground_str_head = ""
        highlightbackground_str_tail = ""
        if judge.Is_In_highlightcolor_or_highlightbackground(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('highlightcolor') != '':
                highlightcolor_str = str(BuJian.cget('highlightcolor'))
                highlightcolor_str_head = "highlightcolor='"
                highlightcolor_str_tail = "', "

            if BuJian.cget('highlightbackground') != '':
                highlightbackground_str = str(BuJian.cget('highlightbackground'))
                highlightbackground_str_head = "highlightbackground='"
                highlightbackground_str_tail = "', "

        # bitmap
        bitmap_photo_str = ""
        bitmap_str_head = ""
        bitmap_str_tail = ""
        if judge.Is_In_bitmap(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('bitmap') != '':
                bitmap_str = str(BuJian.cget('bitmap'))
                bitmap_photo_str = "PhotoImage(file='" + bitmap_str + "'), "
                bitmap_str_head = "bitmap="
                bitmap_str_tail = ", "

        # image
        image_photo_str = ""
        image_str_head = ""
        image_str_tail = ""
        if judge.Is_In_image(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('image') != '':
                image_str = str(BuJian.cget('image'))
                image_photo_str = "PhotoImage(file='" + image_str + "'), "
                image_str_head = "image="
                image_str_tail = ", "

        # padx and pady
        padx_str = ""
        pady_str = ""
        padx_str_head = ""
        padx_str_tail = ""
        pady_str_head = ""
        pady_str_tail = ""
        if judge.Is_In_padx_or_pady(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('padx') != '':
                padx_str = str(BuJian.cget('padx'))
                padx_str_head = "padx="
                padx_str_tail = ", "

            if BuJian.cget('pady') != '':
                pady_str = str(BuJian.cget('pady'))
                pady_str_head = "pady="
                pady_str_tail = ", "

        # text
        text_str = ""
        text_str_head = ""
        text_str_tail = ""
        if judge.Is_In_text(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('text') != '':
                text_str = str(BuJian.cget('text'))
                text_str_head = "text='"
                text_str_tail = "', "

        # takefocus
        takefocus_str = ""
        takefocus_str_head = ""
        takefocus_str_tail = ""
        if judge.Is_In_takefocus(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('takefocus') != '':
                takefocus_str = str(BuJian.cget('takefocus'))
                takefocus_str_head = "takefocus='"
                takefocus_str_tail = "', "

        # command
        command_str = ""
        command_str_head = ""
        command_str_tail = ""
        if judge.Is_In_command(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('command') != '':
                command_str = str(BuJian.cget('command'))
                command_str_head = "command="
                command_str_tail = ""

        # orient
        orient_str = ""
        orient_str_head = ""
        orient_str_tail = ""
        if judge.Is_In_orient(BuJian_LeiXing_DaXie) == TRUE:
            if BuJian.cget('orient') != '':
                orient_str = "'" + str(BuJian.cget('orient')) + "'"
                orient_str_head = "orient="
                orient_str_tail = ""

        Control_Lei = ""
        # 判断是否 Scale
        if (BuJian_LeiXing_DaXie == "Scale_X") or (BuJian_LeiXing_DaXie == "Scale_Y"):
            Control_Lei = "Scale"
        else:
            Control_Lei = str(BuJian_LeiXing_DaXie)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 生成编辑代码
        # + BuJian_Lei[name_container] + ", " \
        Code1 = BuJian_Lei[KJ_name] + " = " + Control_Lei + "(" \
                + anchor_str_head + anchor_str + anchor_str_tail \
                + cursor_str_head + cursor_str + cursor_str_tail \
                + font_str_head + font_str + font_str_tail \
                + bitmap_str_head + bitmap_photo_str + bitmap_str_tail \
                + justify_str_head + justify_str + justify_str_tail \
                + image_str_head + image_photo_str + image_str_tail \
                + width_str_head + width_str + width_str_tail \
                + height_str_head + height_str + height_str_tail \
                + length_str_head + length_str + length_str_tail \
                + foreground_str_head + foreground_str + foreground_str_tail \
                + background_str_head + background_str + background_str_tail \
                + padx_str_head + padx_str + padx_str_tail \
                + pady_str_head + pady_str + pady_str_tail \
                + relief_str_head + relief_str + relief_str_tail \
                + text_str_head + text_str + text_str_tail \
                + state_str_head + state_str + state_str_tail \
                + takefocus_str_head + takefocus_str + takefocus_str_tail \
                + highlightcolor_str_head + highlightcolor_str + highlightcolor_str_tail \
                + highlightbackground_str_head + highlightbackground_str + highlightbackground_str_tail \
                + orient_str_head + orient_str + orient_str_tail \
                + command_str_head + command_str + command_str_tail + ")"

        ZuJianZB = BuJian_Lei[name_coords]
        Code2 = BuJian_Lei[KJ_name] + ".place(x=" + str(ZuJianZB[0]) + ", " + "y=" + str(ZuJianZB[1]) + ')'

        # 代码录入字典**********************************
        name_Code = str(BuJian_LeiXing_XiaoXie) + '_Code' + str(BuJian_NO_i)
        BuJian_Lei[name_Code] = "    " + "    " + Code1 + "\n" + "    " + "    " + Code2 + '\n\n'

        print(BuJian_Lei[name_Code])

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 紧耦合模式
# 窗口设置类
class SetCK_D(Toplevel):
    def __init__(self, Parent):
        super().__init__()
        self.title('Win Setup')
        global canva_H
        global canva_W

        self.Parent = Parent  # 显式地保留父窗口
        self.Propertys("-topmost", -1)
        self.focus_set()

        w = 800
        h = 500
        S_width = self.winfo_screenwidth()
        S_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2, (S_height - h) / 2 - 30)
        self.geometry(size)
        self.resizable(width=False, height=False)

        # 参数设置
        self.Tv_ck_width = canva_W
        self.Tv_ck_height = canva_H

        self.Font = ('Consol', '12')

        self.Set_UI()

    def Set_UI(self):
        self.JG_x = 210
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_name = Label(self, text='Interface Name', font=self.Font)
        self.Lab_ck_name.place(x=0, y=6)

        self.Tv_ck_name = StringVar()
        self.Ent_ck_name = Entry(self, textvariable=self.Tv_ck_name, font=self.Font, width=25)
        self.Ent_ck_name.place(x=self.JG_x, y=6)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_width = Label(self, text='Interface Width', font=self.Font)
        self.Lab_ck_width.place(x=0, y=6 + 40)

        self.Lab_ck_width = Label(self, text=self.Tv_ck_width, font=self.Font, width=25, bg='DeepSkyBlue')
        self.Lab_ck_width.place(x=self.JG_x, y=6 + 40)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_height = Label(self, text='Interface Height', font=self.Font)
        self.Lab_ck_height.place(x=0, y=6 + 80)

        self.Lab_ck_height = Label(self, text=self.Tv_ck_height, font=self.Font, width=25, bg='DeepSkyBlue')
        self.Lab_ck_height.place(x=self.JG_x, y=6 + 80)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_init_x = Label(self, text='Initial X coordinate', font=self.Font)
        self.Lab_ck_init_x.place(x=0, y=120)

        self.Tv_ck_init_x = StringVar()
        self.Ent_ck_init_x = Entry(self, textvariable=self.Tv_ck_init_x, font=self.Font, width=25)
        self.Ent_ck_init_x.place(x=self.JG_x, y=120)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_init_y = Label(self, text='Initial Y coordinate', font=self.Font)
        self.Lab_ck_init_y.place(x=0, y=160)

        self.Tv_ck_init_y = StringVar()
        self.Ent_ck_init_y = Entry(self, textvariable=self.Tv_ck_init_y, font=self.Font, width=25)
        self.Ent_ck_init_y.place(x=self.JG_x, y=160)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_is_width_not_change = Label(self, text='Is width not changeable', font=self.Font)
        self.Lab_ck_is_width_not_change.place(x=0, y=200)

        self.Tv_ck_is_width_not_change = IntVar()
        self.Rad_ck_is_width_not_change1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_width_not_change, value=1)
        self.Rad_ck_is_width_not_change2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_width_not_change, value=2)

        self.Rad_ck_is_width_not_change1.place(x=self.JG_x + 30, y=200)
        self.Rad_ck_is_width_not_change2.place(x=self.JG_x + 120, y=200)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_is_height_not_change = Label(self, text='Is height not changeable', font=self.Font)
        self.Lab_ck_is_height_not_change.place(x=0, y=240)

        self.Tv_ck_is_height_not_change = IntVar()
        self.Rad_ck_is_height_not_change1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_height_not_change, value=1)
        self.Rad_ck_is_height_not_change2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_height_not_change, value=2)

        self.Rad_ck_is_height_not_change1.place(x=self.JG_x + 30, y=240)
        self.Rad_ck_is_height_not_change2.place(x=self.JG_x + 120, y=240)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_is_minsize = Label(self, text='Is minsize interface', font=self.Font)
        self.Lab_ck_is_minsize.place(x=0, y=280)

        self.Lab_ck_is_minsize = Label(self, text='X', font=self.Font)
        self.Lab_ck_is_minsize.place(x=160 + 70, y=320)

        self.Tv_ck_is_minsize = IntVar()
        self.Rad_ck_is_minsize1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_minsize, value=1)
        self.Rad_ck_is_minsize2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_minsize, value=2)

        self.Rad_ck_is_minsize1.place(x=self.JG_x + 30, y=280)
        self.Rad_ck_is_minsize2.place(x=self.JG_x + 120, y=280)

        self.Tv_ck_init_minsize_w = StringVar()
        self.Ent_ck_init_minsize_w = Entry(self, textvariable=self.Tv_ck_init_minsize_w, font=self.Font, width=18)
        self.Ent_ck_init_minsize_w.place(x=6 + 70, y=320)

        self.Tv_ck_init_minsize_h = StringVar()
        self.Ent_ck_init_minsize_h = Entry(self, textvariable=self.Tv_ck_init_minsize_h, font=self.Font, width=18)
        self.Ent_ck_init_minsize_h.place(x=180 + 70, y=320)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_is_maxsize = Label(self, text='Is maxsize interface', font=self.Font)
        self.Lab_ck_is_maxsize.place(x=0, y=360)

        self.Lab_ck_is_maxsize = Label(self, text='X', font=self.Font)
        self.Lab_ck_is_maxsize.place(x=160 + 70, y=400)

        self.Tv_ck_is_maxsize = IntVar()
        self.Rad_ck_is_maxsize1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_maxsize, value=1)
        self.Rad_ck_is_maxsize2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_maxsize, value=2)

        self.Rad_ck_is_maxsize1.place(x=self.JG_x + 30, y=360)
        self.Rad_ck_is_maxsize2.place(x=self.JG_x + 120, y=360)

        self.Tv_ck_init_maxsize_w = StringVar()
        self.Ent_ck_init_maxsize_w = Entry(self, textvariable=self.Tv_ck_init_maxsize_w, font=self.Font, width=18)
        self.Ent_ck_init_maxsize_w.place(x=6 + 70, y=400)

        self.Tv_ck_init_maxsize_h = StringVar()
        self.Ent_ck_init_maxsize_h = Entry(self, textvariable=self.Tv_ck_init_maxsize_h, font=self.Font, width=18)
        self.Ent_ck_init_maxsize_h.place(x=180 + 70, y=400)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_is_toolwindow = Label(self, text='Is interface toolwindow', font=self.Font)
        self.Lab_ck_is_toolwindow.place(x=0, y=440)

        self.Tv_ck_is_toolwindow = IntVar()
        self.Rad_ck_is_toolwindow1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_toolwindow, value=1)
        self.Rad_ck_is_toolwindow2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_toolwindow, value=2)

        self.Rad_ck_is_toolwindow1.place(x=self.JG_x + 30, y=440)
        self.Rad_ck_is_toolwindow2.place(x=self.JG_x + 120, y=440)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_is_topmost = Label(self, text='Is interface topmost', font=self.Font)
        self.Lab_ck_is_topmost.place(x=self.JG_x + 230, y=6)

        self.Tv_ck_is_topmost = IntVar()
        self.Rad_ck_is_topmost1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_topmost, value=1)
        self.Rad_ck_is_topmost2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_topmost, value=2)

        self.Rad_ck_is_topmost1.place(x=self.JG_x + 430, y=6)
        self.Rad_ck_is_topmost2.place(x=self.JG_x + 520, y=6)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.Lab_ck_is_zoomed = Label(self, text='Is  initial zoomed', font=self.Font)
        self.Lab_ck_is_zoomed.place(x=self.JG_x + 230, y=6 + 40)

        self.Tv_ck_is_zoomed = IntVar()
        self.Rad_ck_is_zoomed1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_zoomed, value=1)
        self.Rad_ck_is_zoomed2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_zoomed, value=2)

        self.Rad_ck_is_zoomed1.place(x=self.JG_x + 430, y=6 + 40)
        self.Rad_ck_is_zoomed2.place(x=self.JG_x + 520, y=6 + 40)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 窗口透明度

        self.Lab_ck_is_transparency = Label(self, text='Interface transparency', font=self.Font)
        self.Lab_ck_is_transparency.place(x=self.JG_x + 230, y=6 + 80)

        self.Tv_ck_is_transparency = IntVar()
        self.Rad_ck_is_transparency1 = Radiobutton(self, text="Yes", variable=self.Tv_ck_is_transparency, value=1)
        self.Rad_ck_is_transparency2 = Radiobutton(self, text="No", variable=self.Tv_ck_is_transparency, value=2)

        self.Rad_ck_is_transparency1.place(x=self.JG_x + 430, y=6 + 80)
        self.Rad_ck_is_transparency2.place(x=self.JG_x + 520, y=6 + 80)

        self.V_Scal_ck_is_transparency = DoubleVar()
        self.Scal_ck_is_transparency = Scale(self, from_=0, to=1, orient=HORIZONTAL,
                                             variable=self.V_Scal_ck_is_transparency,
                                             length=330, width=10, resolution=0.01)
        self.Scal_ck_is_transparency.place(x=self.JG_x + 230, y=6 + 110)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 窗口图标

        self.Lab_ck_set_icon = Label(self, text='Set interface icon', font=self.Font)
        self.Lab_ck_set_icon.place(x=self.JG_x + 230, y=6 + 160)

        self.Tv_ck_set_icon = StringVar()
        self.Ent_ck_set_icon = Entry(self, textvariable=self.Tv_ck_set_icon, font=self.Font, width=36)
        self.Ent_ck_set_icon.place(x=self.JG_x + 230, y=6 + 200)

        self.Btn_ck_set_icon = Button(self, text='...', font=('Consol', '10'), width=6, height=1,
                                      command=self.More_Icon)
        self.Btn_ck_set_icon.place(x=self.JG_x + 530, y=6 + 196)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 窗口网格宽度

        self.Lab_ck_set_grid = Label(self, text='Set the grid width', font=self.Font)
        self.Lab_ck_set_grid.place(x=self.JG_x + 230, y=6 + 240)

        self.Tv_ck_set_grid = IntVar()
        self.Comb_ck_set_grid = ttk.Combobox(self, width=23, textvariable=self.Tv_ck_set_grid)

        self.Comb_ck_set_grid['values'] = (10, 20, 30, 40, 50, 60)
        self.Comb_ck_set_grid.place(x=self.JG_x + 400, y=6 + 240)
        self.Comb_ck_set_grid.current(1)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 确定或取消键

        self.Lab_OK = Label(self, text='____________________________________________', font=('Consol', '16'))
        self.Lab_OK.place(x=self.JG_x + 230, y=6 + 280)

        self.Btn_ck_OK = Button(self, text='OK', font=('Consol', '13'), width=6, height=1, command=self.CK_OK)
        self.Btn_ck_OK.place(x=self.JG_x + 300, y=6 + 450)

        self.Btn_ck_Cancel = Button(self, text='Cancel', font=('Consol', '13'), width=6, height=1,
                                    command=self.CK_Cancel)
        self.Btn_ck_Cancel.place(x=self.JG_x + 430, y=6 + 450)

    def More_Icon(self):
        w = 800
        h = 500
        S_width = self.winfo_screenwidth()
        S_height = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2 + 600, (S_height - h) / 2 - 30)
        self.geometry(size)

        get_more_icon = Get_File_Name_GIF()
        icon = get_more_icon.Get_Name()
        self.Tv_ck_set_icon.set(icon)

        size = '%dx%d+%d+%d' % (w, h, (S_width - w) / 2, (S_height - h) / 2 - 30)
        self.geometry(size)

    def CK_OK(self):
        global Str_BianYi
        global ck_name
        global ck_init_x
        global ck_init_y
        global ck_is_width_not_change
        global ck_is_height_not_change
        global ck_is_minsize
        global ck_init_minsize_w
        global ck_init_minsize_h
        global ck_is_maxsize
        global ck_init_maxsize_w
        global ck_init_maxsize_h
        global ck_is_toolwindow
        global ck_is_topmost
        global ck_is_zoomed
        global ck_is_transparency
        global ck_scal_transparency
        global ck_set_icon
        global ck_set_grid
        global ck_is_son_win
        global canva_W
        global canva_H
        global WangGe_KuanDu

        global Str_BianYi_End

        ck_name = self.Ent_ck_name.get()
        ck_init_x = self.Tv_ck_init_x.get()
        ck_init_y = self.Tv_ck_init_y.get()
        ck_is_width_not_change = self.Tv_ck_is_width_not_change.get()
        ck_is_height_not_change = self.Tv_ck_is_height_not_change.get()
        ck_is_minsize = self.Tv_ck_is_minsize.get()
        ck_init_minsize_w = self.Tv_ck_init_minsize_w.get()
        ck_init_minsize_h = self.Tv_ck_init_minsize_h.get()
        ck_is_maxsize = self.Tv_ck_is_maxsize.get()
        ck_init_maxsize_w = self.Tv_ck_init_maxsize_w.get()
        ck_init_maxsize_h = self.Tv_ck_init_maxsize_h.get()
        ck_is_toolwindow = self.Tv_ck_is_toolwindow.get()
        ck_is_topmost = self.Tv_ck_is_topmost.get()
        ck_is_zoomed = self.Tv_ck_is_zoomed.get()
        ck_is_transparency = self.Tv_ck_is_transparency.get()
        ck_scal_transparency = self.V_Scal_ck_is_transparency.get()
        ck_set_icon = self.Tv_ck_set_icon.get()
        ck_set_grid = self.Tv_ck_set_grid.get()

        global tap
        line_next = "\n"

        Str_Import = "# Use the PyDraw to Design UI"\
        + """
# © JY.Lin 
from tkinter import *
from tkinter import ttk  # (when you want to use ttk)
from tkinter.scrolledtext import ScrolledText  # (when you want to use scrolledtext)
from tkinter.messagebox import *  # (when you want to use messagebox)
import tkinter.colorchooser  # (when you want to use colorchooser)
import tkinter.filedialog  # (when you want to use filedialog)
import tkinter as tk  # (when you want to use the short-call)
""" \

        if self.Ent_ck_name.get() == '':
            ck_name = "PyDraw"
        # self.title('PyDraw')
        Str_Main_CK = "class " + str(ck_name) + "(Tk):" + line_next \
                      + tap + "def __init__(self): " + line_next \
                      + tap + tap + "super().__init__() " + line_next\
                      + tap + tap + "self.title(\"" + str(ck_name) + "\")" + line_next

        if ck_init_x == '':
            ck_init_x = 0
        if ck_init_y == 0:
            ck_init_y = 0

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        global Distance
        global bar_W
        global bar_menu_W

        if zi_menu1_sum == 0:
            Distance = bar_W
        else:
            Distance = bar_W + bar_menu_W
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        Str_Coords = tap + tap + "S_width = self.winfo_screenwidth()" + line_next \
                     + tap + tap + "S_height = self.winfo_screenwidth()" + line_next \
                     + tap + tap + "Size = '%dx%d+%d+%d' % (" + str(canva_W) + ", " + str(canva_H-Distance) + ", " + "(S_width - " + str(canva_W) + ") /2, "\
                     + "(S_height - " + str(canva_H-Distance) + ") /2)" + line_next \
                     + tap + tap + "self.geometry(Size)" + line_next

        Str_width_height_change = ''

        if ck_is_width_not_change == 1:
            if ck_is_height_not_change == 1:
                pass
            elif ck_is_height_not_change == 2:
                Str_width_height_change = tap + tap + "self.resizable(width=TRUE, height=False)" + line_next

        elif ck_is_width_not_change == 2:
            if ck_is_height_not_change == 1:
                Str_width_height_change = tap + tap + "self.resizable(width=False, height=TRUE)" + line_next

            elif ck_is_height_not_change == 2:
                Str_width_height_change = tap + tap + "self.resizable(width=False, height=False)" + line_next


        if ck_is_minsize == 1:
            Str_Min_Size = tap + tap + "Min_W = " + str(ck_init_minsize_w) + line_next \
                           + tap + tap + "Min_H = " + str(ck_init_minsize_h) + line_next \
                           + tap + tap + "self.minsize(Min_W, Min_H)" + line_next
        else:
            Str_Min_Size = ""


        if ck_is_maxsize == 1:
            Str_Max_Size = tap + tap + "Max_W = " + str(ck_init_maxsize_w) + line_next\
                         + tap + tap + "Max_H = " + str(ck_init_maxsize_h) + line_next\
                         + tap + tap + "self.maxsize(Max_W, Max_H)" + line_next
        else:
            Str_Max_Size = ""


        if ck_is_toolwindow == 1:
            Str_is_toolwindow = tap + tap + "self.Propertys(\"-toolwindow\", 1)" + line_next
        else:
            Str_is_toolwindow = ''


        if ck_is_topmost == 1:
            Str_is_topmost = tap + tap + "self.Propertys(\"-topmost\", 1)" + line_next
        else:
            Str_is_topmost = ''


        if ck_is_zoomed == 1:
            Str_is_zoomed = tap + tap + "self.state(\"zoomed\")" + line_next
        else:
            Str_is_zoomed = ''


        if ck_is_transparency == 1:
            Str_is_transparency = tap + tap + "self.Propertys(\"-alpha\", " + str(ck_scal_transparency) + ")" + line_next
        else:
            Str_is_transparency = ''


        if ck_set_icon == 1:
            Str_set_icon = tap + tap + "self.iconbitmap('" + str(ck_set_icon) + "')" + line_next
        else:
            Str_set_icon = ''

        WangGe_KuanDu = int(ck_set_grid)

        Str_set_UI = tap + tap + "self.SetUI()" + line_next

        Str_def_UI = tap + "def SetUI(self):" + line_next

        # 编译汇总
        Str_BianYi = Str_Import + line_next + Str_Main_CK + Str_Coords + Str_width_height_change  \
                     + Str_Min_Size + Str_Max_Size + Str_is_toolwindow + Str_is_topmost + Str_is_zoomed \
                     + Str_is_transparency + Str_set_icon + Str_set_UI + line_next + Str_def_UI

        Str_BianYi_End = line_next \
                         + "if __name__ == '__main__':" + line_next \
                         + tap + "PyPa = " + str(ck_name) + "()" + line_next \
                         + tap + "PyPa.SetUI()" + line_next \
                         + tap + "PyPa.mainloop()" + line_next
        self.destroy()


    def CK_Cancel(self):
        self.destroy()




# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# name = "XuanZhong" + str(XuanZhong_sum)
# XuanZhong[name] = (Button1[KJ], 'Button', 'button', Num_i, Button1)

class SJ_Dictionary:
    def SJ_Dict(self, str_SJ):
        # 事件字典
        global SJ_button_press_1
        global SJ_button_release_1
        global SJ_button_press_right_1
        global SJ_button_press_left_2
        global SJ_button_press_right_2
        global SJ_button_press_middle_1
        global SJ_button_press_middle_2
        global SJ_button_press_left_move
        global SJ_cursor_enter
        global SJ_cursor_leave
        global SJ_get_key_focus
        global SJ_lose_key_focus
        global SJ_press_a_key
        global SJ_press_enter_key
        global SJ_when_control_change
        global SJ_shift_mouseWheel
        global SJ_press_combinatorial_key

        global XuanZhong
        global XuanZhong_sum

        if XuanZhong_sum == 1:
            # name = "XuanZhong" + str(XuanZhong_sum)
            # XuanZhong[name] = (Button1[KJ], 'Button', 'button', Num_i, Button1)
            # KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
            # BuJian_Lei[KJ] = BuJian
            # 控件.bind('<事件代码>', event_handler)

            name = "XuanZhong" + str(1)

            xuan = XuanZhong[name]
            BuJian_LeiXing_XiaoXie = xuan[2]
            BuJian_NO_i = xuan[3]
            BuJian_Lei = xuan[4]
            if str_SJ == "button_press_1":
                SJ_code = "1"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_press_1[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)

                # a = SJ_button_press_1[KJ_name]
                # print(str(a[0]))


            elif str_SJ == "button_release_1":
                SJ_code = "ButtonRelease-1"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_release_1[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_right_1":
                SJ_code = "3"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_press_right_1[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_left_2":
                SJ_code = "Double-1"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_press_left_2[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_right_2":
                SJ_code = "Double-3"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_press_right_2[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_middle_1":
                SJ_code = "2"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_press_middle_1[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "button_press_middle_2":
                SJ_code = "	Double-2"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_press_middle_2[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)



            elif str_SJ == "button_press_left_move":
                SJ_code = "	B1-Motion"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_button_press_left_move[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "cursor_enter":
                SJ_code = "Enter"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_cursor_enter[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "cursor_leave":
                SJ_code = "Leave"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_cursor_leave[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "get_key_focus":
                SJ_code = "FocusIn"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_get_key_focus[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "lose_key_focus":
                SJ_code = "FocusOut"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_lose_key_focus[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "press_a_key":
                SJ_code = "Key"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_press_a_key[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "press_enter_key":
                SJ_code = "Return"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_press_enter_key[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "when_control_change":
                SJ_code = "Configure"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_when_control_change[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "control_mouseWheel":
                SJ_code = "Control-MouseWheel"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_shift_mouseWheel[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


            elif str_SJ == "shift_mouseWheel":
                SJ_code = "Shift-MouseWheel"
                KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)

                SJ_shift_mouseWheel[KJ_name] = (str(BuJian_Lei[KJ_name]), ".bind('<" + SJ_code + ">', event_handler)",
                                              BuJian_LeiXing_XiaoXie, BuJian_NO_i)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 判断类
class Judge:
    def Judge_If_Delete(self, BuJian_LeiXing_XiaoXie, BuJian_NO_i):
        global Button1_List_Num
        global Canvas1_List_Num
        global Checkbutton1_List_Num
        global Combobox1_List_Num
        global Entry1_List_Num
        global Frame1_List_Num
        global Label1_List_Num
        global LabelFrame1_List_Num
        global Listbox1_List_Num
        global Menu1_List_Num
        global Message1_List_Num
        global PanedWindow1_List_Num
        global Radiobutton1_List_Num
        global Scale1_List_Num_X
        global Scale1_List_Num_Y
        global Spinbox1_List_Num
        global Text1_List_Num


        if BuJian_LeiXing_XiaoXie == "button":
            if BuJian_NO_i in Button1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "canvas":
            if BuJian_NO_i in Canvas1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "checkbutton":
            if BuJian_NO_i in Checkbutton1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "combobox":
            if BuJian_NO_i in Combobox1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "entry":
            if BuJian_NO_i in Entry1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "frame":
            if BuJian_NO_i in Frame1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "label":
            if BuJian_NO_i in Label1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "labelFrame":
            if BuJian_NO_i in LabelFrame1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "listbox":
            if BuJian_NO_i in Listbox1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "menu":
            if BuJian_NO_i in Menu1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "message":
            if BuJian_NO_i in Message1_List_Num:
                return TRUE
            else:
                return FALSE


        if BuJian_LeiXing_XiaoXie == "panedWindow":
            if BuJian_NO_i in PanedWindow1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "radiobutton":
            if BuJian_NO_i in Radiobutton1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "scale_x":
            if BuJian_NO_i in Scale1_List_Num_X:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "scale_y":
            if BuJian_NO_i in Scale1_List_Num_Y:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "spinbox":
            if BuJian_NO_i in Spinbox1_List_Num:
                return TRUE
            else:
                return FALSE

        if BuJian_LeiXing_XiaoXie == "text":
            if BuJian_NO_i in Text1_List_Num:
                return TRUE
            else:
                return FALSE

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 事件处理类
class SJ_ChuLi:
    def SJ_Bian_Yi(self, SJ_Dictionary, Text_1):
        judge = Judge()
        tap = "    "
        for i in SJ_Dictionary:
            a = SJ_Dictionary[i]
            sj_code = tap + tap + a[0] + a[1] + "\n"
            BuJian_LeiXing_XiaoXie = a[2]
            BuJian_NO_i = a[3]
            if judge.Judge_If_Delete(BuJian_LeiXing_XiaoXie, BuJian_NO_i) == FALSE:
                Text_1.insert(END, sj_code)

    # KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
    # BuJian_Lei[KJ_name]
    def SJ_New(self, BuJian_LeiXing_XiaoXie, BuJian_NO_i, BuJian_Lei):
        KJ_name = str(BuJian_LeiXing_XiaoXie) + '_name' + str(BuJian_NO_i)
        SJ_Dictionary_Zong = (SJ_button_press_1,
            SJ_button_release_1,
            SJ_button_press_right_1,
            SJ_button_press_left_2,
            SJ_button_press_right_2,
            SJ_button_press_middle_1,
            SJ_button_press_middle_2,
            SJ_button_press_left_move,
            SJ_cursor_enter,
            SJ_cursor_leave,
            SJ_get_key_focus,
            SJ_lose_key_focus,
            SJ_press_a_key,
            SJ_press_enter_key,
            SJ_when_control_change,
            SJ_press_space_key,
            SJ_shift_mouseWheel,
            SJ_press_combinatorial_key)

        for SJ_Dictionary in SJ_Dictionary_Zong:
            for i in SJ_Dictionary:
                a = SJ_Dictionary[i]
                SJ_LeiXing_XiaoXie = a[2]
                SJ_NO_i = a[3]
                if SJ_LeiXing_XiaoXie == BuJian_LeiXing_XiaoXie:
                    if SJ_NO_i == BuJian_NO_i:
                        SJ_Dictionary[i] = (BuJian_Lei[KJ_name], a[1], a[2], a[3])


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# menu string 生成类
class Menu_Str:
    def Menu_Str(self):
        global Menu1
        global Menu1_ListCode
        global zi_menu1_sum
        global Str_Menu
        global tap

        Str_Menu = ""

        str_bar = tap + tap + "Menubar = Menu(self)" + "\n"

        # range(a, b, i) 从 a 开始到 b前为止，间隔为 i, 包括 a不包括 b
        for i in range(1, zi_menu1_sum+1, 1):
            zi_menu_tearoff_name = "zi_menu_tearoff_name" + str(i)
            zi_menu_add_cascade_name = "zi_menu_add_cascade_name" + str(i)
            tearoff = Menu1[zi_menu_tearoff_name]
            add_cascade = Menu1[zi_menu_add_cascade_name]

            Code_tearoff = tap + tap + tearoff[0] + "\n"
            Code_add_cascade = tap + tap + add_cascade[0]
            Str_list = ""

            for mlist_j in Menu1_ListCode:
                # Menu1_ListCode[menu_list_code_name] = (Code, zi_menu1_sum, zong+1)
                menu_list = Menu1_ListCode[mlist_j]
                if i == menu_list[1]:
                    Str_list = Str_list + tap + tap + menu_list[0] + "\n"

            Str_son_menu = Code_tearoff + Str_list + Code_add_cascade

            Str_Menu = Str_Menu + Str_son_menu + "\n"

        Str_Conifg = "\n" + tap + tap + "self.config(menu=Menubar)" + "\n\n"

        Str_Menu = str_bar + "\n" + Str_Menu + Str_Conifg

        return Str_Menu

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == '__main__':
    PypA = PyDraw()
    PypA.HuaBu_YiDong()

    PypA.mainloop()










