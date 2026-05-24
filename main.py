import sys
import os

os.environ["QT_QPA_PLATFORM"] = "xcb"
os.environ["QT_STYLE_OVERRIDE"] = "Fusion"

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

from gui.pages.main_window import MainWindow


QApplication.setAttribute(
    Qt.ApplicationAttribute.AA_DontUseNativeMenuBar
)

app = QApplication(sys.argv)

from PyQt6.QtGui import QPalette, QColor

palette = QPalette()

palette.setColor(
    QPalette.ColorRole.WindowText,
    QColor(255, 255, 255)
)

palette.setColor(
    QPalette.ColorRole.Text,
    QColor(255, 255, 255)
)

palette.setColor(
    QPalette.ColorRole.ButtonText,
    QColor(255, 255, 255)
)

palette.setColor(
    QPalette.ColorRole.HighlightedText,
    QColor(255, 255, 255)
)

palette.setColor(
    QPalette.ColorRole.Base,
    QColor("#161922")
)

palette.setColor(
    QPalette.ColorRole.Window,
    QColor("#161922")
)

app.setPalette(palette)

app.setStyle("Fusion")

# ====================================
# ICON
# ====================================

app.setWindowIcon(
    QIcon(
        "assets/images/logo.png"
    )
)

# ====================================
# STYLE
# ====================================

app.setStyleSheet("""

QWidget {

    color: white;

    font-size: 15px;

    background: transparent;
}

QPushButton {

    background-color: #1c1f2b;

    border: 2px solid #2f3f74;

    border-radius: 14px;

    padding: 10px;

    color: white;

    font-weight: bold;
}

QPushButton:hover {

    background-color: #26335c;

    border: 2px solid #4c6fff;
}

QPushButton:pressed {

    background-color: #1d2745;
}

QLineEdit {

    background-color: #161922;

    border: 2px solid #2f3f74;

    border-radius: 12px;

    padding: 10px;

    color: white;

    selection-background-color: #3554d1;

    selection-color: white;
}

QLineEdit:focus {

    border: 2px solid #4c6fff;
}

QComboBox {

    background: #161922;

    background-color: #161922;

    border: 2px solid #2f3f74;

    border-radius: 12px;

    padding: 10px;

    padding-left: 12px;

    color: rgb(255,255,255);

    min-height: 20px;

    selection-background-color: #3554d1;

    selection-color: white;
}

QComboBox:hover {

    border: 2px solid #4c6fff;
}

QComboBox:focus {

    border: 2px solid #4c6fff;
}

QComboBox::drop-down {

    border: none;

    width: 30px;

    background: transparent;
}

QComboBox::down-arrow {

    image: none;
}

QComboBox:on {

    background-color: #161922;
}

# ====================================
# FIX WHITE KDE DROPDOWN
# ====================================

QComboBox QAbstractItemView {

    background-color: #161922;

    alternate-background-color: #161922;

    color: rgb(255,255,255);

    border: 2px solid #2f3f74;

    selection-background-color: #3554d1;

    selection-color: rgb(255,255,255);

    outline: 0;

    show-decoration-selected: 1;
}

QComboBox QAbstractItemView::item {

    background-color: #161922;

    color: rgb(255,255,255);

    min-height: 30px;
}

QComboBox QAbstractItemView::item:selected {

    background-color: #3554d1;

    color: rgb(255,255,255);
}

QAbstractItemView {

    background-color: #161922;

    alternate-background-color: #161922;

    color: white;

    selection-background-color: #3554d1;

    selection-color: white;

    border: 2px solid #2f3f74;
}

QListWidget {

    background-color: #161922;

    border: 2px solid #2f3f74;

    border-radius: 12px;

    color: white;
}

QListWidget::item {

    padding: 8px;
}

QListWidget::item:selected {

    background-color: #3554d1;

    border-radius: 8px;
}

QProgressBar {

    background-color: #161922;

    border: 2px solid #2f3f74;

    border-radius: 10px;

    text-align: center;

    color: white;
}

QProgressBar::chunk {

    background-color: #4c6fff;

    border-radius: 8px;
}

QScrollBar:vertical {

    background: #161922;

    width: 10px;

    border-radius: 5px;
}

QScrollBar::handle:vertical {

    background: #4c6fff;

    border-radius: 5px;
}

""")

window = MainWindow()

window.show()

sys.exit(app.exec())