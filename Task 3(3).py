def merge_files(file_list):
    merged_content = ''
    
    for file in file_list:
        with open(file, 'r') as f:
            content = f.read()
            merged_content += content
    
    with open('merged_file.txt', 'w') as f:
        f.write(merged_content.strip())

file_list = []
while True:
    file_name = input('Введите название файла (или "quit" для завершения): ')
    if file_name.lower() == 'quit':
        break
    file_list.append(file_name)
