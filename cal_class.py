from main import Calender

calender = Calender
year2 = int(input('Enter year:  <-1 to quit> : '))
while year2 < 1800 or year2 > 2099:
    year2 = int(input('Enter year: '))
style = input("Indicate choice: \n 1 for 3 months in 1 row\n 2 for 4 months in 1 row\n 3 for vertical arrangement")


# calender.show_year(year2)
calender.show(year2, style)