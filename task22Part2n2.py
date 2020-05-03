with open('file_.txt', 'r') as f:
    data = f.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

    print('\n Кол- во строк: ', len(line), '\n Кол-во слов: ', len(words), '\n Кол-во пробелов: ', len(spaces), '\n Кол-во букв: ', (len(data)-len(spaces)))