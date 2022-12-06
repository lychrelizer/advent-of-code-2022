input_file = open ('input.txt', 'r')
device_input = input_file.read()

marker_character = 3

for i, character in enumerate(device_input): 
    marker_character += 1
    if (
            character == device_input[i+1] or character == device_input[i+2] or character == device_input[i+3] or
            device_input[i+1] == device_input[i+2] or device_input[i+1] == device_input[i+3] or
            device_input[i+2] == device_input[i+3]
        ):
            continue
    else:
        print(f'Correct solution is: {marker_character}')
        #print(f'{character}{device_input[i+1]}{device_input[i+2]}{device_input[i+3]}')
        break

