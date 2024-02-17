def urlify(text: list[str]) -> int:
    space_count = text.count(' ')
    new_length = len(text) + 2 * space_count
    new_text = [''] * new_length
    for i in range(len(text) - 1, -1, -1):
        if text[i] == ' ':
            new_text[new_length - 1] = '0'
            new_text[new_length - 2] = '2'
            new_text[new_length - 3] = '%'
            new_length -= 3
        else:
            new_text[new_length - 1] = text[i]
            new_length -= 1
    text[:] = new_text
    return len(text)
original_text = list('my url')
new_length = urlify(original_text)
print(new_length)
print(''.join(original_text))

