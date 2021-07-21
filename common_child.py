def commonChild(s1, s2):
    # Write your code here
    maxAt = {}

    for i1 in range(len(s1)):
        maxForI1 = 0
        for i2 in range(len(s2)):
            potentialSum = maxForI1 + 1

            # You might be tempted to use the max() function to simplify the next three lines,
            # but that makes the solution so much slower that several of the test cases fail.
            other = maxAt.get(i2, 0)
            if other > maxForI1:
                maxForI1 = other

            if s1[i1] == s2[i2]:
                maxAt[i2] = potentialSum

    return max(maxAt.values(), default=0)