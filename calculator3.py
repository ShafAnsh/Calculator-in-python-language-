import cmath
import math

def menu():         #main
    print("choose the type of calculation you want to perfrom")
    print("1.Basic Mathematics")
    print("2.Algebra")
    # print("3.Matrix Operations")
    print("4.Geometry")
    # print("5.Unit COnverter")
    print("6.Number System")
    print("7.Statistics")
    # print("8.Trignometry")
    print("0.Exit\n")
#Basic operations

def Basic_mathmatics():     #basic maths 
    print("1.addition:\n""2.subtraction\n""3.Multiplication:\n""4.Division:\n""5.Square Root:\n""6.Power:\n""7.Logarithm:\n""8.Exponential:\n""9.Percentage:\n""10.Factorial:\n""0.Exit:\n")

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def  multiplication(a,b):
    return a * b

def devision(a,b):
    if b == 0:
        return "Can't devide by zero"
    return a / b

def square_root(a):
    return cmath.sqrt(a)

def power(a,b):
    return a**b

def logarithm(a):
    if a<= 0:
        return "Log Undefined"
    return math.log(a)

def exponential(a):
    return cmath.exp(a) 

def percentage(a,b):
    if b == 0:
        return("Can't devide by 0. Choose positive number greater than 0")
    return (a/b) * 100

def factorial(a):
    if a < 0 :
        return "Factorial not defined. Choose greate than 0 "
    return math.factorial(int(a))

#Algebra
def algebra():          #Algebra
    print("Algebra...\n""1.Linear Equation Solver.\n""2.Quadratic Equation Solver.""0.exit")

def linear_eq():
    print("ax + b = 0")
    a = int(input("enter value for a:"))
    b = int(input("enter value for b:"))
    x = -b/a
    if a ==0:
        print("Choose greater than 0 as A must be some value.")
    else:
        x = -b/a
        return x 
        
def quadratic_eq():
    print("ax**2+bx+c=0")
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b :"))
    c = int(input("Enter value of c :"))
    if a == 0:
        print("a can't be 0")
    else:
        d = (b**2)-(4*a*c)
        x1 =(-b + cmath.sqrt(d))/(2*a)
        x2 = (-b - cmath.sqrt(d))/(2*a)
        return x1,x2
    

#Geometry
def area_circle():
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    return area


def area_rectangle():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    return area


def area_triangle():
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    return area

def perimeter_circle():
    r = float(input("Enter radius: "))
    perimeter = 2 * math.pi * r
    return perimeter


def perimeter_rectangle():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    perimeter = 2 * (l + b)
    return perimeter


def perimeter_triangle():
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    perimeter = a + b + c
    return perimeter

def volume_cube():
    s = float(input("Enter side: "))
    volume = s ** 3
    return volume


def volume_sphere():
    r = float(input("Enter radius: "))
    volume = (4 / 3) * math.pi * (r ** 3)
    return volume


def volume_cylinder():
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    volume = math.pi * (r ** 2) * h
    return volume



#Unit Converter  
# def unit_converter():
#     print("UNIT CONVERTER.\n")
#     print("1.Temperature converter\n""2.Length converter\n""3.weight converter\n""4.Time converter\n""5.Speed converter\n""0.Exit\n")

# def temperature_conversion():
#     while True:

#         print("1.Celsius to Fahrenheit")
#         print("2.Fahrenheit to Celsius")
#         print("0.Exit")

#         temp_choice = int(input("Choose 1/2/0: "))

#         if temp_choice == 0:
#             break

#         elif temp_choice == 1:
#             print("Celsius to Fahrenheit:", fahrenheit())

#         elif temp_choice == 2:
#             print("Fahrenheit to Celsius:", celsius())

#         else:
#             print("Invalid Choice... Try Again")
# def meters_to_feet():
#     meters = float(input("Enter meters: "))

#     feet = meters * 3.28084

#     print("Feet:", feet)


# def feet_to_meters():
#     feet = float(input("Enter feet: "))

#     meters = feet / 3.28084

