import random # should be cached when called in main func
# Generate random rhythm 
def Beat(bpm, mode_in):

  if mode_in == "arp"
   # Time between chord sends (default is 1/8th note based on BPM)
    rest = (60/tempo)*0.5
    return(rest)
  
  elif mode_in == "chord"
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

  elif mode_in == "theramin"
    # Rest time for theramin is very quick
    return(0.01)
