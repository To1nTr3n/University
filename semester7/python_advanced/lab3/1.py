filename = input('Which file would tou like to back-up: ')
new_filename_backup = filename +'.bak'
#C1
with open(filename) as f:
    with open(new_filename_backup,'w') as n:
        for line in f:
            n.write(line)

print("Done")


#C2
# backup = open(new_filename_backup, 'w')

# for line in open(filename):
#     backup.write(line)

# backup.close()
# print("Done")

    
