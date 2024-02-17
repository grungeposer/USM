def urlify(text: list[str]) -> int:
    space_count = text.count(' ')
    new_length = len(text) + 2 * space_count
    for i in range(len(text) - 1, -1, -1):
        if text[i] == ' ':
            text[new_length - 1] = '0'
            text[new_length - 2] = '2'
            text[new_length - 3] = '%'
            new_length -= 3
        else:
            text[new_length - 1] = text[i]
            new_length -= 1
    return len(text)
original_text = list('my url')
new_length = urlify(original_text)
print(new_len)