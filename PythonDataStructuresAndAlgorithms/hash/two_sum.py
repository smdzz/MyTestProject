# 两数之和
# 假设给我们一个无序列表[3, 7, 10, 4, 5],列表内不包含重复的数字,从中选择两个数,使他们的和等于11[]


# 方法一:暴力破解(不需要考虑顺序)
def two_sum_1(num_list, target):
    for x in range(len(num_list) - 1):
        for y in range(x + 1, len(num_list)):
            if num_list[x] + num_list[y] == target:
                return [x, y]
            else:
                continue
    return "未找到"


num_list = [3, 7, 10, 4, 5]
print(two_sum_1(num_list, 11))


# 方法二:排序,左右查找
def two_sum_2(num_list, target):
    result = []
    new_num_list = sorted(num_list)
    left = 0
    right = len(num_list)-1
    while left < right:
        if new_num_list[left] + new_num_list[right] == target:
            for x in range(len(num_list)):
                if new_num_list[left] == num_list[x]:
                    result.append(x)
                if new_num_list[right] == num_list[x]:
                    result.append(x)
            return result
        elif new_num_list[left] + new_num_list[right] > target:
            right -= 1
        elif new_num_list[left] + new_num_list[right] < target:
            left += 1
    else:
        return "未找到"


num_list = [3, 7, 10, 4, 5]
print(two_sum_2(num_list, 11))


# 方法三: 一遍字典模拟哈希
def two_sum_2(num_list, target):
    _dict = {}
    for i, m in enumerate(num_list):
        if _dict.get(target - m) is not None:
            return [_dict.get(target - m), i]
        _dict[m] = i


num_list = [3, 7, 10, 4, 5]
print(two_sum_2(num_list, 11))
