import Exercise.LinkedList as ld
import Exercise.exercise as e

s = ld.linked_list() # Lista enlazada
lines = e.readFile('file.txt')

for data in lines:
  user,hours_work=data.split("=")
  times = hours_work.split(",")
  earned = e.calculate_salary(times)
  print("The amount to pay ",user, "is:", earned ,"USD")
  s.add_at_end(user,earned)

s.print_list() # Imprimimos la lista de nodos
