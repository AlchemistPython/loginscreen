from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
Config.set("graphics","width",400)
Config.set("graphics","height",200)

class LoginScreen(Widget):
    pass

class Generate(Widget):
    def press(self):
        print("Hola mundo")

class DocumentCreator(App):
    def build(self):
       return LoginScreen()

if __name__ == "__main__":
    DocumentCreator().run()