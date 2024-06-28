
# a = list(map(int,input().split()))
# a= sum(a)
# print(a)

# a = list(map(int,input().split()))
# sum = 0
# for digit in a:
#     sum += digit
# print(sum)

# a = list(map(int,input().split()))
# sum = 0
# while len(a) > 0:
#     sum += a[0]
#     a.remove(a[0])
# print(sum)


a = list(map(int,input().split()))
sum = 0
b=0
while len(a) > 0:
    b= a.pop()
    sum += b
print(sum)