import sys

text = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

l = list(text.split(word))

print(len(l) - 1)