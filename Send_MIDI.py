# Ultrasonic Distance Sensor- MIDI Send to Poly D
from gpiozero import DistanceSensor
from time import sleep
import mido
import random 

from pythonosc import osc_message_builder
from pythonosc import udp_client

# Import custom function
from Chord_Lib import Chord_Lib
from Rand_Rhythm import Beat

sensor = DistanceSensor(echo=17, trigger=4)
# sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

# Initialize Poly D as i/o
inport = mido.open_input('POLY D MIDI 1')
outport = mido.open_output('POLY D MIDI 1')

# User input for the tempo
tempo = int(input("Input a Tempo in BPM: "))

# Read the ultrasonic distance center and calculate midi send
while True:
    pitch = round(sensor.distance * 60 + 40) # 40, E2 was 87 and 21; within piano CHORD range of midi notes

    # Reset the controller after each send if 3 note chord played after 4 note chord
    outport.reset()
    # Play single note baed on distance
    # rand_note = mido.Message('note_on', note = pitch)
    
    # Or, call chord library function, get random chord
    chord = Chord_Lib(pitch)
    # print(chord)
    # Send notes to Poly D
    note1 = mido.Message('note_on', note = chord[0])
    note2 = mido.Message('note_on', note = chord[1])
    note3 = mido.Message('note_on', note = chord[2])
    outport.send(note1)
    outport.send(note2)
    outport.send(note3)
    # print(note1)
    # print((chord[3]))
    if len(chord) >3:
        # print(chord[3])
        note4 = mido.Message('note_on', note = chord[3])
        outport.send(note4)

    # Time between chord sends (default is 1/8th note based on BPM)
    # rest = (60/tempo)*0.5
    # print(rest)
    # Random division between chord or note sends
    rest = Beat(tempo)
    sleep(rest)
