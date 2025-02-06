n = int(input())  # Number of problems
solved = 0  # Count of problems solved by at least 2 people

for _ in range(n):
    sures = list(map(int, input().split()))
    if sum(sures) >= 2:  # Check if at least two people are sure
        solved += 1

print(solved)  # Output the final count
