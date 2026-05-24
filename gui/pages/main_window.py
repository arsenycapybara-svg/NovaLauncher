from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
    QLabel
)

from PyQt6.QtGui import (
    QPixmap,
    QIcon
)

from PyQt6.QtCore import Qt

from gui.pages.play_page import PlayPage
from gui.pages.mods_page import ModsPage
from gui.pages.settings_page import SettingsPage
from gui.pages.accounts_page import AccountsPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # ====================================
        # WINDOW
        # ====================================

        self.setWindowTitle(
            "Nova Launcher"
        )

        self.resize(
            1200,
            700
        )

        self.setWindowIcon(
            QIcon(
                "assets/images/logo.png"
            )
        )

        # ====================================
        # BACKGROUND
        # ====================================

        self.background = QLabel(self)

        self.background.setPixmap(
            QPixmap(
                "assets/images/fon.jpg"
            )
        )

        self.background.setScaledContents(
            True
        )

        self.background.setGeometry(
            0,
            0,
            1200,
            700
        )

        # ====================================
        # CENTRAL
        # ====================================

        self.central = QWidget()

        self.central.setStyleSheet(
            "background: transparent;"
        )

        self.setCentralWidget(
            self.central
        )

        # ====================================
        # MAIN LAYOUT
        # ====================================

        self.main_layout = QHBoxLayout()

        self.central.setLayout(
            self.main_layout
        )

        # ====================================
        # SIDEBAR
        # ====================================

        self.sidebar = QVBoxLayout()

        # ====================================
        # LOGO
        # ====================================

        self.logo = QLabel()

        self.logo.setPixmap(
            QPixmap(
                "assets/images/logo.png"
            )
        )

        self.logo.setScaledContents(
            True
        )

        self.logo.setFixedSize(
            140,
            140
        )

        self.logo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.logo.setStyleSheet(
            """
            background: transparent;
            border-radius: 20px;
            """
        )

        self.sidebar.addWidget(
            self.logo
        )

        # ====================================
        # BUTTONS
        # ====================================

        self.play_button = QPushButton(
            "PLAY"
        )

        self.mods_button = QPushButton(
            "MODS"
        )

        self.account_button = QPushButton(
            "ACCOUNT"
        )

        self.settings_button = QPushButton(
            "SETTINGS"
        )

        self.sidebar.addWidget(
            self.play_button
        )

        self.sidebar.addWidget(
            self.mods_button
        )

        self.sidebar.addWidget(
            self.account_button
        )

        self.sidebar.addWidget(
            self.settings_button
        )

        self.sidebar.addStretch()

        # ====================================
        # VERSION LABEL
        # ====================================

        self.version_label = QLabel(
            "Nova Launcher 1.0.1beta"
        )

        self.version_label.setStyleSheet(
            """
            color: rgba(255,255,255,120);
            font-size: 13px;
            padding: 10px;
            """
        )

        self.sidebar.addWidget(
            self.version_label
        )

        # ====================================
        # STACKED WIDGET
        # ====================================

        self.stacked_widget = QStackedWidget()

        self.stacked_widget.setStyleSheet(
            "background: transparent;"
        )

        # ====================================
        # PAGES
        # ====================================

        self.play_page = PlayPage()

        self.mods_page = ModsPage()

        self.account_page = AccountsPage()

        self.settings_page = SettingsPage()

        # ====================================
        # ACCOUNT SIGNAL
        # ====================================

        self.account_page.account_changed.connect(
            self.play_page.nickname_input.setText
        )

        # ====================================
        # ADD PAGES
        # ====================================

        self.stacked_widget.addWidget(
            self.play_page
        )

        self.stacked_widget.addWidget(
            self.mods_page
        )

        self.stacked_widget.addWidget(
            self.account_page
        )

        self.stacked_widget.addWidget(
            self.settings_page
        )

        # ====================================
        # ADD TO MAIN
        # ====================================

        self.main_layout.addLayout(
            self.sidebar,
            1
        )

        self.main_layout.addWidget(
            self.stacked_widget,
            4
        )

        # ====================================
        # EVENTS
        # ====================================

        self.play_button.clicked.connect(
            lambda: self.switch_page(0)
        )

        self.mods_button.clicked.connect(
            lambda: self.switch_page(1)
        )

        self.account_button.clicked.connect(
            lambda: self.switch_page(2)
        )

        self.settings_button.clicked.connect(
            lambda: self.switch_page(3)
        )

    # ====================================
    # SWITCH PAGE
    # ====================================

    def switch_page(self, index):

        self.stacked_widget.setCurrentIndex(
            index
        )

    # ====================================
    # RESIZE EVENT
    # ====================================

    def resizeEvent(self, event):

        self.background.setGeometry(
            0,
            0,
            self.width(),
            self.height()
        )

        super().resizeEvent(event)