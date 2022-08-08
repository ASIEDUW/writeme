 
import os
import sys
import time
import socket
import random
import pathlib
import datetime
import selinrcs
import threading
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class selix():
    def __init__(self):
        app =QApplication(sys.argv)
        
        self.win=QMainWindow()
        self.win.setWindowTitle('selix')
        self.win.setWindowOpacity(0.99)
        self.win.move(150,30)
        self.win.setWindowIcon(QIcon(':notes'))
        self.win.setFixedSize(1100,670)
        self.win.setStyleSheet("background-color:#DDDDDD")

        self.toolframe = QFrame(self.win)
        self.toolframe.resize(1090,40)
        self.toolframe.move(5,0)
        self.toolframe.setStyleSheet("background-color:#060f2e;border-radius:5px;")

        self.l1=QLabel(self.win)
        self.l1.move(10,10)
        self.l1.resize(20,20)
        self.l1.setStyleSheet("background-color:rgb(200,0,0);border-radius:10px;")

        self.l2=QLabel(self.win)
        self.l2.move(35,10)
        self.l2.resize(20,20)
        self.l2.setStyleSheet("background-color:rgb(255,0,255);border-radius:10px;")

        self.l3=QLabel(self.win)
        self.l3.move(60,10)
        self.l3.resize(20,20)
        self.l3.setStyleSheet("background-color:rgb(255,192,03);border-radius:10px;")

        self.l4=QLabel(self.win)
        self.l4.move(85,10)
        self.l4.resize(20,20)
        self.l4.setStyleSheet("background-color:green;border-radius:10px;")

        self.tabframe = QFrame(self.win)
        self.tabframe.resize(200,620)
        self.tabframe.move(5,45)
        self.tabframe.setStyleSheet("background-color:#2B65EC;border-top-right-radius:8px;border-top-left-radius:8px;")

        self.namela= QLabel('<center>..selix..</center>',self.win)
        self.namela.resize(190,40)
        self.namela.move(10,50)
        self.namela.setStyleSheet("background-color:#2B65EC;color:white;font-family:monospace,lobster;font-size:40px;")
        
        self.calendar = QCalendarWidget(self.win)
        self.calendar.resize(196,230)
        self.calendar.move(7,430)

        self.shadow = QFrame(self.win)
        self.shadow.resize(815,805)
        self.shadow.move(245,50)
        self.shadow.setStyleSheet("Background-color:#CCCCCC;border-radius:5px;")

        self.text=QTextEdit(self.win)
        self.text.resize(795,605)
        self.text.move(255,60)
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text.setStyleSheet("background-color:#FFFFFF;border-radius:2px;")

        self.wordcnt=QLabel(self.win)
        self.wordcnt.resize(40,40)
        self.wordcnt.move(1055,625)
        self.wordcnt.setStyleSheet("background-color:#8296b5;")
        
        self.open  = QAction(QIcon(':open'), 'Open',self.win)
        self.new  = QAction(QIcon(':new'), 'New',self.win)
        self.save = QAction(QIcon(':disk'), 'Save',self.win)
        self.undo = QAction(QIcon(':undo'), 'Undo',self.win)
        self.redo = QAction(QIcon(':redo'), 'Redo',self.win)
        self.image= QAction(QIcon(':image'),'Image',self.win)
        self.cut  = QAction(QIcon(':cut'),  'Cut',self.win)
        self.copy = QAction(QIcon(':copy'), 'Copy',self.win)
        self.paste= QAction(QIcon(':paste'),'Paste',self.win)
        self.fonts= QAction(QIcon(':fonts'),'Increase-font',self.win)
        self.fontd= QAction(QIcon(':fontred'),'Decrease-font',self.win)
        self.left= QAction(QIcon(':left'),'Align-Left',self.win)
        self.right= QAction(QIcon(':right'),'Align-Rigth',self.win)
        self.center= QAction(QIcon(':center'),'Align-Center',self.win)
        self.color= QAction(QIcon(':color'),'Color-font',self.win)
        self.underline= QAction(QIcon(':underline'),'underline',self.win)
        self.bold= QAction(QIcon(':bold'),'Bold',self.win)
        self.font= QAction(QIcon(':font'),'Font',self.win)
        self.undoo= QAction(QIcon(':undoo'),'Undoo',self.win)

        ######---- Actions for filemenu--------
        self.mnew=QAction("&New",self.win)
        self.mopen=QAction("&Open",self.win)
        self.msave=QAction("&Save",self.win)
        self.msaveas=QAction("&Save As..",self.win)
        self.mexit=QAction("&Exit",self.win)

        ##---------Actions for viewmenu----------------
        self.vreadmode=QAction("readmode",self.win)
        self.vnight=QAction("night mode",self.win)
        ##------------Actions for edit menu--------------
        self.eundo=QAction("Undo",self.win)
        self.eredo=QAction("Redo",self.win)
        self.ecopy=QAction("Copy",self.win)
        self.ecut=QAction("Cut",self.win)
        self.epaste=QAction("Paste",self.win)
        ###----------creating a menubar to hold the menus-----------
        self.menubar =QMenuBar(self.win)
        self.menubar.setStyleSheet("font-size:16px;")
        self.menubar.move(210,5)
        self.menubar.resize(180,30)
        
        ######--------filemenu--------------------
        self.filemenu =QMenu('File',self.win)
        self.filemenu.addAction(self.mnew)
        self.filemenu.addAction(self.mopen)
        self.filemenu.addAction(self.msave)
        self.filemenu.addAction(self.msaveas)
        self.filemenu.addAction(self.mexit)

        ####----------view menu------------------
        self.viewmenu =QMenu('View',self.win)
        self.viewmenu.addAction(self.vnight)
        self.viewmenu.addAction(self.vreadmode)

        self.editmenu =QMenu('Edit',self.win)
        self.editmenu.addAction(self.eundo)
        self.editmenu.addAction(self.eredo)
        self.editmenu.addAction(self.ecopy)
        self.editmenu.addAction(self.ecut)
        self.editmenu.addAction(self.epaste)
        
        
        self.helpmenu =QMenu('Help',self.win)
        self.menubar.addMenu(self.filemenu)
        self.menubar.addMenu(self.viewmenu)
        self.menubar.addMenu(self.editmenu)
        self.menubar.addMenu(self.helpmenu)

        self.toolbar=QToolBar(self.win)
        self.toolbar.setStyleSheet("background-color:#CCCCCC;")
        self.toolbar.move(395,5)
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)
        self.toolbar.resize(325,30)

        self.editing=QToolBar(self.win)
        self.editing.setStyleSheet("background-color:#CCCCCC;")
        self.editing.move(725,5)
        self.editing.setMovable(False)
        self.editing.setFloatable(False)
        self.editing.resize(365,30)

        self.toolbar.addAction(self.open)
        self.toolbar.addAction(self.new)
        self.toolbar.addAction(self.save)
        self.toolbar.addAction(self.undo)
        self.toolbar.addAction(self.redo)
        self.toolbar.addAction(self.copy)
        self.toolbar.addAction(self.cut)
        self.toolbar.addAction(self.paste)
        self.toolbar.addAction(self.image)
        
        self.editing.addAction(self.bold)
        self.editing.addAction(self.underline)
        self.editing.addAction(self.font)
        self.editing.addAction(self.left)
        self.editing.addAction(self.center)
        self.editing.addAction(self.right)
        self.editing.addAction(self.fonts)
        self.editing.addAction(self.fontd)
        self.editing.addAction(self.color)
        self.editing.addAction(self.undoo)

