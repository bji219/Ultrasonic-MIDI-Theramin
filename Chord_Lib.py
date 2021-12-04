# This python file contains the chord library based on the distance from the ultrasonic distance sensor
import random # should be cached when main func called
import fnmatch # wildcards
def Chord_Lib(reading,mode_in): 
	
	
	# set the variable root equal to the distance sensor reading
	root = reading

	# Create dictionary of notes based on the root
	note_dict = {}
	notes = ['m2','maj2','m3','maj3','p4','tritone','p5','aug5','p6','m7','maj7','oct','b9','ninth','shp9','tenth','elvnth','shp11','twlth','b13','thirt']

	count=1
	for i in notes:
		note = root+count
		note_dict[i] = note
		count+=1	

	# print(note_dict)
	# Create chord dictionary
	chord_dict = {'min_triad':[root,note_dict.get('m3'),note_dict.get('p5')],
			  'maj_triad':[root,note_dict.get('maj3'),note_dict.get('p5')],
			  'aug':[root,note_dict.get('maj3'),note_dict.get('aug5')],
			  'dim':[root,note_dict.get('m3'),note_dict.get('tritone')],
			  'sus2':[root,note_dict.get('maj2'),note_dict.get('p5')],
			  'sus4':[root,note_dict.get('p4'),note_dict.get('p5')],
			  'min6':[root,note_dict.get('m3'),note_dict.get('p5'),note_dict.get('p6')],
			  'min7':[root,note_dict.get('m3'),note_dict.get('p5'),note_dict.get('m7')],
			  'maj6': [root,note_dict.get('maj3'),note_dict.get('p5'),note_dict.get('p6')],
			  'maj7': [root,note_dict.get('maj3'),note_dict.get('p5'),note_dict.get('maj7')],
			  'min_maj7': [root,note_dict.get('m3'),note_dict.get('p5'),note_dict.get('maj7')],
			  'dom7': [root,note_dict.get('maj3'),note_dict.get('p5'),note_dict.get('m7')],
                          'fifthy': [root,note_dict.get('p5'),note_dict.get('oct')],
                          'fifthier': [root,note_dict.get('p5'),note_dict.get('oct'),note_dict.get('twlth')],
                          'fourthy': [root,note_dict.get('p4'),note_dict.get('m7')],
                          'fourthier': [root,note_dict.get('p4'),note_dict.get('m7'),note_dict.get('shp9')]};
	
	# Create sub-dictionaries for other synthesizer modes
	major_chords = {j:chord_dict[j] for j in (fnmatch.filter(chord_dict.keys(), 'maj*'))}
	minor_chords = {k:chord_dict[k] for k in (fnmatch.filter(chord_dict.keys(), 'min*'))}
	sussy_chords = {l:chord_dict[l] for l in (fnmatch.filter(chord_dict.keys(), 'sus*'))}
	fifth = {m:chord_dict[m] for m in (fnmatch.filter(chord_dict.keys(), 'fifth*'))}
	fourth = {n:chord_dict[n] for n in (fnmatch.filter(chord_dict.keys(), 'fourth*'))}
	sussy_chords.update(fifth,fourth)

	if mode_in == "rand"
		# random chord (3 or 4 notes)
		choice = random.choice(list(chord_dict.values()))
	elif mode_in == "maj"
		choice = random.choice(list(major_chords.values()))
	elif mode_in == "min"
		choice = random.choice(list(minor_chords.values()))	
	elif mode_in == "sus"
		choice = random.choice(list(sussy_chords.values()))	
		
	# Return array of MIDI values
	return(choice)
