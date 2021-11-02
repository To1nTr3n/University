def read(reader):
    line = reader.readline()
    if not line:
        return None
    key, name = line.split()
    _line = [name]
    reading = True
    serial_number = 1
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, atom_type ,x, y, z = line.split()
            if int(num) != serial_number:
                print(f"Have {serial_number} serial numbers: but only {num} only values")
            _line.append([atom_type,x,y,z])
            serial_number+=1
    return _line
if __name__ == '__main__':
    with open("PHD.txt",'r') as input_file:
        print(read(input_file))