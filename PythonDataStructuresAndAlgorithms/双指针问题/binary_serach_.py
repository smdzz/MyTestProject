# 有序数组的二分查找
# 二分查找又叫做折半查找,每次查找后,查找的范围都减半,这样查找到最后,查找范围只剩一个数时,判断它是否为要查找的数,如果是
# 就记录位置,如果不是,则要查找的数不存在在这个数组中


def binary_search(search, list_test):
    head, tail = 0, len(list_test)  # 指定头指针为列表的第一个位置0, 尾指针为最大下标值+1也就是数组的长度
    while tail - head > 1:  # 当尾指针tail减去头指针head等于1时,查找范围只有head指向的数
        middle = (tail + head) // 2  # middle为存储中间数的坐标,//2表示取整
        if search == list_test[middle]:
            return middle
        elif search > list_test[middle]:  # 如果middle指向的数小于要找的数,则不用将middle保存在范围内,而是使用middle+1保存为head
            head = middle + 1
        elif search < list_test[middle]:
            tail = middle
    else:
        if search == list_test[head]:
            return head
        return "要查找的数不存在"


print(binary_search(13, [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]))
