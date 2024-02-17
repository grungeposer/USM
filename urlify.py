def urlify(text: list[str]) -> int:
    slow = fast = 0
    count_space = 0
    while fast < len(text):
        if text[fast] == '':
            break
        if text[fast] == ' ':
            count_space += 1
        fast += 1
    del text[:fast - 1:-1]
    new_size = fast - 1 + (2 * count_space)
    text += [''] * (2 * count_space)
    slow = len(text) - 1
    fast -= 1
    while fast >= 0:
        if text[fast] == ' ':
            text[slow] = '0'
            text[slow - 1] = '2'
            text[slow - 2] = '%'
            slow -= 3
        else:
            text[slow] = text[fast]
            slow -= 1
        fast -= 1
    return new_size + 1
text = list('my url') + [''] * 21
new_len = urlify(text)

assert new_len == 8
assert text[:new_len] == list('my%20url')
