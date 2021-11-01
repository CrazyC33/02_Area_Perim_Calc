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
print("----------------------")
print("Fence Cost Calculator ")
print("----------------------")

keep_going = ""
while keep_going == "":

    width=num_check("Please enter the width of the rectangle.")
    height=num_check("Please enter the height of the rectangle.")
    cost=num_check("Please enter the Price per Metre of the fence.")

    perimeter = 2 * (width + height)
    total_cost = cost * perimeter
    print("Perimeter = ",perimeter)
    print("Total Cost per metre = ",total_cost)

    keep_going = input("Please <enter> to keep going or any key to quit")
print()
print("Thanks for using the Fence Cost Calculator")