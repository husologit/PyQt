from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("这是一个多功能表格")
        self.resize(920, 240)
        self.setColumnCount(6)
        self.setRowCount(4)
        self.setColumnWidth(0, 100)  # 设置0列的列宽
        # self.setRowHeight(0, 40)  # 设置0行的行高
        self.table()
        # self.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)  # 选中整行
        # self.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.setSpan(2, 0, 2, 2)
        self.insertRow(4)
        self.setItem(4, 3, QTableWidgetItem(""))
        a = self.item(4, 3)  # 返回指定单元格的对象
        a.setText("这是啥")
        a.setBackground(QBrush(QColor(255, 0, 0)))
        a.setForeground(QColor(Qt.blue))
        self.cellWidget(1,3)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def mousePressEvent(self, e):
        super(MyTable, self).mousePressEvent(e)
        print(self.itemAt(e.pos()).text())





    def table(self):
        # todo 设置表头
        self.setHorizontalHeaderLabels(["姓名", "性别", "日期", "职业", "收入", "进度", ])
        self.horizontalHeader().setStyleSheet("background-color:cyan;")
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setVerticalHeaderLabels([])
        # todo 表格中添加图片
        lbp = QLabel()
        lbp.setPixmap(QPixmap("aa.png"))
        lbp.setFixedSize(QSize(384, 216))
        lbp.setScaledContents(True)
        self.setCellWidget(0, 4, lbp)
        # todo 添加一个自己设置了大小和类型的文字。
        twi = QTableWidgetItem("Graph")
        twi.setFont(QFont("Times", 10, 12, True))
        self.setItem(1, 0, twi)
        # 添加一个弹出的日期选择，设置默认值为当前日期,显示格式为年月日。
        for i in range(self.rowCount()):
            dte = QDateTimeEdit()
            dte.setDateTime(QDateTime.currentDateTime())
            dte.setDisplayFormat("yyyy/MM/dd")
            dte.setCalendarPopup(True)
            dte.setStyleSheet("""
            QDateTimeEdit QCalendarWidget
            {
                alternate-background-color: rgb(128, 128, 128); //颜色自己可以改
                    background-color: #2F2F3E;
            }
            """)
            self.setCellWidget(i, 2, dte)
        for i in range(self.rowCount()):
            cb = QComboBox()
            cb.addItems(["上折", "下折", "压平", "压死边", "圆弧"])
            cb.setStyleSheet("""QComboBox{
            border:1px solid red;
            background-color:aliceblue;
            }""")

            self.setCellWidget(i, 3, cb)
        # TODO 添加进度条
        for i in range(self.rowCount()):
            self.progressBar = QtWidgets.QProgressBar(self)
            self.progressBar.setProperty("value", 0)
            self.progressBar.setObjectName("progressBar")
            self.progressBar.setStyleSheet("""
            QProgressBar:horizontal {
            border: 1px solid #3A3939;
            text-align: center;
            padding: 1px;
            background: transparent;
            border-color:aliceblue;
            }
            QProgressBar::chunk:horizontal {
            background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));
            }
            """)
            self.setCellWidget(i, 5, self.progressBar)
            self.step = 0
            self.timer = QTimer()
            self.timer.setInterval(150)
            self.timer.start()
            # 信号连接到槽
            self.timer.timeout.connect(self.onTimerOut)
            self.count = 0

    def onTimerOut(self):  # 重写TimeOUt
        self.count += 1
        if self.count > 10:
            self.timer.stop()
        else:
            self.progressBar.setValue(self.count)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QWidget()
    myWindow.setContentsMargins(0, 0, 0, 0)
    myWindow.setWindowIcon(QIcon("cd.png"))
    myTable = MyTable()

    btn = QPushButton("获取内容")
    hlayout = QHBoxLayout()
    hlayout.addWidget(myTable)
    hlayout.addWidget(btn)


    def a():
        # myTable.setRowHidden(1, False) if myTable.isRowHidden(1) else myTable.setRowHidden(1, True)
        b = myTable.findItems('G', Qt.MatchContains)


        print(type(myTable.cellWidget(1, 3)))
        print(type(myTable.cellWidget(1, 2)))
        print(myTable.cellWidget(1, 3).currentText())
        print(myTable.cellWidget(1, 2).text())
        print(type(myTable.cellWidget(1, 0)))
        print(myTable.item(1, 0).text())

        for i in b:
            print(i.row())



    btn.clicked.connect(a)

    myWindow.setLayout(hlayout)
    myWindow.show()
    app.exit(app.exec_())
