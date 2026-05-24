import requests
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QListWidget, QMessageBox
)
from PyQt6.QtCore import pyqtSignal, QThread
from core.config_manager import ConfigManager


# Класс для фоновой авторизации с отладкой
class AuthWorker(QThread):
    finished = pyqtSignal(bool, str)

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.proxies = {
            "http": "socks5://user324752:wron2y@185.20.186.151:19574",
            "https": "socks5://user324752:wron2y@185.20.186.151:19574"
        }

    def run(self):
        # Исправленный URL для аутентификации Ely.by
        url = "https://authserver.ely.by/auth/authenticate"
        payload = {
            "agent": {"name": "Minecraft", "version": 1},
            "username": self.username,
            "password": self.password
        }
        try:
            print(f"Попытка входа для: {self.username}")
            response = requests.post(url, json=payload, proxies=self.proxies, timeout=10)

            # Выводим результат в консоль для отладки
            print(f"Код ответа: {response.status_code}")
            print(f"Ответ сервера: {response.text}")

            self.finished.emit(response.status_code == 200, self.username)
        except Exception as e:
            # Выводим ошибку в консоль
            print(f"Auth error (DEBUG): {e}")
            self.finished.emit(False, self.username)


class AccountsPage(QWidget):
    account_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.title = QLabel("Ely.by Accounts")
        self.layout.addWidget(self.title)

        self.nickname_input = QLineEdit()
        self.nickname_input.setPlaceholderText("Ely.by nickname or email")
        self.layout.addWidget(self.nickname_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Ely.by password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_input)

        self.add_button = QPushButton("Login & Add Account")
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Selected")
        self.layout.addWidget(self.remove_button)

        self.accounts_list = QListWidget()
        self.layout.addWidget(self.accounts_list)

        self.add_button.clicked.connect(self.add_account)
        self.remove_button.clicked.connect(self.remove_account)
        self.accounts_list.itemClicked.connect(self.select_account)

        self.load_accounts()

    def add_account(self):
        nickname = self.nickname_input.text().strip()
        password = self.password_input.text().strip()

        if not nickname or not password:
            QMessageBox.warning(self, "Error", "Enter nickname/email and password")
            return

        self.add_button.setEnabled(False)
        self.worker = AuthWorker(nickname, password)
        self.worker.finished.connect(self.on_auth_finished)
        self.worker.start()

    def on_auth_finished(self, success, nickname):
        self.add_button.setEnabled(True)
        if success:
            config = ConfigManager.load()
            accounts = config.get("accounts", [])

            if nickname not in accounts:
                accounts.append(nickname)

            config["accounts"] = accounts
            config["nickname"] = nickname
            ConfigManager.save(config)

            self.load_accounts()
            self.account_changed.emit(nickname)
            self.nickname_input.clear()
            self.password_input.clear()
            QMessageBox.information(self, "Success", f"Account {nickname} authorized!")
        else:
            QMessageBox.critical(self, "Error", "Invalid credentials or proxy connection error")

    def load_accounts(self):
        self.accounts_list.clear()
        config = ConfigManager.load()
        for nickname in config.get("accounts", []):
            self.accounts_list.addItem(nickname)

    def remove_account(self):
        item = self.accounts_list.currentItem()
        if not item: return
        nickname = item.text()
        config = ConfigManager.load()
        if nickname in config.get("accounts", []):
            config["accounts"].remove(nickname)
            ConfigManager.save(config)
            self.load_accounts()

    def select_account(self, item):
        nickname = item.text()
        config = ConfigManager.load()
        config["nickname"] = nickname
        ConfigManager.save(config)
        self.account_changed.emit(nickname)