# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saveEditorcxCBFU.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1242, 1138)
        self.actionLoad_Save_File = QAction(MainWindow)
        self.actionLoad_Save_File.setObjectName(u"actionLoad_Save_File")
        self.actionSave_File = QAction(MainWindow)
        self.actionSave_File.setObjectName(u"actionSave_File")
        self.actionSave_File.setEnabled(False)
        self.actionLoad_File = QAction(MainWindow)
        self.actionLoad_File.setObjectName(u"actionLoad_File")
        self.actionView_Templates = QAction(MainWindow)
        self.actionView_Templates.setObjectName(u"actionView_Templates")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resourceFrame = QFrame(self.centralwidget)
        self.resourceFrame.setObjectName(u"resourceFrame")
        self.resourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.resourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.resourceFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.goldGroupBox = QGroupBox(self.resourceFrame)
        self.goldGroupBox.setObjectName(u"goldGroupBox")
        self.verticalLayout = QVBoxLayout(self.goldGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.goldSpinBox = QSpinBox(self.goldGroupBox)
        self.goldSpinBox.setObjectName(u"goldSpinBox")
        self.goldSpinBox.setEnabled(False)
        self.goldSpinBox.setMaximum(9999999)
        self.goldSpinBox.setSingleStep(100)

        self.verticalLayout.addWidget(self.goldSpinBox)


        self.horizontalLayout_2.addWidget(self.goldGroupBox)

        self.supplyGroupBox = QGroupBox(self.resourceFrame)
        self.supplyGroupBox.setObjectName(u"supplyGroupBox")
        self.verticalLayout_5 = QVBoxLayout(self.supplyGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.supplySpinBox = QSpinBox(self.supplyGroupBox)
        self.supplySpinBox.setObjectName(u"supplySpinBox")
        self.supplySpinBox.setEnabled(False)
        self.supplySpinBox.setMaximum(9999999)
        self.supplySpinBox.setSingleStep(100)

        self.verticalLayout_5.addWidget(self.supplySpinBox)


        self.horizontalLayout_2.addWidget(self.supplyGroupBox)

        self.manpowerGroupBox = QGroupBox(self.resourceFrame)
        self.manpowerGroupBox.setObjectName(u"manpowerGroupBox")
        self.verticalLayout_4 = QVBoxLayout(self.manpowerGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.manpowerSpinBox = QSpinBox(self.manpowerGroupBox)
        self.manpowerSpinBox.setObjectName(u"manpowerSpinBox")
        self.manpowerSpinBox.setEnabled(False)
        self.manpowerSpinBox.setMaximum(9999999)
        self.manpowerSpinBox.setSingleStep(100)

        self.verticalLayout_4.addWidget(self.manpowerSpinBox)


        self.horizontalLayout_2.addWidget(self.manpowerGroupBox)

        self.ammoGroupBox = QGroupBox(self.resourceFrame)
        self.ammoGroupBox.setObjectName(u"ammoGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.ammoGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ammoSpinBox = QSpinBox(self.ammoGroupBox)
        self.ammoSpinBox.setObjectName(u"ammoSpinBox")
        self.ammoSpinBox.setEnabled(False)
        self.ammoSpinBox.setMaximum(9999999)
        self.ammoSpinBox.setSingleStep(100)

        self.verticalLayout_2.addWidget(self.ammoSpinBox)


        self.horizontalLayout_2.addWidget(self.ammoGroupBox)


        self.horizontalLayout.addWidget(self.resourceFrame)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.armyTab = QWidget()
        self.armyTab.setObjectName(u"armyTab")
        self.verticalLayout_91 = QVBoxLayout(self.armyTab)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.horizontalWidget = QWidget(self.armyTab)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.divisionGroupBox_4 = QGroupBox(self.horizontalWidget)
        self.divisionGroupBox_4.setObjectName(u"divisionGroupBox_4")
        self.verticalLayout_57 = QVBoxLayout(self.divisionGroupBox_4)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.divisionCheckBox_4 = QCheckBox(self.divisionGroupBox_4)
        self.divisionCheckBox_4.setObjectName(u"divisionCheckBox_4")
        self.divisionCheckBox_4.setEnabled(False)
        self.divisionCheckBox_4.setProperty(u"index", 3)

        self.verticalLayout_57.addWidget(self.divisionCheckBox_4)

        self.regimentGroupBox_4_1 = QGroupBox(self.divisionGroupBox_4)
        self.regimentGroupBox_4_1.setObjectName(u"regimentGroupBox_4_1")
        self.verticalLayout_58 = QVBoxLayout(self.regimentGroupBox_4_1)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.regimentTypeComboBox_4_1 = QComboBox(self.regimentGroupBox_4_1)
        self.regimentTypeComboBox_4_1.setObjectName(u"regimentTypeComboBox_4_1")
        self.regimentTypeComboBox_4_1.setEnabled(False)

        self.verticalLayout_58.addWidget(self.regimentTypeComboBox_4_1)

        self.veterancyGroupBox_4_1 = QGroupBox(self.regimentGroupBox_4_1)
        self.veterancyGroupBox_4_1.setObjectName(u"veterancyGroupBox_4_1")
        self.verticalLayout_59 = QVBoxLayout(self.veterancyGroupBox_4_1)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.veterancySpinBox_4_1 = QSpinBox(self.veterancyGroupBox_4_1)
        self.veterancySpinBox_4_1.setObjectName(u"veterancySpinBox_4_1")
        self.veterancySpinBox_4_1.setEnabled(False)
        self.veterancySpinBox_4_1.setMaximum(9)

        self.verticalLayout_59.addWidget(self.veterancySpinBox_4_1)


        self.verticalLayout_58.addWidget(self.veterancyGroupBox_4_1)


        self.verticalLayout_57.addWidget(self.regimentGroupBox_4_1)

        self.regimentGroupBox_4_2 = QGroupBox(self.divisionGroupBox_4)
        self.regimentGroupBox_4_2.setObjectName(u"regimentGroupBox_4_2")
        self.verticalLayout_60 = QVBoxLayout(self.regimentGroupBox_4_2)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.regimentTypeComboBox_4_2 = QComboBox(self.regimentGroupBox_4_2)
        self.regimentTypeComboBox_4_2.setObjectName(u"regimentTypeComboBox_4_2")
        self.regimentTypeComboBox_4_2.setEnabled(False)

        self.verticalLayout_60.addWidget(self.regimentTypeComboBox_4_2)

        self.veterancyGroupBox_4_2 = QGroupBox(self.regimentGroupBox_4_2)
        self.veterancyGroupBox_4_2.setObjectName(u"veterancyGroupBox_4_2")
        self.verticalLayout_61 = QVBoxLayout(self.veterancyGroupBox_4_2)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.veterancySpinBox_4_2 = QSpinBox(self.veterancyGroupBox_4_2)
        self.veterancySpinBox_4_2.setObjectName(u"veterancySpinBox_4_2")
        self.veterancySpinBox_4_2.setEnabled(False)
        self.veterancySpinBox_4_2.setMaximum(9)

        self.verticalLayout_61.addWidget(self.veterancySpinBox_4_2)


        self.verticalLayout_60.addWidget(self.veterancyGroupBox_4_2)


        self.verticalLayout_57.addWidget(self.regimentGroupBox_4_2)

        self.regimentGroupBox_4_3 = QGroupBox(self.divisionGroupBox_4)
        self.regimentGroupBox_4_3.setObjectName(u"regimentGroupBox_4_3")
        self.verticalLayout_67 = QVBoxLayout(self.regimentGroupBox_4_3)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.regimentTypeComboBox_4_3 = QComboBox(self.regimentGroupBox_4_3)
        self.regimentTypeComboBox_4_3.setObjectName(u"regimentTypeComboBox_4_3")
        self.regimentTypeComboBox_4_3.setEnabled(False)

        self.verticalLayout_67.addWidget(self.regimentTypeComboBox_4_3)

        self.veterancyGroupBox_4_3 = QGroupBox(self.regimentGroupBox_4_3)
        self.veterancyGroupBox_4_3.setObjectName(u"veterancyGroupBox_4_3")
        self.verticalLayout_68 = QVBoxLayout(self.veterancyGroupBox_4_3)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.veterancySpinBox_4_3 = QSpinBox(self.veterancyGroupBox_4_3)
        self.veterancySpinBox_4_3.setObjectName(u"veterancySpinBox_4_3")
        self.veterancySpinBox_4_3.setEnabled(False)
        self.veterancySpinBox_4_3.setMaximum(9)

        self.verticalLayout_68.addWidget(self.veterancySpinBox_4_3)


        self.verticalLayout_67.addWidget(self.veterancyGroupBox_4_3)


        self.verticalLayout_57.addWidget(self.regimentGroupBox_4_3)

        self.regimentGroupBox_4_4 = QGroupBox(self.divisionGroupBox_4)
        self.regimentGroupBox_4_4.setObjectName(u"regimentGroupBox_4_4")
        self.verticalLayout_92 = QVBoxLayout(self.regimentGroupBox_4_4)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.regimentTypeComboBox_4_4 = QComboBox(self.regimentGroupBox_4_4)
        self.regimentTypeComboBox_4_4.setObjectName(u"regimentTypeComboBox_4_4")
        self.regimentTypeComboBox_4_4.setEnabled(False)

        self.verticalLayout_92.addWidget(self.regimentTypeComboBox_4_4)

        self.veterancyGroupBox_4_4 = QGroupBox(self.regimentGroupBox_4_4)
        self.veterancyGroupBox_4_4.setObjectName(u"veterancyGroupBox_4_4")
        self.verticalLayout_100 = QVBoxLayout(self.veterancyGroupBox_4_4)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.veterancySpinBox_4_4 = QSpinBox(self.veterancyGroupBox_4_4)
        self.veterancySpinBox_4_4.setObjectName(u"veterancySpinBox_4_4")
        self.veterancySpinBox_4_4.setEnabled(False)
        self.veterancySpinBox_4_4.setMaximum(9)

        self.verticalLayout_100.addWidget(self.veterancySpinBox_4_4)


        self.verticalLayout_92.addWidget(self.veterancyGroupBox_4_4)


        self.verticalLayout_57.addWidget(self.regimentGroupBox_4_4)


        self.horizontalLayout_5.addWidget(self.divisionGroupBox_4)

        self.divisionGroupBox_2 = QGroupBox(self.horizontalWidget)
        self.divisionGroupBox_2.setObjectName(u"divisionGroupBox_2")
        self.verticalLayout_37 = QVBoxLayout(self.divisionGroupBox_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.divisionCheckBox_2 = QCheckBox(self.divisionGroupBox_2)
        self.divisionCheckBox_2.setObjectName(u"divisionCheckBox_2")
        self.divisionCheckBox_2.setEnabled(False)
        self.divisionCheckBox_2.setProperty(u"index", 1)

        self.verticalLayout_37.addWidget(self.divisionCheckBox_2)

        self.regimentGroupBox_2_1 = QGroupBox(self.divisionGroupBox_2)
        self.regimentGroupBox_2_1.setObjectName(u"regimentGroupBox_2_1")
        self.verticalLayout_44 = QVBoxLayout(self.regimentGroupBox_2_1)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.regimentTypeComboBox_2_1 = QComboBox(self.regimentGroupBox_2_1)
        self.regimentTypeComboBox_2_1.setObjectName(u"regimentTypeComboBox_2_1")
        self.regimentTypeComboBox_2_1.setEnabled(False)

        self.verticalLayout_44.addWidget(self.regimentTypeComboBox_2_1)

        self.veterancyGroupBox_2_1 = QGroupBox(self.regimentGroupBox_2_1)
        self.veterancyGroupBox_2_1.setObjectName(u"veterancyGroupBox_2_1")
        self.verticalLayout_45 = QVBoxLayout(self.veterancyGroupBox_2_1)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.veterancySpinBox_2_1 = QSpinBox(self.veterancyGroupBox_2_1)
        self.veterancySpinBox_2_1.setObjectName(u"veterancySpinBox_2_1")
        self.veterancySpinBox_2_1.setEnabled(False)
        self.veterancySpinBox_2_1.setMaximum(9)

        self.verticalLayout_45.addWidget(self.veterancySpinBox_2_1)


        self.verticalLayout_44.addWidget(self.veterancyGroupBox_2_1)


        self.verticalLayout_37.addWidget(self.regimentGroupBox_2_1)

        self.regimentGroupBox_2_2 = QGroupBox(self.divisionGroupBox_2)
        self.regimentGroupBox_2_2.setObjectName(u"regimentGroupBox_2_2")
        self.verticalLayout_46 = QVBoxLayout(self.regimentGroupBox_2_2)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.regimentTypeComboBox_2_2 = QComboBox(self.regimentGroupBox_2_2)
        self.regimentTypeComboBox_2_2.setObjectName(u"regimentTypeComboBox_2_2")
        self.regimentTypeComboBox_2_2.setEnabled(False)

        self.verticalLayout_46.addWidget(self.regimentTypeComboBox_2_2)

        self.veterancyGroupBox_2_2 = QGroupBox(self.regimentGroupBox_2_2)
        self.veterancyGroupBox_2_2.setObjectName(u"veterancyGroupBox_2_2")
        self.verticalLayout_47 = QVBoxLayout(self.veterancyGroupBox_2_2)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.veterancySpinBox_2_2 = QSpinBox(self.veterancyGroupBox_2_2)
        self.veterancySpinBox_2_2.setObjectName(u"veterancySpinBox_2_2")
        self.veterancySpinBox_2_2.setEnabled(False)
        self.veterancySpinBox_2_2.setMaximum(9)

        self.verticalLayout_47.addWidget(self.veterancySpinBox_2_2)


        self.verticalLayout_46.addWidget(self.veterancyGroupBox_2_2)


        self.verticalLayout_37.addWidget(self.regimentGroupBox_2_2)

        self.regimentGroupBox_2_3 = QGroupBox(self.divisionGroupBox_2)
        self.regimentGroupBox_2_3.setObjectName(u"regimentGroupBox_2_3")
        self.verticalLayout_48 = QVBoxLayout(self.regimentGroupBox_2_3)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.regimentTypeComboBox_2_3 = QComboBox(self.regimentGroupBox_2_3)
        self.regimentTypeComboBox_2_3.setObjectName(u"regimentTypeComboBox_2_3")
        self.regimentTypeComboBox_2_3.setEnabled(False)

        self.verticalLayout_48.addWidget(self.regimentTypeComboBox_2_3)

        self.veterancyGroupBox_2_3 = QGroupBox(self.regimentGroupBox_2_3)
        self.veterancyGroupBox_2_3.setObjectName(u"veterancyGroupBox_2_3")
        self.verticalLayout_49 = QVBoxLayout(self.veterancyGroupBox_2_3)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.veterancySpinBox_2_3 = QSpinBox(self.veterancyGroupBox_2_3)
        self.veterancySpinBox_2_3.setObjectName(u"veterancySpinBox_2_3")
        self.veterancySpinBox_2_3.setEnabled(False)
        self.veterancySpinBox_2_3.setMaximum(9)

        self.verticalLayout_49.addWidget(self.veterancySpinBox_2_3)


        self.verticalLayout_48.addWidget(self.veterancyGroupBox_2_3)


        self.verticalLayout_37.addWidget(self.regimentGroupBox_2_3)

        self.regimentGroupBox_2_4 = QGroupBox(self.divisionGroupBox_2)
        self.regimentGroupBox_2_4.setObjectName(u"regimentGroupBox_2_4")
        self.verticalLayout_72 = QVBoxLayout(self.regimentGroupBox_2_4)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.regimentTypeComboBox_2_4 = QComboBox(self.regimentGroupBox_2_4)
        self.regimentTypeComboBox_2_4.setObjectName(u"regimentTypeComboBox_2_4")
        self.regimentTypeComboBox_2_4.setEnabled(False)

        self.verticalLayout_72.addWidget(self.regimentTypeComboBox_2_4)

        self.veterancyGroupBox_2_4 = QGroupBox(self.regimentGroupBox_2_4)
        self.veterancyGroupBox_2_4.setObjectName(u"veterancyGroupBox_2_4")
        self.verticalLayout_98 = QVBoxLayout(self.veterancyGroupBox_2_4)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.veterancySpinBox_2_4 = QSpinBox(self.veterancyGroupBox_2_4)
        self.veterancySpinBox_2_4.setObjectName(u"veterancySpinBox_2_4")
        self.veterancySpinBox_2_4.setEnabled(False)
        self.veterancySpinBox_2_4.setMaximum(9)

        self.verticalLayout_98.addWidget(self.veterancySpinBox_2_4)


        self.verticalLayout_72.addWidget(self.veterancyGroupBox_2_4)


        self.verticalLayout_37.addWidget(self.regimentGroupBox_2_4)


        self.horizontalLayout_5.addWidget(self.divisionGroupBox_2)

        self.divisionGroupBox_1 = QGroupBox(self.horizontalWidget)
        self.divisionGroupBox_1.setObjectName(u"divisionGroupBox_1")
        self.divisionGroupBox_1.setEnabled(True)
        self.verticalLayout_36 = QVBoxLayout(self.divisionGroupBox_1)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.divisionCheckBox_1 = QCheckBox(self.divisionGroupBox_1)
        self.divisionCheckBox_1.setObjectName(u"divisionCheckBox_1")
        self.divisionCheckBox_1.setEnabled(False)
        self.divisionCheckBox_1.setCheckable(True)
        self.divisionCheckBox_1.setProperty(u"index", 0)

        self.verticalLayout_36.addWidget(self.divisionCheckBox_1)

        self.regimentGroupBox_1_1 = QGroupBox(self.divisionGroupBox_1)
        self.regimentGroupBox_1_1.setObjectName(u"regimentGroupBox_1_1")
        self.verticalLayout_38 = QVBoxLayout(self.regimentGroupBox_1_1)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.regimentTypeComboBox_1_1 = QComboBox(self.regimentGroupBox_1_1)
        self.regimentTypeComboBox_1_1.setObjectName(u"regimentTypeComboBox_1_1")
        self.regimentTypeComboBox_1_1.setEnabled(False)

        self.verticalLayout_38.addWidget(self.regimentTypeComboBox_1_1)

        self.veterancyGroupBox_1_1 = QGroupBox(self.regimentGroupBox_1_1)
        self.veterancyGroupBox_1_1.setObjectName(u"veterancyGroupBox_1_1")
        self.verticalLayout_39 = QVBoxLayout(self.veterancyGroupBox_1_1)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.veterancySpinBox_1_1 = QSpinBox(self.veterancyGroupBox_1_1)
        self.veterancySpinBox_1_1.setObjectName(u"veterancySpinBox_1_1")
        self.veterancySpinBox_1_1.setEnabled(False)
        self.veterancySpinBox_1_1.setMaximum(9)

        self.verticalLayout_39.addWidget(self.veterancySpinBox_1_1)


        self.verticalLayout_38.addWidget(self.veterancyGroupBox_1_1)


        self.verticalLayout_36.addWidget(self.regimentGroupBox_1_1)

        self.regimentGroupBox_1_2 = QGroupBox(self.divisionGroupBox_1)
        self.regimentGroupBox_1_2.setObjectName(u"regimentGroupBox_1_2")
        self.verticalLayout_40 = QVBoxLayout(self.regimentGroupBox_1_2)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.regimentTypeComboBox_1_2 = QComboBox(self.regimentGroupBox_1_2)
        self.regimentTypeComboBox_1_2.setObjectName(u"regimentTypeComboBox_1_2")
        self.regimentTypeComboBox_1_2.setEnabled(False)

        self.verticalLayout_40.addWidget(self.regimentTypeComboBox_1_2)

        self.veterancyGroupBox_1_2 = QGroupBox(self.regimentGroupBox_1_2)
        self.veterancyGroupBox_1_2.setObjectName(u"veterancyGroupBox_1_2")
        self.verticalLayout_41 = QVBoxLayout(self.veterancyGroupBox_1_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.veterancySpinBox_1_2 = QSpinBox(self.veterancyGroupBox_1_2)
        self.veterancySpinBox_1_2.setObjectName(u"veterancySpinBox_1_2")
        self.veterancySpinBox_1_2.setEnabled(False)
        self.veterancySpinBox_1_2.setMaximum(9)

        self.verticalLayout_41.addWidget(self.veterancySpinBox_1_2)


        self.verticalLayout_40.addWidget(self.veterancyGroupBox_1_2)


        self.verticalLayout_36.addWidget(self.regimentGroupBox_1_2)

        self.regimentGroupBox_1_3 = QGroupBox(self.divisionGroupBox_1)
        self.regimentGroupBox_1_3.setObjectName(u"regimentGroupBox_1_3")
        self.verticalLayout_42 = QVBoxLayout(self.regimentGroupBox_1_3)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.regimentTypeComboBox_1_3 = QComboBox(self.regimentGroupBox_1_3)
        self.regimentTypeComboBox_1_3.setObjectName(u"regimentTypeComboBox_1_3")
        self.regimentTypeComboBox_1_3.setEnabled(False)

        self.verticalLayout_42.addWidget(self.regimentTypeComboBox_1_3)

        self.veterancyGroupBox_1_3 = QGroupBox(self.regimentGroupBox_1_3)
        self.veterancyGroupBox_1_3.setObjectName(u"veterancyGroupBox_1_3")
        self.verticalLayout_43 = QVBoxLayout(self.veterancyGroupBox_1_3)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.veterancySpinBox_1_3 = QSpinBox(self.veterancyGroupBox_1_3)
        self.veterancySpinBox_1_3.setObjectName(u"veterancySpinBox_1_3")
        self.veterancySpinBox_1_3.setEnabled(False)
        self.veterancySpinBox_1_3.setMaximum(9)

        self.verticalLayout_43.addWidget(self.veterancySpinBox_1_3)


        self.verticalLayout_42.addWidget(self.veterancyGroupBox_1_3)


        self.verticalLayout_36.addWidget(self.regimentGroupBox_1_3)

        self.regimentGroupBox_1_4 = QGroupBox(self.divisionGroupBox_1)
        self.regimentGroupBox_1_4.setObjectName(u"regimentGroupBox_1_4")
        self.verticalLayout_71 = QVBoxLayout(self.regimentGroupBox_1_4)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.regimentTypeComboBox_1_4 = QComboBox(self.regimentGroupBox_1_4)
        self.regimentTypeComboBox_1_4.setObjectName(u"regimentTypeComboBox_1_4")
        self.regimentTypeComboBox_1_4.setEnabled(False)

        self.verticalLayout_71.addWidget(self.regimentTypeComboBox_1_4)

        self.veterancyGroupBox_1_4 = QGroupBox(self.regimentGroupBox_1_4)
        self.veterancyGroupBox_1_4.setObjectName(u"veterancyGroupBox_1_4")
        self.verticalLayout_93 = QVBoxLayout(self.veterancyGroupBox_1_4)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.veterancySpinBox_1_4 = QSpinBox(self.veterancyGroupBox_1_4)
        self.veterancySpinBox_1_4.setObjectName(u"veterancySpinBox_1_4")
        self.veterancySpinBox_1_4.setEnabled(False)
        self.veterancySpinBox_1_4.setMaximum(9)

        self.verticalLayout_93.addWidget(self.veterancySpinBox_1_4)


        self.verticalLayout_71.addWidget(self.veterancyGroupBox_1_4)


        self.verticalLayout_36.addWidget(self.regimentGroupBox_1_4)


        self.horizontalLayout_5.addWidget(self.divisionGroupBox_1)

        self.divisionGroupBox_3 = QGroupBox(self.horizontalWidget)
        self.divisionGroupBox_3.setObjectName(u"divisionGroupBox_3")
        self.verticalLayout_50 = QVBoxLayout(self.divisionGroupBox_3)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.divisionCheckBox_3 = QCheckBox(self.divisionGroupBox_3)
        self.divisionCheckBox_3.setObjectName(u"divisionCheckBox_3")
        self.divisionCheckBox_3.setEnabled(False)
        self.divisionCheckBox_3.setProperty(u"index", 2)

        self.verticalLayout_50.addWidget(self.divisionCheckBox_3)

        self.regimentGroupBox_3_1 = QGroupBox(self.divisionGroupBox_3)
        self.regimentGroupBox_3_1.setObjectName(u"regimentGroupBox_3_1")
        self.regimentGroupBox_3_1.setEnabled(True)
        self.verticalLayout_51 = QVBoxLayout(self.regimentGroupBox_3_1)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.regimentTypeComboBox_3_1 = QComboBox(self.regimentGroupBox_3_1)
        self.regimentTypeComboBox_3_1.setObjectName(u"regimentTypeComboBox_3_1")
        self.regimentTypeComboBox_3_1.setEnabled(False)

        self.verticalLayout_51.addWidget(self.regimentTypeComboBox_3_1)

        self.veterancyGroupBox_3_1 = QGroupBox(self.regimentGroupBox_3_1)
        self.veterancyGroupBox_3_1.setObjectName(u"veterancyGroupBox_3_1")
        self.verticalLayout_52 = QVBoxLayout(self.veterancyGroupBox_3_1)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.veterancySpinBox_3_1 = QSpinBox(self.veterancyGroupBox_3_1)
        self.veterancySpinBox_3_1.setObjectName(u"veterancySpinBox_3_1")
        self.veterancySpinBox_3_1.setEnabled(False)
        self.veterancySpinBox_3_1.setMaximum(9)

        self.verticalLayout_52.addWidget(self.veterancySpinBox_3_1)


        self.verticalLayout_51.addWidget(self.veterancyGroupBox_3_1)


        self.verticalLayout_50.addWidget(self.regimentGroupBox_3_1)

        self.regimentGroupBox_3_2 = QGroupBox(self.divisionGroupBox_3)
        self.regimentGroupBox_3_2.setObjectName(u"regimentGroupBox_3_2")
        self.verticalLayout_53 = QVBoxLayout(self.regimentGroupBox_3_2)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.regimentTypeComboBox_3_2 = QComboBox(self.regimentGroupBox_3_2)
        self.regimentTypeComboBox_3_2.setObjectName(u"regimentTypeComboBox_3_2")
        self.regimentTypeComboBox_3_2.setEnabled(False)

        self.verticalLayout_53.addWidget(self.regimentTypeComboBox_3_2)

        self.veterancyGroupBox_3_2 = QGroupBox(self.regimentGroupBox_3_2)
        self.veterancyGroupBox_3_2.setObjectName(u"veterancyGroupBox_3_2")
        self.verticalLayout_54 = QVBoxLayout(self.veterancyGroupBox_3_2)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.veterancySpinBox_3_2 = QSpinBox(self.veterancyGroupBox_3_2)
        self.veterancySpinBox_3_2.setObjectName(u"veterancySpinBox_3_2")
        self.veterancySpinBox_3_2.setEnabled(False)
        self.veterancySpinBox_3_2.setMaximum(9)

        self.verticalLayout_54.addWidget(self.veterancySpinBox_3_2)


        self.verticalLayout_53.addWidget(self.veterancyGroupBox_3_2)


        self.verticalLayout_50.addWidget(self.regimentGroupBox_3_2)

        self.regimentGroupBox_3_3 = QGroupBox(self.divisionGroupBox_3)
        self.regimentGroupBox_3_3.setObjectName(u"regimentGroupBox_3_3")
        self.verticalLayout_55 = QVBoxLayout(self.regimentGroupBox_3_3)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.regimentTypeComboBox_3_3 = QComboBox(self.regimentGroupBox_3_3)
        self.regimentTypeComboBox_3_3.setObjectName(u"regimentTypeComboBox_3_3")
        self.regimentTypeComboBox_3_3.setEnabled(False)

        self.verticalLayout_55.addWidget(self.regimentTypeComboBox_3_3)

        self.veterancyGroupBox_3_3 = QGroupBox(self.regimentGroupBox_3_3)
        self.veterancyGroupBox_3_3.setObjectName(u"veterancyGroupBox_3_3")
        self.verticalLayout_56 = QVBoxLayout(self.veterancyGroupBox_3_3)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.veterancySpinBox_3_3 = QSpinBox(self.veterancyGroupBox_3_3)
        self.veterancySpinBox_3_3.setObjectName(u"veterancySpinBox_3_3")
        self.veterancySpinBox_3_3.setEnabled(False)
        self.veterancySpinBox_3_3.setMaximum(9)

        self.verticalLayout_56.addWidget(self.veterancySpinBox_3_3)


        self.verticalLayout_55.addWidget(self.veterancyGroupBox_3_3)


        self.verticalLayout_50.addWidget(self.regimentGroupBox_3_3)

        self.regimentGroupBox_3_4 = QGroupBox(self.divisionGroupBox_3)
        self.regimentGroupBox_3_4.setObjectName(u"regimentGroupBox_3_4")
        self.verticalLayout_73 = QVBoxLayout(self.regimentGroupBox_3_4)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.regimentTypeComboBox_3_4 = QComboBox(self.regimentGroupBox_3_4)
        self.regimentTypeComboBox_3_4.setObjectName(u"regimentTypeComboBox_3_4")
        self.regimentTypeComboBox_3_4.setEnabled(False)

        self.verticalLayout_73.addWidget(self.regimentTypeComboBox_3_4)

        self.veterancyGroupBox_3_4 = QGroupBox(self.regimentGroupBox_3_4)
        self.veterancyGroupBox_3_4.setObjectName(u"veterancyGroupBox_3_4")
        self.verticalLayout_99 = QVBoxLayout(self.veterancyGroupBox_3_4)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.veterancySpinBox_3_4 = QSpinBox(self.veterancyGroupBox_3_4)
        self.veterancySpinBox_3_4.setObjectName(u"veterancySpinBox_3_4")
        self.veterancySpinBox_3_4.setEnabled(False)
        self.veterancySpinBox_3_4.setMaximum(9)

        self.verticalLayout_99.addWidget(self.veterancySpinBox_3_4)


        self.verticalLayout_73.addWidget(self.veterancyGroupBox_3_4)


        self.verticalLayout_50.addWidget(self.regimentGroupBox_3_4)


        self.horizontalLayout_5.addWidget(self.divisionGroupBox_3)

        self.divisionGroupBox_5 = QGroupBox(self.horizontalWidget)
        self.divisionGroupBox_5.setObjectName(u"divisionGroupBox_5")
        self.divisionGroupBox_5.setEnabled(True)
        self.verticalLayout_69 = QVBoxLayout(self.divisionGroupBox_5)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.divisionCheckBox_5 = QCheckBox(self.divisionGroupBox_5)
        self.divisionCheckBox_5.setObjectName(u"divisionCheckBox_5")
        self.divisionCheckBox_5.setEnabled(False)
        self.divisionCheckBox_5.setProperty(u"index", 4)

        self.verticalLayout_69.addWidget(self.divisionCheckBox_5)

        self.regimentGroupBox_5_1 = QGroupBox(self.divisionGroupBox_5)
        self.regimentGroupBox_5_1.setObjectName(u"regimentGroupBox_5_1")
        self.verticalLayout_70 = QVBoxLayout(self.regimentGroupBox_5_1)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.regimentTypeComboBox_5_1 = QComboBox(self.regimentGroupBox_5_1)
        self.regimentTypeComboBox_5_1.setObjectName(u"regimentTypeComboBox_5_1")
        self.regimentTypeComboBox_5_1.setEnabled(False)

        self.verticalLayout_70.addWidget(self.regimentTypeComboBox_5_1)

        self.veterancyGroupBox_5_1 = QGroupBox(self.regimentGroupBox_5_1)
        self.veterancyGroupBox_5_1.setObjectName(u"veterancyGroupBox_5_1")
        self.veterancyGroupBox_5_1.setEnabled(True)
        self.verticalLayout_101 = QVBoxLayout(self.veterancyGroupBox_5_1)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.veterancySpinBox_5_1 = QSpinBox(self.veterancyGroupBox_5_1)
        self.veterancySpinBox_5_1.setObjectName(u"veterancySpinBox_5_1")
        self.veterancySpinBox_5_1.setEnabled(False)
        self.veterancySpinBox_5_1.setMaximum(9)

        self.verticalLayout_101.addWidget(self.veterancySpinBox_5_1)


        self.verticalLayout_70.addWidget(self.veterancyGroupBox_5_1)


        self.verticalLayout_69.addWidget(self.regimentGroupBox_5_1)

        self.regimentGroupBox_5_2 = QGroupBox(self.divisionGroupBox_5)
        self.regimentGroupBox_5_2.setObjectName(u"regimentGroupBox_5_2")
        self.verticalLayout_102 = QVBoxLayout(self.regimentGroupBox_5_2)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.regimentTypeComboBox_5_2 = QComboBox(self.regimentGroupBox_5_2)
        self.regimentTypeComboBox_5_2.setObjectName(u"regimentTypeComboBox_5_2")
        self.regimentTypeComboBox_5_2.setEnabled(False)

        self.verticalLayout_102.addWidget(self.regimentTypeComboBox_5_2)

        self.veterancyGroupBox_5_2 = QGroupBox(self.regimentGroupBox_5_2)
        self.veterancyGroupBox_5_2.setObjectName(u"veterancyGroupBox_5_2")
        self.verticalLayout_103 = QVBoxLayout(self.veterancyGroupBox_5_2)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.veterancySpinBox_5_2 = QSpinBox(self.veterancyGroupBox_5_2)
        self.veterancySpinBox_5_2.setObjectName(u"veterancySpinBox_5_2")
        self.veterancySpinBox_5_2.setEnabled(False)
        self.veterancySpinBox_5_2.setMaximum(9)

        self.verticalLayout_103.addWidget(self.veterancySpinBox_5_2)


        self.verticalLayout_102.addWidget(self.veterancyGroupBox_5_2)


        self.verticalLayout_69.addWidget(self.regimentGroupBox_5_2)

        self.regimentGroupBox_5_3 = QGroupBox(self.divisionGroupBox_5)
        self.regimentGroupBox_5_3.setObjectName(u"regimentGroupBox_5_3")
        self.verticalLayout_11 = QVBoxLayout(self.regimentGroupBox_5_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.regimentTypeComboBox_5_3 = QComboBox(self.regimentGroupBox_5_3)
        self.regimentTypeComboBox_5_3.setObjectName(u"regimentTypeComboBox_5_3")
        self.regimentTypeComboBox_5_3.setEnabled(False)

        self.verticalLayout_11.addWidget(self.regimentTypeComboBox_5_3)

        self.veterancyGroupBox_5_3 = QGroupBox(self.regimentGroupBox_5_3)
        self.veterancyGroupBox_5_3.setObjectName(u"veterancyGroupBox_5_3")
        self.verticalLayout_105 = QVBoxLayout(self.veterancyGroupBox_5_3)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.veterancySpinBox_5_3 = QSpinBox(self.veterancyGroupBox_5_3)
        self.veterancySpinBox_5_3.setObjectName(u"veterancySpinBox_5_3")
        self.veterancySpinBox_5_3.setEnabled(False)
        self.veterancySpinBox_5_3.setMaximum(9)

        self.verticalLayout_105.addWidget(self.veterancySpinBox_5_3)


        self.verticalLayout_11.addWidget(self.veterancyGroupBox_5_3)


        self.verticalLayout_69.addWidget(self.regimentGroupBox_5_3)

        self.regimentGroupBox_5_4 = QGroupBox(self.divisionGroupBox_5)
        self.regimentGroupBox_5_4.setObjectName(u"regimentGroupBox_5_4")
        self.verticalLayout_106 = QVBoxLayout(self.regimentGroupBox_5_4)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.regimentTypeComboBox_5_4 = QComboBox(self.regimentGroupBox_5_4)
        self.regimentTypeComboBox_5_4.setObjectName(u"regimentTypeComboBox_5_4")
        self.regimentTypeComboBox_5_4.setEnabled(False)

        self.verticalLayout_106.addWidget(self.regimentTypeComboBox_5_4)

        self.veterancyGroupBox_5_4 = QGroupBox(self.regimentGroupBox_5_4)
        self.veterancyGroupBox_5_4.setObjectName(u"veterancyGroupBox_5_4")
        self.verticalLayout_107 = QVBoxLayout(self.veterancyGroupBox_5_4)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.veterancySpinBox_5_4 = QSpinBox(self.veterancyGroupBox_5_4)
        self.veterancySpinBox_5_4.setObjectName(u"veterancySpinBox_5_4")
        self.veterancySpinBox_5_4.setEnabled(False)
        self.veterancySpinBox_5_4.setMaximum(9)

        self.verticalLayout_107.addWidget(self.veterancySpinBox_5_4)


        self.verticalLayout_106.addWidget(self.veterancyGroupBox_5_4)


        self.verticalLayout_69.addWidget(self.regimentGroupBox_5_4)


        self.horizontalLayout_5.addWidget(self.divisionGroupBox_5)


        self.verticalLayout_91.addWidget(self.horizontalWidget)

        self.reserveGroupBox = QGroupBox(self.armyTab)
        self.reserveGroupBox.setObjectName(u"reserveGroupBox")
        self.reserveGroupBox.setEnabled(True)
        self.horizontalLayout_3 = QHBoxLayout(self.reserveGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.reserveGroupBox_1 = QGroupBox(self.reserveGroupBox)
        self.reserveGroupBox_1.setObjectName(u"reserveGroupBox_1")
        self.verticalLayout_6 = QVBoxLayout(self.reserveGroupBox_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.reserveTypeComboBox_1 = QComboBox(self.reserveGroupBox_1)
        self.reserveTypeComboBox_1.setObjectName(u"reserveTypeComboBox_1")
        self.reserveTypeComboBox_1.setEnabled(False)

        self.verticalLayout_6.addWidget(self.reserveTypeComboBox_1)

        self.reserveVeterancyGroupBox_1 = QGroupBox(self.reserveGroupBox_1)
        self.reserveVeterancyGroupBox_1.setObjectName(u"reserveVeterancyGroupBox_1")
        self.verticalLayout_62 = QVBoxLayout(self.reserveVeterancyGroupBox_1)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.reserveVeterancySpinBox_1 = QSpinBox(self.reserveVeterancyGroupBox_1)
        self.reserveVeterancySpinBox_1.setObjectName(u"reserveVeterancySpinBox_1")
        self.reserveVeterancySpinBox_1.setEnabled(False)
        self.reserveVeterancySpinBox_1.setMaximum(9)

        self.verticalLayout_62.addWidget(self.reserveVeterancySpinBox_1)


        self.verticalLayout_6.addWidget(self.reserveVeterancyGroupBox_1)


        self.horizontalLayout_3.addWidget(self.reserveGroupBox_1)

        self.reserveGroupBox_2 = QGroupBox(self.reserveGroupBox)
        self.reserveGroupBox_2.setObjectName(u"reserveGroupBox_2")
        self.verticalLayout_7 = QVBoxLayout(self.reserveGroupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.reserveTypeComboBox_2 = QComboBox(self.reserveGroupBox_2)
        self.reserveTypeComboBox_2.setObjectName(u"reserveTypeComboBox_2")
        self.reserveTypeComboBox_2.setEnabled(False)

        self.verticalLayout_7.addWidget(self.reserveTypeComboBox_2)

        self.reserveVeterancyGroupBox_2 = QGroupBox(self.reserveGroupBox_2)
        self.reserveVeterancyGroupBox_2.setObjectName(u"reserveVeterancyGroupBox_2")
        self.verticalLayout_63 = QVBoxLayout(self.reserveVeterancyGroupBox_2)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.reserveVeterancySpinBox_2 = QSpinBox(self.reserveVeterancyGroupBox_2)
        self.reserveVeterancySpinBox_2.setObjectName(u"reserveVeterancySpinBox_2")
        self.reserveVeterancySpinBox_2.setEnabled(False)
        self.reserveVeterancySpinBox_2.setMaximum(9)

        self.verticalLayout_63.addWidget(self.reserveVeterancySpinBox_2)


        self.verticalLayout_7.addWidget(self.reserveVeterancyGroupBox_2)


        self.horizontalLayout_3.addWidget(self.reserveGroupBox_2)

        self.reserveGroupBox_3 = QGroupBox(self.reserveGroupBox)
        self.reserveGroupBox_3.setObjectName(u"reserveGroupBox_3")
        self.verticalLayout_8 = QVBoxLayout(self.reserveGroupBox_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.reserveTypeComboBox_3 = QComboBox(self.reserveGroupBox_3)
        self.reserveTypeComboBox_3.setObjectName(u"reserveTypeComboBox_3")
        self.reserveTypeComboBox_3.setEnabled(False)

        self.verticalLayout_8.addWidget(self.reserveTypeComboBox_3)

        self.reserveVeterancyGroupBox_3 = QGroupBox(self.reserveGroupBox_3)
        self.reserveVeterancyGroupBox_3.setObjectName(u"reserveVeterancyGroupBox_3")
        self.verticalLayout_64 = QVBoxLayout(self.reserveVeterancyGroupBox_3)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.reserveVeterancySpinBox_3 = QSpinBox(self.reserveVeterancyGroupBox_3)
        self.reserveVeterancySpinBox_3.setObjectName(u"reserveVeterancySpinBox_3")
        self.reserveVeterancySpinBox_3.setEnabled(False)
        self.reserveVeterancySpinBox_3.setMaximum(9)

        self.verticalLayout_64.addWidget(self.reserveVeterancySpinBox_3)


        self.verticalLayout_8.addWidget(self.reserveVeterancyGroupBox_3)


        self.horizontalLayout_3.addWidget(self.reserveGroupBox_3)

        self.reserveGroupBox_4 = QGroupBox(self.reserveGroupBox)
        self.reserveGroupBox_4.setObjectName(u"reserveGroupBox_4")
        self.verticalLayout_9 = QVBoxLayout(self.reserveGroupBox_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.reserveTypeComboBox_4 = QComboBox(self.reserveGroupBox_4)
        self.reserveTypeComboBox_4.setObjectName(u"reserveTypeComboBox_4")
        self.reserveTypeComboBox_4.setEnabled(False)

        self.verticalLayout_9.addWidget(self.reserveTypeComboBox_4)

        self.reserveVeterancyGroupBox_4 = QGroupBox(self.reserveGroupBox_4)
        self.reserveVeterancyGroupBox_4.setObjectName(u"reserveVeterancyGroupBox_4")
        self.verticalLayout_65 = QVBoxLayout(self.reserveVeterancyGroupBox_4)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.reserveVeterancySpinBox_4 = QSpinBox(self.reserveVeterancyGroupBox_4)
        self.reserveVeterancySpinBox_4.setObjectName(u"reserveVeterancySpinBox_4")
        self.reserveVeterancySpinBox_4.setEnabled(False)
        self.reserveVeterancySpinBox_4.setMaximum(9)

        self.verticalLayout_65.addWidget(self.reserveVeterancySpinBox_4)


        self.verticalLayout_9.addWidget(self.reserveVeterancyGroupBox_4)


        self.horizontalLayout_3.addWidget(self.reserveGroupBox_4)

        self.reserveGroupBox_5 = QGroupBox(self.reserveGroupBox)
        self.reserveGroupBox_5.setObjectName(u"reserveGroupBox_5")
        self.verticalLayout_10 = QVBoxLayout(self.reserveGroupBox_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.reserveTypeComboBox_5 = QComboBox(self.reserveGroupBox_5)
        self.reserveTypeComboBox_5.setObjectName(u"reserveTypeComboBox_5")
        self.reserveTypeComboBox_5.setEnabled(False)

        self.verticalLayout_10.addWidget(self.reserveTypeComboBox_5)

        self.reserveVeterancyGroupBox_5 = QGroupBox(self.reserveGroupBox_5)
        self.reserveVeterancyGroupBox_5.setObjectName(u"reserveVeterancyGroupBox_5")
        self.verticalLayout_66 = QVBoxLayout(self.reserveVeterancyGroupBox_5)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.reserveVeterancySpinBox_5 = QSpinBox(self.reserveVeterancyGroupBox_5)
        self.reserveVeterancySpinBox_5.setObjectName(u"reserveVeterancySpinBox_5")
        self.reserveVeterancySpinBox_5.setEnabled(False)
        self.reserveVeterancySpinBox_5.setMaximum(9)

        self.verticalLayout_66.addWidget(self.reserveVeterancySpinBox_5)


        self.verticalLayout_10.addWidget(self.reserveVeterancyGroupBox_5)


        self.horizontalLayout_3.addWidget(self.reserveGroupBox_5)


        self.verticalLayout_91.addWidget(self.reserveGroupBox)

        self.tabWidget.addTab(self.armyTab, "")
        self.leaderTab = QWidget()
        self.leaderTab.setObjectName(u"leaderTab")
        self.verticalLayout_90 = QVBoxLayout(self.leaderTab)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.leaderGroupBox = QGroupBox(self.leaderTab)
        self.leaderGroupBox.setObjectName(u"leaderGroupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.leaderGroupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leaderGroupBox_4 = QGroupBox(self.leaderGroupBox)
        self.leaderGroupBox_4.setObjectName(u"leaderGroupBox_4")
        self.verticalLayout_31 = QVBoxLayout(self.leaderGroupBox_4)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.leaderNameGroupBox_4 = QGroupBox(self.leaderGroupBox_4)
        self.leaderNameGroupBox_4.setObjectName(u"leaderNameGroupBox_4")
        self.verticalLayout_17 = QVBoxLayout(self.leaderNameGroupBox_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.leaderNameLabel_4 = QLabel(self.leaderNameGroupBox_4)
        self.leaderNameLabel_4.setObjectName(u"leaderNameLabel_4")
        self.leaderNameLabel_4.setAutoFillBackground(False)
        self.leaderNameLabel_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.leaderNameLabel_4)


        self.verticalLayout_31.addWidget(self.leaderNameGroupBox_4)

        self.leaderComboBox_4_1 = QComboBox(self.leaderGroupBox_4)
        self.leaderComboBox_4_1.setObjectName(u"leaderComboBox_4_1")
        self.leaderComboBox_4_1.setEnabled(False)

        self.verticalLayout_31.addWidget(self.leaderComboBox_4_1)

        self.leaderComboBox_4_2 = QComboBox(self.leaderGroupBox_4)
        self.leaderComboBox_4_2.setObjectName(u"leaderComboBox_4_2")
        self.leaderComboBox_4_2.setEnabled(False)

        self.verticalLayout_31.addWidget(self.leaderComboBox_4_2)

        self.leaderComboBox_4_3 = QComboBox(self.leaderGroupBox_4)
        self.leaderComboBox_4_3.setObjectName(u"leaderComboBox_4_3")
        self.leaderComboBox_4_3.setEnabled(False)

        self.verticalLayout_31.addWidget(self.leaderComboBox_4_3)

        self.leaderComboBox_4_4 = QComboBox(self.leaderGroupBox_4)
        self.leaderComboBox_4_4.setObjectName(u"leaderComboBox_4_4")
        self.leaderComboBox_4_4.setEnabled(False)

        self.verticalLayout_31.addWidget(self.leaderComboBox_4_4)

        self.leaderComboBox_4_5 = QComboBox(self.leaderGroupBox_4)
        self.leaderComboBox_4_5.setObjectName(u"leaderComboBox_4_5")
        self.leaderComboBox_4_5.setEnabled(False)

        self.verticalLayout_31.addWidget(self.leaderComboBox_4_5)

        self.leaderLevelGroupBox_4 = QGroupBox(self.leaderGroupBox_4)
        self.leaderLevelGroupBox_4.setObjectName(u"leaderLevelGroupBox_4")
        self.verticalLayout_87 = QVBoxLayout(self.leaderLevelGroupBox_4)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.leaderLevelSpinBox_4 = QSpinBox(self.leaderLevelGroupBox_4)
        self.leaderLevelSpinBox_4.setObjectName(u"leaderLevelSpinBox_4")
        self.leaderLevelSpinBox_4.setEnabled(False)
        self.leaderLevelSpinBox_4.setMinimum(1)
        self.leaderLevelSpinBox_4.setMaximum(5)

        self.verticalLayout_87.addWidget(self.leaderLevelSpinBox_4)


        self.verticalLayout_31.addWidget(self.leaderLevelGroupBox_4)

        self.leaderSkillPointGroupBox_4 = QGroupBox(self.leaderGroupBox_4)
        self.leaderSkillPointGroupBox_4.setObjectName(u"leaderSkillPointGroupBox_4")
        self.verticalLayout_110 = QVBoxLayout(self.leaderSkillPointGroupBox_4)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.leaderSkillPointSpinBox_4 = QSpinBox(self.leaderSkillPointGroupBox_4)
        self.leaderSkillPointSpinBox_4.setObjectName(u"leaderSkillPointSpinBox_4")
        self.leaderSkillPointSpinBox_4.setEnabled(False)

        self.verticalLayout_110.addWidget(self.leaderSkillPointSpinBox_4)


        self.verticalLayout_31.addWidget(self.leaderSkillPointGroupBox_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.deleteLeaderButton_4 = QPushButton(self.leaderGroupBox_4)
        self.deleteLeaderButton_4.setObjectName(u"deleteLeaderButton_4")
        self.deleteLeaderButton_4.setEnabled(False)
        self.deleteLeaderButton_4.setProperty(u"index", 3)
        self.deleteLeaderButton_4.setProperty(u"reserveLeader", False)

        self.horizontalLayout_15.addWidget(self.deleteLeaderButton_4)

        self.createLeaderButton_4 = QPushButton(self.leaderGroupBox_4)
        self.createLeaderButton_4.setObjectName(u"createLeaderButton_4")
        self.createLeaderButton_4.setEnabled(False)
        self.createLeaderButton_4.setProperty(u"index", 3)
        self.createLeaderButton_4.setProperty(u"reserveLeader", False)

        self.horizontalLayout_15.addWidget(self.createLeaderButton_4)


        self.verticalLayout_31.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_4.addWidget(self.leaderGroupBox_4)

        self.leaderGroupBox_2 = QGroupBox(self.leaderGroupBox)
        self.leaderGroupBox_2.setObjectName(u"leaderGroupBox_2")
        self.verticalLayout_82 = QVBoxLayout(self.leaderGroupBox_2)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.leaderNameGroupBox_2 = QGroupBox(self.leaderGroupBox_2)
        self.leaderNameGroupBox_2.setObjectName(u"leaderNameGroupBox_2")
        self.verticalLayout_15 = QVBoxLayout(self.leaderNameGroupBox_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.leaderNameLabel_2 = QLabel(self.leaderNameGroupBox_2)
        self.leaderNameLabel_2.setObjectName(u"leaderNameLabel_2")
        self.leaderNameLabel_2.setAutoFillBackground(False)
        self.leaderNameLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.leaderNameLabel_2)


        self.verticalLayout_82.addWidget(self.leaderNameGroupBox_2)

        self.leaderComboBox_2_1 = QComboBox(self.leaderGroupBox_2)
        self.leaderComboBox_2_1.setObjectName(u"leaderComboBox_2_1")
        self.leaderComboBox_2_1.setEnabled(False)

        self.verticalLayout_82.addWidget(self.leaderComboBox_2_1)

        self.leaderComboBox_2_2 = QComboBox(self.leaderGroupBox_2)
        self.leaderComboBox_2_2.setObjectName(u"leaderComboBox_2_2")
        self.leaderComboBox_2_2.setEnabled(False)

        self.verticalLayout_82.addWidget(self.leaderComboBox_2_2)

        self.leaderComboBox_2_3 = QComboBox(self.leaderGroupBox_2)
        self.leaderComboBox_2_3.setObjectName(u"leaderComboBox_2_3")
        self.leaderComboBox_2_3.setEnabled(False)

        self.verticalLayout_82.addWidget(self.leaderComboBox_2_3)

        self.leaderComboBox_2_4 = QComboBox(self.leaderGroupBox_2)
        self.leaderComboBox_2_4.setObjectName(u"leaderComboBox_2_4")
        self.leaderComboBox_2_4.setEnabled(False)

        self.verticalLayout_82.addWidget(self.leaderComboBox_2_4)

        self.leaderComboBox_2_5 = QComboBox(self.leaderGroupBox_2)
        self.leaderComboBox_2_5.setObjectName(u"leaderComboBox_2_5")
        self.leaderComboBox_2_5.setEnabled(False)

        self.verticalLayout_82.addWidget(self.leaderComboBox_2_5)

        self.leaderLevelGroupBox_2 = QGroupBox(self.leaderGroupBox_2)
        self.leaderLevelGroupBox_2.setObjectName(u"leaderLevelGroupBox_2")
        self.verticalLayout_83 = QVBoxLayout(self.leaderLevelGroupBox_2)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.leaderLevelSpinBox_2 = QSpinBox(self.leaderLevelGroupBox_2)
        self.leaderLevelSpinBox_2.setObjectName(u"leaderLevelSpinBox_2")
        self.leaderLevelSpinBox_2.setEnabled(False)
        self.leaderLevelSpinBox_2.setMinimum(1)
        self.leaderLevelSpinBox_2.setMaximum(5)

        self.verticalLayout_83.addWidget(self.leaderLevelSpinBox_2)


        self.verticalLayout_82.addWidget(self.leaderLevelGroupBox_2)

        self.leaderSkillPointGroupBox_2 = QGroupBox(self.leaderGroupBox_2)
        self.leaderSkillPointGroupBox_2.setObjectName(u"leaderSkillPointGroupBox_2")
        self.verticalLayout_104 = QVBoxLayout(self.leaderSkillPointGroupBox_2)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.leaderSkillPointSpinBox_2 = QSpinBox(self.leaderSkillPointGroupBox_2)
        self.leaderSkillPointSpinBox_2.setObjectName(u"leaderSkillPointSpinBox_2")
        self.leaderSkillPointSpinBox_2.setEnabled(False)

        self.verticalLayout_104.addWidget(self.leaderSkillPointSpinBox_2)


        self.verticalLayout_82.addWidget(self.leaderSkillPointGroupBox_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.deleteLeaderButton_2 = QPushButton(self.leaderGroupBox_2)
        self.deleteLeaderButton_2.setObjectName(u"deleteLeaderButton_2")
        self.deleteLeaderButton_2.setEnabled(False)
        self.deleteLeaderButton_2.setProperty(u"index", 1)
        self.deleteLeaderButton_2.setProperty(u"reserveLeader", False)

        self.horizontalLayout_6.addWidget(self.deleteLeaderButton_2)

        self.createLeaderButton_2 = QPushButton(self.leaderGroupBox_2)
        self.createLeaderButton_2.setObjectName(u"createLeaderButton_2")
        self.createLeaderButton_2.setEnabled(False)
        self.createLeaderButton_2.setProperty(u"index", 1)
        self.createLeaderButton_2.setProperty(u"reserveLeader", False)

        self.horizontalLayout_6.addWidget(self.createLeaderButton_2)


        self.verticalLayout_82.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_4.addWidget(self.leaderGroupBox_2)

        self.leaderGroupBox_1 = QGroupBox(self.leaderGroupBox)
        self.leaderGroupBox_1.setObjectName(u"leaderGroupBox_1")
        self.verticalLayout_12 = QVBoxLayout(self.leaderGroupBox_1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.leaderNameGroupBox_1 = QGroupBox(self.leaderGroupBox_1)
        self.leaderNameGroupBox_1.setObjectName(u"leaderNameGroupBox_1")
        self.verticalLayout_14 = QVBoxLayout(self.leaderNameGroupBox_1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.leaderNameLabel_1 = QLabel(self.leaderNameGroupBox_1)
        self.leaderNameLabel_1.setObjectName(u"leaderNameLabel_1")
        self.leaderNameLabel_1.setAutoFillBackground(False)
        self.leaderNameLabel_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.leaderNameLabel_1)


        self.verticalLayout_12.addWidget(self.leaderNameGroupBox_1)

        self.leaderComboBox_1_1 = QComboBox(self.leaderGroupBox_1)
        self.leaderComboBox_1_1.setObjectName(u"leaderComboBox_1_1")
        self.leaderComboBox_1_1.setEnabled(False)

        self.verticalLayout_12.addWidget(self.leaderComboBox_1_1)

        self.leaderComboBox_1_2 = QComboBox(self.leaderGroupBox_1)
        self.leaderComboBox_1_2.setObjectName(u"leaderComboBox_1_2")
        self.leaderComboBox_1_2.setEnabled(False)

        self.verticalLayout_12.addWidget(self.leaderComboBox_1_2)

        self.leaderComboBox_1_3 = QComboBox(self.leaderGroupBox_1)
        self.leaderComboBox_1_3.setObjectName(u"leaderComboBox_1_3")
        self.leaderComboBox_1_3.setEnabled(False)

        self.verticalLayout_12.addWidget(self.leaderComboBox_1_3)

        self.leaderComboBox_1_4 = QComboBox(self.leaderGroupBox_1)
        self.leaderComboBox_1_4.setObjectName(u"leaderComboBox_1_4")
        self.leaderComboBox_1_4.setEnabled(False)

        self.verticalLayout_12.addWidget(self.leaderComboBox_1_4)

        self.leaderComboBox_1_5 = QComboBox(self.leaderGroupBox_1)
        self.leaderComboBox_1_5.setObjectName(u"leaderComboBox_1_5")
        self.leaderComboBox_1_5.setEnabled(False)

        self.verticalLayout_12.addWidget(self.leaderComboBox_1_5)

        self.leaderLevelGroupBox_1 = QGroupBox(self.leaderGroupBox_1)
        self.leaderLevelGroupBox_1.setObjectName(u"leaderLevelGroupBox_1")
        self.verticalLayout_79 = QVBoxLayout(self.leaderLevelGroupBox_1)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.leaderLevelSpinBox_1 = QSpinBox(self.leaderLevelGroupBox_1)
        self.leaderLevelSpinBox_1.setObjectName(u"leaderLevelSpinBox_1")
        self.leaderLevelSpinBox_1.setEnabled(False)
        self.leaderLevelSpinBox_1.setMinimum(1)
        self.leaderLevelSpinBox_1.setMaximum(5)

        self.verticalLayout_79.addWidget(self.leaderLevelSpinBox_1)


        self.verticalLayout_12.addWidget(self.leaderLevelGroupBox_1)

        self.leaderSkillPointGroupBox_1 = QGroupBox(self.leaderGroupBox_1)
        self.leaderSkillPointGroupBox_1.setObjectName(u"leaderSkillPointGroupBox_1")
        self.verticalLayout_81 = QVBoxLayout(self.leaderSkillPointGroupBox_1)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.leaderSkillPointSpinBox_1 = QSpinBox(self.leaderSkillPointGroupBox_1)
        self.leaderSkillPointSpinBox_1.setObjectName(u"leaderSkillPointSpinBox_1")
        self.leaderSkillPointSpinBox_1.setEnabled(False)

        self.verticalLayout_81.addWidget(self.leaderSkillPointSpinBox_1)


        self.verticalLayout_12.addWidget(self.leaderSkillPointGroupBox_1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.deleteLeaderButton_1 = QPushButton(self.leaderGroupBox_1)
        self.deleteLeaderButton_1.setObjectName(u"deleteLeaderButton_1")
        self.deleteLeaderButton_1.setEnabled(False)
        self.deleteLeaderButton_1.setProperty(u"index", 0)
        self.deleteLeaderButton_1.setProperty(u"reserveLeader", False)

        self.horizontalLayout_7.addWidget(self.deleteLeaderButton_1)

        self.createLeaderButton_1 = QPushButton(self.leaderGroupBox_1)
        self.createLeaderButton_1.setObjectName(u"createLeaderButton_1")
        self.createLeaderButton_1.setEnabled(False)
        self.createLeaderButton_1.setProperty(u"index", 0)
        self.createLeaderButton_1.setProperty(u"reserveLeader", False)

        self.horizontalLayout_7.addWidget(self.createLeaderButton_1)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_4.addWidget(self.leaderGroupBox_1)

        self.leaderGroupBox_3 = QGroupBox(self.leaderGroupBox)
        self.leaderGroupBox_3.setObjectName(u"leaderGroupBox_3")
        self.verticalLayout_84 = QVBoxLayout(self.leaderGroupBox_3)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.leaderNameGroupBox_3 = QGroupBox(self.leaderGroupBox_3)
        self.leaderNameGroupBox_3.setObjectName(u"leaderNameGroupBox_3")
        self.verticalLayout_16 = QVBoxLayout(self.leaderNameGroupBox_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.leaderNameLabel_3 = QLabel(self.leaderNameGroupBox_3)
        self.leaderNameLabel_3.setObjectName(u"leaderNameLabel_3")
        self.leaderNameLabel_3.setAutoFillBackground(False)
        self.leaderNameLabel_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.leaderNameLabel_3)


        self.verticalLayout_84.addWidget(self.leaderNameGroupBox_3)

        self.leaderComboBox_3_1 = QComboBox(self.leaderGroupBox_3)
        self.leaderComboBox_3_1.setObjectName(u"leaderComboBox_3_1")
        self.leaderComboBox_3_1.setEnabled(False)

        self.verticalLayout_84.addWidget(self.leaderComboBox_3_1)

        self.leaderComboBox_3_2 = QComboBox(self.leaderGroupBox_3)
        self.leaderComboBox_3_2.setObjectName(u"leaderComboBox_3_2")
        self.leaderComboBox_3_2.setEnabled(False)

        self.verticalLayout_84.addWidget(self.leaderComboBox_3_2)

        self.leaderComboBox_3_3 = QComboBox(self.leaderGroupBox_3)
        self.leaderComboBox_3_3.setObjectName(u"leaderComboBox_3_3")
        self.leaderComboBox_3_3.setEnabled(False)

        self.verticalLayout_84.addWidget(self.leaderComboBox_3_3)

        self.leaderComboBox_3_4 = QComboBox(self.leaderGroupBox_3)
        self.leaderComboBox_3_4.setObjectName(u"leaderComboBox_3_4")
        self.leaderComboBox_3_4.setEnabled(False)

        self.verticalLayout_84.addWidget(self.leaderComboBox_3_4)

        self.leaderComboBox_3_5 = QComboBox(self.leaderGroupBox_3)
        self.leaderComboBox_3_5.setObjectName(u"leaderComboBox_3_5")
        self.leaderComboBox_3_5.setEnabled(False)

        self.verticalLayout_84.addWidget(self.leaderComboBox_3_5)

        self.leaderLevelGroupBox_3 = QGroupBox(self.leaderGroupBox_3)
        self.leaderLevelGroupBox_3.setObjectName(u"leaderLevelGroupBox_3")
        self.verticalLayout_85 = QVBoxLayout(self.leaderLevelGroupBox_3)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.leaderLevelSpinBox_3 = QSpinBox(self.leaderLevelGroupBox_3)
        self.leaderLevelSpinBox_3.setObjectName(u"leaderLevelSpinBox_3")
        self.leaderLevelSpinBox_3.setEnabled(False)
        self.leaderLevelSpinBox_3.setMinimum(1)
        self.leaderLevelSpinBox_3.setMaximum(5)

        self.verticalLayout_85.addWidget(self.leaderLevelSpinBox_3)


        self.verticalLayout_84.addWidget(self.leaderLevelGroupBox_3)

        self.leaderSkillPointGroupBox_3 = QGroupBox(self.leaderGroupBox_3)
        self.leaderSkillPointGroupBox_3.setObjectName(u"leaderSkillPointGroupBox_3")
        self.verticalLayout_108 = QVBoxLayout(self.leaderSkillPointGroupBox_3)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.leaderSkillPointSpinBox_3 = QSpinBox(self.leaderSkillPointGroupBox_3)
        self.leaderSkillPointSpinBox_3.setObjectName(u"leaderSkillPointSpinBox_3")
        self.leaderSkillPointSpinBox_3.setEnabled(False)

        self.verticalLayout_108.addWidget(self.leaderSkillPointSpinBox_3)


        self.verticalLayout_84.addWidget(self.leaderSkillPointGroupBox_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.deleteLeaderButton_3 = QPushButton(self.leaderGroupBox_3)
        self.deleteLeaderButton_3.setObjectName(u"deleteLeaderButton_3")
        self.deleteLeaderButton_3.setEnabled(False)
        self.deleteLeaderButton_3.setProperty(u"index", 2)
        self.deleteLeaderButton_3.setProperty(u"reserveLeader", False)

        self.horizontalLayout_8.addWidget(self.deleteLeaderButton_3)

        self.createLeaderButton_3 = QPushButton(self.leaderGroupBox_3)
        self.createLeaderButton_3.setObjectName(u"createLeaderButton_3")
        self.createLeaderButton_3.setEnabled(False)
        self.createLeaderButton_3.setProperty(u"index", 2)
        self.createLeaderButton_3.setProperty(u"reserveLeader", False)

        self.horizontalLayout_8.addWidget(self.createLeaderButton_3)


        self.verticalLayout_84.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_4.addWidget(self.leaderGroupBox_3)

        self.leaderGroupBox_5 = QGroupBox(self.leaderGroupBox)
        self.leaderGroupBox_5.setObjectName(u"leaderGroupBox_5")
        self.verticalLayout_88 = QVBoxLayout(self.leaderGroupBox_5)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.leaderNameGroupBox_5 = QGroupBox(self.leaderGroupBox_5)
        self.leaderNameGroupBox_5.setObjectName(u"leaderNameGroupBox_5")
        self.verticalLayout_18 = QVBoxLayout(self.leaderNameGroupBox_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.leaderNameLabel_5 = QLabel(self.leaderNameGroupBox_5)
        self.leaderNameLabel_5.setObjectName(u"leaderNameLabel_5")
        self.leaderNameLabel_5.setAutoFillBackground(False)
        self.leaderNameLabel_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.leaderNameLabel_5)


        self.verticalLayout_88.addWidget(self.leaderNameGroupBox_5)

        self.leaderComboBox_5_1 = QComboBox(self.leaderGroupBox_5)
        self.leaderComboBox_5_1.setObjectName(u"leaderComboBox_5_1")
        self.leaderComboBox_5_1.setEnabled(False)

        self.verticalLayout_88.addWidget(self.leaderComboBox_5_1)

        self.leaderComboBox_5_2 = QComboBox(self.leaderGroupBox_5)
        self.leaderComboBox_5_2.setObjectName(u"leaderComboBox_5_2")
        self.leaderComboBox_5_2.setEnabled(False)

        self.verticalLayout_88.addWidget(self.leaderComboBox_5_2)

        self.leaderComboBox_5_3 = QComboBox(self.leaderGroupBox_5)
        self.leaderComboBox_5_3.setObjectName(u"leaderComboBox_5_3")
        self.leaderComboBox_5_3.setEnabled(False)

        self.verticalLayout_88.addWidget(self.leaderComboBox_5_3)

        self.leaderComboBox_5_4 = QComboBox(self.leaderGroupBox_5)
        self.leaderComboBox_5_4.setObjectName(u"leaderComboBox_5_4")
        self.leaderComboBox_5_4.setEnabled(False)

        self.verticalLayout_88.addWidget(self.leaderComboBox_5_4)

        self.leaderComboBox_5_5 = QComboBox(self.leaderGroupBox_5)
        self.leaderComboBox_5_5.setObjectName(u"leaderComboBox_5_5")
        self.leaderComboBox_5_5.setEnabled(False)

        self.verticalLayout_88.addWidget(self.leaderComboBox_5_5)

        self.leaderLevelGroupBox_5 = QGroupBox(self.leaderGroupBox_5)
        self.leaderLevelGroupBox_5.setObjectName(u"leaderLevelGroupBox_5")
        self.verticalLayout_89 = QVBoxLayout(self.leaderLevelGroupBox_5)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.leaderLevelSpinBox_5 = QSpinBox(self.leaderLevelGroupBox_5)
        self.leaderLevelSpinBox_5.setObjectName(u"leaderLevelSpinBox_5")
        self.leaderLevelSpinBox_5.setEnabled(False)
        self.leaderLevelSpinBox_5.setMinimum(1)
        self.leaderLevelSpinBox_5.setMaximum(5)

        self.verticalLayout_89.addWidget(self.leaderLevelSpinBox_5)


        self.verticalLayout_88.addWidget(self.leaderLevelGroupBox_5)

        self.leaderSkillPointGroupBox_5 = QGroupBox(self.leaderGroupBox_5)
        self.leaderSkillPointGroupBox_5.setObjectName(u"leaderSkillPointGroupBox_5")
        self.verticalLayout_111 = QVBoxLayout(self.leaderSkillPointGroupBox_5)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.leaderSkillPointSpinBox_5 = QSpinBox(self.leaderSkillPointGroupBox_5)
        self.leaderSkillPointSpinBox_5.setObjectName(u"leaderSkillPointSpinBox_5")
        self.leaderSkillPointSpinBox_5.setEnabled(False)

        self.verticalLayout_111.addWidget(self.leaderSkillPointSpinBox_5)


        self.verticalLayout_88.addWidget(self.leaderSkillPointGroupBox_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.deleteLeaderButton_5 = QPushButton(self.leaderGroupBox_5)
        self.deleteLeaderButton_5.setObjectName(u"deleteLeaderButton_5")
        self.deleteLeaderButton_5.setEnabled(False)
        self.deleteLeaderButton_5.setProperty(u"index", 4)
        self.deleteLeaderButton_5.setProperty(u"reserveLeader", False)

        self.horizontalLayout_9.addWidget(self.deleteLeaderButton_5)

        self.createLeaderButton_5 = QPushButton(self.leaderGroupBox_5)
        self.createLeaderButton_5.setObjectName(u"createLeaderButton_5")
        self.createLeaderButton_5.setEnabled(False)
        self.createLeaderButton_5.setProperty(u"index", 4)
        self.createLeaderButton_5.setProperty(u"reserveLeader", False)

        self.horizontalLayout_9.addWidget(self.createLeaderButton_5)


        self.verticalLayout_88.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_4.addWidget(self.leaderGroupBox_5)


        self.verticalLayout_90.addWidget(self.leaderGroupBox)

        self.groupBox_15 = QGroupBox(self.leaderTab)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout = QGridLayout(self.groupBox_15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reserveLeaderGroupBox_1 = QGroupBox(self.groupBox_15)
        self.reserveLeaderGroupBox_1.setObjectName(u"reserveLeaderGroupBox_1")
        self.verticalLayout_13 = QVBoxLayout(self.reserveLeaderGroupBox_1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.reserveLeaderNameGroupBox_1 = QGroupBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderNameGroupBox_1.setObjectName(u"reserveLeaderNameGroupBox_1")
        self.verticalLayout_19 = QVBoxLayout(self.reserveLeaderNameGroupBox_1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.reserveLeaderNameLabel_1 = QLabel(self.reserveLeaderNameGroupBox_1)
        self.reserveLeaderNameLabel_1.setObjectName(u"reserveLeaderNameLabel_1")
        self.reserveLeaderNameLabel_1.setAutoFillBackground(False)
        self.reserveLeaderNameLabel_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.reserveLeaderNameLabel_1)


        self.verticalLayout_13.addWidget(self.reserveLeaderNameGroupBox_1)

        self.reserveLeaderComboBox_1_1 = QComboBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderComboBox_1_1.setObjectName(u"reserveLeaderComboBox_1_1")
        self.reserveLeaderComboBox_1_1.setEnabled(False)

        self.verticalLayout_13.addWidget(self.reserveLeaderComboBox_1_1)

        self.reserveLeaderComboBox_1_2 = QComboBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderComboBox_1_2.setObjectName(u"reserveLeaderComboBox_1_2")
        self.reserveLeaderComboBox_1_2.setEnabled(False)

        self.verticalLayout_13.addWidget(self.reserveLeaderComboBox_1_2)

        self.reserveLeaderComboBox_1_3 = QComboBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderComboBox_1_3.setObjectName(u"reserveLeaderComboBox_1_3")
        self.reserveLeaderComboBox_1_3.setEnabled(False)

        self.verticalLayout_13.addWidget(self.reserveLeaderComboBox_1_3)

        self.reserveLeaderComboBox_1_4 = QComboBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderComboBox_1_4.setObjectName(u"reserveLeaderComboBox_1_4")
        self.reserveLeaderComboBox_1_4.setEnabled(False)

        self.verticalLayout_13.addWidget(self.reserveLeaderComboBox_1_4)

        self.reserveLeaderComboBox_1_5 = QComboBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderComboBox_1_5.setObjectName(u"reserveLeaderComboBox_1_5")
        self.reserveLeaderComboBox_1_5.setEnabled(False)

        self.verticalLayout_13.addWidget(self.reserveLeaderComboBox_1_5)

        self.reserveLeaderLevelGroupBox_1 = QGroupBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderLevelGroupBox_1.setObjectName(u"reserveLeaderLevelGroupBox_1")
        self.verticalLayout_74 = QVBoxLayout(self.reserveLeaderLevelGroupBox_1)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.reserveLeaderLevelSpinBox_1 = QSpinBox(self.reserveLeaderLevelGroupBox_1)
        self.reserveLeaderLevelSpinBox_1.setObjectName(u"reserveLeaderLevelSpinBox_1")
        self.reserveLeaderLevelSpinBox_1.setEnabled(False)
        self.reserveLeaderLevelSpinBox_1.setMinimum(1)
        self.reserveLeaderLevelSpinBox_1.setMaximum(5)

        self.verticalLayout_74.addWidget(self.reserveLeaderLevelSpinBox_1)


        self.verticalLayout_13.addWidget(self.reserveLeaderLevelGroupBox_1)

        self.reserveLeaderSkillPointGroupBox_1 = QGroupBox(self.reserveLeaderGroupBox_1)
        self.reserveLeaderSkillPointGroupBox_1.setObjectName(u"reserveLeaderSkillPointGroupBox_1")
        self.verticalLayout_112 = QVBoxLayout(self.reserveLeaderSkillPointGroupBox_1)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.reserveLeaderSkillPointSpinBox_1 = QSpinBox(self.reserveLeaderSkillPointGroupBox_1)
        self.reserveLeaderSkillPointSpinBox_1.setObjectName(u"reserveLeaderSkillPointSpinBox_1")
        self.reserveLeaderSkillPointSpinBox_1.setEnabled(False)

        self.verticalLayout_112.addWidget(self.reserveLeaderSkillPointSpinBox_1)


        self.verticalLayout_13.addWidget(self.reserveLeaderSkillPointGroupBox_1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.reserveDeleteLeaderButton_1 = QPushButton(self.reserveLeaderGroupBox_1)
        self.reserveDeleteLeaderButton_1.setObjectName(u"reserveDeleteLeaderButton_1")
        self.reserveDeleteLeaderButton_1.setEnabled(False)
        self.reserveDeleteLeaderButton_1.setProperty(u"index", 0)
        self.reserveDeleteLeaderButton_1.setProperty(u"reserveLeader", True)

        self.horizontalLayout_10.addWidget(self.reserveDeleteLeaderButton_1)

        self.reserveCreateLeaderButton_1 = QPushButton(self.reserveLeaderGroupBox_1)
        self.reserveCreateLeaderButton_1.setObjectName(u"reserveCreateLeaderButton_1")
        self.reserveCreateLeaderButton_1.setEnabled(False)
        self.reserveCreateLeaderButton_1.setProperty(u"index", 0)
        self.reserveCreateLeaderButton_1.setProperty(u"reserveLeader", True)

        self.horizontalLayout_10.addWidget(self.reserveCreateLeaderButton_1)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)


        self.gridLayout.addWidget(self.reserveLeaderGroupBox_1, 0, 0, 1, 1)

        self.reserveLeaderGroupBox_2 = QGroupBox(self.groupBox_15)
        self.reserveLeaderGroupBox_2.setObjectName(u"reserveLeaderGroupBox_2")
        self.verticalLayout_94 = QVBoxLayout(self.reserveLeaderGroupBox_2)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.reserveLeaderNameGroupBox_2 = QGroupBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderNameGroupBox_2.setObjectName(u"reserveLeaderNameGroupBox_2")
        self.verticalLayout_20 = QVBoxLayout(self.reserveLeaderNameGroupBox_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.reserveLeaderNameLabel_2 = QLabel(self.reserveLeaderNameGroupBox_2)
        self.reserveLeaderNameLabel_2.setObjectName(u"reserveLeaderNameLabel_2")
        self.reserveLeaderNameLabel_2.setAutoFillBackground(False)
        self.reserveLeaderNameLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.reserveLeaderNameLabel_2)


        self.verticalLayout_94.addWidget(self.reserveLeaderNameGroupBox_2)

        self.reserveLeaderComboBox_2_1 = QComboBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderComboBox_2_1.setObjectName(u"reserveLeaderComboBox_2_1")
        self.reserveLeaderComboBox_2_1.setEnabled(False)

        self.verticalLayout_94.addWidget(self.reserveLeaderComboBox_2_1)

        self.reserveLeaderComboBox_2_2 = QComboBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderComboBox_2_2.setObjectName(u"reserveLeaderComboBox_2_2")
        self.reserveLeaderComboBox_2_2.setEnabled(False)

        self.verticalLayout_94.addWidget(self.reserveLeaderComboBox_2_2)

        self.reserveLeaderComboBox_2_3 = QComboBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderComboBox_2_3.setObjectName(u"reserveLeaderComboBox_2_3")
        self.reserveLeaderComboBox_2_3.setEnabled(False)

        self.verticalLayout_94.addWidget(self.reserveLeaderComboBox_2_3)

        self.reserveLeaderComboBox_2_4 = QComboBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderComboBox_2_4.setObjectName(u"reserveLeaderComboBox_2_4")
        self.reserveLeaderComboBox_2_4.setEnabled(False)

        self.verticalLayout_94.addWidget(self.reserveLeaderComboBox_2_4)

        self.reserveLeaderComboBox_2_5 = QComboBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderComboBox_2_5.setObjectName(u"reserveLeaderComboBox_2_5")
        self.reserveLeaderComboBox_2_5.setEnabled(False)

        self.verticalLayout_94.addWidget(self.reserveLeaderComboBox_2_5)

        self.reserveLeaderLevelGroupBox_2 = QGroupBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderLevelGroupBox_2.setObjectName(u"reserveLeaderLevelGroupBox_2")
        self.verticalLayout_75 = QVBoxLayout(self.reserveLeaderLevelGroupBox_2)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.reserveLeaderLevelSpinBox_2 = QSpinBox(self.reserveLeaderLevelGroupBox_2)
        self.reserveLeaderLevelSpinBox_2.setObjectName(u"reserveLeaderLevelSpinBox_2")
        self.reserveLeaderLevelSpinBox_2.setEnabled(False)
        self.reserveLeaderLevelSpinBox_2.setMinimum(1)
        self.reserveLeaderLevelSpinBox_2.setMaximum(5)

        self.verticalLayout_75.addWidget(self.reserveLeaderLevelSpinBox_2)


        self.verticalLayout_94.addWidget(self.reserveLeaderLevelGroupBox_2)

        self.reserveLeaderSkillPointGroupBox_2 = QGroupBox(self.reserveLeaderGroupBox_2)
        self.reserveLeaderSkillPointGroupBox_2.setObjectName(u"reserveLeaderSkillPointGroupBox_2")
        self.verticalLayout_113 = QVBoxLayout(self.reserveLeaderSkillPointGroupBox_2)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.reserveLeaderSkillPointSpinBox_2 = QSpinBox(self.reserveLeaderSkillPointGroupBox_2)
        self.reserveLeaderSkillPointSpinBox_2.setObjectName(u"reserveLeaderSkillPointSpinBox_2")
        self.reserveLeaderSkillPointSpinBox_2.setEnabled(False)

        self.verticalLayout_113.addWidget(self.reserveLeaderSkillPointSpinBox_2)


        self.verticalLayout_94.addWidget(self.reserveLeaderSkillPointGroupBox_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.reserveDeleteLeaderButton_2 = QPushButton(self.reserveLeaderGroupBox_2)
        self.reserveDeleteLeaderButton_2.setObjectName(u"reserveDeleteLeaderButton_2")
        self.reserveDeleteLeaderButton_2.setEnabled(False)
        self.reserveDeleteLeaderButton_2.setProperty(u"index", 1)
        self.reserveDeleteLeaderButton_2.setProperty(u"reserveLeader", True)

        self.horizontalLayout_11.addWidget(self.reserveDeleteLeaderButton_2)

        self.reserveCreateLeaderButton_2 = QPushButton(self.reserveLeaderGroupBox_2)
        self.reserveCreateLeaderButton_2.setObjectName(u"reserveCreateLeaderButton_2")
        self.reserveCreateLeaderButton_2.setEnabled(False)
        self.reserveCreateLeaderButton_2.setProperty(u"index", 1)
        self.reserveCreateLeaderButton_2.setProperty(u"reserveLeader", True)

        self.horizontalLayout_11.addWidget(self.reserveCreateLeaderButton_2)


        self.verticalLayout_94.addLayout(self.horizontalLayout_11)


        self.gridLayout.addWidget(self.reserveLeaderGroupBox_2, 0, 1, 1, 1)

        self.reserveLeaderGroupBox_3 = QGroupBox(self.groupBox_15)
        self.reserveLeaderGroupBox_3.setObjectName(u"reserveLeaderGroupBox_3")
        self.reserveLeaderGroupBox_3.setEnabled(True)
        self.verticalLayout_95 = QVBoxLayout(self.reserveLeaderGroupBox_3)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.reserveLeaderNameGroupBox_3 = QGroupBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderNameGroupBox_3.setObjectName(u"reserveLeaderNameGroupBox_3")
        self.verticalLayout_21 = QVBoxLayout(self.reserveLeaderNameGroupBox_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.reserveLeaderNameLabel_3 = QLabel(self.reserveLeaderNameGroupBox_3)
        self.reserveLeaderNameLabel_3.setObjectName(u"reserveLeaderNameLabel_3")
        self.reserveLeaderNameLabel_3.setAutoFillBackground(False)
        self.reserveLeaderNameLabel_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.reserveLeaderNameLabel_3)


        self.verticalLayout_95.addWidget(self.reserveLeaderNameGroupBox_3)

        self.reserveLeaderComboBox_3_1 = QComboBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderComboBox_3_1.setObjectName(u"reserveLeaderComboBox_3_1")
        self.reserveLeaderComboBox_3_1.setEnabled(False)

        self.verticalLayout_95.addWidget(self.reserveLeaderComboBox_3_1)

        self.reserveLeaderComboBox_3_2 = QComboBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderComboBox_3_2.setObjectName(u"reserveLeaderComboBox_3_2")
        self.reserveLeaderComboBox_3_2.setEnabled(False)

        self.verticalLayout_95.addWidget(self.reserveLeaderComboBox_3_2)

        self.reserveLeaderComboBox_3_3 = QComboBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderComboBox_3_3.setObjectName(u"reserveLeaderComboBox_3_3")
        self.reserveLeaderComboBox_3_3.setEnabled(False)

        self.verticalLayout_95.addWidget(self.reserveLeaderComboBox_3_3)

        self.reserveLeaderComboBox_3_4 = QComboBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderComboBox_3_4.setObjectName(u"reserveLeaderComboBox_3_4")
        self.reserveLeaderComboBox_3_4.setEnabled(False)

        self.verticalLayout_95.addWidget(self.reserveLeaderComboBox_3_4)

        self.reserveLeaderComboBox_3_5 = QComboBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderComboBox_3_5.setObjectName(u"reserveLeaderComboBox_3_5")
        self.reserveLeaderComboBox_3_5.setEnabled(False)

        self.verticalLayout_95.addWidget(self.reserveLeaderComboBox_3_5)

        self.reserveLeaderLevelGroupBox_3 = QGroupBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderLevelGroupBox_3.setObjectName(u"reserveLeaderLevelGroupBox_3")
        self.verticalLayout_76 = QVBoxLayout(self.reserveLeaderLevelGroupBox_3)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.reserveLeaderLevelSpinBox_3 = QSpinBox(self.reserveLeaderLevelGroupBox_3)
        self.reserveLeaderLevelSpinBox_3.setObjectName(u"reserveLeaderLevelSpinBox_3")
        self.reserveLeaderLevelSpinBox_3.setEnabled(False)
        self.reserveLeaderLevelSpinBox_3.setMinimum(1)
        self.reserveLeaderLevelSpinBox_3.setMaximum(5)

        self.verticalLayout_76.addWidget(self.reserveLeaderLevelSpinBox_3)


        self.verticalLayout_95.addWidget(self.reserveLeaderLevelGroupBox_3)

        self.reserveLeaderSkillPointGroupBox_3 = QGroupBox(self.reserveLeaderGroupBox_3)
        self.reserveLeaderSkillPointGroupBox_3.setObjectName(u"reserveLeaderSkillPointGroupBox_3")
        self.verticalLayout_114 = QVBoxLayout(self.reserveLeaderSkillPointGroupBox_3)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.reserveLeaderSkillPointSpinBox_3 = QSpinBox(self.reserveLeaderSkillPointGroupBox_3)
        self.reserveLeaderSkillPointSpinBox_3.setObjectName(u"reserveLeaderSkillPointSpinBox_3")
        self.reserveLeaderSkillPointSpinBox_3.setEnabled(False)

        self.verticalLayout_114.addWidget(self.reserveLeaderSkillPointSpinBox_3)


        self.verticalLayout_95.addWidget(self.reserveLeaderSkillPointGroupBox_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.reserveDeleteLeaderButton_3 = QPushButton(self.reserveLeaderGroupBox_3)
        self.reserveDeleteLeaderButton_3.setObjectName(u"reserveDeleteLeaderButton_3")
        self.reserveDeleteLeaderButton_3.setEnabled(False)
        self.reserveDeleteLeaderButton_3.setProperty(u"index", 2)
        self.reserveDeleteLeaderButton_3.setProperty(u"reserveLeader", True)

        self.horizontalLayout_12.addWidget(self.reserveDeleteLeaderButton_3)

        self.reserveCreateLeaderButton_3 = QPushButton(self.reserveLeaderGroupBox_3)
        self.reserveCreateLeaderButton_3.setObjectName(u"reserveCreateLeaderButton_3")
        self.reserveCreateLeaderButton_3.setEnabled(False)
        self.reserveCreateLeaderButton_3.setProperty(u"index", 2)
        self.reserveCreateLeaderButton_3.setProperty(u"reserveLeader", True)

        self.horizontalLayout_12.addWidget(self.reserveCreateLeaderButton_3)


        self.verticalLayout_95.addLayout(self.horizontalLayout_12)


        self.gridLayout.addWidget(self.reserveLeaderGroupBox_3, 0, 2, 1, 1)

        self.reserveLeaderGroupBox_4 = QGroupBox(self.groupBox_15)
        self.reserveLeaderGroupBox_4.setObjectName(u"reserveLeaderGroupBox_4")
        self.verticalLayout_96 = QVBoxLayout(self.reserveLeaderGroupBox_4)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.reserveLeaderNameGroupBox_4 = QGroupBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderNameGroupBox_4.setObjectName(u"reserveLeaderNameGroupBox_4")
        self.verticalLayout_22 = QVBoxLayout(self.reserveLeaderNameGroupBox_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.reserveLeaderNameLabel_4 = QLabel(self.reserveLeaderNameGroupBox_4)
        self.reserveLeaderNameLabel_4.setObjectName(u"reserveLeaderNameLabel_4")
        self.reserveLeaderNameLabel_4.setAutoFillBackground(False)
        self.reserveLeaderNameLabel_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.reserveLeaderNameLabel_4)


        self.verticalLayout_96.addWidget(self.reserveLeaderNameGroupBox_4)

        self.reserveLeaderComboBox_4_1 = QComboBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderComboBox_4_1.setObjectName(u"reserveLeaderComboBox_4_1")
        self.reserveLeaderComboBox_4_1.setEnabled(False)

        self.verticalLayout_96.addWidget(self.reserveLeaderComboBox_4_1)

        self.reserveLeaderComboBox_4_2 = QComboBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderComboBox_4_2.setObjectName(u"reserveLeaderComboBox_4_2")
        self.reserveLeaderComboBox_4_2.setEnabled(False)

        self.verticalLayout_96.addWidget(self.reserveLeaderComboBox_4_2)

        self.reserveLeaderComboBox_4_3 = QComboBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderComboBox_4_3.setObjectName(u"reserveLeaderComboBox_4_3")
        self.reserveLeaderComboBox_4_3.setEnabled(False)

        self.verticalLayout_96.addWidget(self.reserveLeaderComboBox_4_3)

        self.reserveLeaderComboBox_4_4 = QComboBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderComboBox_4_4.setObjectName(u"reserveLeaderComboBox_4_4")
        self.reserveLeaderComboBox_4_4.setEnabled(False)

        self.verticalLayout_96.addWidget(self.reserveLeaderComboBox_4_4)

        self.reserveLeaderComboBox_4_5 = QComboBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderComboBox_4_5.setObjectName(u"reserveLeaderComboBox_4_5")
        self.reserveLeaderComboBox_4_5.setEnabled(False)

        self.verticalLayout_96.addWidget(self.reserveLeaderComboBox_4_5)

        self.reserveLeaderLevelGroupBox_4 = QGroupBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderLevelGroupBox_4.setObjectName(u"reserveLeaderLevelGroupBox_4")
        self.verticalLayout_77 = QVBoxLayout(self.reserveLeaderLevelGroupBox_4)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.reserveLeaderLevelSpinBox_4 = QSpinBox(self.reserveLeaderLevelGroupBox_4)
        self.reserveLeaderLevelSpinBox_4.setObjectName(u"reserveLeaderLevelSpinBox_4")
        self.reserveLeaderLevelSpinBox_4.setEnabled(False)
        self.reserveLeaderLevelSpinBox_4.setMinimum(1)
        self.reserveLeaderLevelSpinBox_4.setMaximum(5)

        self.verticalLayout_77.addWidget(self.reserveLeaderLevelSpinBox_4)


        self.verticalLayout_96.addWidget(self.reserveLeaderLevelGroupBox_4)

        self.reserveLeaderSkillPointGroupBox_4 = QGroupBox(self.reserveLeaderGroupBox_4)
        self.reserveLeaderSkillPointGroupBox_4.setObjectName(u"reserveLeaderSkillPointGroupBox_4")
        self.verticalLayout_115 = QVBoxLayout(self.reserveLeaderSkillPointGroupBox_4)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.reserveLeaderSkillPointSpinBox_4 = QSpinBox(self.reserveLeaderSkillPointGroupBox_4)
        self.reserveLeaderSkillPointSpinBox_4.setObjectName(u"reserveLeaderSkillPointSpinBox_4")
        self.reserveLeaderSkillPointSpinBox_4.setEnabled(False)

        self.verticalLayout_115.addWidget(self.reserveLeaderSkillPointSpinBox_4)


        self.verticalLayout_96.addWidget(self.reserveLeaderSkillPointGroupBox_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.reserveDeleteLeaderButton_4 = QPushButton(self.reserveLeaderGroupBox_4)
        self.reserveDeleteLeaderButton_4.setObjectName(u"reserveDeleteLeaderButton_4")
        self.reserveDeleteLeaderButton_4.setEnabled(False)
        self.reserveDeleteLeaderButton_4.setProperty(u"index", 3)
        self.reserveDeleteLeaderButton_4.setProperty(u"reserveLeader", True)

        self.horizontalLayout_13.addWidget(self.reserveDeleteLeaderButton_4)

        self.reserveCreateLeaderButton_4 = QPushButton(self.reserveLeaderGroupBox_4)
        self.reserveCreateLeaderButton_4.setObjectName(u"reserveCreateLeaderButton_4")
        self.reserveCreateLeaderButton_4.setEnabled(False)
        self.reserveCreateLeaderButton_4.setProperty(u"index", 3)
        self.reserveCreateLeaderButton_4.setProperty(u"reserveLeader", True)

        self.horizontalLayout_13.addWidget(self.reserveCreateLeaderButton_4)


        self.verticalLayout_96.addLayout(self.horizontalLayout_13)


        self.gridLayout.addWidget(self.reserveLeaderGroupBox_4, 0, 3, 1, 1)

        self.reserveLeaderGroupBox_5 = QGroupBox(self.groupBox_15)
        self.reserveLeaderGroupBox_5.setObjectName(u"reserveLeaderGroupBox_5")
        self.verticalLayout_97 = QVBoxLayout(self.reserveLeaderGroupBox_5)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.reserveLeaderNameGroupBox_5 = QGroupBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderNameGroupBox_5.setObjectName(u"reserveLeaderNameGroupBox_5")
        self.verticalLayout_23 = QVBoxLayout(self.reserveLeaderNameGroupBox_5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.reserveLeaderNameLabel_5 = QLabel(self.reserveLeaderNameGroupBox_5)
        self.reserveLeaderNameLabel_5.setObjectName(u"reserveLeaderNameLabel_5")
        self.reserveLeaderNameLabel_5.setAutoFillBackground(False)
        self.reserveLeaderNameLabel_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.reserveLeaderNameLabel_5)


        self.verticalLayout_97.addWidget(self.reserveLeaderNameGroupBox_5)

        self.reserveLeaderComboBox_5_1 = QComboBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderComboBox_5_1.setObjectName(u"reserveLeaderComboBox_5_1")
        self.reserveLeaderComboBox_5_1.setEnabled(False)

        self.verticalLayout_97.addWidget(self.reserveLeaderComboBox_5_1)

        self.reserveLeaderComboBox_5_2 = QComboBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderComboBox_5_2.setObjectName(u"reserveLeaderComboBox_5_2")
        self.reserveLeaderComboBox_5_2.setEnabled(False)

        self.verticalLayout_97.addWidget(self.reserveLeaderComboBox_5_2)

        self.reserveLeaderComboBox_5_3 = QComboBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderComboBox_5_3.setObjectName(u"reserveLeaderComboBox_5_3")
        self.reserveLeaderComboBox_5_3.setEnabled(False)

        self.verticalLayout_97.addWidget(self.reserveLeaderComboBox_5_3)

        self.reserveLeaderComboBox_5_4 = QComboBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderComboBox_5_4.setObjectName(u"reserveLeaderComboBox_5_4")
        self.reserveLeaderComboBox_5_4.setEnabled(False)

        self.verticalLayout_97.addWidget(self.reserveLeaderComboBox_5_4)

        self.reserveLeaderComboBox_5_5 = QComboBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderComboBox_5_5.setObjectName(u"reserveLeaderComboBox_5_5")
        self.reserveLeaderComboBox_5_5.setEnabled(False)

        self.verticalLayout_97.addWidget(self.reserveLeaderComboBox_5_5)

        self.reserveLeaderLevelGroupBox_5 = QGroupBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderLevelGroupBox_5.setObjectName(u"reserveLeaderLevelGroupBox_5")
        self.verticalLayout_78 = QVBoxLayout(self.reserveLeaderLevelGroupBox_5)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.reserveLeaderLevelSpinBox_5 = QSpinBox(self.reserveLeaderLevelGroupBox_5)
        self.reserveLeaderLevelSpinBox_5.setObjectName(u"reserveLeaderLevelSpinBox_5")
        self.reserveLeaderLevelSpinBox_5.setEnabled(False)
        self.reserveLeaderLevelSpinBox_5.setMinimum(1)
        self.reserveLeaderLevelSpinBox_5.setMaximum(5)

        self.verticalLayout_78.addWidget(self.reserveLeaderLevelSpinBox_5)


        self.verticalLayout_97.addWidget(self.reserveLeaderLevelGroupBox_5)

        self.reserveLeaderSkillPointGroupBox_5 = QGroupBox(self.reserveLeaderGroupBox_5)
        self.reserveLeaderSkillPointGroupBox_5.setObjectName(u"reserveLeaderSkillPointGroupBox_5")
        self.verticalLayout_116 = QVBoxLayout(self.reserveLeaderSkillPointGroupBox_5)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.reserveLeaderSkillPointSpinBox_5 = QSpinBox(self.reserveLeaderSkillPointGroupBox_5)
        self.reserveLeaderSkillPointSpinBox_5.setObjectName(u"reserveLeaderSkillPointSpinBox_5")
        self.reserveLeaderSkillPointSpinBox_5.setEnabled(False)

        self.verticalLayout_116.addWidget(self.reserveLeaderSkillPointSpinBox_5)


        self.verticalLayout_97.addWidget(self.reserveLeaderSkillPointGroupBox_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.reserveDeleteLeaderButton_5 = QPushButton(self.reserveLeaderGroupBox_5)
        self.reserveDeleteLeaderButton_5.setObjectName(u"reserveDeleteLeaderButton_5")
        self.reserveDeleteLeaderButton_5.setEnabled(False)
        self.reserveDeleteLeaderButton_5.setProperty(u"index", 4)
        self.reserveDeleteLeaderButton_5.setProperty(u"reserveLeader", True)

        self.horizontalLayout_14.addWidget(self.reserveDeleteLeaderButton_5)

        self.reserveCreateLeaderButton_5 = QPushButton(self.reserveLeaderGroupBox_5)
        self.reserveCreateLeaderButton_5.setObjectName(u"reserveCreateLeaderButton_5")
        self.reserveCreateLeaderButton_5.setEnabled(False)
        self.reserveCreateLeaderButton_5.setProperty(u"index", 4)
        self.reserveCreateLeaderButton_5.setProperty(u"reserveLeader", True)

        self.horizontalLayout_14.addWidget(self.reserveCreateLeaderButton_5)


        self.verticalLayout_97.addLayout(self.horizontalLayout_14)


        self.gridLayout.addWidget(self.reserveLeaderGroupBox_5, 0, 4, 1, 1)


        self.verticalLayout_90.addWidget(self.groupBox_15)

        self.tabWidget.addTab(self.leaderTab, "")
        self.inventoryTab = QWidget()
        self.inventoryTab.setObjectName(u"inventoryTab")
        self.tabWidget.addTab(self.inventoryTab, "")
        self.devTab = QWidget()
        self.devTab.setObjectName(u"devTab")
        self.verticalLayout_24 = QVBoxLayout(self.devTab)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.devTabWidget = QTabWidget(self.devTab)
        self.devTabWidget.setObjectName(u"devTabWidget")
        self.locTab = QWidget()
        self.locTab.setObjectName(u"locTab")
        self.verticalLayout_25 = QVBoxLayout(self.locTab)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.locTableWidget = QTableWidget(self.locTab)
        if (self.locTableWidget.columnCount() < 2):
            self.locTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.locTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.locTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.locTableWidget.rowCount() < 5):
            self.locTableWidget.setRowCount(5)
        self.locTableWidget.setObjectName(u"locTableWidget")
        self.locTableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.locTableWidget.setAutoFillBackground(False)
        self.locTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.locTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.locTableWidget.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.locTableWidget.setRowCount(5)
        self.locTableWidget.setSupportedDragActions(Qt.DropAction.IgnoreAction)
        self.locTableWidget.verticalHeader().setVisible(True)

        self.verticalLayout_25.addWidget(self.locTableWidget)

        self.devTabWidget.addTab(self.locTab, "")
        self.unitTemplateTab = QWidget()
        self.unitTemplateTab.setObjectName(u"unitTemplateTab")
        self.verticalLayout_26 = QVBoxLayout(self.unitTemplateTab)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.unitTemplateTreeWidget = QTreeWidget(self.unitTemplateTab)
        self.unitTemplateTreeWidget.setObjectName(u"unitTemplateTreeWidget")
        self.unitTemplateTreeWidget.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.verticalLayout_26.addWidget(self.unitTemplateTreeWidget)

        self.devTabWidget.addTab(self.unitTemplateTab, "")
        self.flagTemplateTab = QWidget()
        self.flagTemplateTab.setObjectName(u"flagTemplateTab")
        self.verticalLayout_27 = QVBoxLayout(self.flagTemplateTab)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.flagTemplateTreeWidget = QTreeWidget(self.flagTemplateTab)
        self.flagTemplateTreeWidget.setObjectName(u"flagTemplateTreeWidget")
        self.flagTemplateTreeWidget.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.verticalLayout_27.addWidget(self.flagTemplateTreeWidget)

        self.devTabWidget.addTab(self.flagTemplateTab, "")
        self.bustTemplateTab = QWidget()
        self.bustTemplateTab.setObjectName(u"bustTemplateTab")
        self.verticalLayout_28 = QVBoxLayout(self.bustTemplateTab)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.bustTemplateTreeWidget = QTreeWidget(self.bustTemplateTab)
        self.bustTemplateTreeWidget.setObjectName(u"bustTemplateTreeWidget")
        self.bustTemplateTreeWidget.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.verticalLayout_28.addWidget(self.bustTemplateTreeWidget)

        self.devTabWidget.addTab(self.bustTemplateTab, "")
        self.upgradeTab = QWidget()
        self.upgradeTab.setObjectName(u"upgradeTab")
        self.verticalLayout_29 = QVBoxLayout(self.upgradeTab)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.upgradeTemplateTreeWidget = QTreeWidget(self.upgradeTab)
        self.upgradeTemplateTreeWidget.setObjectName(u"upgradeTemplateTreeWidget")
        self.upgradeTemplateTreeWidget.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.verticalLayout_29.addWidget(self.upgradeTemplateTreeWidget)

        self.devTabWidget.addTab(self.upgradeTab, "")
        self.skillsTab = QWidget()
        self.skillsTab.setObjectName(u"skillsTab")
        self.verticalLayout_30 = QVBoxLayout(self.skillsTab)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.skillsTreeWidget = QTreeWidget(self.skillsTab)
        self.skillsTreeWidget.setObjectName(u"skillsTreeWidget")
        self.skillsTreeWidget.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.verticalLayout_30.addWidget(self.skillsTreeWidget)

        self.devTabWidget.addTab(self.skillsTab, "")

        self.verticalLayout_24.addWidget(self.devTabWidget)

        self.tabWidget.addTab(self.devTab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1242, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionLoad_File)
        self.menuFile.addAction(self.actionSave_File)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.devTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Save_File.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.actionSave_File.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.actionLoad_File.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.actionView_Templates.setText(QCoreApplication.translate("MainWindow", u"View Templates", None))
        self.goldGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Thalers", None))
        self.supplyGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Supply", None))
        self.manpowerGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Manpower", None))
        self.ammoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Ammunition", None))
        self.divisionGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Division #4", None))
        self.divisionCheckBox_4.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.regimentGroupBox_4_1.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #1", None))
        self.regimentTypeComboBox_4_1.setProperty(u"originalValue", "")
        self.veterancyGroupBox_4_1.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_4_1.setProperty(u"originalValue", "")
        self.regimentGroupBox_4_2.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #2", None))
        self.regimentTypeComboBox_4_2.setProperty(u"originalValue", "")
        self.veterancyGroupBox_4_2.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_4_2.setProperty(u"originalValue", "")
        self.regimentGroupBox_4_3.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #3", None))
        self.regimentTypeComboBox_4_3.setProperty(u"originalValue", "")
        self.veterancyGroupBox_4_3.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_4_3.setProperty(u"originalValue", "")
        self.regimentGroupBox_4_4.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #4", None))
        self.regimentTypeComboBox_4_4.setProperty(u"originalValue", "")
        self.veterancyGroupBox_4_4.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_4_4.setProperty(u"originalValue", "")
        self.divisionGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Division #2", None))
        self.divisionCheckBox_2.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.regimentGroupBox_2_1.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #1", None))
        self.regimentTypeComboBox_2_1.setProperty(u"originalValue", "")
        self.veterancyGroupBox_2_1.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_2_1.setProperty(u"originalValue", "")
        self.regimentGroupBox_2_2.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #2", None))
        self.regimentTypeComboBox_2_2.setProperty(u"originalValue", "")
        self.veterancyGroupBox_2_2.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_2_2.setProperty(u"originalValue", "")
        self.regimentGroupBox_2_3.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #3", None))
        self.regimentTypeComboBox_2_3.setProperty(u"originalValue", "")
        self.veterancyGroupBox_2_3.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_2_3.setProperty(u"originalValue", "")
        self.regimentGroupBox_2_4.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #4", None))
        self.regimentTypeComboBox_2_4.setProperty(u"originalValue", "")
        self.veterancyGroupBox_2_4.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_2_4.setProperty(u"originalValue", "")
        self.divisionGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Division #1", None))
        self.divisionCheckBox_1.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.regimentGroupBox_1_1.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #1", None))
        self.regimentTypeComboBox_1_1.setProperty(u"originalValue", "")
        self.veterancyGroupBox_1_1.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_1_1.setProperty(u"originalValue", "")
        self.regimentGroupBox_1_2.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #2", None))
        self.regimentTypeComboBox_1_2.setProperty(u"originalValue", "")
        self.veterancyGroupBox_1_2.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_1_2.setProperty(u"originalValue", "")
        self.regimentGroupBox_1_3.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #3", None))
        self.regimentTypeComboBox_1_3.setProperty(u"originalValue", "")
        self.veterancyGroupBox_1_3.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_1_3.setProperty(u"originalValue", "")
        self.regimentGroupBox_1_4.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #4", None))
        self.regimentTypeComboBox_1_4.setProperty(u"originalValue", "")
        self.veterancyGroupBox_1_4.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_1_4.setProperty(u"originalValue", "")
        self.divisionGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Division #3", None))
        self.divisionCheckBox_3.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.regimentGroupBox_3_1.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #1", None))
        self.regimentTypeComboBox_3_1.setProperty(u"originalValue", "")
        self.veterancyGroupBox_3_1.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_3_1.setProperty(u"originalValue", "")
        self.regimentGroupBox_3_2.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #2", None))
        self.regimentTypeComboBox_3_2.setProperty(u"originalValue", "")
        self.veterancyGroupBox_3_2.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_3_2.setProperty(u"originalValue", "")
        self.regimentGroupBox_3_3.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #3", None))
        self.regimentTypeComboBox_3_3.setProperty(u"originalValue", "")
        self.veterancyGroupBox_3_3.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_3_3.setProperty(u"originalValue", "")
        self.regimentGroupBox_3_4.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #4", None))
        self.regimentTypeComboBox_3_4.setProperty(u"originalValue", "")
        self.veterancyGroupBox_3_4.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_3_4.setProperty(u"originalValue", "")
        self.divisionGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Division #5", None))
        self.divisionCheckBox_5.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.regimentGroupBox_5_1.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #1", None))
        self.regimentTypeComboBox_5_1.setProperty(u"originalValue", "")
        self.veterancyGroupBox_5_1.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_5_1.setProperty(u"originalValue", "")
        self.regimentGroupBox_5_2.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #2", None))
        self.regimentTypeComboBox_5_2.setProperty(u"originalValue", "")
        self.veterancyGroupBox_5_2.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_5_2.setProperty(u"originalValue", "")
        self.regimentGroupBox_5_3.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #3", None))
        self.regimentTypeComboBox_5_3.setProperty(u"originalValue", "")
        self.veterancyGroupBox_5_3.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_5_3.setProperty(u"originalValue", "")
        self.regimentGroupBox_5_4.setTitle(QCoreApplication.translate("MainWindow", u"Regiment #4", None))
        self.regimentTypeComboBox_5_4.setProperty(u"originalValue", "")
        self.veterancyGroupBox_5_4.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.veterancySpinBox_5_4.setProperty(u"originalValue", "")
        self.reserveGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Reserve", None))
        self.reserveGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Division #1", None))
        self.reserveTypeComboBox_1.setProperty(u"originalValue", "")
        self.reserveVeterancyGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.reserveVeterancySpinBox_1.setProperty(u"originalValue", "")
        self.reserveGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Division #1", None))
        self.reserveTypeComboBox_2.setProperty(u"originalValue", "")
        self.reserveVeterancyGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.reserveVeterancySpinBox_2.setProperty(u"originalValue", "")
        self.reserveGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Division #1", None))
        self.reserveTypeComboBox_3.setProperty(u"originalValue", "")
        self.reserveVeterancyGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.reserveVeterancySpinBox_3.setProperty(u"originalValue", "")
        self.reserveGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Division #1", None))
        self.reserveTypeComboBox_4.setProperty(u"originalValue", "")
        self.reserveVeterancyGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.reserveVeterancySpinBox_4.setProperty(u"originalValue", "")
        self.reserveGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Division #1", None))
        self.reserveTypeComboBox_5.setProperty(u"originalValue", "")
        self.reserveVeterancyGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Veterancy Point", None))
        self.reserveVeterancySpinBox_5.setProperty(u"originalValue", "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.armyTab), QCoreApplication.translate("MainWindow", u"Army", None))
        self.leaderGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Leaders", None))
        self.leaderGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Leader #4", None))
        self.leaderNameGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.leaderNameLabel_4.setText("")
        self.leaderComboBox_4_1.setProperty(u"originalValue", "")
        self.leaderComboBox_4_2.setProperty(u"originalValue", "")
        self.leaderComboBox_4_3.setProperty(u"originalValue", "")
        self.leaderComboBox_4_4.setProperty(u"originalValue", "")
        self.leaderComboBox_4_5.setProperty(u"originalValue", "")
        self.leaderLevelGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.leaderLevelSpinBox_4.setProperty(u"originalValue", "")
        self.leaderSkillPointGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.leaderSkillPointSpinBox_4.setProperty(u"originalValue", "")
        self.deleteLeaderButton_4.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.createLeaderButton_4.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.leaderGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Leader #2", None))
        self.leaderNameGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.leaderNameLabel_2.setText("")
        self.leaderComboBox_2_1.setProperty(u"originalValue", "")
        self.leaderComboBox_2_2.setProperty(u"originalValue", "")
        self.leaderComboBox_2_3.setProperty(u"originalValue", "")
        self.leaderComboBox_2_4.setProperty(u"originalValue", "")
        self.leaderComboBox_2_5.setProperty(u"originalValue", "")
        self.leaderLevelGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.leaderLevelSpinBox_2.setProperty(u"originalValue", "")
        self.leaderSkillPointGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.leaderSkillPointSpinBox_2.setProperty(u"originalValue", "")
        self.deleteLeaderButton_2.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.createLeaderButton_2.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.leaderGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Leader #1", None))
        self.leaderNameGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.leaderNameLabel_1.setText("")
        self.leaderComboBox_1_1.setProperty(u"originalValue", "")
        self.leaderComboBox_1_2.setProperty(u"originalValue", "")
        self.leaderComboBox_1_3.setProperty(u"originalValue", "")
        self.leaderComboBox_1_4.setProperty(u"originalValue", "")
        self.leaderComboBox_1_5.setProperty(u"originalValue", "")
        self.leaderLevelGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.leaderLevelSpinBox_1.setProperty(u"originalValue", "")
        self.leaderSkillPointGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.leaderSkillPointSpinBox_1.setProperty(u"originalValue", "")
        self.deleteLeaderButton_1.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.createLeaderButton_1.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.leaderGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Leader #3", None))
        self.leaderNameGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.leaderNameLabel_3.setText("")
        self.leaderComboBox_3_1.setProperty(u"originalValue", "")
        self.leaderComboBox_3_2.setProperty(u"originalValue", "")
        self.leaderComboBox_3_3.setProperty(u"originalValue", "")
        self.leaderComboBox_3_4.setProperty(u"originalValue", "")
        self.leaderComboBox_3_5.setProperty(u"originalValue", "")
        self.leaderLevelGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.leaderLevelSpinBox_3.setProperty(u"originalValue", "")
        self.leaderSkillPointGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.leaderSkillPointSpinBox_3.setProperty(u"originalValue", "")
        self.deleteLeaderButton_3.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.createLeaderButton_3.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.leaderGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Leader #5", None))
        self.leaderNameGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.leaderNameLabel_5.setText("")
        self.leaderComboBox_5_1.setProperty(u"originalValue", "")
        self.leaderComboBox_5_2.setProperty(u"originalValue", "")
        self.leaderComboBox_5_3.setProperty(u"originalValue", "")
        self.leaderComboBox_5_4.setProperty(u"originalValue", "")
        self.leaderComboBox_5_5.setProperty(u"originalValue", "")
        self.leaderLevelGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.leaderLevelSpinBox_5.setProperty(u"originalValue", "")
        self.leaderSkillPointGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.leaderSkillPointSpinBox_5.setProperty(u"originalValue", "")
        self.deleteLeaderButton_5.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.createLeaderButton_5.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Reserve", None))
        self.reserveLeaderGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Leader #1", None))
        self.reserveLeaderNameGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.reserveLeaderNameLabel_1.setText("")
        self.reserveLeaderComboBox_1_1.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_1_2.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_1_3.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_1_4.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_1_5.setProperty(u"originalValue", "")
        self.reserveLeaderLevelGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.reserveLeaderLevelSpinBox_1.setProperty(u"originalValue", "")
        self.reserveLeaderSkillPointGroupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.reserveLeaderSkillPointSpinBox_1.setProperty(u"originalValue", "")
        self.reserveDeleteLeaderButton_1.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.reserveCreateLeaderButton_1.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.reserveLeaderGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Leader #2", None))
        self.reserveLeaderNameGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.reserveLeaderNameLabel_2.setText("")
        self.reserveLeaderComboBox_2_1.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_2_2.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_2_3.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_2_4.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_2_5.setProperty(u"originalValue", "")
        self.reserveLeaderLevelGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.reserveLeaderLevelSpinBox_2.setProperty(u"originalValue", "")
        self.reserveLeaderSkillPointGroupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.reserveLeaderSkillPointSpinBox_2.setProperty(u"originalValue", "")
        self.reserveDeleteLeaderButton_2.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.reserveCreateLeaderButton_2.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.reserveLeaderGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Leader #3", None))
        self.reserveLeaderNameGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.reserveLeaderNameLabel_3.setText("")
        self.reserveLeaderComboBox_3_1.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_3_2.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_3_3.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_3_4.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_3_5.setProperty(u"originalValue", "")
        self.reserveLeaderLevelGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.reserveLeaderLevelSpinBox_3.setProperty(u"originalValue", "")
        self.reserveLeaderSkillPointGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.reserveLeaderSkillPointSpinBox_3.setProperty(u"originalValue", "")
        self.reserveDeleteLeaderButton_3.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.reserveCreateLeaderButton_3.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.reserveLeaderGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Leader #4", None))
        self.reserveLeaderNameGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.reserveLeaderNameLabel_4.setText("")
        self.reserveLeaderComboBox_4_1.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_4_2.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_4_3.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_4_4.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_4_5.setProperty(u"originalValue", "")
        self.reserveLeaderLevelGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.reserveLeaderLevelSpinBox_4.setProperty(u"originalValue", "")
        self.reserveLeaderSkillPointGroupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.reserveLeaderSkillPointSpinBox_4.setProperty(u"originalValue", "")
        self.reserveDeleteLeaderButton_4.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.reserveCreateLeaderButton_4.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.reserveLeaderGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Reserve Leader #5", None))
        self.reserveLeaderNameGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Name", None))
        self.reserveLeaderNameLabel_5.setText("")
        self.reserveLeaderComboBox_5_1.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_5_2.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_5_3.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_5_4.setProperty(u"originalValue", "")
        self.reserveLeaderComboBox_5_5.setProperty(u"originalValue", "")
        self.reserveLeaderLevelGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Level", None))
        self.reserveLeaderLevelSpinBox_5.setProperty(u"originalValue", "")
        self.reserveLeaderSkillPointGroupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Unspent Skillpoints", None))
        self.reserveLeaderSkillPointSpinBox_5.setProperty(u"originalValue", "")
        self.reserveDeleteLeaderButton_5.setText(QCoreApplication.translate("MainWindow", u"Remove Leader", None))
        self.reserveCreateLeaderButton_5.setText(QCoreApplication.translate("MainWindow", u"Create Leader", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.leaderTab), QCoreApplication.translate("MainWindow", u"Leaders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inventoryTab), QCoreApplication.translate("MainWindow", u"Inventory", None))
        ___qtablewidgetitem = self.locTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Key", None)); # type: ignore
        ___qtablewidgetitem1 = self.locTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None)); # type: ignore
        self.devTabWidget.setTabText(self.devTabWidget.indexOf(self.locTab), QCoreApplication.translate("MainWindow", u"Loc", None))
        ___qtreewidgetitem = self.unitTemplateTreeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Unit Template", None));
        self.devTabWidget.setTabText(self.devTabWidget.indexOf(self.unitTemplateTab), QCoreApplication.translate("MainWindow", u"UnitTemplate", None))
        ___qtreewidgetitem1 = self.flagTemplateTreeWidget.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Flag Template", None));
        self.devTabWidget.setTabText(self.devTabWidget.indexOf(self.flagTemplateTab), QCoreApplication.translate("MainWindow", u"FlagTemplate", None))
        ___qtreewidgetitem2 = self.bustTemplateTreeWidget.headerItem()
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Bust Template", None));
        self.devTabWidget.setTabText(self.devTabWidget.indexOf(self.bustTemplateTab), QCoreApplication.translate("MainWindow", u"BustTemplate", None))
        ___qtreewidgetitem3 = self.upgradeTemplateTreeWidget.headerItem()
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Upgrade Template", None));
        self.devTabWidget.setTabText(self.devTabWidget.indexOf(self.upgradeTab), QCoreApplication.translate("MainWindow", u"UpgradeTemplate", None))
        ___qtreewidgetitem4 = self.skillsTreeWidget.headerItem()
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Skills List", None));
        self.devTabWidget.setTabText(self.devTabWidget.indexOf(self.skillsTab), QCoreApplication.translate("MainWindow", u"Skills", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devTab), QCoreApplication.translate("MainWindow", u"Dev", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