#     print("Meters:", meters)


# def kilometers_to_meters():
#     kilometers = float(input("Enter kilometers: "))

#     meters = kilometers * 1000

#     print("Meters:", meters)

# def meters_to_kilometers():
#     meters = float(input("Enter meters: "))

#     kilometers = meters / 1000

#     print("Kilometers:", kilometers)


# def centimeters_to_meters():
#     centimeters = float(input("Enter centimeters: "))

#     meters = centimeters / 100

#     print("Meters:", meters)


# def meters_to_centimeters():
#     meters = float(input("Enter meters: "))

#     centimeters = meters * 100

#     print("Centimeters:", centimeters)


 
# def fahrenheit():
#     c = float(input("Enter celcius:"))
#     f = (c*9/5)+32
#     return f
        
# def celsius():
#     f = float(input("Enter fehranheit:"))
#     c = (f-32)*5/9
#     return c




#statistics
def statistics_menu():
    print("STATISTICS..\n""1.mean: \n ""2.median: \n ""3.mode: \n ""4.Break..\n")

def mean(numbers):
    total = sum(numbers)
    return total / len(numbers)

def median(numbers):
    numbers.sort()
    n = len(numbers)

    if n % 2 == 0:
        mid1 = numbers[n // 2]
        mid2 = numbers[(n // 2) - 1]
        return (mid1 + mid2) / 2
    else:
        return numbers[n//2]

def mode(numbers):
    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = max(frequency.values())

    for key, value in frequency.items():
        if value == max_count:
            return key

#Number system convertor:
def number_system_converter():
    print("\n--- Number System Converter ---")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Octal to Decimal")
    print("4. Decimal to Octal")
    print("5. Hexadecimal to Decimal")
    print("6. Decimal to Hexadecimal")
    print("0. Back")

def binary_to_decimal():
    binary = input("Enter binary number: ")
    decimal = int(binary, 2)
    return decimal

def decimal_to_binary():
    decimal = int(input("Enter decimal number: "))
    binary = bin(decimal)[2:]
    return binary

def octal_to_decimal():
    octal = input("Enter octal number: ")
    decimal = int(octal, 8)
    return decimal

def decimal_to_octal():
    decimal = int(input("Enter decimal number: "))
    octal = oct(decimal)[2:]
    return octal

def hexadecimal_to_decimal():
    hexa = input("Enter hexadecimal number: ")
    decimal = int(hexa, 16)
    return decimal

def decimal_to_hexadecimal():
    decimal = int(input("Enter decimal number: "))
    hexa = hex(decimal)[2:]
    return hexa


while True:
    menu()
    choice = int(input("Choose number from 0 to 8: "))

    if choice == 1:
        while True:
            Basic_mathmatics()
            choice = int(input("Choose operation from 0 to 10: "))

            if choice == 0:
                break

            if choice in [1,2,3,4,6,9]:
                a = float(input("Enter value for a: "))
                b = float(input("Enter value for b: "))

            elif choice in [5, 7, 8, 10]:
                a = float(input("Enter value for a: "))

            if choice ==1:
                print(a,"+",b,"=",addition(a,b))
            elif choice == 2:
                print(a,"-",b,"=",subtraction(a,b))
            elif choice == 3:
                print(a,"*",b,"=",multiplication(a,b))
            elif choice == 4:
                print(a,"/",b,"=",devision(a,b))
            elif choice == 5:
                print("Square Root",square_root(a))
            elif choice == 6:
                print(a,"**",b,"=",power(a,b))
            elif choice == 7:
                print("Log:",logarithm(a))
            elif choice == 8:
                print("Exponential:",exponential(a))
            elif choice == 9:
                print("Percentage : ",percentage(a,b))
            elif choice == 10:
                print("Factorial",factorial(a))
            else:
                print("Invalid choice:")


    
    

    elif choice ==2:
        print("\nALgebra\n")
        
        while True:
            algebra()
            basic_choice = int(input("choose from 0,1,2:\n"))

            if  basic_choice == 0:
                break

            if basic_choice == 1:
                print("The value of x is :",linear_eq())
            elif basic_choice == 2:
               x1, x2 = quadratic_eq()
               print("x1 =", x1, "x2 =", x2)
            
            else:
                print("invalid , choose again..")

    elif choice ==3:
        print("\nMatirx Operation\n")

    elif choice ==4:
        print("\nGeometry\m")
        while True:
            print("Geometry..\n""1.Area calculator.\n""2.Perimeter calculator.\n""3.Volume calculator.\n""0.Exit\n")
            choice = int(input("Enter choice from 1,2,3,0\n"))
            if choice == 1:

                print("\nAREA CALCULATOR")
                print("1. Circle")
                print("2. Rectangle")
                print("3. Triangle")

                area_choice = int(input("Enter choice: "))

                if area_choice == 1:
                    print("Area of Circle =", area_circle())

                elif area_choice == 2:
                    print("Area of Rectangle =", area_rectangle())

                elif area_choice == 3:
                    print("Area of Triangle =", area_triangle())

                else:
                    print("Invalid choice")


            elif choice == 2:

                print("\nPERIMETER CALCULATOR")
                print("1. Circle")
                print("2. Rectangle")
                print("3. Triangle")

                peri_choice = int(input("Enter choice: "))

                if peri_choice == 1:
                    print("Circumference of Circle =", perimeter_circle())

                elif peri_choice == 2:
                    print("Perimeter of Rectangle =", perimeter_rectangle())

                elif peri_choice == 3:
                    print("Perimeter of Triangle =", perimeter_triangle())

                else:
                    print("Invalid choice")

            elif choice == 3:

                print("\nVOLUME CALCULATOR")
                print("1. Cube")
                print("2. Sphere")
                print("3. Cylinder")

                vol_choice = int(input("Enter choice: "))

                if vol_choice == 1:
                    print("Volume of Cube =", volume_cube())

                elif vol_choice == 2:
                    print("Volume of Sphere =", volume_sphere())

                elif vol_choice == 3:
                    print("Volume of Cylinder =", volume_cylinder())

                else:
                    print("Invalid choice")

            elif choice == 0:
                print("Program Ended")
                break

            else:
                print("Invalid choice")


    elif choice ==5:
        print("\nUnit Converter\n")
        while True:
            unit_converter()
            basic_choice = int(input("Choose from 1 to 6:\n"))

            if basic_choice == 0:
                break

            elif basic_choice == 1:
                temperature_conversion()

            else:
                print("Invalid.. Choose again")

            
            
    elif choice ==6:
        print("\nNumber System\n")
        while True:
            number_system_converter()
            choice = input("choose from 0 to 6.\n")
            if choice == "0":
                break

            if choice == "1":
                print("Decimal =", binary_to_decimal())

            elif choice == "2":
                print("Binary =", decimal_to_binary())

            elif choice == "3":
                print("Decimal =", octal_to_decimal())

            elif choice == "4":
                print("Octal =", decimal_to_octal())

            elif choice == "5":
                print("Decimal =", hexadecimal_to_decimal())

            elif choice == "6":
                print("Hexadecimal =", decimal_to_hexadecimal())
            else:
                print("Invalid")


        
    elif choice ==7:
        print("\nStatistics\n")
        while True:
            statistics_menu()
            basic_choice = int(input("choose from 0,1,2,3,:\n"))
            if  basic_choice == 0:
                break

            if basic_choice == 1:            
                nums = list(map(float, input("Enter numbers separated by space: ").split()))            
                print("Mean =",mean(nums))       
                
            elif basic_choice == 2:            
                nums = list(map(float, input("Enter numbers separated by space: ").split()))            
                print("Median =", median(nums))       
            elif basic_choice == 3:            
                nums = list(map(float, input("Enter numbers separated by space: ").split()))
                print("Mode =", mode(nums))

            else:            
                print("Invalid choice")
        
    elif choice ==8:
        print("Trignometry")
        
        


    elif choice ==0:
        print("exit")
        break
    else:
         print("Invalid")





