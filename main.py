from kivy.app import App
from kivy.uix.widget import Widget

class LoginScreen(Widget):
    pass

class DocumentCreator(App):
    def build(self):
       return LoginScreen()

if __name__ == "__main__":
    DocumentCreator().run()