#####---------------------------------------------action trigers for toolbar--------------------------------------------------------------------------
        self.open.triggered.connect(self.openfun)
        self.new.triggered.connect(self.newfun)
        self.cut.triggered.connect(self.cutfun)
        self.paste.triggered.connect(self.pastefun)
        self.copy.triggered.connect(self.copyfun)
        self.undo.triggered.connect(self.undofun)
        self.redo.triggered.connect(self.redofun)
        self.image.triggered.connect(self.imagefun)
        self.save.triggered.connect(self.savefun)
###----------------------------actions for editting toolbar------------------------------------------------------------------
        self.fonts.triggered.connect(self.fontsfun)
        self.fontd.triggered.connect(self.fontdfun)
        self.bold.triggered.connect(self.boldfun)
        self.underline.triggered.connect(self.underlinefun)
        self.right.triggered.connect(self.rightfun)
        self.left.triggered.connect(self.leftfun)
        self.center.triggered.connect(self.centerfun)
        self.font.triggered.connect(self.fontfun)
        self.color.triggered.connect(self.colorfun)
        
#######--------------------------------------------action triggers for menu---------------------------------------------------------
        self.mopen.triggered.connect(self.openfun)
        self.msaveas.triggered.connect(self.saveasfun)
        self.msave.triggered.connect(self.savefun)
        self.mnew.triggered.connect(self.newfun)
        self.mexit.triggered.connect(self.exitfun)
        self.vnight.triggered.connect(self.nightfun)
        self.vreadmode.triggered.connect(self.readmodefun)
        self.eundo.triggered.connect(self.undofun)
        self.eredo.triggered.connect(self.redofun)
        self.ecut.triggered.connect(self.cutfun)
        self.ecopy.triggered.connect(self.copyfun)
        self.epaste.triggered.connect(self.pastefun)
        

        self.dat1=''
        self.dat2=''
        self.dat3=''
        self.dat4=''
        self.text.setFontPointSize(9)
        self.fontincr=0
        self.sfile=''
        self.docm=False
        self.boldcnt=0
        self.undercnt=0
        self.w1 = worker()
        self.w1.sig.connect(self.style)
        self.w1.start()
        
        self.win.show()
        sys.exit(app.exec_())
