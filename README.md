## Ultrasonic MIDI Theramin
 
### Inspiration
After receiving a raspberry pi 3 for my birthday, I wanted to test the possibilities for integrating hardware and software. Inspired by this project on [raspberry pi's website](https://projects.raspberrypi.org/en/projects/ultrasonic-theremin/0), I decided to get my hands on an ultrasonic distance sensor and see what I could do.

### Sonic Pi Integration and Modified Code
Initially I followed the sonic pi tutorial for the ultrasonic theramin. Raspberry pi provides a wiring diagram and bill of materials for the HC-SR04 ultrasonic distance sensor. After wiring everyting up, I played around with the example python script for reading the sensor data and sending it to Sonic Pi via OSC messaging (see below).
```python
from gpiozero import DistanceSensor
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client

sensor = DistanceSensor(echo=17, trigger=4)
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

while True:
    pitch = round(sensor.distance * 100 + 30)
    sender.send_message('/play_this', pitch)
    sleep(0.1)
```
Sonic Pi was receiving the signal from the Python Script with the following:
```
live_loop :listen do
    use_real_time
    note = sync "/osc/play_this"
    play note[0]
end
```
Before I could get sound out of my stereo, I needed to configure the raspberry pi sound configuration files to interface with my Focusrite 2i2:
```

```
The raspberry pi is a great option to make your own bluetooth stereo system. I used [raspotify](https://github.com/dtcooper/raspotify) by dtcooper, which works like a charm. 


### Python Code (why use Sonic Pi?)
Playing around with the Sonic Pi software synths is fun, but why stop there? I have a Behringer Poly D, and why not try making some distance-based bloops and bleeps? Rather than trying to configure the MIDI settings on Sonic Pi v3.1 (raspberry pi version, not supported by Sam Aaron), I decided to skip the middle man and use only Python. This way, the signal from the ultrasonic distance sensor can interact directly with a hardware sythnesizer using MIDI rather than software. There is less latency and quicker sleep times do not cause tearing in the audio. I installed the [python mido package](https://mido.readthedocs.io/en/latest/) to be able to work with python and MIDI objects and modified the original code:
```python
# include modified code here

```

The script sends a MIDI command through USB MIDI to the Poly D. The note value is calculated based on the distance of your hand (or foot, or whatever) from the sensor. Mido also includes functionality for sending MIDI control commands and pitch bends, so there are a lot of possibilities.
```python
# include 'control_change' mido command and 'pitchwheel' commands here

```

### Random Chord Generator
Playing single notes is great, and adjusting the glide on my synth allowed the notes to be more [legato](https://en.wikipedia.org/wiki/Legato), but what about the other possibilities? The Poly D has 4 oscillators, which means it is capable of [paraphonicly](https://www.sweetwater.com/insync/paraphonic/) playing 4 note chords. By using the ultrasonic distance sensor reading to calculate the root, we can calculate pitches relative to the root as well as a handful of chords. For sake of musicality I am narrowing the note range to be that of a [piano](https://newt.phys.unsw.edu.au/jw/notes.html) (from A0 to C8, or MIDI note 21 to 108).

```python
root = round(sensor.Distance*87+ 21)

# Notes relative to the root
notes = ['m2','maj2','m3','maj3','p4','tritone','p5','aug5','p6','m7','maj7','oct','b9','ninth','shp9','tenth','elvnth','shp11','twlth','b13','thirt']

# Create dictionary of notes based on the root
note_dict = {}
count=1
for i in notes:
	note = root+count
	note_dict[i] = note
	count+=1	
 
# Create chord dictionary
chord_dict = {'min_triad':[root,note_dict.get('m3'),note_dict.get('p5')],
			  'maj_triad':[root,note_dict.get('maj3'),note_dict.get('p5')],
			  'aug':[root,note_dict.get('maj3'),note_dict.get('aug5')],
			  'dim':[root,note_dict.get('m3'),note_dict.get('tritone')],
			  'sus2':[root,note_dict.get('maj2'),note_dict.get('p5')],
			  'sus4':[root,note_dict.get('p4'),note_dict.get('p5')],
			  'min6':[root,note_dict.get('m3'),note_dict.get('p5'),note_dict.get('p6')],
			  'min7':[root,note_dict.get('m3'),note_dict.get('p5'),note_dict.get('m7')],
			  'maj6': [root, note_dict.get('maj3'), note_dict.get('p5'), note_dict.get('m6')],
			  'maj7': [root, note_dict.get('maj3'), note_dict.get('p5'), note_dict.get('maj7')],
			  'min_maj7': [root, note_dict.get('m3'), note_dict.get('p5'), note_dict.get('maj7')],
			  'dom7': [root, note_dict.get('maj3'), note_dict.get('p5'), note_dict.get('m7')]};

# Random Chord (3 or 4 notes)
choice = random.choice(list(chord_dict.values()))

# Create MIDI messages to send to Poly D
note1 = mido.Message('note_on', note = choice[0])
note2 = mido.Message('note_on', note = choice[1])
note3 = mido.Message('note_on', note = choice[2])

if len(choice) >3:
	note4 = mido.Message('note_on', note = choice[3])
	print(note1,note2,note3,note4)

```
While this is great for generating chords based on one reading, the next step would be to generate random chord *progressions* based on the root.




### Laser Cut Snap-Fit Case
The wiring on the proto-board seemed to interfere with the effectiveness of the distance sensor, and if I ever wanted to disconnect the sensor from the onboard pins of the raspberry pi, it would be nice to have a module that I can easily reattach. I decided to design a simple snap-together case made of acryllic to accomplish this. I housed the wiring and circuitry within the box and designed the box to fit within a smartphone camera tripod. 


```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
