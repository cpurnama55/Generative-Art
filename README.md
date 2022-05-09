# Generative-Art
For Art 210 final art project.

This script is an audio visualizer which draws on a canvas.

Drawing_driver.py is the main script which basically takes in input from device microphone, analyzes the most dominant frequency, and draws
different things on a canvas using Python's Turtle library. This script is an instance of generative art, art created by a program that a person
doesn't necessarily have complete control over.

You should theoretically be able to use the script if you clone the repo and pip install using the requirements.txt file. I had trouble with PyAudio installation so that is the only thing you would have to install with pip manually or with a work around if you have issues with pip install. 

All this code was done in a virtual environment to it's recommended you use a virtual environment to download the modules and run the script just as a good practice.

Below is a drawing bades on audio input from the song 'Dancing Queen' by ABBA.
![Alt text](pictures/Dancing_Queen.png?raw=true "A drawing based on audio input from the song 'Dancing Queen' by ABBA")
