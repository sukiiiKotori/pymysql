# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Py\Desktop\vscode\pymysql\teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_tea(object):
    def setupUi(self, MainWindow_tea):
        MainWindow_tea.setObjectName("MainWindow_tea")
        MainWindow_tea.resize(800, 600)
        MainWindow_tea.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow_tea)
        self.centralwidget.setObjectName("centralwidget")
        self.report_button = QtWidgets.QPushButton(self.centralwidget)
        self.report_button.setGeometry(QtCore.QRect(10, 190, 151, 41))
        self.report_button.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.report_button.setObjectName("report_button")
        self.leave_button = QtWidgets.QPushButton(self.centralwidget)
        self.leave_button.setGeometry(QtCore.QRect(10, 260, 151, 41))
        self.leave_button.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.leave_button.setObjectName("leave_button")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 30, 621, 561))
        self.tabWidget.setStyleSheet("QTabWidget::pane{\n"
"    border:none;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_report = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_report.setGeometry(QtCore.QRect(20, 80, 581, 311))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.tableWidget_report.setFont(font)
        self.tableWidget_report.setStyleSheet("/********QTableWidget*********/\n"
"QHeaderView{                            /*设置标题(包括垂直+水平的)*/\n"
"    \n"
"              font-size: 15px;                /*11榜*/\n"
"          border: 1px solid rgb(255, 255, 255);\n"
"       /* border-bottom: 2px solid rgb(35, 100, 224);         下边框深蓝色*/\n"
"        background: rgb(100, 188, 238);                /*背景浅蓝色*/ \n"
"          min-height:40px;\n"
"           \n"
"} \n"
" \n"
" \n"
"QHeaderView::section:horizontal {                     /*设置标题(水平的)*/\n"
"        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
"          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding-left: 2px;\n"
"        min-width:60px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {            /*设置鼠标停留状态*/\n"
"        color: white;                            /*字体白色*/\n"
"        background: rgb(11,82,202);                /*背景深蓝色*/\n"
"}\n"
"QHeaderView::section:horizontal:pressed {            /*设置鼠标按下状态*/\n"
"        color: white;\n"
"        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
"}\n"
"QHeaderView::section:vertical {                     /*设置标题(垂直的)*/\n"
"        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
"          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
"        color: rgb(2, 65, 132);\n"
"        background: rgb(255, 255, 255,180);\n"
"        padding-top: 3px;\n"
"        min-width:60px;\n"
"        \n"
"}\n"
"QHeaderView::section:vertical:hover {            /*设置鼠标停留状态*/\n"
"        color: white;                            /*字体白色*/\n"
"        background: rgb(11,82,202);                /*背景深蓝色*/\n"
"}\n"
"QHeaderView::section:vertical:pressed {            /*设置鼠标按下状态*/\n"
"        color: white;\n"
"        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
"}\n"
" \n"
" \n"
"QHeaderView::up-arrow {                        /*设置向上排序指针*/\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 10px;                         /*设置右内边距*/\n"
"        image: url(:/arrow_up.png);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
"     \n"
"}\n"
"QHeaderView::down-arrow {                        /*设置向下排序指针*/\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 10px;\n"
"        image: url(:/arrow_down.png);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
"     \n"
"}\n"
"QTableWidget,QTableView {\n"
"                font-size: 15px;                /*10榜*/                \n"
"                color : rgb(1,37,116);                \n"
"        border: 2px solid rgb(100, 188, 238);        \n"
"        background: rgb(248,248,248);\n"
"        gridline-color: rgb(196,226,255);    \n"
"        text-align: center;    \n"
"        outline:0px;            /*禁止焦点*/\n"
"        \n"
"}\n"
"QTableWidget::item,QTableView::item {                            /*设置视图项*/\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        border: none; \n"
"        background: rgba(251,251,253,200);\n"
"       \n"
"       /* border-right: 1px solid rgb(100, 188, 238); */\n"
"        /*border-bottom: 1px solid rgb(100, 188, 238);*/\n"
"}\n"
"QTableWidget::item:selected,QTableView::item:selected {                    /*设置选中的视图项*/\n"
"        background: rgba(207,230,253,200);\n"
"        color : rgb(1,37,116);                \n"
"}\n"
" \n"
" \n"
"QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
"{ \n"
"    background: rgb(250,250,250); \n"
"}\n"
" \n"
"QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
"{ \n"
"    background: rgb(240,247,254); \n"
"}")
        self.tableWidget_report.setAutoScroll(True)
        self.tableWidget_report.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_report.setObjectName("tableWidget_report")
        self.tableWidget_report.setColumnCount(4)
        self.tableWidget_report.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_report.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_report.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_report.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_report.setHorizontalHeaderItem(3, item)
        self.tableWidget_report.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidget_report.verticalHeader().setDefaultSectionSize(37)
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(240, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("    border: 2px solid #f3f3f3;/*设置线宽*/\n"
"    background-color: rgb(237, 242, 255);/*背景颜色*/\n"
"    border-radius: 10px;/*圆角*/\n"
"    border-style:solid;/*边框为实线型*/\n"
"    border-width:2px;/*边框宽度*/\n"
"    border-color:rgb(77, 123, 255);/*边框颜色*/\n"
"\n"
"    padding-left: 10px;/*左侧边距*/\n"
" QDateEdit::up-button{\n"
"subcontrol-origin:border;\n"
"     subcontrol-position:right;\n"
"      60px;\n"
"     height: 60px;                \n"
" }\n"
" QDateEdit::down-button{subcontrol-origin:border;\n"
"     subcontrol-position:left;\n"
"      60px;\n"
"     height: 60px;\n"
" }")
        self.dateEdit.setDate(QtCore.QDate(2022, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(120, 30, 111, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 85, 255);")
        self.label.setObjectName("label")
        self.get_report = QtWidgets.QPushButton(self.tab)
        self.get_report.setGeometry(QtCore.QRect(210, 420, 191, 41))
        self.get_report.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.get_report.setObjectName("get_report")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 10, 621, 521))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_leave = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_leave.setGeometry(QtCore.QRect(0, 40, 621, 311))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.tableWidget_leave.setFont(font)
        self.tableWidget_leave.setStyleSheet("/********QTableWidget*********/\n"
"QHeaderView{                            /*设置标题(包括垂直+水平的)*/\n"
"    \n"
"              font-size: 15px;                /*11榜*/\n"
"          border: 1px solid rgb(255, 255, 255);\n"
"       /* border-bottom: 2px solid rgb(35, 100, 224);         下边框深蓝色*/\n"
"        background: rgb(100, 188, 238);                /*背景浅蓝色*/ \n"
"          min-height:40px;\n"
"           \n"
"} \n"
" \n"
" \n"
"QHeaderView::section:horizontal {                     /*设置标题(水平的)*/\n"
"        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
"          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding-left: 2px;\n"
"        min-width:60px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {            /*设置鼠标停留状态*/\n"
"        color: white;                            /*字体白色*/\n"
"        background: rgb(11,82,202);                /*背景深蓝色*/\n"
"}\n"
"QHeaderView::section:horizontal:pressed {            /*设置鼠标按下状态*/\n"
"        color: white;\n"
"        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
"}\n"
"QHeaderView::section:vertical {                     /*设置标题(垂直的)*/\n"
"        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
"          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
"        color: rgb(2, 65, 132);\n"
"        background: rgb(255, 255, 255,180);\n"
"        padding-top: 3px;\n"
"        min-width:60px;\n"
"        \n"
"}\n"
"QHeaderView::section:vertical:hover {            /*设置鼠标停留状态*/\n"
"        color: white;                            /*字体白色*/\n"
"        background: rgb(11,82,202);                /*背景深蓝色*/\n"
"}\n"
"QHeaderView::section:vertical:pressed {            /*设置鼠标按下状态*/\n"
"        color: white;\n"
"        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
"}\n"
" \n"
" \n"
"QHeaderView::up-arrow {                        /*设置向上排序指针*/\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 10px;                         /*设置右内边距*/\n"
"        image: url(:/arrow_up.png);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
"     \n"
"}\n"
"QHeaderView::down-arrow {                        /*设置向下排序指针*/\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 10px;\n"
"        image: url(:/arrow_down.png);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
"     \n"
"}\n"
"QTableWidget,QTableView {\n"
"                font-size: 15px;                /*10榜*/                \n"
"                color : rgb(1,37,116);                \n"
"        border: 2px solid rgb(100, 188, 238);        \n"
"        background: rgb(248,248,248);\n"
"        gridline-color: rgb(196,226,255);    \n"
"        text-align: center;    \n"
"        outline:0px;            /*禁止焦点*/\n"
"        \n"
"}\n"
"QTableWidget::item,QTableView::item {                            /*设置视图项*/\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        border: none; \n"
"        background: rgba(251,251,253,200);\n"
"       \n"
"       /* border-right: 1px solid rgb(100, 188, 238); */\n"
"        /*border-bottom: 1px solid rgb(100, 188, 238);*/\n"
"}\n"
"QTableWidget::item:selected,QTableView::item:selected {                    /*设置选中的视图项*/\n"
"        background: rgba(207,230,253,200);\n"
"        color : rgb(1,37,116);                \n"
"}\n"
" \n"
" \n"
"QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
"{ \n"
"    background: rgb(250,250,250); \n"
"}\n"
" \n"
"QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
"{ \n"
"    background: rgb(240,247,254); \n"
"}")
        self.tableWidget_leave.setAutoScroll(True)
        self.tableWidget_leave.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_leave.setObjectName("tableWidget_leave")
        self.tableWidget_leave.setColumnCount(5)
        self.tableWidget_leave.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave.setHorizontalHeaderItem(4, item)
        self.tableWidget_leave.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidget_leave.verticalHeader().setDefaultSectionSize(37)
        self.leave_button_2 = QtWidgets.QPushButton(self.tab_3)
        self.leave_button_2.setGeometry(QtCore.QRect(200, 370, 191, 41))
        self.leave_button_2.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.leave_button_2.setObjectName("leave_button_2")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_leave_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_leave_2.setGeometry(QtCore.QRect(0, 40, 621, 311))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(-1)
        self.tableWidget_leave_2.setFont(font)
        self.tableWidget_leave_2.setStyleSheet("/********QTableWidget*********/\n"
"QHeaderView{                            /*设置标题(包括垂直+水平的)*/\n"
"    \n"
"              font-size: 15px;                /*11榜*/\n"
"          border: 1px solid rgb(255, 255, 255);\n"
"       /* border-bottom: 2px solid rgb(35, 100, 224);         下边框深蓝色*/\n"
"        background: rgb(100, 188, 238);                /*背景浅蓝色*/ \n"
"          min-height:40px;\n"
"           \n"
"} \n"
" \n"
" \n"
"QHeaderView::section:horizontal {                     /*设置标题(水平的)*/\n"
"        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
"          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding-left: 2px;\n"
"        min-width:60px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {            /*设置鼠标停留状态*/\n"
"        color: white;                            /*字体白色*/\n"
"        background: rgb(11,82,202);                /*背景深蓝色*/\n"
"}\n"
"QHeaderView::section:horizontal:pressed {            /*设置鼠标按下状态*/\n"
"        color: white;\n"
"        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
"}\n"
"QHeaderView::section:vertical {                     /*设置标题(垂直的)*/\n"
"        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
"          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
"        color: rgb(2, 65, 132);\n"
"        background: rgb(255, 255, 255,180);\n"
"        padding-top: 3px;\n"
"        min-width:60px;\n"
"        \n"
"}\n"
"QHeaderView::section:vertical:hover {            /*设置鼠标停留状态*/\n"
"        color: white;                            /*字体白色*/\n"
"        background: rgb(11,82,202);                /*背景深蓝色*/\n"
"}\n"
"QHeaderView::section:vertical:pressed {            /*设置鼠标按下状态*/\n"
"        color: white;\n"
"        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
"}\n"
" \n"
" \n"
"QHeaderView::up-arrow {                        /*设置向上排序指针*/\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 10px;                         /*设置右内边距*/\n"
"        image: url(:/arrow_up.png);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
"     \n"
"}\n"
"QHeaderView::down-arrow {                        /*设置向下排序指针*/\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 10px;\n"
"        image: url(:/arrow_down.png);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
"     \n"
"}\n"
"QTableWidget,QTableView {\n"
"                font-size: 15px;                /*10榜*/                \n"
"                color : rgb(1,37,116);                \n"
"        border: 2px solid rgb(100, 188, 238);        \n"
"        background: rgb(248,248,248);\n"
"        gridline-color: rgb(196,226,255);    \n"
"        text-align: center;    \n"
"        outline:0px;            /*禁止焦点*/\n"
"        \n"
"}\n"
"QTableWidget::item,QTableView::item {                            /*设置视图项*/\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        border: none; \n"
"        background: rgba(251,251,253,200);\n"
"       \n"
"       /* border-right: 1px solid rgb(100, 188, 238); */\n"
"        /*border-bottom: 1px solid rgb(100, 188, 238);*/\n"
"}\n"
"QTableWidget::item:selected,QTableView::item:selected {                    /*设置选中的视图项*/\n"
"        background: rgba(207,230,253,200);\n"
"        color : rgb(1,37,116);                \n"
"}\n"
" \n"
" \n"
"QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
"{ \n"
"    background: rgb(250,250,250); \n"
"}\n"
" \n"
"QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
"{ \n"
"    background: rgb(240,247,254); \n"
"}")
        self.tableWidget_leave_2.setAutoScroll(True)
        self.tableWidget_leave_2.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_leave_2.setObjectName("tableWidget_leave_2")
        self.tableWidget_leave_2.setColumnCount(5)
        self.tableWidget_leave_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        item.setFont(font)
        self.tableWidget_leave_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_leave_2.horizontalHeader().setDefaultSectionSize(123)
        self.tableWidget_leave_2.verticalHeader().setDefaultSectionSize(37)
        self.leave_button_3 = QtWidgets.QPushButton(self.tab_4)
        self.leave_button_3.setGeometry(QtCore.QRect(330, 370, 191, 41))
        self.leave_button_3.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.leave_button_3.setObjectName("leave_button_3")
        self.leave_button_4 = QtWidgets.QPushButton(self.tab_4)
        self.leave_button_4.setGeometry(QtCore.QRect(70, 370, 191, 41))
        self.leave_button_4.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.leave_button_4.setObjectName("leave_button_4")
        self.label_leave = QtWidgets.QLabel(self.tab_4)
        self.label_leave.setGeometry(QtCore.QRect(150, 430, 301, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_leave.setFont(font)
        self.label_leave.setStyleSheet("color:rgb(255, 0, 0);")
        self.label_leave.setText("")
        self.label_leave.setObjectName("label_leave")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.password_comfirm_lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.password_comfirm_lineEdit.setGeometry(QtCore.QRect(180, 230, 221, 41))
        self.password_comfirm_lineEdit.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_comfirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_comfirm_lineEdit.setObjectName("password_comfirm_lineEdit")
        self.leave_button_5 = QtWidgets.QPushButton(self.tab_5)
        self.leave_button_5.setGeometry(QtCore.QRect(220, 300, 141, 41))
        self.leave_button_5.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.leave_button_5.setObjectName("leave_button_5")
        self.password_lineEdit_new = QtWidgets.QLineEdit(self.tab_5)
        self.password_lineEdit_new.setGeometry(QtCore.QRect(180, 160, 221, 41))
        self.password_lineEdit_new.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit_new.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit_new.setObjectName("password_lineEdit_new")
        self.password_lineEdit_old = QtWidgets.QLineEdit(self.tab_5)
        self.password_lineEdit_old.setGeometry(QtCore.QRect(180, 90, 221, 41))
        self.password_lineEdit_old.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"font: 10pt \"微软雅黑\";\n"
"border-radius:10px\n"
"")
        self.password_lineEdit_old.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit_old.setObjectName("password_lineEdit_old")
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        self.label_9.setGeometry(QtCore.QRect(200, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_5, "")
        self.change_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_password_button.setGeometry(QtCore.QRect(10, 330, 151, 41))
        self.change_password_button.setStyleSheet("QPushButton{\n"
"    font: 12pt \"微软雅黑\";\n"
"    \n"
"    background-color:rgb(46, 154, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 3px solid rgb(46, 154, 255);\n"
"    border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color:rgb(46, 154, 255);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px\n"
"}\n"
"")
        self.change_password_button.setObjectName("change_password_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 331, 51))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow_tea.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_tea)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_tea)

    def retranslateUi(self, MainWindow_tea):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_tea.setWindowTitle(_translate("MainWindow_tea", "班主任管理"))
        self.report_button.setText(_translate("MainWindow_tea", "学生填报管理"))
        self.leave_button.setText(_translate("MainWindow_tea", "学生请假管理"))
        item = self.tableWidget_report.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_tea", "姓名"))
        item = self.tableWidget_report.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_tea", "学号"))
        item = self.tableWidget_report.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_tea", "当日体温"))
        item = self.tableWidget_report.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_tea", "填报地点"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow_tea", "yyyy-M-d"))
        self.label.setText(_translate("MainWindow_tea", "请选择日期"))
        self.get_report.setText(_translate("MainWindow_tea", "本班学生填报记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow_tea", "Tab 1"))
        item = self.tableWidget_leave.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_tea", "姓名"))
        item = self.tableWidget_leave.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_tea", "学号"))
        item = self.tableWidget_leave.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_tea", "离校时间"))
        item = self.tableWidget_leave.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_tea", "时长"))
        item = self.tableWidget_leave.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_tea", "目的地"))
        self.leave_button_2.setText(_translate("MainWindow_tea", "刷新纪录"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow_tea", "                   已批准                  "))
        item = self.tableWidget_leave_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_tea", "姓名"))
        item = self.tableWidget_leave_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_tea", "学号"))
        item = self.tableWidget_leave_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_tea", "离校时间"))
        item = self.tableWidget_leave_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_tea", "时长"))
        item = self.tableWidget_leave_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_tea", "目的地"))
        self.leave_button_3.setText(_translate("MainWindow_tea", "批准请假"))
        self.leave_button_4.setText(_translate("MainWindow_tea", "查看未批准学生"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow_tea", "                  未批准                  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow_tea", "Tab 2"))
        self.password_comfirm_lineEdit.setPlaceholderText(_translate("MainWindow_tea", "确认新密码"))
        self.leave_button_5.setText(_translate("MainWindow_tea", "确认修改"))
        self.password_lineEdit_new.setPlaceholderText(_translate("MainWindow_tea", "新密码"))
        self.password_lineEdit_old.setPlaceholderText(_translate("MainWindow_tea", "请输入旧密码以确认身份"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow_tea", "Tab 3"))
        self.change_password_button.setText(_translate("MainWindow_tea", "修改密码"))
