from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QGroupBox,
    QMessageBox
)

from core.config_manager import ConfigManager


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.config = ConfigManager.load()

        # ====================================
        # GROUP
        # ====================================

        group = QGroupBox(
            "Java Configuration"
        )

        group_layout = QVBoxLayout()

        # ====================================
        # JAVA PATH
        # ====================================

        self.java_label = QLabel(
            "Java Path"
        )

        self.java_input = QLineEdit()

        self.java_input.setText(
            self.config.get(
                "java_path",
                ""
            )
        )

        self.select_java_btn = QPushButton(
            "Select Java"
        )

        # ====================================
        # JVM ARGUMENTS
        # ====================================

        self.jvm_label = QLabel(
            "JVM Arguments"
        )

        self.jvm_input = QLineEdit()

        ram = self.config.get(
            "ram",
            "4G"
        )

        self.jvm_input.setText(
            f"-Xmx{ram} -Xms{ram}"
        )

        # ====================================
        # SAVE BUTTON
        # ====================================

        self.save_btn = QPushButton(
            "Save Settings"
        )

        # ====================================
        # ADD WIDGETS
        # ====================================

        group_layout.addWidget(
            self.java_label
        )

        group_layout.addWidget(
            self.java_input
        )

        group_layout.addWidget(
            self.select_java_btn
        )

        group_layout.addWidget(
            self.jvm_label
        )

        group_layout.addWidget(
            self.jvm_input
        )

        group.setLayout(
            group_layout
        )

        self.layout.addWidget(
            group
        )

        self.layout.addWidget(
            self.save_btn
        )

        # ====================================
        # EVENTS
        # ====================================

        self.select_java_btn.clicked.connect(
            self.select_java
        )

        self.save_btn.clicked.connect(
            self.save_settings
        )

    # ====================================
    # SELECT JAVA
    # ====================================

    def select_java(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Java",
            "",
            "Java (*)"
        )

        if file_path:

            self.java_input.setText(
                file_path
            )

    # ====================================
    # SAVE SETTINGS
    # ====================================

    def save_settings(self):

        config = ConfigManager.load()

        config["java_path"] = (
            self.java_input.text()
        )

        config["jvm_args"] = (
            self.jvm_input.text()
        )

        ConfigManager.save(config)

        QMessageBox.information(
            self,
            "Saved",
            "Settings saved"
        )

    # ====================================
    # REFRESH JVM
    # ====================================

    def refresh_ram(self):

        config = ConfigManager.load()

        ram = config.get(
            "ram",
            "4G"
        )

        self.jvm_input.setText(
            f"-Xmx{ram} -Xms{ram}"
        )