datali = []
datali2 = []

datan = int(input("Enter a number: "))
for i in range(1, datan+1):
    data = int(input("Enter the numbers: "))
    datali.append(data)
    datali2.append(data)
datali.sort()
datali2.sort(reverse=True)
print("The assending order is:", datali)
print("The decending order is:",datali2)