# a = input()
# print(len(a))

# a = int(input())
# count = 0
# while count < len(str(a)):
#     count += 1
# print(count)

a = abs(int(input()))
count = 0
while a > 0:
    print('Первоначальное ',a)
    a //= 10
    print('Обработанное ', a)
    count += 1
print(count)
