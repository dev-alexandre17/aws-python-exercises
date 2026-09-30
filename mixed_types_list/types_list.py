def mixed_types_list():
    mixed_list = [7, 45, 3.14, True, "Hello World", "45", 2.78, 23]
    
    print(f'Lista de tipos mistos\n')
    
    for i, item in enumerate(mixed_list):
        print(f'Index: {i}, Item: {item}, Type: {type(item)}')
    
mixed_types_list()
    
