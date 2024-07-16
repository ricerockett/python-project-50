def format_diff_tree(tree):
    result = ''
    for key in tree:
        result += f'{key}:{tree[key]}'
    return result