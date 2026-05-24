from pathlib import Path
import os
import subprocess
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget,
    QLabel, QGroupBox, QHBoxLayout
)


class ModsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.current_instance = "main"
        self.mods_path = Path(f"instances/{self.current_instance}/mods")
        self.mods_path.mkdir(parents=True, exist_ok=True)

        self.layout = QVBoxLayout(self)

        # --- КАРТОЧКА ---
        group = QGroupBox("Installed Mods")
        group_layout = QVBoxLayout()
        self.mods_list = QListWidget()
        group_layout.addWidget(self.mods_list)
        group.setLayout(group_layout)
        self.layout.addWidget(group)

        # Кнопки
        btn_layout1 = QHBoxLayout()
        self.refresh_button = QPushButton("Refresh Mods")
        self.open_folder_button = QPushButton("Open Mods Folder")
        btn_layout1.addWidget(self.refresh_button)
        btn_layout1.addWidget(self.open_folder_button)

        btn_layout2 = QHBoxLayout()
        self.install_fabric_button = QPushButton("Install Fabric")
        self.install_forge_button = QPushButton("Install Forge")
        btn_layout2.addWidget(self.install_fabric_button)
        btn_layout2.addWidget(self.install_forge_button)

        self.layout.addLayout(btn_layout1)
        self.layout.addLayout(btn_layout2)
        self.layout.addStretch()

        # События
        self.refresh_button.clicked.connect(self.load_mods)
        self.open_folder_button.clicked.connect(self.open_mods_folder)
        self.install_fabric_button.clicked.connect(self.install_fabric)
        self.install_forge_button.clicked.connect(self.install_forge)

        self.apply_page_styles()
        self.load_mods()

    def apply_page_styles(self):
        self.setStyleSheet("""
            * { font-family: 'Minecraft'; }
            QGroupBox { border: 1px solid #333; border-radius: 8px; margin-top: 10px; padding-top: 10px; color: #aaa; font-weight: bold; }
            QListWidget { background-color: #1e1e1e; border: 1px solid #333; border-radius: 5px; color: white; }
            QPushButton { background-color: #252525; color: #fff; border: 1px solid #333; border-radius: 5px; padding: 8px; }
            QPushButton:hover { border: 1px solid #4b4bff; }
        """)

    # --- ТВОИ МЕТОДЫ ---
    def load_mods(self):
        self.mods_list.clear()
        mods = list(self.mods_path.glob("*.jar"))
        if not mods:
            self.mods_list.addItem("No mods installed")
            return
        for mod in mods:
            self.mods_list.addItem(mod.name)

    def open_mods_folder(self):
        path = str(self.mods_path.absolute())
        if os.name == "nt":
            os.startfile(path)
        else:
            subprocess.Popen(["xdg-open", path])

    def install_fabric(self):
        from PyQt6.QtWidgets import QInputDialog, QMessageBox
        from core.fabric_installer import FabricInstaller
        version_id, ok = QInputDialog.getText(self, "Fabric Install", "Minecraft Version:")
        if not ok or not version_id: return
        try:
            FabricInstaller.install(version_id, str(Path(f"instances/{self.current_instance}").absolute()))
            QMessageBox.information(self, "Success", f"Fabric installed for {version_id}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def install_forge(self):
        from PyQt6.QtWidgets import QInputDialog, QMessageBox
        from core.forge_installer import ForgeInstaller
        version_id, ok = QInputDialog.getText(self, "Forge Install", "Minecraft Version:")
        if not ok or not version_id: return
        try:
            ForgeInstaller.install(version_id, str(Path(f"instances/{self.current_instance}").absolute()))
            QMessageBox.information(self, "Success", f"Forge installed for {version_id}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))