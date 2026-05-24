from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QCheckBox,
    QHBoxLayout
)

from PyQt6.QtGui import QColor

from core.launcher_core import LauncherCore
from core.config_manager import ConfigManager

import minecraft_launcher_lib


class PlayPage(QWidget):

    def __init__(self):
        super().__init__()

        self.core = LauncherCore()

        self.layout = QVBoxLayout(self)

        # ====================================
        # CONFIG
        # ====================================

        config = ConfigManager.load()

        # ====================================
        # INSTANCE
        # ====================================

        self.layout.addWidget(
            QLabel("Instance:")
        )

        self.instance_box = QComboBox()

        self.instance_box.addItems([
            "main"
        ])

        self.layout.addWidget(
            self.instance_box
        )

        # ====================================
        # NICKNAME
        # ====================================

        self.layout.addWidget(
            QLabel("Nickname:")
        )

        self.nickname_input = QLineEdit()

        self.nickname_input.setText(
            config.get(
                "nickname",
                "Player"
            )
        )

        self.layout.addWidget(
            self.nickname_input
        )

        # ====================================
        # RAM
        # ====================================

        self.layout.addWidget(
            QLabel("RAM:")
        )

        self.ram_selector = QComboBox()

        self.ram_selector.addItems([
            "2G",
            "4G",
            "6G",
            "8G",
            "12G",
            "16G"
        ])

        self.ram_selector.setCurrentText(
            config.get(
                "ram",
                "4G"
            )
        )

        self.layout.addWidget(
            self.ram_selector
        )

        # ====================================
        # SNAPSHOTS
        # ====================================

        self.snapshot_checkbox = QCheckBox(
            "Show Snapshots"
        )

        self.layout.addWidget(
            self.snapshot_checkbox
        )

        # ====================================
        # BUTTONS
        # ====================================

        buttons_layout = QHBoxLayout()

        self.create_button = QPushButton(
            "Create"
        )

        self.delete_button = QPushButton(
            "Delete"
        )

        buttons_layout.addWidget(
            self.create_button
        )

        buttons_layout.addWidget(
            self.delete_button
        )

        self.layout.addLayout(
            buttons_layout
        )

        # ====================================
        # VERSION LIST
        # ====================================

        self.version_list = QListWidget()

        self.layout.addWidget(
            self.version_list
        )

        # ====================================
        # VERSION LABEL
        # ====================================

        self.selected_version_label = QLabel(
            "No version selected"
        )

        self.layout.addWidget(
            self.selected_version_label
        )

        # ====================================
        # INSTALL BUTTON
        # ====================================

        self.install_button = QPushButton(
            "Install"
        )

        self.layout.addWidget(
            self.install_button
        )

        # ====================================
        # PLAY BUTTON
        # ====================================

        self.play_button = QPushButton(
            "PLAY"
        )

        self.layout.addWidget(
            self.play_button
        )

        # ====================================
        # STATUS
        # ====================================

        self.status_label = QLabel(
            "Ready"
        )

        self.layout.addWidget(
            self.status_label
        )

        # ====================================
        # LOGS
        # ====================================

        self.logs_list = QListWidget()

        self.layout.addWidget(
            self.logs_list
        )

        # ====================================
        # DATA
        # ====================================

        self.show_snapshots = False

        # ====================================
        # EVENTS
        # ====================================

        self.snapshot_checkbox.stateChanged.connect(
            self.toggle_snapshots
        )

        self.version_list.itemClicked.connect(
            self.select_version
        )

        self.install_button.clicked.connect(
            self.install_version
        )

        self.play_button.clicked.connect(
            self.play_game
        )

        self.ram_selector.currentTextChanged.connect(
            self.save_ram
        )

        # ====================================
        # LOAD
        # ====================================

        self.load_versions()

    # ====================================
    # LOAD VERSIONS
    # ====================================

    def load_versions(self):

        self.version_list.clear()

        versions = minecraft_launcher_lib.utils.get_version_list()

        installed_versions = [
            version["id"]
            for version in minecraft_launcher_lib.utils.get_installed_versions(
                "minecraft"
            )
        ]

        for version in versions:

            version_id = version["id"]

            version_type = version["type"]

            if (
                not self.show_snapshots
                and version_type == "snapshot"
            ):

                continue

            if version_id in installed_versions:

                item_text = (
                    f"{version_id} [+]"
                )

            else:

                item_text = version_id

            self.version_list.addItem(
                item_text
            )

        self.paint_installed_versions()

    # ====================================
    # GREEN INSTALLED
    # ====================================

    def paint_installed_versions(self):

        for index in range(
            self.version_list.count()
        ):

            item = self.version_list.item(
                index
            )

            if "[+]" in item.text():

                item.setForeground(
                    QColor(
                        0,
                        255,
                        0
                    )
                )

    # ====================================
    # SNAPSHOTS
    # ====================================

    def toggle_snapshots(self):

        self.show_snapshots = (
            self.snapshot_checkbox.isChecked()
        )

        self.load_versions()

    # ====================================
    # SELECT VERSION
    # ====================================

    def select_version(self, item):

        self.selected_version_label.setText(
            item.text()
        )

    # ====================================
    # INSTALL VERSION
    # ====================================

    def install_version(self):

        version = (
            self.selected_version_label.text()
            .replace(" [+]", "")
        )

        if version == "No version selected":

            return

        self.status_label.setText(
            f"Installing {version}..."
        )

        minecraft_launcher_lib.install.install_minecraft_version(
            version,
            "minecraft"
        )

        self.status_label.setText(
            "Install complete"
        )

        self.logs_list.addItem(
            f"Installed {version}"
        )

        self.load_versions()

    # ====================================
    # SAVE RAM
    # ====================================

    def save_ram(self, ram):

        config = ConfigManager.load()

        config["ram"] = ram

        ConfigManager.save(
            config
        )

    # ====================================
    # PLAY GAME
    # ====================================

    def play_game(self):

        version = (
            self.selected_version_label.text()
            .replace(" [+]", "")
        )

        if version == "No version selected":

            QMessageBox.warning(
                self,
                "Error",
                "Select version"
            )

            return

        nickname = (
            self.nickname_input.text()
            .strip()
        )

        if not nickname:

            QMessageBox.warning(
                self,
                "Error",
                "Enter nickname"
            )

            return

        config = ConfigManager.load()

        config["nickname"] = nickname

        ConfigManager.save(
            config
        )

        try:

            self.status_label.setText(
                "Launching..."
            )

            self.core.launch_game(
                version,
                nickname
            )

            self.logs_list.addItem(
                f"Launched {version}"
            )

            self.status_label.setText(
                "Game launched"
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Launch Error",
                str(error)
            )

            self.status_label.setText(
                "Launch failed"
            )