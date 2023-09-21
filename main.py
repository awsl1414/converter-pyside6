from PySide6.QtWidgets import QApplication, QWidget

from Ui_main import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.lengthVar = {"米": 100, "千米": 100000, "厘米": 1, "分米": 10}
        # self.weigthVar = {"克": 1, "千克": 1000, "斤": 500}
        self.lengthVar = {"米": 100, "千米": 100000, "厘米": 1, "分米": 10}
        self.weigthVar = {"克": 1, "千克": 1000, "斤": 500}
        self.TypeDict = {"长度": self.lengthVar, "质量": self.weigthVar}
        self.dataTypeComboBox.addItems(self.TypeDict.keys())
        self.oneComboBox.addItems(self.lengthVar.keys())
        self.twoComboBox.addItems(self.lengthVar.keys())
        self.bind()

    def bind(self):
        self.dataTypeComboBox.currentIndexChanged.connect(self.typeChanged)
        self.calcBtn.clicked.connect(self.calc)

    def calc(self):
        bigType = self.dataTypeComboBox.currentText()
        # 获取第一个输入框
        value = self.oneInputLineEdit.text()
        if value == "":
            return
        currentText = self.oneComboBox.currentText()
        transType = self.twoComboBox.currentText()
        standardization = float(value) * self.TypeDict[bigType][currentText]
        result = standardization / self.TypeDict[bigType][transType]
        self.originDataLable.setText(f"{value}{currentText} = ")
        self.transDataLable.setText(f"{result} {transType}")
        self.twoInputLineEdit.setText(str(result))

    def typeChanged(self, text):
        self.oneComboBox.clear()
        self.twoComboBox.clear()
        if text == 0:
            self.oneComboBox.addItems(self.lengthVar.keys())
            self.twoComboBox.addItems(self.lengthVar.keys())
        self.oneComboBox.addItems(self.weigthVar.keys())
        self.twoComboBox.addItems(self.weigthVar.keys())


if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
