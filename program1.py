def nums_to_list(x: int):
    digit = 0
    nums_list = []
    while x > 0:
        digit = x%10
        nums_list.append(digit)
        x //= 10

    nums_list.reverse()
    return nums_list

print(nums_to_list(233))
