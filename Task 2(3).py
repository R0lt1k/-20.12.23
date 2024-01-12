def transliterate(input_file, output_file, direction):
    translit_dict = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': "'",
        'ы': 'y',
        'ь': "'",
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
    }
    
    with open(input_file, 'r') as f:
        content = f.read()
    
    if direction == 'ru_to_en':
        for rus, eng in translit_dict.items():
            content = content.replace(rus, eng)
    elif direction == 'en_to_ru':
        for rus, eng in translit_dict.items():
            content = content.replace(eng, rus)
    else:
        print("Неверное направление транслитерации!")
        return
    
    with open(output_file, 'w') as f:
        f.write(content)
