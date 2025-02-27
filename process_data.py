import pickle

#object property file load
file1 = open("./object_features_data.obj",'rb')
object_properties = pickle.load(file1)

#possible rooms and location, possible questions LLM can ask
GROOM = ['living room', 'bedroom', 'bathroom', 'office', 'dining room', 'kitchen', 'garage']
G_place = ['in sink', 'on wall', 'on shelf', 'on countertop', 'on floor', 'on coffee table', 'on kitchen table', 'on bedside table']
Questions_LLM_ask = ["fullness", "cleanliness", "material", "class", "color", "reference object"]

counter1=0
counter2=0
counter3=0

for image_id in range(1,22):
  #read the description file, skip number 19 because it was found noisy
  if image_id == 19:
    continue
  file = open('./expression_data/object'+ str(image_id)+'.txt', 'r')
  Lines = file.readlines()
  
  for input_str in Lines:
    roomKnown = ""
    LocationKnown = ""
    
    #Check if the room and location was already provided in the description and skip these expressions
    for item in GROOM:
      if item in input_str.lower():
        roomKnown = item
    for item in G_place:
      if item in input_str.lower():
        LocationKnown = item
    if roomKnown and LocationKnown:
      continue
    elif roomKnown or LocationKnown:
      continue
    
    #Room or location was not provided, LLM should predict
    else:
      counter3 += 1
      if object_properties[image_id]["room"] != "none": #Check if the label was none
        print ("LLM room prediction for ", input_str) # Calculate the score both for HIT@1, HIT@3 and with or without clarifications
        counter1 +=1
      if object_properties[image_id]["specific_place"] != "none": #Check if the label was none
        print ("LLM location prediction for ", input_str) # Calculate the score both for HIT@1, HIT@3 and with or without clarifications
        counter2 +=1
        
print(counter1,counter2, counter3)
