# 1. Write some code to generate a list containing at least five of your favorite foods, colors, sports teams, or any other category of your choosing, and assign it to an appropriately named variable:

colorlist= ["black", "blue", "red", "yellow", "pink"]


# 2. Write some code to display your list:

print(colorlist)


# 3. Write some code to display the first element in your list using its index:

print(colorlist[0])


# 4. Write some code to display the length of your list:

print(len(colorlist))

# 5. Write some code to change the last element in your list to a different food, color, sports team, etc., and then display your list:

colorlist[2]= 'orange'
print(colorlist)

# 6. Write some code to append a new food, color, sports team, etc. to your list, and then display your list and the length of your list:

colorlist.append('purple')
print(colorlist)


# 7. Write some code to remove the fourth element of your list using its value, and then display your list and the length of your list:

colorlist.remove(colorlist[3])
len(colorlist)
print(colorlist)


# 8. Write some code to remove the second element of your list using its index, and then display your list and the length of your list:

colorlist.remove(colorlist[1])
len(colorlist)
print(colorlist)
