# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 235)
        self.formLayout_2 = QtWidgets.QFormLayout(Form)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_sort = QtWidgets.QLineEdit(Form)
        self.lineEdit_sort.setObjectName("lineEdit_sort")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sort)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_roast = QtWidgets.QLineEdit(Form)
        self.lineEdit_roast.setObjectName("lineEdit_roast")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_roast)
        self.checkBox_ground = QtWidgets.QCheckBox(Form)
        self.checkBox_ground.setObjectName("checkBox_ground")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_ground)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_description = QtWidgets.QLineEdit(Form)
        self.lineEdit_description.setObjectName("lineEdit_description")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_description)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox_price = QtWidgets.QSpinBox(Form)
        self.spinBox_price.setMinimum(1)
        self.spinBox_price.setMaximum(999999999)
        self.spinBox_price.setObjectName("spinBox_price")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_price)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.spinBox_grams = QtWidgets.QSpinBox(Form)
        self.spinBox_grams.setMinimum(1)
        self.spinBox_grams.setMaximum(999999999)
        self.spinBox_grams.setObjectName("spinBox_grams")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox_grams)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setObjectName("btn")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Сорт"))
        self.label_2.setText(_translate("Form", "Прожарка"))
        self.checkBox_ground.setText(_translate("Form", "Молотый"))
        self.label_3.setText(_translate("Form", "Описание вкуса"))
        self.label_4.setText(_translate("Form", "Цена"))
        self.label_5.setText(_translate("Form", "Объем упаковки"))
        self.btn.setText(_translate("Form", "Добавить / Изменить"))
