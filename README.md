# Stand-By Clock LED Matrix
---

## Description
This project is a clock that uses a LED matrix to display the time.
Insperation from the apple stand-by mode was taken to create this project.
this project was created using a Raspberry Pi Zero 2W with the Adafruit LED Matrix Pi Hat
and a 64x32 LED matrix.

## Features
- Displays the time in a 12 - hour format (with out the AM/PM)
- Displays the current temperature in Fahrenheit of the location you choose. Updates every 10 minutes using the OpenWeatherMap API

## Requirements
- Raspberry Pi that has 4 cores, 1GB of RAM, and a 64-bit OS.(Raspberry Pi Zero 2W was used for this project).

* Raspberry Pi Zero W (first generation) will not work with this project because it only has a 1 core processor. It can run and display the time but it flicker and can become distracting.

- Adafruit LED Matrix Pi Hat

- 64x32 LED Matrix

- OpenWeatherMap API key

- Python 3.7 or higher

- Power supply: 5V 5A
