from PyQt6.QtCore import QThread, pyqtSignal


class DownloadWorker(QThread):

    progress_changed = pyqtSignal(int)
    status_changed = pyqtSignal(str)
    finished_signal = pyqtSignal()
    error_signal = pyqtSignal(str)

    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        try:
            self.func(
                self.set_status,
                self.set_progress
            )

            self.finished_signal.emit()

        except Exception as e:
            self.error_signal.emit(str(e))

    def set_status(self, text):
        self.status_changed.emit(text)

    def set_progress(self, value):
        self.progress_changed.emit(value)