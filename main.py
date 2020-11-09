import Exercise.LinkedList as ld
import Exercise.exercise as e


def main():
  #linked_list = ld.linked_list() # Lista enlazada
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
    
   #linked_list.add_at_end(user,earned)
  #linked_list.print_list()


main()
