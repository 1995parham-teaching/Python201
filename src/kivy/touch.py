# In The Name Of God
# ========================================
# [] File Name : touch.py
#
# [] Creation Date : 13-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================


from kivy.app import App


class TouchApp(App):
    def on_hello_press(self):
        print('Hellooooo')


TouchApp().run()
