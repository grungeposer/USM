def remove_zeroes(numbers: list[int]) -> int:
    non_zero_index = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[non_zero_index], numbers[i] = numbers[i], numbers[non_zero_index]
            non_zero_index += 1
    return non_zero_index
nums = [0, 42, 21, 0, 100, 0, 5, 1, 0, 7, 3, 0, 404, 0]
new_len = remove_zeroes(nums)
print(nums[:new_len])
print(new_len)
