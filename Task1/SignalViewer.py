#####################################
#        Signal Viewer App          #
#                                   #
#            Team 16                #
#                                   #
#                                   #
#####################################

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider
from PyQt5.QtGui import QIcon , QFont, QPixmap # Package to set an icon , fonts and images
from PyQt5.QtCore import Qt , QTimer  # used for alignments.
from PyQt5.QtWidgets import QLayout , QVBoxLayout , QHBoxLayout, QGridLayout ,QWidget, QFileDialog, QPushButton
import pyqtgraph as pg

# Important Variables
num_of_files = 0


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi Channel Signal Viewer")
        self.resize(1290, 909)
        self.setupUiElements()
        self.setStyleSheet("Background-color:#F0F0F0;")

    def setupUiElements(self):
        
        # Create the central widget -> Wich Will Contain All our layout.
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        ##### Graph 1 Section ####
        self.Graph1_Section = QtWidgets.QWidget(self.centralwidget)
        self.Graph1_Section.setGeometry(QtCore.QRect(0, 10, 1281, 421))
        self.Graph1_Section.setObjectName("Graph1_Section")
        self.Graph1 = QtWidgets.QWidget(self.Graph1_Section)
        self.Graph1.setGeometry(QtCore.QRect(59, 29, 861, 271))
        self.Graph1.setObjectName("Graph1")
        graph_1_layout = QHBoxLayout(self.Graph1)
        self.graph1 = pg.PlotWidget(title="Graph 1 Signals")
        graph_1_layout.addWidget(self.graph1)
        
        #-- Graph 1 Horizontal Slider --#
        self.graph_1_H_slider = QSlider(self.Graph1_Section)
        self.graph_1_H_slider.setGeometry(QtCore.QRect(60, 310, 871, 22))
        self.graph_1_H_slider.setOrientation(QtCore.Qt.Horizontal)
        self.graph_1_H_slider.setObjectName("graph_1_H_slider")
        
        #-- Graph 1 Vertical Slider --#
        self.graph_1_V_slider = QSlider(self.Graph1_Section)
        self.graph_1_V_slider.setGeometry(QtCore.QRect(940, 30, 22, 271))
        self.graph_1_V_slider.setOrientation(QtCore.Qt.Vertical)
        self.graph_1_V_slider.setObjectName("graph_1_V_slider")
        
        #-- Graph 1 Zoom In --#
        self.zoom_in_graph1 = QtWidgets.QPushButton("+" ,self.Graph1_Section)
        self.zoom_in_graph1.setGeometry(QtCore.QRect(1000, 150, 100, 100))
        self.zoom_in_graph1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zoom_in_graph1.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 2px solid black;
                border-radius: 50px;
                font-size: 40px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)
        self.zoom_in_graph1.setObjectName("zoom_in_graph1")
        
        #-- Graph 1 Zoom Out --#
        self.zoom_out_graph1 = QtWidgets.QPushButton("-", self.Graph1_Section)
        self.zoom_out_graph1.setGeometry(QtCore.QRect(1130, 150, 100, 100))
        self.zoom_out_graph1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zoom_out_graph1.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 2px solid black;
                border-radius: 50px;
                font-size: 40px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)
        self.zoom_out_graph1.setObjectName("zoom_out_graph1")
        
        #-- Graph 1 Show/Hide --#
        self.show_graph_1 = QtWidgets.QPushButton("Show", self.Graph1_Section)
        self.show_graph_1.setGeometry(QtCore.QRect(1000, 50, 111, 51))
        self.show_graph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_graph_1.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 1px solid black;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)
        self.show_graph_1.setObjectName("show_graph_1")
        
        self.hide_graph_1 = QtWidgets.QPushButton("Hide" , self.Graph1_Section)
        self.hide_graph_1.setGeometry(QtCore.QRect(1130, 50, 111, 51))
        self.hide_graph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hide_graph_1.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 1px solid black;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)
        self.hide_graph_1.setObjectName("hide_graph_1")
        
        #-- Graph 1 Browse File --#
        self.browse_file_1 = QtWidgets.QPushButton("Browse File" , self.Graph1_Section)
        self.browse_file_1.setGeometry(QtCore.QRect(800, 360, 131, 41))
        self.browse_file_1.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.browse_file_1.setObjectName("browse_file_1")
        self.browse_file_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #-- Graph 1 Transfer --#
        self.change_to_graph_2 = QPushButton("Move to Graph 2 👇", self.Graph1_Section)
        self.change_to_graph_2.setGeometry(QtCore.QRect(1015, 360, 180, 40))
        self.change_to_graph_2.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                border-radius:10px;
                background-color: #DBDBDB;
                border: 2px solid black;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }
        """)
        self.change_to_graph_2.setObjectName("move_to_graph_2")
        self.change_to_graph_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #-- Graph 1 Change Color --#
        self.Change_color_1 = QtWidgets.QPushButton("Change Color", self.Graph1_Section)
        self.Change_color_1.setGeometry(QtCore.QRect(640, 360, 151, 41))
        self.Change_color_1.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.Change_color_1.setObjectName("Change_color_1")
        
        #-- Graph 1 High Speed --#
        self.high_speed_1 = QtWidgets.QPushButton("Speed (+)", self.Graph1_Section)
        self.high_speed_1.setGeometry(QtCore.QRect(380, 360, 111, 41))
        self.high_speed_1.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.high_speed_1.setObjectName("high_speed_1")
        self.high_speed_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        #-- Graph 1 Slow Speed --#
        self.slow_speed_1 = QtWidgets.QPushButton( "Speed (-)", self.Graph1_Section)
        self.slow_speed_1.setGeometry(QtCore.QRect(500, 360, 111, 41))
        self.slow_speed_1.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.slow_speed_1.setObjectName("slow_speed_1")
        self.slow_speed_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        #-- Graph 1 Stop Simulating --#
        self.stop_graph_1 = QtWidgets.QPushButton("Stop", self.Graph1_Section)
        self.stop_graph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_graph_1.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.stop_graph_1.setObjectName("start_graph_1")
        self.stop_graph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_graph_1.setGeometry(QtCore.QRect(150, 360, 91, 41))

        #-- Graph 1 Start Simulating --#
        self.start_graph_1 = QtWidgets.QPushButton("Start", self.Graph1_Section)
        self.start_graph_1.setGeometry(QtCore.QRect(60, 360, 81, 41))
        self.start_graph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_graph_1.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.start_graph_1.setObjectName("start_graph_1")
        self.start_graph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #-- Graph 1 Rewind --#
        self.rewind_graph1 = QtWidgets.QPushButton("Rewind",self.Graph1_Section)
        self.rewind_graph1.setGeometry(QtCore.QRect(250, 360, 91, 41))
        self.rewind_graph1.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.rewind_graph1.setObjectName("rewind_graph1")



        #-- The Same Thing For Graph 2 --#
        self.Graph2_Section = QtWidgets.QWidget(self.centralwidget)
        self.Graph2_Section.setGeometry(QtCore.QRect(0, 440, 1281, 421))
        self.Graph2_Section.setObjectName("Graph2_Section")
        self.Graph2 = QtWidgets.QWidget(self.Graph2_Section)
        self.Graph2.setGeometry(QtCore.QRect(59, 29, 861, 261))
        self.Graph2.setObjectName("Graph1_2")
        graph_2_layout = QVBoxLayout(self.Graph2)
        self.graph2 = pg.PlotWidget(title="Graph 2 Signals")
        graph_2_layout.addWidget(self.graph2)

        self.graph_1_H_slider_2 = QSlider(self.Graph2_Section)
        self.graph_1_H_slider_2.setGeometry(QtCore.QRect(60, 300, 871, 22))
        self.graph_1_H_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.graph_1_H_slider_2.setObjectName("graph_1_H_slider_2")
        
        self.graph_1_V_slider_2 = QtWidgets.QSlider(self.Graph2_Section)
        self.graph_1_V_slider_2.setGeometry(QtCore.QRect(940, 30, 22, 251))
        self.graph_1_V_slider_2.setOrientation(QtCore.Qt.Vertical)
        self.graph_1_V_slider_2.setObjectName("graph_1_V_slider_2")
        
        self.zoom_in_graph2 = QtWidgets.QPushButton("+",self.Graph2_Section)
        self.zoom_in_graph2.setGeometry(QtCore.QRect(1000, 150, 100, 100))
        self.zoom_in_graph2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zoom_in_graph2.setStyleSheet("")
        self.zoom_in_graph2.setObjectName("zoom_in_graph2")
        self.zoom_in_graph2.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 2px solid black;
                border-radius: 50px;
                font-size: 40px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)


        self.zoom_out_graph2 = QtWidgets.QPushButton("-",self.Graph2_Section)
        self.zoom_out_graph2.setGeometry(QtCore.QRect(1130, 150, 100, 100))
        self.zoom_out_graph2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zoom_out_graph2.setStyleSheet("")
        self.zoom_out_graph2.setObjectName("zoom_out_graph2")
        self.zoom_out_graph2.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 2px solid black;
                border-radius: 50px;
                font-size: 40px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)

        
        self.show_graph_2 = QtWidgets.QPushButton("Show",self.Graph2_Section)
        self.show_graph_2.setGeometry(QtCore.QRect(1000, 50, 111, 51))
        self.show_graph_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_graph_2.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 1px solid black;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)
        self.show_graph_2.setObjectName("show_graph_2")

        
        self.hide_graph_2 = QtWidgets.QPushButton("Hide",self.Graph2_Section)
        self.hide_graph_2.setGeometry(QtCore.QRect(1130, 50, 111, 51))
        self.hide_graph_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hide_graph_2.setStyleSheet("""
            QPushButton {
                background-color: #DBDBDB;
                border: 1px solid black;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                background-color: white;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }

            QPushButton::pressed {
                background-color: darkgray;
                border: 2px solid #000000;
                border-radius: 50px;
                box-shadow: inset 3px 3px 8px rgba(0, 0, 0, 0.8); /* Stronger inset shadow when pressed */
            }
        """)
        self.hide_graph_2.setObjectName("hide_graph_2")
        
        self.browse_file_2 = QPushButton("Browse File",self.Graph2_Section)
        self.browse_file_2.setGeometry(QtCore.QRect(800, 350, 131, 41))
        self.browse_file_2.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.browse_file_2.setObjectName("browse_file_2")
        
        self.Change_color_2 = QtWidgets.QPushButton("Change Color",self.Graph2_Section)
        self.Change_color_2.setGeometry(QtCore.QRect(640, 350, 151, 41))
        self.Change_color_2.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.Change_color_2.setObjectName("Change_color_2")
        
        
        self.high_speed_2 = QtWidgets.QPushButton("Speed (+)",self.Graph2_Section)
        self.high_speed_2.setGeometry(QtCore.QRect(380, 350, 111, 41))
        self.high_speed_2.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.high_speed_2.setObjectName("high_speed_2")

        self.slow_speed_2 = QtWidgets.QPushButton("Speed (-)",self.Graph2_Section)
        self.slow_speed_2.setGeometry(QtCore.QRect(500, 350, 111, 41))
        self.slow_speed_2.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.slow_speed_2.setObjectName("slow_speed_2")
        
        self.stop_graph_2 = QtWidgets.QPushButton("Stop",self.Graph2_Section)
        self.stop_graph_2.setGeometry(QtCore.QRect(150, 350, 91, 41))
        self.stop_graph_2.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.stop_graph_2.setObjectName("stop_graph_2")
        
        self.start_graph_2 = QtWidgets.QPushButton("Start",self.Graph2_Section)
        self.start_graph_2.setGeometry(QtCore.QRect(60, 350, 81, 41))
        self.start_graph_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_graph_2.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.start_graph_2.setObjectName("start_graph_2")
        
        self.rewind_graph2 = QtWidgets.QPushButton("Rewind" , self.Graph2_Section)
        self.rewind_graph2.setGeometry(QtCore.QRect(250, 350, 91, 41))
        self.rewind_graph2.setStyleSheet("font-weight:bold;font-size:16px;background-color:white")
        self.rewind_graph2.setObjectName("rewind_graph2")
        
        #-- Graph 2 Transfer --#
        self.change_to_graph_1 = QPushButton("Move to Graph 1 👆", self.Graph2_Section)
        self.change_to_graph_1.setGeometry(QtCore.QRect(1020, 350, 180, 40))
        self.change_to_graph_1.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
            }

            QPushButton::hover {
                border-radius:10px;
                background-color: #DBDBDB;
                border: 2px solid black;
                box-shadow: inset 3px 3px 5px rgba(0, 0, 0, 0.5); /* Simulate an inset shadow */
            }
        """)
        self.change_to_graph_1.setObjectName("move_to_graph_2")
        self.change_to_graph_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        


        # Menu Bar for more features.
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 20))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("QMenuBar { background-color: white; }")


        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("Signal Options")
        self.setMenuBar(self.menubar)

        
        self.actionLink_Signals = QtWidgets.QAction(self)
        self.actionLink_Signals.setObjectName("Link Signals")
        self.actionSignal_Glue = QtWidgets.QAction(self)
        self.actionSignal_Glue.setObjectName("Signal Glue")
        self.menuOptions.addAction(self.actionLink_Signals)
        self.menuOptions.addAction(self.actionSignal_Glue)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.coordinates = self.menubar.addMenu('Bla Bla Coordinates')

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.menuOptions.setTitle(_translate("MainWindow", "Signal Options"))
        self.actionLink_Signals.setText(_translate("MainWindow", "Link Signals"))
        self.actionSignal_Glue.setText(_translate("MainWindow", "Signal Glue"))


    def openSignalFile(self):
        #Open File Explorer Window
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Open Signal File", "", "Signal Files (*.edf *.txt)", options=options)
        if file:
            try:
                # Parse Signal Data From the File.
                signal_data = self.load_signal(file)
                # Plot this data in the Graph.
                self.plot_signal(self.graph1, signal_data)
            except Exception as e:
                print(f"Error loading file: {e}")
    
    def load_signal(self, file_path):
        return np.loadtxt(file_path, delimiter=',')

    def plot_signal(self, graph, signal_data):
        graph.plot(signal_data[:, 1], pen='g') 


def main():

    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()



#self.graph = pg.PlotWidget(title="Cine Mode Signal")
#