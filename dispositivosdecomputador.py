class Teclado:
    def __init__(self):
        pass

    def conectar_teclado(self):
        print("O teclado foi conectado!")

    def desconectar_teclado(self):
        print("O teclado foi desconectado!")


class Mouse:
    def __init__(self):
        pass

    def conectar_mouse(self):
        print("O Mouse foi conectado!")

    def desconectar_mouse(self):
        print("O Mouse foi desconectado!")


class Monitor:
    def __init__(self):
        pass

    def conectar_monitor(self):
        print("O Monitor está conectado!")

    def desconectar_monitor(self):
        print("O Monitor foi desconectado!")


class Computador:
    def __init__(self):
        self.teclado = Teclado()
        self.mouse = Mouse()
        self.monitor = Monitor()

    def iniciar_computador(self):
        print("O Computador está sendo iniciado!")
        self.teclado.conectar_teclado()
        self.mouse.conectar_mouse()
        self.monitor.conectar_monitor()

    def desligar_computador(self):
        print("O Computador está sendo desligado!")
        self.teclado.desconectar_teclado()
        self.mouse.desconectar_mouse()
        self.monitor.desconectar_monitor()

meu_computador = Computador()
meu_computador.iniciar_computador()
meu_computador.desligar_computador()
