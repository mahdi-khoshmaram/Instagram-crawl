def write(name):
    with open('temp.txt', 'r', encoding='utf-8') as fh:
        comments = fh.read()

    with open(f"{name}_comments_click_dirty_remain.txt", 'a', encoding='utf-8') as fh:
        fh.write('\n-----------------------------------------------date---------------\n')
        fh.write(comments)


