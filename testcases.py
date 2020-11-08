import unittest
import Exercise.exercise as e

class TestStringMethods(unittest.TestCase):
    def test_openFile(self):
        lista = e.readFile("FILE.TXT") 
        if lista == None:
            self.assertEqual(e.readFile("FILE.txt"),None)
        else:
            self.assertNotEqual(e.readFile("file.txt"),None)

    def test_ConvertHourInMinutes(self):
        number = e.totalHoursToMinutes(0,0)
        self.assertEqual(number,0)


    def test_salary(self):
        times1 = ['MO10:00-12:00','TH12:00-14:00','SU20:00-21:00']
        times2 = ['MO10:00-11:00','TH13:00-14:00','SU20:00-21:00']
        self.assertNotEqual(e.calculate_salary(times1),e.calculate_salary(times2))

    def test_emptysalary(self):
        times1 = []
        self.assertEqual(e.calculate_salary(times1),0)


if __name__ == '__main__':
    unittest.main()
