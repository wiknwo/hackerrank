def DFSrec(adj,s,visited,val):
    visited[s] = 1
    val += 1
    for i in adj[s]:
        if visited[i]==0:
            val = DFSrec(adj,i,visited,val)

    return val

def roadsAndLibraries(n, c_lib, c_road, cities):
    # print("n",n)
    # print("c_lib",c_lib)
    # print("c_road",c_road)
    # print("cities",cities)

    if c_road>c_lib:
        return n*c_lib
    else:

        ##adjacency matrix construction
        adj = dict()
        for i in cities:
            #print("i",i)
            if i[0] in adj:
                adj[i[0]].append(i[1])
            else:
                adj[i[0]] = [i[1]]

            if i[1] in adj:
                adj[i[1]].append(i[0])
            else:
                adj[i[1]] = [i[0]]

        for i in range(1,n+1):
            if i in adj:
                pass
            else:
                adj[i] = []


        #print("adj",adj)


        ##algorithm
        visited = [0]*(n+1)

        countNodes = 0
        countComponents = 0

        l = []
        for i in range(1,n+1):
            if visited[i]==0:
                val = 0
                nodes = DFSrec(adj,i,visited,val)
                countComponents += 1
                l.append(nodes)

        #print("l",l)
        #print("countComponents",countComponents)

        total = 0
        for i in l:
            total = total + (c_road*(i-1))

        total = total + countComponents*c_lib

        return total