import sys

from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget, QPushButton,QVBoxLayout,QStackedWidget,QLabel,QHBoxLayout)
from PyQt5.QtCore import Qt
from graph import DrawingGraph

class AlgorithmVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Algorithm Visualizer")
        self.setGeometry(100, 100, 700, 500)
        self.setStyleSheet("font-family:Times New Roman;"
                           "background-color: hsl(43, 21%, 87%)")
        self.current_algo = ""
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.menu_page()
        self.visualize_page()
        
        self.stacked_widget.addWidget(self.page_menu) #0
        self.stacked_widget.addWidget(self.page_visual) #1
    def menu_page(self):
        self.page_menu = QWidget()
        layout = QVBoxLayout()
        #title
        title = QLabel("CHỌN THUẬT TOÁN SẮP XẾP")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:32px;"
                            "font-weight:bold;"
                            "margin-bottom: 20px;")
        #selection algorithm
        bnt_quick = QPushButton("1. Quick Sort")
        bnt_merge = QPushButton("2. Merge Sort")
        bnt_heap = QPushButton("3. Heap Sort")
        # styles
        bnt_quick.setMaximumWidth(200)
        bnt_merge.setMaximumWidth(200)
        bnt_heap.setMaximumWidth(200)
        self.page_menu.setStyleSheet(""" 
            QPushButton{
                font-size:22px;
                margin-bottom:15px;
                padding: 10px;
                
            
            } 
            QPushButton:hover{
                background-color: hsl(44, 9%, 71%)
            }         
        """)
        #connect
        bnt_quick.clicked.connect(lambda:self.open_visualize("Quick Sort"))
        bnt_merge.clicked.connect(lambda:self.open_visualize("Merge Sort"))
        bnt_heap.clicked.connect(lambda:self.open_visualize("Heap Sort"))
        #set layout
        layout.addWidget(title)
        layout.addWidget(bnt_quick,alignment=Qt.AlignCenter)
        layout.addWidget(bnt_merge,alignment=Qt.AlignCenter)
        layout.addWidget(bnt_heap,alignment=Qt.AlignCenter)
        self.page_menu.setLayout(layout)
    def visualize_page(self):
        self.page_visual = QWidget()
        layout  = QVBoxLayout()
        
        #labels
        self.lbl_title = QLabel("Khu vực chạy thuật toán")
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setStyleSheet("font-size: 32px;")
        # run_algo zone
        self.graphDraw = DrawingGraph()
        
        btn_generate = QPushButton("Tạo mảng ngẫu nhiên")
        btn_generate.clicked.connect(lambda: self.graphDraw.gen_arr())
        
        btn_start = QPushButton("Chạy thuật toán")
        btn_start.clicked.connect(self.start_sorting)
        #back
        btn_back = QPushButton("Quay lại menu")
        btn_back.setMaximumWidth(200)
        self.page_visual.setStyleSheet("""
            QPushButton{
                        font-size:22px;
                        margin-bottom:15px;
                        padding: 10px;
                            
                        
                        } 
            QPushButton:hover{
                            background-color: hsl(44, 9%, 71%)
                        }         
                               
        """)
        btn_back.clicked.connect(self.back_to_menu)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(btn_generate)
        button_layout.addWidget(btn_start)
        button_layout.addWidget(btn_back)
        
        layout.addWidget(self.lbl_title)
        layout.addWidget(self.graphDraw,1) # 1 for the prioritizing zone
        layout.addLayout(button_layout)
        
        self.page_visual.setLayout(layout)
        
    def open_visualize(self,algo_name):
        self.current_algo = algo_name
        self.lbl_title.setText(f"Đang mô phỏng thuật toán {algo_name}")
        self.stacked_widget.setCurrentIndex(1)
    def start_sorting(self):
        self.graphDraw.run_algorithm(self.current_algo)
    def back_to_menu(self):
        self.stacked_widget.setCurrentIndex(0)
    
        
        
def main():
    app = QApplication(sys.argv)
    window = AlgorithmVisualizer()
    window.show()
    sys.exit(app.exec_())
if __name__ =="__main__":
    main()