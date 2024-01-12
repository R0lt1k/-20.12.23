def common_symbols(file_list):
    common_symbols = []
    
    with open(file_list[0], 'r') as f:
        common_symbols = list(f.read())
    
    for file in file_list[1:]:
        with open(file, 'r') as f:
            content = list(f.read())
