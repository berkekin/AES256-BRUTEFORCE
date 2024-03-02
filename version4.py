import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QProgressBar, QFileDialog
from PyQt6.QtCore import QThread, pyqtSignal
from itertools import product
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

class DecryptorThread(QThread):
    update_progress = pyqtSignal(int)
    decryption_successful = pyqtSignal(str, str)  # Anahtar ve IV için sinyal

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        key_space = range(256)
        iv_space = range(256)

        with open(self.file_path, 'rb') as f:
            encrypted_data = f.read()

        total_combinations = 256 ** 32  # 256 bit anahtar uzayı
        combinations_tried = 0

        for key_tuple in product(key_space, repeat=32):  # 256 bit anahtar
            for iv_tuple in product(iv_space, repeat=16):  # 128 bit IV
                key = bytes(key_tuple)
                iv = bytes(iv_tuple)
                cipher = AES.new(key, AES.MODE_CBC, iv)
                try:
                    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
                    self.decryption_successful.emit(key.hex(), iv.hex())
                    return
                except ValueError:
                    pass

                combinations_tried += 1
                if combinations_tried % 1000000 == 0:  # Her 1.000.000 denemede bir güncelleme
                    progress = int((combinations_tried / total_combinations) * 100)
                    self.update_progress.emit(progress)

        self.update_progress.emit(100)  # İşlem tamamlandı, ilerlemeyi %100 yap

class AESDecryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.open_button = QPushButton('Şifreli Dosya Seç')
        self.open_button.clicked.connect(self.openFileDialog)
        self.layout.addWidget(self.open_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

        self.progress_bar = QProgressBar(self)
        self.layout.addWidget(self.progress_bar)

        self.setWindowTitle('AES Brute-force Şifre Çözücü')
        self.setGeometry(100, 100, 800, 600)

    def openFileDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Şifreli Dosya Seç")
        if file_name:
            self.result_text.append(f'Seçilen Dosya: {file_name}')
            self.startDecryption(file_name)
        else:
            self.result_text.append('Dosya seçilmedi.')

    def startDecryption(self, file_path):
        self.decryptor_thread = DecryptorThread(file_path)
        self.decryptor_thread.update_progress.connect(self.updateProgress)
        self.decryptor_thread.decryption_successful.connect(self.decryptionSuccess)
        self.decryptor_thread.start()

    def updateProgress(self, progress):
        self.progress_bar.setValue(progress)

    def decryptionSuccess(self, key, iv):
        self.result_text.append(f'Şifre çözme başarılı. Anahtar: {key}, IV: {iv}')

def main():
    app = QApplication(sys.argv)
    ex = AESDecryptor()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
