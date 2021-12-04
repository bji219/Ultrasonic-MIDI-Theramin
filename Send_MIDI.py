# Ultrasonic Distance Sensor- MIDI Send to Poly D
from gpiozero import DistanceSensor
from time import sleep
import mido
import random 

from pythonosc import osc_message_builder
from pythonosc import udp_client

# Import custom functions
from Chord_Lib import Chord_Lib
from Rand_Rhythm import Beat

# Initialize the pins on the Raspberry Pi
sensor = DistanceSensor(echo=17, trigger=4)

# Initialize Poly D as i/o
inport = mido.open_input('POLY D MIDI 1')
outport = mido.open_output('POLY D MIDI 1')

# User inputs: 
mode = input("Choose synthesizer mode [chord, arp, or theramin]: ")
check = False

while check == False
    if mode == "chord"
        tempo = int(input("Input a Tempo in BPM: "))
        chord_mode = input("Choose a chord mode [maj, min, sus, or rand]: ")
        check = True
    
    elif mode == "arp"
        tempo = int(input("Input a Tempo in BPM: "))
        arp_mode = input("Choose an arpeggiator style [maj, min, sus, or rand]: ")
        play_arp(tempo, arp_mode)
        check = True
    
    elif mode == "thermin"
        play_theramin()
        check = True
    
    elif
        print("Invalid input.")

# Read the ultrasonic distance center and calculate midi send
while True:
    
    if mode == "chord"
        # 40, E2 was 87 and 21; within piano CHORD range of midi notes
        pitch = round(sensor.distance * 60 + 40) 
        
        # call chord library function, get random chord
        chord = Chord_Lib(pitch, chord_mode)
        
        # Send notes to Poly D
        note1 = mido.Message('note_on', note = chord[0])
        note2 = mido.Message('note_on', note = chord[1])
        note3 = mido.Message('note_on', note = chord[2])
        outport.send(note1)
        outport.send(note2)
        outport.send(note3)
    
        if len(chord) >3:
            # print(chord[3])
            note4 = mido.Message('note_on', note = chord[3])
            outport.send(note4)
    else
        pitch = round(sensor.distance * 87 + 21) # wider range for arp and theramin 
        # Play single note baed on distance
        rand_note = mido.Message('note_on', note = pitch)
        outport.send(rand_note)
        
    # Reset the controller after each send (if 3 note chord played after 4 note chord)
    outport.reset()
   
    # Random division between chord or note sends
    rest = Beat(tempo, mode)
    sleep(rest)
