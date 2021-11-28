# Ultrasonic Distance Sensor- MIDI Send to Poly D
from gpiozero import DistanceSensor
from time import sleep
import mido
import random 

from pythonosc import osc_message_builder
from pythonosc import udp_client

# Import custom function
from Chord_Lib import Chord_Lib

sensor = DistanceSensor(echo=17, trigger=4)
# sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

# Initialize Poly D as i/o
inport = mido.open_input('Poly D MIDI')
outport = mido.open_output('Poly D MIDI')

# Read the ultrasonic distance center and calculate midi send
while True:
    pitch = round(sensor.distance * 87 + 21) # within piano range of midi notes
    
    # Play single note baed on distance
    rand_note = mido.Message('note_on', note = pitch)
    
    # Or, call chord library function, get random chord
    Chord_Lib(pitch)
    
    # Send notes to Poly D
    note1 = mido.Message('note_on', note = choice[0])
	  note2 = mido.Message('note_on', note = choice[1])
    note3 = mido.Message('note_on', note = choice[2])
	  if len(choice) >3:
		  note4 = mido.Message('note_on', note = choice[3])
    
    # Time between chord sends
    sleep(0.1)
