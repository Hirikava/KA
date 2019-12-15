


field = list()
for i in range(0,8):
    field.append(list())
    for j in range(0, 8):
        field[i].append('.')


white = list()
black = list()

def fill_collection(tokens,collection,char):
    if(tokens.__len__() >= 2):
        i = 0
        while(int(tokens[i]) != 0 and int(tokens[i+1]) != 0 and i <= tokens.__len__()):
            collection.append((int(tokens[i + 1]) - 1,(int(tokens[i]) - 1)))
            field[int(tokens[i+1]) - 1][int(tokens[i]) - 1] = char
            i += 2

def cord_is_valid(x,y):
    return x > 0 and y > 0 and x < 8 and y < 8

def make_cord_sequence(x,y):
    yield (x + 1,y)
    yield (x - 1,y)
    yield  (x, y+1)
    yield  (x, y -1)

def determine_groups(pecies,allie_char,neutral_char):
    used = set()
    groups = list()
    for i in pecies:
        if(i not in used):
            group = (1,list())
            sequence = list()
            sequence.append(i)
            while(sequence.__len__() > 0):
                current = sequence.pop(0)
                if current in used:
                    continue
                used.add(current)
                for cord in make_cord_sequence(current[0],current[1]):
                    if cord_is_valid(cord[0],cord[1]):
                        if(field[cord[0]][cord[1]] == allie_char and cord not in used):
                            sequence.append(cord)
                            group = (group[0] + 1,group[1])
                        if (field[cord[0]][cord[1]] == neutral_char):
                            group[1].append(cord)
            groups.append(group)
    return groups


with open("in.txt") as file_in:
    white_tokens = file_in.readline().split(' ')
    fill_collection(white_tokens,white,'w')
    black_tokens = file_in.readline().split(' ')
    fill_collection(black_tokens, black, 'b')


black_groups = determine_groups(black,'b','.')
white_groups = determine_groups(white,'w','.')

def merge(groups):
    possible_answers = ((group[0],group[1][0]) for group in groups if group[1].__len__() == 1)
    mrg = dict()
    max  = 0
    for gr in possible_answers:
        if gr[1] not in mrg:
            mrg[gr[1]] = gr[0]
        else:
            mrg[gr[1]] += gr[0]
        if(max < mrg[gr[1]]):
            max = mrg[gr[1]]
    return [key for key in mrg if mrg[key] == max]

black_possible_answers = merge(white_groups)
white_possible_answers = merge(black_groups)

for i in range(0,8):
    for j in range(0, 8):
        print(field[i][j],end="")
    print()

with open('out.txt', 'w') as file_out:
    for possible_answers in [white_possible_answers,black_possible_answers]:
        if(possible_answers.__len__() == 0):
            file_out.write('N\n')
        else:
            for cord in possible_answers:
                file_out.write((cord[1]+1).__str__() + " " + (cord[0] +1).__str__())
                file_out.write("  ")
            file_out.write('\n')