
mat_of_adj = dict()
with open("in.txt") as file_in:
    count_token = file_in.readline().split(' ')
    k = int(count_token[0])
    l = int(count_token[1])
    if(k == l):
        for i in range(0,k):
            tokens = file_in.readline().split(' ')
            mat_of_adj[i] = set()
            for token in tokens:
                mat_of_adj[i].add(int(token) - 1)
    else:
        with open('out.txt','w') as file_out:
            file_out.write('N')
        exit(0)

used = [0 for i in range(0,k)]
saturation = [-1 for i in range(0,2*k)]

def kuhn_algo(vrtx):
    if (used[vrtx]):
        return False
    used[vrtx] = True
    for vrtx2 in mat_of_adj[vrtx]:
        if(saturation[vrtx2] == -1 or kuhn_algo(saturation[vrtx2])):
            saturation[vrtx2] = vrtx
            saturation[vrtx] = vrtx2
            return True
    return False



for i in range(0,k):
    used = [0 for j in range(0,k)]
    if(not kuhn_algo(i)):
        with open('out.txt', 'w') as file_out:
            file_out.write('N')
        exit()

with open('out.txt', 'w') as file_out:
    file_out.write('Y\n')
    for i in range(0,k):
        file_out.write(str(i + 1) + "-" + str(saturation[i] + 1)+"\n")





