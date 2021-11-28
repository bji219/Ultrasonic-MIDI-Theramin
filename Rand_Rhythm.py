import random
# Generate random rhythm 
def Beat(bpm):

  # Convert BPM to milliseconds
  whole = (60000/bpm)*4
  half = (60000/bpm)*2
  quarter = (60000/bpm)*1
  eigth = (60000/bpm)*0.5
  sixteenth = (60000/bpm)*0.25
  
  # Choose random division
  array = [whole,half,quarter,eigth,sixteenth]
  division = random.choice(array)
  return(division)
