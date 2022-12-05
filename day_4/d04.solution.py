input_file = open('input.txt', 'r')
assignments = input_file.readlines()

fully_contained_count = 0
overlap_count = 0

for pair in assignments:
    sections = pair.replace('\n', '').split(',')

    # some (most likely) overcomplicated preparations
    sections[0] = sections[0].split('-')
    sections[1] = sections[1].split('-')

    # Part 1 check starts here
    # checks if first assignment fully contains second assignment
    if int(sections[0][0]) <= int(sections[1][0]) and int(sections[0][1]) >= int(sections[1][1]):
        fully_contained_count += 1

    # checks if second assignment fully contains first assignment
    elif int(sections[1][0]) <= int(sections[0][0]) and int(sections[1][1]) >= int(sections[0][1]):
        fully_contained_count += 1

    # Part 2 starts here.
    if int(sections[0][1]) >= int(sections[1][0]) and int(sections[0][0]) <= int(sections[1][0]):
        print (sections)
        overlap_count += 1
    elif int(sections[1][1]) >= int(sections[0][0]) and int(sections[1][0]) <= int(sections[0][0]):
        print (sections)
        overlap_count += 1

print(f'Solution part 1: {fully_contained_count}')
print(f'Solution part 2: {overlap_count}')