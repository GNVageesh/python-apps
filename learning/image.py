import sys
from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        img = Image(source='/home/vageesh/Downloads/kali.jpg',
                    size_hint=(1, .5), pos_hint={'center_x': .5, 'center_y': .5})
        return img


try:
    app = MainApp()
    app.run()
except KeyboardInterrupt:
    sys.exit()
