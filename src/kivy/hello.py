# In The Name Of God
# ========================================
# [] File Name : hello.py
#
# [] Creation Date : 12-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================


from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello World')


TestApp().run()
