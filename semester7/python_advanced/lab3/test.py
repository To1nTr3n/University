list_number = []

# for line in open('test.txt'):
#     list_number.append(line.strip().split(" "))
# print(list_number)


for line in open('test.txt'):
    x = line.strip().split(" ") #[2,3]
    for i in x:
        list_number.append(int(i))
    x= []
    
tong = 0
for i in list_number:
    tong+=i
print(list_number)
print(tong)