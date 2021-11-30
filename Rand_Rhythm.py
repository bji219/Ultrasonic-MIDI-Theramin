import random # should be cached when called in main func
# Generate random rhythm 
def Beat(bpm):

  # Convert BPM to milliseconds
  whole = (60/bpm)*4
  half = (60/bpm)*2
  quarter = (60/bpm)*1
  eigth = (60/bpm)*0.5
  sixteenth = (60/bpm)*0.25
  
  # Choose random division
  array = [whole,half,quarter,eigth,sixteenth]
  division = random.choice(array)
  # print(division)
  return(division)
