Christian Guerrero

# IOET EXERCISE
**A brief explanation about my solution is that through a file that the user enters immediately separates the part of the employee's name and the hours that has worked, so that later we can determine the value that corresponds to the employee for working the hours indicated in the file but taking into account the price of those hours.**

Un explicacion breve acerca de mi solucion, es que mediante un archivo que ingrese el usuario inmediatamente se separa la parte del nombre del empleado y las horas que ha trabajado para que asi luego podamos determinar el valor que corresponde al empleado por trabajar las horas que se indicaba en el archivo pero tomando en cuenta que monto tienen esas horas.

## Architecture
**The architecture of my program consists of a module called Exercise that contains a file 'exercise.py' which has all the functions that are used to carry out the correct execution of the program, as something additional also has a file 'LinkedList.py' which in this of having been requested can store all the users with their respective salaries.**

La arquitectura de mi programa consiste en un modulo llamado Exercise que contiene un archivo 'exercise.py' el cual tiene todo las funciones que se utilizan para llevar a cabo la correcta ejecucion del programa, como algo adicional tambien tiene un archivo 'LinkedList.py' el cual en este de haberse solicitado puede almacenar todos los usuarios con sus respectivos sueldos.

## Approach
**The main approach to calculate the amount of salary to be paid to the employees was to take as a list the hours they have worked and then process them and calculate the amount of hours they have worked as well as knowing what value those hours have and in this way obtain the total salary of each employee.**

El enfoque principal para poder calcular la cantidad de sueldo a pagar de los empleados fue la de tomar como arreglo las horas que han trabajado para luego procesarlas y calcular la cantidad de horas que han trabajado además de conocer que valor tienen esas horas que han trabajado y de esta manera obtendria el sueldo total de cada empleado.

## Methodology
**The methodology I used to solve this exercise was to apply cycles, however as a result the algorithm that calculates the amount of salary to be paid by the employees is o(n) meaning that it is not so efficient, this can be improved by recursivity or even divide and conquer**

La metodologia que utilice para resolver este ejercicio fue la de aplicar ciclos, sin embargo como resultado el algoritmo que calcula la cantidad de sueldo a pagar de los empleados es o(n) :c , pudiendo este mejorarse aplicando recursividad o incluso dividir y conquistar

## Instructions
If you want to execute the exercise
``` 
python main.py 
``` 
If you want to execute the testcases
``` 
python testcases.py
```
## Example
``` 
C:\Users\Christian Guerrero\Desktop\IOET> python main.py 
Please, Enter the file: file.txt
The amount to pay  RENE is: 215 USD
The amount to pay  ASTRID is: 85 USD
``` 
```
PS C:\Users\Christian Guerrero\Desktop\IOET> python testcases.py    
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK 
``` 
