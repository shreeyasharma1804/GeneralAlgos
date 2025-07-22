from utilities import *

def list_type(indendation_tracker, parent_object, indendation, value):
    
    curr_indendation = 0
    curr_obj = parent_object[-1]
    
    while curr_indendation < indendation:
        parent_key = indendation_tracker[curr_indendation][-1]
        if(curr_indendation == indendation - 1 and curr_obj[parent_key] == {}):
            curr_obj[parent_key] = []
        curr_obj = curr_obj[parent_key]
        curr_indendation += 1
    
    curr_obj.append(value)
    
        
          
def create_python_object(lines, indendation_tracker, parent_object):
    
    for line in lines:
        
       indendation = count_leading_spaces_loop(line)//2
       key_values = line.split(":")
       key = key_values[0].strip()
       value = None
       
       if(indendation in indendation_tracker):
          indendation_tracker[indendation].append(key)
       else:
          indendation_tracker[indendation] = [key]
       
       
       if(key[0] == "-"):
           list_type(indendation_tracker, parent_object, indendation, key[2:])
           continue
       elif (len(key_values[1].strip()) == 0):
           value = {}
       else:
           value = key_values[1].strip()
       
       if(indendation == 0):
           parent_object.append({key: value}) 
       else:
           curr_obj = parent_object[-1]
           curr_indendation = 0
           while(curr_indendation < indendation):
               parent_key = indendation_tracker[curr_indendation][-1]
               curr_obj = curr_obj[parent_key]
               curr_indendation += 1
           curr_obj[key] = value


indendation_tracker = {}
lines = convert_to_array()
parent_object = []

create_python_object(lines, indendation_tracker, parent_object)

print(parent_object)
# print(indendation_tracker)
