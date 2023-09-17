
from PyQt6.QtWidgets import (
                        QMainWindow,
                        QPushButton,
                        QLabel,
                        QDialog,
                        QVBoxLayout,
                        QHBoxLayout,
                        QFileDialog,
                        QWidget,
                        QProgressBar
                    )
from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtGui import QIcon, QPixmap


import pathlib
import os
import webbrowser
import time


import paths_settings
from automatic_tagging import AutomaticTagging


path = pathlib.Path(pathlib.Path(__file__).parent)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        x, y = 800, 340
        
        self.setMinimumSize(QSize(x, y))
        self.setMaximumSize(QSize(x, y))
        self.setWindowIcon(QIcon(paths_settings.ICON_PATH))
        self.setWindowTitle("mp3 & flac tag")

        box = QVBoxLayout()
        box.setContentsMargins(10, 10, 10, 10)


        choose_button = QPushButton(text= paths_settings.CHOOSE_FILE)
        choose_button.clicked.connect(self.open_choose_window)
        choose_button.setFixedSize(QSize(x - 20, 50))
        box.addWidget(choose_button)


        sourcec_code_button = QPushButton(text= paths_settings.SOURCE_CODE)
        sourcec_code_button.clicked.connect(self.open_source_code_site)
        sourcec_code_button.setFixedSize(QSize(x - 20, 50))
        box.addWidget(sourcec_code_button)


        label = QLabel(self)
        picture = QPixmap(paths_settings.BANNER_PATH)
        label.setPixmap(picture)
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        box.addWidget(label)


        widgets = QWidget()
        widgets.setLayout(box)
        self.setCentralWidget(widgets)

    def open_choose_window(self):
        tracklist_file, _ = QFileDialog.getOpenFileName(self, 
                                                        caption= paths_settings.CHOOSE_FILE,
                                                        filter= f"""
                                                                {paths_settings.FILTER_TXT} (*.txt);;
                                                                {paths_settings.FILTER_ALL} (*)
                                                                """,
                                                        )
        if tracklist_file.endswith(".txt"):
            progress = ProgressInTagging(tracklist_file)
            End(progress.time_delta)

        else:
            ChooseCorrectFile()
    
    def open_source_code_site(self):
        webbrowser.open_new_tab("https://github.com/skrzypa/FLAC_MP3_tag")
    


class ChooseCorrectFile(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!")
        self.setWindowIcon(QIcon(paths_settings.ICON_PATH))
        self.setFixedSize(400, 50)

        box = QVBoxLayout(self)
        text_error = QLabel(paths_settings.CHOOSE_CORRECT_FILE)
        box.addWidget(text_error)

        self.exec()
    

    
class End(QDialog):
    def __init__(self, seconds: float):
        super().__init__()

        self.setWindowTitle("End")
        self.setWindowIcon(QIcon(paths_settings.ICON_PATH))
        self.setFixedSize(400, 50)

        box = QVBoxLayout(self)
        text_error = QLabel(paths_settings.TIME_DELTA % seconds)
        box.addWidget(text_error)

        self.exec()



class ProgressInTagging(QDialog):
    def __init__(self, tracklist_file):
        super().__init__()

        self.setWindowTitle("Tagging")
        self.setWindowIcon(QIcon(paths_settings.ICON_PATH))
        self.setFixedSize(400, 100)

        self.tracklist_file = tracklist_file
        
        self.auto = AutomaticTagging(self.tracklist_file)

        self.box = QVBoxLayout(self)
        self.box.setContentsMargins(10, 10, 10, 10)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(self.auto.len_of_music_files)
        self.box.addWidget(self.progress_bar)

        self.start = QPushButton(paths_settings.START)
        self.start.clicked.connect(lambda _: self.progress())
        self.box.addWidget(self.start)

        self.exec()

    def progress(self):
        start_time = time.time()

        for nr, (file, title, file_format) in enumerate(zip(self.auto.music_files, self.auto.titles, self.auto.music_files_formats), start= 1):
            self.auto.tag_music_file(nr, file, title, file_format)
            self.progress_bar.setValue(nr)

        end_time = time.time()
        self.time_delta = end_time - start_time
        
        self.accept()