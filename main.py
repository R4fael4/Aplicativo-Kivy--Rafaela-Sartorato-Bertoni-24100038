from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (450, 650)


class Manager(ScreenManager):
    pass 


class Menu(Screen):
    pass


class Cardapio(Screen):
    pass

class Pedido(Screen):
    pass

class Comanda(Screen):
    def salvar_comanda(self):
        numero = self.ids.numero_input.text
        nome = self.ids.nome_input.text
        pedido = self.ids.pedido_input.text
        gorjeta = self.ids.gorjeta_input.text
        endereco = self.ids.endereco_input.text

        with open('comanda.txt', 'a') as arquivo:
            arquivo.write(f'Número: {numero}\n')
            arquivo.write(f'Nome do Cliente: {nome}\n')
            arquivo.write(f'Pedido Realizado: {pedido}\n')
            arquivo.write(f'Gorjeta: {gorjeta}\n')
            arquivo.write(f'Endereço: {endereco}\n')
            arquivo.write('-' * 50 + '\n')

        self.ids.numero_input.text = ''
        self.ids.nome_input.text = ''
        self.ids.pedido_input.text = ''
        self.ids.gorjeta_input.text = ''
        self.ids.endereco_input.text = ''


class Test(App):
    def build(self):
        return Manager()
    

Test().run()