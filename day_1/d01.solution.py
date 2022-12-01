# Idea is to read the input.txt line by line. Interpret each line as an integer
# and sum it up in an array. Repeat adding until an empty line occurs.
# When the entire file was read sort the array in descending order.
# Output the first element. That should do the Trick.

# Load file
input_file = open('input.txt', 'r')
file_lines = input_file.readlines()

# List of sums
sums = [0]
sum_count = 0

# Iterate through all lines
for line in file_lines:
    if line.strip() == "":
        # skip blank lines
        sum_count+=1
        sums.append(0)
    else:
        # add value to current sum
        sums[sum_count] += int(line.strip())

# Sort yada yada
sums.sort()
sums.reverse()

# Answer to part one is just the highest number in our list, which is the first
# element.
print(sums[0])

# Part 2 begins here