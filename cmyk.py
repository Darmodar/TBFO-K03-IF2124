
def CYK_parse(CNF, input):
    spliting = input.split(" ")
    length_spliting = len(spliting)
    store = [[set([]) for j in range(length_spliting)] for i in range(length_spliting)]

    for j in range(length_spliting):
        for head, body in CNF.items():
            for rule in body:
                if len(rule) == 1 and rule[0] == spliting[j]:
                    store[j][j].add(head)

        for i in range(j, -1, -1):
            for k in range(i, j):
                for head, body in CNF.items():
                    for rule in body:
                        if len(rule) == 2 and rule[0] in store[i][k] and rule[1] in store[k + 1][j]:
                            store[i][j].add(head)

    # print(store[0][length_spliting - 1])

    return len(store[0][length_spliting - 1]) != 0