import os
import pygame
pygame.mixer.init()  # Initialize pygame mixer for sound

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
import requests

Window.size = (360, 640)

class HeatwaveAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20)

        # Load alert.wav using pygame
        try:
            self.sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "alert.wav"))
            print("✅ Pygame sound loaded successfully!")
        except Exception as e:
            self.sound = None
            print(f"❌ Failed to load sound: {e}")

        # Title
        self.add_widget(Label(
            text="🔥 Summer Heatwave Alert System",
            font_size='20sp',
            bold=True,
            size_hint=(1, 0.1),
            color=(1, 0.2, 0.2, 1)
        ))

        # City selector
        self.city_spinner = Spinner(
            text='Select a City',
            values=('Delhi', 'Hyderabad', 'Mumbai', 'Chennai', 'Kolkata',
                    'Bengaluru', 'Ahmedabad', 'Pune', 'Jaipur', 'Lucknow'),
            size_hint=(1, None),
            height=44
        )
        self.add_widget(self.city_spinner)

        # Check button
        check_button = Button(
            text="Check Heatwave Alert",
            size_hint=(1, None),
            height=50,
            background_color=(0.9, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size='16sp'
        )
        check_button.bind(on_press=self.get_prediction)
        self.add_widget(check_button)

        # Result label
        self.result_label = Label(
            text='',
            font_size='16sp',
            halign='center',
            valign='middle',
            markup=True,
            opacity=0,
            size_hint=(1, 0.4)
        )
        self.add_widget(self.result_label)

    def animate_result(self, text, color="white"):
        self.result_label.text = text
        self.result_label.color = (1, 1, 1, 1) if color == "white" else (1, 0, 0, 1)
        anim = Animation(opacity=1, duration=1)
        self.result_label.opacity = 0
        anim.start(self.result_label)

    def play_alert_sound(self, *_):
        if self.sound:
            print("🔊 Playing sound with pygame...")
            self.sound.stop()
            self.sound.play()
        else:
            print("❌ Sound is not loaded.")

    def get_prediction(self, instance):
        city = self.city_spinner.text
        if city == 'Select a City':
            self.animate_result("⚠️ Please select a city to proceed!", "white")
            return

        try:
            r = requests.get(f"http://127.0.0.1:5000/predict_live?city={city}")
            if r.ok:
                data = r.json()
                temp = data.get("temperature", "N/A")
                if data.get("heatwave"):
                    Clock.schedule_once(self.play_alert_sound, 0)
                    self.animate_result(
                        f"[color=#FF0000][b]🔥 Heatwave Alert![/b][/color]\n"
                        f"City: {city}\nTemp: {temp}°C\nStay Safe!",
                        "red"
                    )
                else:
                    self.animate_result(
                        f"[color=#00FF00][b]✅ No Heatwave[/b][/color]\n"
                        f"City: {city}\nTemp: {temp}°C\nWeather is Normal.",
                        "white"
                    )
            else:
                self.animate_result("❌ Server error!", "white")
        except Exception as e:
            self.animate_result(f"⚠️ Error: {str(e)}", "white")

class HeatwaveApp(App):
    def build(self):
        self.title = "Heatwave Alert App"
        return HeatwaveAppLayout()

if __name__ == "__main__":
    HeatwaveApp().run()
