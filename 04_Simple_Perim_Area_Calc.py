def num_check(question):
    valid = False

    while not valid:
        try:
            response = float(input(question))

            if response > 0:
                return response
            else: 
                print("Please enter a number that is more than zero.")
        except ValueError:
            print("Please enter a number.")

# Main program 
print("----------------------------")
print("Area + Perimeter Calculator ")
print("----------------------------")

keep_going = ""
while keep_going == "":

    width=num_check("Please enter the width of the square.")
    height=num_check("Please enter the height of the square.")

    area = width * height
    perimeter = 2 * (width + height)
    print("Area = ",area)
    print("Perimeter = ",perimeter)

    keep_going = input("Please <enter> to keep going or any key to quit")
print()
print("Thanks for using the Area+Perimeter Calculator")
#width = float(input("Please enter the width of the square: ")) 
#if width < 0:
#    print("Please enter a number greater than zero: ")
#if width == 0:
#    print(float(input("Please enter a number that is greater than zero: ")))
#else:
##    height = float(input("Please enter the height of the square: "))
 #   if height < 0:
 #       print(float(input("Please enter a number that is greater than zero: ")))   
 #   if height == 0:
 #       print(float(input("Please enter a number that is greater than zero: "))) 

