new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

# Insert is true insert. shifts all items in array forward (linear run time)
# Append. addes item to end of the list. (usually constant time)
# extend. lets you add a new list to the original list. (run time k)

# delete. shifts all indexs to the left

