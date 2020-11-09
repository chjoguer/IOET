'''
Function that return the data from a file
@Parameter: name's file
'''
def readFile(file_name):
    try:
      fp = open(file_name, "r")
      lines = fp.readlines()
      fp.close()
    except Exception as e:
      print("The file doesn't exist")
      return -1
    return lines


''' 
Function that retun the total earned by elapsed hours
@Parameter: list of time
'''
def calculate_salary(array):
  salary = 0
  for i in array:
    time_start =i[2:].split("-")[0].split(':')[0] 
    time_end =i[2:].split("-")[1].split(':')[0]
    hour =i[2:].split("-")[0].split(':')[0]
    minutes =i[2:].split("-")[0].split(':')[1] 
    delta_t = int(time_end)-int(time_start)
    minuter=totalHoursToMinutes(int(hour),int(minutes))
    if i[:2] == 'MO' or i[:2] == 'TU' or i[:2] == 'WE' or i[:2] == 'TH' or i[:2] == 'FR':
      #00:01-09:00
      if 1 <= minuter  <= 540 :
        print("$25: ",delta_t)
        salary += 25*delta_t
      #09:01-18:00
      if 541 <= minuter  <= 1080:
        print("$15: ",delta_t)
        salary += 15*delta_t
      #18:01-00:00
      if 1081 <= minuter <=1440:
        print("$20: ",delta_t)
        salary += 20*delta_t
    elif i[:2]=='SA' or i[:2]=='SU' :
      #01:00-09:00
      if 1 <= minuter  <= 540 :
        print("$30: ",delta_t)
        salary += 30*delta_t
      #09:01-18:00
      if 541 <= minuter  <= 1080:
        print("$20: ",delta_t)
        salary += 20*delta_t
      #18:01-00:00
      if 1081 <= minuter <=1440:
        print("$25: ",delta_t)
        salary += 25*delta_t  

  return salary
      

''' 
Function that return hours in minutes
@Parameter: hours
@Parameter: Minutes
'''
def totalHoursToMinutes(hours,mins):
  return hours*60 + mins



def help_message():
  print()
  print("This a help message..")
  print("You should put a exists file in the local directory")

