import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
print("maximun score:",maximum)
print("minimun score:",minimum)