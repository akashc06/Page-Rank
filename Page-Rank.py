import math

def page_rank(file):

    P = []
    L = {}
    M = {}
    d = 0.85
    PPR = 0
    PR = {}
    Newpr = {}
    file_handle = open(file, 'r')
    for lists in file_handle.readlines():
        list_of_nodes = lists.strip('\n').split(' ')
        P.extend(list_of_nodes)
        M["".join(list_of_nodes[0])] = list(set(list_of_nodes[1:]))
    file_handle.close()
    P = list(set(P))
    for node in P:
        list_of_outlinks = list(set(M.get(node, [])))
        for page in list_of_outlinks:
            if page not in L:
                L[page] = 1
            else:
                L[page] += 1
    keys_list = M.keys()
    S = list(set(keys_list) - set(L.keys()))
    N = len(P)

    for node in P:
        PR[node] = 1 / N
    count = 0
    OldPR = 0
    while count < 4:
        OldPR = PPR
        sink_pr = 0
        for node in S:
            sink_pr += PR.get(node, 0)
        for page in P:
            Newpr[page] = (1 - d) / N
            Newpr[page] += d * (sink_pr / N)
            inlinks_list = M.get(page, [])
            for inlink in inlinks_list:
                Newpr[page] += ((d * PR.get(inlink, 0)) / (L.get(inlink, 1)))
        for p in Newpr:
            PR[p] = Newpr[p]
        HPR = 0
        for i in P:
            x = (PR[i] * math.log(PR[i],2))
            HPR += x
        PPR = pow(2,-HPR)
        if(abs(OldPR - PPR) < 1):
            count += 1
        else:
            count = 0
    for p in P:
        print (p + " " + str(PR[p]))

page_rank("G1.txt")