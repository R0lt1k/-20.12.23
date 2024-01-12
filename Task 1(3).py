def remove_unacceptable_words(text_file, unacceptable_file):
    with open(text_file, 'r') as f:
        content = f.read()
    
    with open(unacceptable_file, 'r') as f:
        unacceptable_words = f.read().splitlines()
    
    for word in unacceptable_words:
        content = content.replace(word, '')
    
    with open('new_text.txt', 'w') as f:
        f.write(content)
