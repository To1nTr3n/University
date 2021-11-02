def process_line(reader):
    next(reader)
    print(reader.read())
        #do something

with open('alkaline_metals.txt','r') as f:
    process_line(f)

