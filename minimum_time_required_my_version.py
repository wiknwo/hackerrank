def minTime(machines, goal):
    items, days = 0, 0
    while items < goal:
        days += 1
        for machine in machines:
            if days % machine == 0:
                items += 1
    return days