# functions go here
print()
print("*****Area & Perimeter Calculator*****")
print()

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        try:
            response = float(input("Width "))
            if response > 0:
                return response
            else: 
                print("Please enter a number that is more than zero")
        except ValueError:
            print("Please enter a number")        

# Main Routine goes here
    width = num_check("Width: ")
    height = num_check("Height: ")

    area = width * height
    perimeter = 2 * (width + height)

# Output Results    
    print("Perimeter: {} units".format(perimeter))
    print("Area: {} square units".format(area))
