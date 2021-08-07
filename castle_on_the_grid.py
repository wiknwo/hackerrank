def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here

    # initiate dictionary of coordinates:distances
    distance = {(x, y): math.inf for x in range(len(grid)) for y in range(len(grid))}
    distance[(startX, startY)] = 0

    stack = deque()
    stack.append((startX, startY))
    while stack:
        # x and y coordinates of current node
        cx, cy = stack.pop()
        # distance of current node
        cdistance = distance[(cx, cy)]
        # return distance if current node is goal
        if (cx, cy) == (goalX, goalY):
            return cdistance

        neighbors = []

        # explore up
        x = cx - 1
        while x > -1 and grid[x][cy] != 'X':
            neighbors.append((x, cy))
            x -= 1

        # explore down
        x = cx + 1
        while x < n and grid[x][cy] != 'X':
            neighbors.append((x, cy))
            x += 1

        # explore left
        y = cy - 1
        while y > -1 and grid[cx][y] != 'X':
            neighbors.append((cx, y))
            y -= 1

        # explore right
        y = cy + 1
        while y < n and grid[cx][y] != 'X':
            neighbors.append((cx, y))
            y += 1
    
        # add nodes whose distances have decreased to the stack
        for node in neighbors:
            if cdistance + 1 < distance[node]:
                distance[node] = cdistance + 1
                stack.appendleft(node)