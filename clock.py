#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import time
from datetime import datetime
import random
import requests

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)
        self.weather_data = {"temp":"N/A","desc": "Loading..."}
        self.last_weather_update = 0
        self.api_key = "79a48df5a827d76ffbcc7cb15f263183"
        self.city = "Trujillo+Alto"

    def fetch_weather(self):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=imperial"
            #print("URL", url)
            response = requests.get(url)
            #print("Response:", response)
            if response.status_code == 200:
                data = response.json()
                #print(data)
                self.weather_data = {
                    "temp": f"{round(data['main']['temp'])}°F",
                    "desc": data['weather'][0]['description'].capitalize()
                }
            else:
                self.weather_data = {"temp": "N/A", "desc": "Error fetching weather"}
        except Exception as e:
            self.weather_data ={"temp":"N/A", "desc": "Error connecting"}

    def run(self):
        options = RGBMatrixOptions()
        options.cols = 64
        options.led_slowdown_gpio = 3

        canvas = self.matrix
        # Load fonts
        time_font = graphics.Font()
        time_font.LoadFont("fonts/helvR12.bdf")
        date_font = graphics.Font()
        date_font.LoadFont("fonts/6x9.bdf")
        maridian_font = graphics.Font()
        maridian_font.LoadFont("fonts/10x20.bdf")

        while True:
            now = datetime.now()                                                                                             #current_time = now.strftime("%I%M")  # Format time as "7:00 PM"

            current_hour = now.strftime("%I")  # Format time as "7:00 PM"
            current_min = now.strftime("%M")  # Format time as "7:00 PM"
            current_date = now.strftime("%d")  # Format date as "08/23/24"
            am_or_pm = now.strftime("%p") # Format AM or PM
            day_of_the_week = now.strftime("%a") # Format day of the week as "Mon"
                                                                                                                             # Determine the color based on time of day
            hour = now.hour
            if 21 <= hour or hour < 7:  # Bedtime: 9 PM - 7 AM
                if hour >= 23 or hour < 5: # 11 PM - 5AM
                    color = graphics.Color(1, 0, 0)  # Dark Red
                else:
                    color = graphics.Color(15, 0, 0)  #Red
            elif 8 <= hour < 17:  # Morning: 8 AM - 6 PM
                color = graphics.Color(70, 70, 70)  # White
            else:  # Evening: 6 PM - 10 PM
                color = graphics.Color(70, 30, 0)  # Orange

            # Fetch weather data every 10 minutes
            if current_min[1] == '0':
                self.fetch_weather()

            # Clear the canvas
            canvas.Clear()

            # Draw time and temperature
            graphics.DrawText(canvas, maridian_font, 7, 13, color, f"{current_hour}:{current_min}")
            graphics.DrawText(canvas, date_font, 33, 31, color, f"{self.weather_data['temp']}")
             # Calculate the time to sleep until the next minute
            now = datetime.now()  # Update now to get the most accurate current time
            seconds_to_sleep = 60 - now.second - now.microsecond / 1_000_000
            time.sleep(seconds_to_sleep)  # Sleep until the beginning of the next minute

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
