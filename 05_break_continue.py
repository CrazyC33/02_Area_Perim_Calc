print("-" * 23)
print("*** Looping Demo #2 ***")
print("-" * 23)

for item in range(0, 5):
    print(item)

    keep_going = input("<enter> to keep looping, or any key to quit")

    if keep_going != "":
        break
print("-" * 11)
print("We are done")
print("-" * 11)