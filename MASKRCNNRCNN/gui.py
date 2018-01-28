# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shutu.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import guiutils
from guiutils import Figure_Canvas

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 850)
        #左边的gridlayout
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 90, 500, 700))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        #imageView
        self.imageView = QLabel("选择你要显示的图片")
        self.imageView.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.imageView)
        
        self.pb1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb1.setObjectName("pb1")
        #点击事件
        self.pb1.clicked.connect(self.on_btn_open_clicked)
        
        self.verticalLayout.addWidget(self.pb1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        
        #右边的gridlayout
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(800, 90, 500, 700))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # ===通过graphicview来显示图形
        self.graphicview = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicview.setObjectName("graphicview")
        self.verticalLayout_2.addWidget(self.graphicview)
                
        self.pb2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb2.setMaximumSize(QtCore.QSize(112, 34))
        self.pb2.setObjectName("pb2")
        #点击事件
        self.pb2.clicked.connect(self.run_clicked)
        
        self.verticalLayout_2.addWidget(self.pb2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数字图像处理课程项目——基于公开数据集的图像目标检测与分割"))
        Form.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pb1.setText(_translate("Form", "选择图片"))
        self.pb2.setText(_translate("Form", "预测结果"))
        
    @pyqtSlot(bool)
    def on_btn_open_clicked(self, checked):
        self.filename = QFileDialog.getOpenFileName(self, "OpenFile", ".", 
            "Image Files(*.jpg *.jpeg *.png)")[0]
        if len(self.filename):
            self.image = QImage(self.filename)
            self.imageView.setPixmap(QPixmap.fromImage(self.image))
    
    @pyqtSlot(bool)
    def run_clicked(self, checked):
        dr = Figure_Canvas() #实例化一个FigureCanvas
        dr.show_result(self.filename)  # 画图
        graphicscene = QtWidgets.QGraphicsScene()  # 创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        graphicscene.addWidget(dr)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        self.graphicview.setScene(graphicscene) # 把QGraphicsScene放入QGraphicsView
        self.graphicview.show()  # 调用show方法呈现图形
   
    
