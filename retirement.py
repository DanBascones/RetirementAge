import datetime
import calendar

def main():
    year, month = retirement_age()
    month = retirement_date()

def retirement_age():

    # init
    terminate = False

    # program greeting
    print("Social Security Full Retirement Age Calculator")

    year = 0
    month = 0

    # calculate retirement date

    while not terminate:
        retirement_age = int(input("Enter your year of birth [or Enter to exit]: "))
        monthint = int(input("Enter your month of birth: "))

        if retirement_age == 0:
            terminate = True

        elif retirement_age <= 1937:
            print("Your full retirement age is 65")
            print("This will be in " + month + " " + str(retirement_age + 65))

        elif retirement_age <= 1938:
            monthint = monthint + 2
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 65 and 2 months")
            print("This will be in " + month + " " + str(retirement_age + 65))

        elif retirement_age == 1939:
            monthint = monthint + 4
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 65 and 4 months")
            print("This will be in " + month + " " + str(retirement_age + 65))

        elif retirement_age == 1940:
            monthint = monthint + 6
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 65 and 6 months")
            print("This will be in " + month + " " + str(retirement_age + 65))

        elif retirement_age == 1941:
            monthint = monthint + 8
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 65 and 8 months")
            print("This will be in " + month + " " + str(retirement_age + 65))

        elif retirement_age == 1942:
            monthint = monthint + 10
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 65 and 10 months")
            print("This will be in " + month + " " + str(retirement_age + 65))

        elif 1943 <= retirement_age <= 1954:
            monthint = monthint
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 66")
            print("This will be in " + month + " " + str(retirement_age + 66))

        elif retirement_age == 1955:
            monthint = monthint + 2
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 66 and 2 months")
            print("This will be in " + month + " " + str(retirement_age + 66))

        elif retirement_age == 1956:
            monthint = monthint + 4
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 66 and 4 months")
            print("This will be in " + month + " " + str(retirement_age + 66))

        elif retirement_age == 1957:
            monthint = monthint + 6
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 66 and 6 months")
            print("This will be in " + month + " " + str(retirement_age + 66))

        elif retirement_age == 1958:
            monthint = monthint + 8
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 66 and 8 months")
            print("This will be in " + month + " " + str(retirement_age + 66))

        elif retirement_age == 1959:
            monthint = monthint + 10
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 66 and 10 months")
            print("This will be in " + month + " " + str(retirement_age + 66))

        elif retirement_age >= 1960:
            monthint = monthint
            month = datetime.date(1900, monthint, 1).strftime('%B')
            print("Your full retirement age is 67")
            print("This will be in " + month + " " + str(retirement_age + 67))

    return year, month

main()