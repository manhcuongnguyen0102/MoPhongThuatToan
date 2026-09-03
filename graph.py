import sys
import random
import time
from quickSort import quick_sort
from MergeSort import merge_sort
from HeapSort import heap_sort
from PyQt5.QtWidgets import  QWidget,QApplication
from PyQt5.QtGui import QPainter, QColor 

class DrawingGraph(QWidget):
    def __init__(self):
        super().__init__()
        self.arr = []
    def gen_arr(self,size=50):
        self.arr = [random.randint(10,100) for _ in range(size)]
        self.update() # re- paint the screen
    def redraw_graph(self):
        self.update()
        QApplication.processEvents()
        time.sleep(0.05)
    def run_algorithm(self,algo_name):
        if not self.arr:
            return 
        if algo_name == "Quick Sort" :
            quick_sort(self.arr,0,len(self.arr)-1,self.redraw_graph)
        elif algo_name =="Merge Sort":
            merge_sort(self.arr,0,len(self.arr)-1,self.redraw_graph)
        elif algo_name =="Heap Sort":
            heap_sort(self.arr,self.redraw_graph)
            
    def paintEvent(self, event):
        if not self.arr:
            return
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("black"))
        graph_width = self.width()
        graph_height = self.height()
        
        bar_width = graph_width/len(self.arr)
        max_val = max(self.arr)
        
        for i,val in enumerate(self.arr):
            bar_height = (val/max_val)*(graph_height-20)
            # vi tri cua cac bar
            x = i*bar_width
            y =  graph_height-bar_height
            #style bars
           
            painter.setBrush(QColor.fromHsl(110, 234, 89))
            
            painter.setPen(QColor.fromHsl(110, 255, 120))
            
            #paint bar
            painter.drawRect(int(x),int(y),int(bar_width),int(bar_height))

            
        