from re import I


N = int(input("Enter your finish count "))
bill = list(range(1, N+1))
sum = 0
for i in bill:
    sum += i
print("summ of first elements = " + str(sum))
