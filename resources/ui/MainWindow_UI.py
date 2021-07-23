# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbYear = QtWidgets.QComboBox(self.widget)
        self.cbYear.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cbYear.setFont(font)
        self.cbYear.setObjectName("cbYear")
        self.horizontalLayout.addWidget(self.cbYear)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 36))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.editLimit = QtWidgets.QLineEdit(self.widget)
        self.editLimit.setMinimumSize(QtCore.QSize(36, 36))
        self.editLimit.setMaximumSize(QtCore.QSize(36, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.editLimit.setFont(font)
        self.editLimit.setObjectName("editLimit")
        self.horizontalLayout.addWidget(self.editLimit)
        self.btnRecal = QtWidgets.QPushButton(self.widget)
        self.btnRecal.setMinimumSize(QtCore.QSize(0, 36))
        self.btnRecal.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnRecal.setFont(font)
        self.btnRecal.setObjectName("btnRecal")
        self.horizontalLayout.addWidget(self.btnRecal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnManageData = QtWidgets.QPushButton(self.widget)
        self.btnManageData.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnManageData.setFont(font)
        self.btnManageData.setObjectName("btnManageData")
        self.horizontalLayout.addWidget(self.btnManageData)
        self.btnSync = QtWidgets.QPushButton(self.widget)
        self.btnSync.setMinimumSize(QtCore.QSize(0, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnSync.setFont(font)
        self.btnSync.setObjectName("btnSync")
        self.horizontalLayout.addWidget(self.btnSync)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tb0 = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tb0.setFont(font)
        self.tb0.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tb0.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb0.setObjectName("tb0")
        self.tb0.setColumnCount(0)
        self.tb0.setRowCount(0)
        self.tb0.horizontalHeader().setDefaultSectionSize(38)
        self.tb0.horizontalHeader().setMinimumSectionSize(38)
        self.tb0.verticalHeader().setDefaultSectionSize(38)
        self.tb0.verticalHeader().setMinimumSectionSize(38)
        self.verticalLayout_3.addWidget(self.tb0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tb1 = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tb1.setFont(font)
        self.tb1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tb1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tb1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tb1.setObjectName("tb1")
        self.tb1.setColumnCount(0)
        self.tb1.setRowCount(0)
        self.tb1.horizontalHeader().setDefaultSectionSize(38)
        self.tb1.horizontalHeader().setMinimumSectionSize(38)
        self.tb1.verticalHeader().setDefaultSectionSize(38)
        self.tb1.verticalHeader().setMinimumSectionSize(38)
        self.verticalLayout_4.addWidget(self.tb1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tb2 = QtWidgets.QTableWidget(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tb2.setFont(font)
        self.tb2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tb2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tb2.setObjectName("tb2")
        self.tb2.setColumnCount(0)
        self.tb2.setRowCount(0)
        self.tb2.horizontalHeader().setDefaultSectionSize(38)
        self.tb2.horizontalHeader().setMinimumSectionSize(38)
        self.tb2.verticalHeader().setDefaultSectionSize(38)
        self.tb2.verticalHeader().setMinimumSectionSize(38)
        self.verticalLayout_5.addWidget(self.tb2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tb3 = QtWidgets.QTableWidget(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tb3.setFont(font)
        self.tb3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tb3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb3.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tb3.setObjectName("tb3")
        self.tb3.setColumnCount(0)
        self.tb3.setRowCount(0)
        self.tb3.horizontalHeader().setDefaultSectionSize(38)
        self.tb3.horizontalHeader().setMinimumSectionSize(38)
        self.tb3.verticalHeader().setDefaultSectionSize(38)
        self.tb3.verticalHeader().setMinimumSectionSize(38)
        self.verticalLayout_6.addWidget(self.tb3)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tb4 = QtWidgets.QTableWidget(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tb4.setFont(font)
        self.tb4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tb4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb4.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tb4.setObjectName("tb4")
        self.tb4.setColumnCount(0)
        self.tb4.setRowCount(0)
        self.tb4.horizontalHeader().setDefaultSectionSize(38)
        self.tb4.horizontalHeader().setMinimumSectionSize(38)
        self.tb4.verticalHeader().setDefaultSectionSize(38)
        self.tb4.verticalHeader().setMinimumSectionSize(38)
        self.verticalLayout_7.addWidget(self.tb4)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tb5 = QtWidgets.QTableWidget(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tb5.setFont(font)
        self.tb5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tb5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb5.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tb5.setObjectName("tb5")
        self.tb5.setColumnCount(0)
        self.tb5.setRowCount(0)
        self.tb5.horizontalHeader().setDefaultSectionSize(38)
        self.tb5.horizontalHeader().setMinimumSectionSize(38)
        self.tb5.verticalHeader().setDefaultSectionSize(38)
        self.tb5.verticalHeader().setMinimumSectionSize(38)
        self.verticalLayout_8.addWidget(self.tb5)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tb7 = QtWidgets.QTableWidget(self.tab_7)
        self.tb7.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tb7.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb7.setObjectName("tb7")
        self.tb7.setColumnCount(0)
        self.tb7.setRowCount(0)
        self.verticalLayout_9.addWidget(self.tb7)
        self.tabWidget.addTab(self.tab_7, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.btnSync.clicked.connect(MainWindow.doSync)
        self.btnManageData.clicked.connect(MainWindow.openManagerData)
        self.btnRecal.clicked.connect(MainWindow.doReCal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "澳门六合彩-过三关v1.0"))
        self.label.setText(_translate("MainWindow", "选择年份："))
        self.label_2.setText(_translate("MainWindow", "连续限制："))
        self.btnRecal.setText(_translate("MainWindow", "重新计算"))
        self.btnManageData.setText(_translate("MainWindow", "管理数据"))
        self.btnSync.setText(_translate("MainWindow", "同步数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "业务统计"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "大小"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "单双"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "合-大小"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "合-单双"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "尾大小"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "分布统计"))
