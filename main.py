from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        label = Label(text = 'Всем привет!')
        return label

if __name__ == "__main__":
    MyApp().run()
