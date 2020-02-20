import cv2
import glob
import csv
import numpy as np
import math
import pickle
import OutLine as op

# GUI modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


path= ""

def get_size_data_e(e):
    (x, y) = e[0][0]
    (MA, ma) = e[0][1]
    angle = e[0][2]
    A = math.pi * MA * ma
    return A



def process():
    
    """
Takes in an image name, runs pick cell, then finds size of cells
and globifier. Returns list of lists of time and cell size  
    """
    #op.globifier(img)
    pickle_in = open("list.pickle", "rb")
    ctrs = pickle.load(pickle_in)
    pickle_in_t = open("time.pickle", "rb")
    time = pickle.load(pickle_in_t)
    print(ctrs)
    output= []
    i=0
    while i < len(ctrs):
        j = 0
        if len(ctrs[i])==0:
            print("empty")
        else:
            row = [time[i]]
            while j <len(ctrs[i]):
                row.append(get_size_data_e(ctrs[i][j]))
                j= j+1
            output.append(row)
        i= i+1 

    return output


def make_csv(lolocd):
    """
take in a list of lists and writes the time and data value in a csv
    """
    with open('cell Data file', 'w') as csvfile:
        wr = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(["time", "cells"])
        for locd in lolocd:
            wr.writerow(locd)
        return csv


def run():
    op.run_multi_wf(pick()+ "/")
    
def file():
    make_csv(process())


class App(QWidget):
    #path = ""
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 250
        self.top = 250
        self.width = 640
        self.height = 480
        self.path = self.initUI()
        #self.quit()
        
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        a = self.openFileNameDialog()
        
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        
        self.show()
        self.close()
        return a
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getExistingDirectory(self,"Select Directory", options=options)
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            #global path
            #path = fileName
            print(fileName)
            return fileName
        
    
##    def openFileNamesDialog(self):
##        options = QFileDialog.Options()
##        options |= QFileDialog.DontUseNativeDialog
##        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
##        if files:
##            print(files)
    
##    def saveFileDialog(self):
##        options = QFileDialog.Options()
##        options |= QFileDialog.DontUseNativeDialog
##        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
##        if fileName:
##            print(fileName)

#if __name__ == '__main__':

def pick():
    app = QApplication(sys.argv)
    print("got here1")
    ex = App()
    print("got here 2")
    #sys.exit(app.exec_())
    print("got here3")
    return ex.path 
    
    
    


    
