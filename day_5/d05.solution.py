#             [C]         [N] [R]    
# [J] [T]     [H]         [P] [L]    
# [F] [S] [T] [B]         [M] [D]    
# [C] [L] [J] [Z] [S]     [L] [B]    
# [N] [Q] [G] [J] [J]     [F] [F] [R]
# [D] [V] [B] [L] [B] [Q] [D] [M] [T]
# [B] [Z] [Z] [T] [V] [S] [V] [S] [D]
# [W] [P] [P] [D] [G] [P] [B] [P] [V]
#  1   2   3   4   5   6   7   8   9 

# as defined by input file
slots = {}
slots[1] = "WBDNCFJ"
slots[2] = "PZVQLST"
slots[3] = "PZBGJT"
slots[4] = "DTLJZBHC"
slots[5] = "GVBJS"
slots[6] = "PSQ"
slots[7] = "BVDFLMPN"
slots[8] = "PSMFBDLR"
slots[9] = "VDTR"

# the moving function
def moveCrate(num, src, dst):
    for i in range(num):
        # append element to destination
        slots[dst] += slots[src][-1]

        # remove last element from source
        slots[src] = slots[src][:-1]

# new moving function for part 2
def moveCrate9001(num, src, dst):
    slots[dst] += slots[src][len(slots[src])-num:len(slots[src])]
    slots[src] = slots[src][0:len(slots[src])-num]

# ok.. here we go
input_file = open('input.txt', 'r')
lines = input_file.readlines()

for directions in lines:
    # skip all lines that don't contain directions
    if not directions.startswith("move"):
        continue

    # extract all the numbers from directions (items 1, 3 and 5)
    direction = directions.split()
    
    # part 1
    # moveCrate(int(direction[1]), int(direction[3]), int(direction[5]))
    
    # part 2
    moveCrate9001(int(direction[1]), int(direction[3]), int(direction[5]))
    

# I could use 
# print(slots)
# and manually extract the solution, but I want a clean script output. Therefore...

# print('Solution part 1: ', end = '')
print('Solution part 2: ', end = '')
for x, slot in slots.items():
    print(slot[-1], end = '')
print()