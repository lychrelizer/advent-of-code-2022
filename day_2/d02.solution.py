# Day 2

# Define some score variables.
# Different hands and outcomes have different scores
score_rock = 1
score_paper = 2
score_scissors = 3

score_win = 6
score_draw = 3
score_lose = 0

# Possible outcomes of a game aren't too many to put them in a list
# A & X = rock
# B & Y = paper
# C & Z = scissors
hand_match = {
    "A" : {
        "X" : score_rock + score_draw,
        "Y" : score_paper + score_win,
        "Z" : score_scissors + score_lose, 
    },
    "B" : {
        "X" : score_rock + score_lose,
        "Y" : score_paper + score_draw,
        "Z" : score_scissors + score_win, 
    },
    "C" : {
        "X" : score_rock + score_win,
        "Y" : score_paper + score_lose,
        "Z" : score_scissors + score_draw, 
    }
}

# Some file handling
input_file = open('input.txt', 'r')
matches = input_file.readlines()

total_score = 0

# Iterate through all lines
for line in matches:
    # split hands
    game = line.split()
    # add the current score
    total_score += hand_match[game[0]][game[1]]

print(total_score)
