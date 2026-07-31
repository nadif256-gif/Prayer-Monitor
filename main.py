from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class PrayerMonitorApp(App):
    def build(self):
        Window.clearcolor = (0.07, 0.11, 0.18, 1)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text="مراقب الصلاة", font_size='26sp', color=(0.83, 0.69, 0.22, 1)))
        for p in ["🌅 الصبح", "☀️ الظهر", "🌤️ العصر", "🌇 المغرب", "🌙 العشاء"]:
            layout.add_widget(Button(text=p, font_size='16sp', background_color=(0.05, 0.36, 0.46, 1)))
        return layout

if __name__ == '__main__':
    PrayerMonitorApp().run()
