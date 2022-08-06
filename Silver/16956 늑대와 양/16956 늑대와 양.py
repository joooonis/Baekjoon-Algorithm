r, c = map(int, input().split())

farm = [[None for _ in range(c)] for _ in range(r)]

for i in range(r):
    line = list(input())
    for j in range(c):
        if line[j] == 'S':
            farm[i][j] = 'S'
        elif line[j] == 'W':
            farm[i][j] = 'W'

isPossible = True

for i in range(r):
    for j in range(c):
        if farm[i][j] == 'S':
            if i > 0:
                if farm[i-1][j] == None:
                    farm[i-1][j] = 'D'
                elif farm[i-1][j] == 'W':
                    isPossible = False
            if i < r - 1:
                if farm[i+1][j] == None:
                    farm[i+1][j] = 'D'
                elif farm[i+1][j] == 'W':
                    isPossible = False
            if j > 0:
                if farm[i][j-1] == None:
                    farm[i][j-1] = 'D'
                elif farm[i][j-1] == 'W':
                    isPossible = False
            if j < c - 1:
                if farm[i][j+1] == None:
                    farm[i][j+1] = 'D'
                elif farm[i][j+1] == 'W':
                    isPossible = False

if isPossible:
    print(1)
    for i in range(r):
        line = ''
        for j in range(c):
            if farm[i][j] == 'S': line += 'S'
            elif farm[i][j] == 'W': line += 'W'
            elif farm[i][j] == 'D': line += 'D'
            else:
                line += '.'
        print(line)
else:
    print(0)

