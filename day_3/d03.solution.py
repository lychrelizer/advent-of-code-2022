# Preconsideration:
# Split strings in half, search for equal characters in both strings
# sum up the defined value for the characters. It works... in theory.

# Load file as usual
input_file = open('input.txt', 'r')
rucksacks = input_file.readlines()

total_sum = 0
total_sum_part2 = 0

current_iteration = 0

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

    # calculations for part 2 (every third iteration)
    if current_iteration % 3 == 0:
        
        for item in rucksack:
            if item in rucksacks[current_iteration+1] and item in rucksacks[current_iteration+2]:
                
                # sum calculation is equal to calculation in part 1
                item_value = bytes(item, 'utf-8')[0]-38 
                if item_value > 52 :
                    item_value -= 58

                total_sum_part2 += item_value

                break

    current_iteration += 1

# don't forget the output
print (f'Solution part 1: {total_sum}')
print (f'Solution part 2: {total_sum_part2}')