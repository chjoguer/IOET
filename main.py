import Exercise.LinkedList as ld
import Exercise.exercise as e

s = ld.linked_list() # Lista enlazada
name_file = input("Please, Enter the file: ")
lines = e.readFile(name_file)

if lines==-1:
  e.help_message()
  exit(0)

for data in lines:
  user,hours_work=data.split("=")
  times = hours_work.split(",")
  earned = e.calculate_salary(times)
  print("The amount to pay ",user, "is:", earned ,"USD")
  s.add_at_end(user,earned)

s.print_list() # Imprimimos la lista de nodos
