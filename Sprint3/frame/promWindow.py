import sys
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from process_miner import visualizer
from .centralWidget import Ui_centralWidget
import global_util
from process_miner.calculate import Filter, Calculate, Evaluation
from process_miner.model import Model, Accuracy
from process_miner.weight import TimeWeight, StorageWeight, AccuracyWeight, WeightSetting

class ProMWidget(QWidget, Ui_centralWidget):
    def __init__(self):
        super().__init__()
        # loadUi("./centralWidget.ui", self)
        self.setupUi(self)
        self.pushButtonOpen.clicked.connect(self.slot_btn_open_file)
        self.pushButtonRun.clicked.connect(self.slot_btn_show_result)
        self.pushButtonSubmit.clicked.connect(self.slot_btn_submit_weight)
        self.file = ""
        self.timeWeight = ""
        self.storageWeight = 0
        self.accuracyWeight = ""
        self.best_filter = None
        self.selectedMiner = None

    @pyqtSlot()
    def slot_btn_open_file(self):
        print("1111111111111")
        self.file, file_type = QFileDialog.getOpenFileName(self, 'open file', './input_file', '*.xes;;*.csv;;')
        print(file_type)
        print(self.file)

    @pyqtSlot()
    def slot_btn_show_result(self):
        print("22222222222222")
        output = visualizer.import_xes_data(self.file)
        output_full_name = global_util.get_full_path_output_file(output)
        png = QPixmap(output_full_name).scaled(self.labelImage.width(), self.labelImage.height())
        self.labelImage.setPixmap(png)

    @pyqtSlot()
    def slot_btn_submit_weight(self):

        self.timeWeight = self.lineEditTime.text()
        self.storageWeight = self.spinBoxStorage.text()
        self.accuracyWeight = self.lineEditAcc.text()


    def __set_filter(self, best_filter):
        self.best_filter = best_filter
