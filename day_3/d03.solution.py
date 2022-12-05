# Preconsideration:
# Split strings in half, search for equal characters in both strings
# sum up the defined value for the characters. It works... in theory.

# Load file as usual
input_file = open('input.txt', 'r')
rucksacks = input_file.readlines()

total_sum = 0

# Iterate through all lines
for rucksack in rucksacks:

    # get string length, omit line feed
    size = len(rucksack)-1
    
    #divide strings in half and treat as individual "compartments"
    compartments = [rucksack[0 : int(size/2)], rucksack[int(size/2) : size]]

    # iterate through first compartment of every rucksack
    for item in compartments[0]:
        
        # find doubles in both compartments
        if item in compartments[1]:

            # calculate item value and add to total sum
            # Uppercase 'A' has ascii value 65 and should be 27. So we decrease by 38
            item_value = bytes(item, 'utf-8')[0]-38 

            # lowercase 'a' has an ascii value of 97. So we need to decrease by further 58 
            if item_value > 52 :
                item_value -= 58

            # finally add current item_value to total sum
            total_sum += item_value

            # kthxbye for-loop
            break

print (total_sum)