def read_history(file_path):
    f = open(file_path, "r", encoding='utf-8')
    return(f.read())
    f.close()


def write_history(file_path, content):
    with open(file_path, 'r', encoding='utf-8') as f:
        history = f.readlines()

    total_words = ' '.join(history).split()

    while len(total_words) > 100 and history:
        history = history[1:]
        total_words = ' '.join(history).split()

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(history)

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write('\n' + content)


