import sys
from PyQt5 import uic, QtWidgets
from machine.enigma import Enigma



qtCreatorFile = "enigma.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Cifrado.clicked.connect(self.accionEncriptar)
        self.Descifrado.clicked.connect(self.accionDesEncriptar)
   
    def accionEncriptar(self):
        mensaje=self.Mensaje.text().upper()
        enigma1c=self.enigma1.text().upper()
        #maquina enigma para encriptar
        enigma1 = Enigma(enigma1c.upper())
        result =self.encrypt(mensaje, enigma1)
        
        self.Salida.setText(result)
    
    def accionDesEncriptar(self):
        mensaje=self.Mensaje.text().upper()
        #maquina enigma para encriptar
        enigma1c = self.enigma1.text().upper()
        #maquina enigma para desencriptar
        enigma2c = self.enigma2.text().upper()
        enigma1 = Enigma(enigma1c)
        enigma2 = Enigma(enigma2c)

        result = self.encrypt(mensaje, enigma1)
        result2 = self.encrypt(result, enigma2)
        self.Salida.setText(result2)

   
    def encrypt(self,words, machine):
        result = []
        for i in words:
              result.append(machine.encrypt_letter(i))
        return "".join(result)



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())