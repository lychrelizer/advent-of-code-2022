input_file = open ('input.txt', 'r')
device_input = input_file.read()

# part 1
# marker_length = 4

# part 2
marker_length = 14 

marker_character = marker_length

# finding markers of defined length
for i, char in enumerate(device_input): 

    # substring to check
    marker = device_input[i:i+marker_length]

    # compare unique item list length with defined marker length
    if len(set(marker)) == marker_length:
        print(f'Solution is {marker_character}')
        
        # we can end here
        break

    marker_character += 1