def read(reader):
    line = reader.readline()
    if not line:
        return None
    
    if not (line.startswith('CMNT')) or line.isspace():
        key, name = line.split()
        _line = [name]
    else:
        _line = None
    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT')) or line.isspace():
            key, num, atom_type ,x, y, z = line.split()
            if _line == None:
                _line = []
            _line.append([atom_type,x,y,z])
    return _line
if __name__ == '__main__':
    with open("PHD.txt",'r') as input_file:
        print(read(input_file))