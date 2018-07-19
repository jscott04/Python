# Jared Scott
# Group 5

#opens teams.txt and strip and splits it, stores in a list of lists called lines
lines = [line.strip().split(' ') for line in open('teams.txt', 'r')]

#list of lists called new_lines that changes the win value to an integer
new_lines = [[lines[i][0], int(lines[i][1])] for i in range(len(lines))]
names = [lines[i][0] for i in range(len(lines))] #list of all names
wins = [int(lines[i][1]) for i in range(len(lines))] #list of all wins as integers
wins = sorted(wins) #sorts the list wins (used to determine highest wins)

teams = [print('The', new_lines[i][0], 'have won', new_lines[i][1], 'games.') for i in range(len(new_lines))]

short_names = [new_lines[i][0] for i in range(len(new_lines)) if len(new_lines[i][0]) < 5]
# for loop adds the new_lines[i][0] (team name) to the list short_names if the length of the name is less than 5
print('Teams with names shorter than 5 letters:', short_names) #prints a list of teams with names shorter than 5 characters

highest_wins = [new_lines[i][0] for i in range(len(wins)) if new_lines[i][1] in wins[-3:]]
# this for loop adds new_lines[i][0] (team name) to the highest_wins list if new_lines[i][1] (wins) are in the last 3 indices of wins
# since the wins list is sorted for least to greatest, the last 3 indices are the three highest amount of wins.
print('The three teams with the highest wins are:', sorted(highest_wins))
#prints a list of the three teams with the highest wins in alphabetical order