######--------------------------------------------functions for standard toolbars---------------------------------------------------------------------------------
    def openfun(self):
        filedialog =QFileDialog(self.win)
        file=filedialog.getOpenFileName(self.win,"Opnen Text","C:\\","text(*txt)")[0]
        if str(file) != '':
           file=pathlib.Path(file)
           f=open(file,'r')
           while True:
               line=f.read()
               f.close()
               break
           self.text.append(line)
    def newfun(self):
        self.text.setText('')
        self.newflag=True
    def saveasfun(self):
        filedialog = QFileDialog(self.win)
        self.sfile=filedialog.getSaveFileName(self.win,"Save As","C:\\")[0]
        if str(self.sfile) != '':
           self.sfile=pathlib.Path(self.sfile)
           f=open(self.sfile,'w')
           while True:
               text=self.text.selectAll()
               self.text.copy()
               f.write(QApplication.clipboard().text())
               f.close()
               break   
    def savefun(self):
        if str(self.sfile)=='':
            self.saveasfun+
            else:    
            f=open(self.sfile,'w')
            while True:
                text=self.text.selectAll()
                self.text.copy()
                f.write(QApplication.clipboard().text())
                f.close()
                break
        self.docm = False
    def cutfun(self):
        self.text.cut()
    def pastefun(self):
        self.text.paste()   
    def copyfun(self):
        self.text.copy()
    def undofun(self):
        self.text.undo()
    def redofun(self):
        self.text.redo()
    def imagefun(self):
        filedialog =QFileDialog(self.win)
        file=filedialog.getOpenFileName(self.win,"open image","C:\\","image(*jpg)")[0]
        if str(file) !='':
           file=pathlib.Path(file)
           self.text.append(f"<img src='{file}' height =500 width=500>")
###-------------function for  editting toolbar ---------------------------------------------------------------------
    def fontsfun(self):
        self.fontincr=self.fontincr+1
        self.text.setFontPointSize(self.text.fontPointSize()+self.fontincr)
        self.incflag=True
    def fontdfun(self):
        self.fontincr=self.fontincr-1
        self.text.setFontPointSize(self.text.fontPointSize()+self.fontincr)
        self.incflag=True
    def boldfun(self):
        self.boldcnt=self.boldcnt+1
        if self.boldcnt%2==0:
            self.text.setFontWeight(QFont.Normal)
        else:
            self.text.setFontWeight(QFont.Bold)
    def underlinefun(self):
        self.text.setFontUnderline(True)
    def leftfun(self):
        self.text.setAlignment(Qt.AlignLeft)
    def centerfun(self):
        self.text.setAlignment(Qt.AlignCenter)
    def rightfun(self):
        self.text.setAlignment(Qt.AlignRight)
    def fontfun(self):
        fontd,ok = QFontDialog.getFont()
        if ok:
            self.text.setFont(fontd)
    def colorfun(self):
        colord = QColorDialog.getColor()
        self.text.setTextColor(QColor(colord))
           
###------------function for menus---------------------------------------------------------------------
    def nightfun(self):
        self.text.setStyleSheet("background-color:#b2bed1;border-radius:2px;")
    def readmodefun(self):
        self.text.setStyleSheet("background-color:#FFFFFF;border-radius:2px;")
    def exitfun(self):
        sys.exit()
    def textreturn(self):
        self.retcnt=self.retcnt+1
        self.wordcnt.setText('<p>L/{self.retcnt}</p>')
    def style(self,dat1,dat2,dat3,dat4):
        self.l1.setStyleSheet(dat1)
        self.l2.setStyleSheet(dat2)
        self.l3.setStyleSheet(dat3)
        self.l4.setStyleSheet(dat4)

        

class worker(QThread):
    sig=pyqtSignal(str,str,str,str)
    def __init__(self):
        super().__init__()
        self.sig1=("background-color:green;border-radius:0px")
        self.sig2=("background-color:rgb(255,192,03);border-radius:0px")
        self.sig3=("background-color:rgb(200,0,0);border-radius:0px")
        self.sig4=("background-color:rgb(255,0,255);border-radius:0px")
        
        self.sigl1=("background-color:rgb(255,0,255);border-radius:10px")
        self.sigl2=("background-color:rgb(200,0,0);border-radius:10px")
        self.sigl3=("background-color:rgb(255,192,03);border-radius:10px")
        self.sigl4=("background-color:green;border-radius:10px")
    def run(self):
        while True:
            try:
                time.sleep(2)
                self.sig.emit(self.sig1,self.sig2,self.sig3,self.sig4)
                time.sleep(2)
                self.sig.emit(self.sigl1,self.sigl2,self.sigl3,self.sigl4)
            except:
                print('error')
                break
clipboard=QApplication.clipboard()            

selix()        
        
        
