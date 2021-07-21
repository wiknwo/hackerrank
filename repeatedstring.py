def repeatedString(s, n):
    # Write your code here
    return (s[:n%len(s)].count('a')+(s.count('a')*(n//len(s))))