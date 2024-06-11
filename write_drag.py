name = "victoria"

def write(date):
    with open('temp.txt', 'r', encoding='utf-8') as fh:
        comments = fh.read()

    with open(f'{name}_comments_drag_dirty.txt', 'a', encoding='utf-8') as fh:
        fh.write('\ndate:')
        fh.write(date + '\n')
        fh.write(comments)

