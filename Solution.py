# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
E = set(input().split())

m = int(input())
F = set(input().split())

print(len(E | F))
