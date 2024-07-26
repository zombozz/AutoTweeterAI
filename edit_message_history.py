def read_history(file_path):
    f = open(file_path, "r")
    return(f.read())
    f.close()


def write_history(file_path, content):
    with open(file_path, 'r') as f:
        history = f.readlines()

    total_words = ' '.join(history).split()

    if len(total_words) > 600:
        history = history[1:]

    with open(file_path, 'w') as f:
        f.writelines(history)
    
    with open(file_path, 'a') as f:
        f.write('\n' + content)


