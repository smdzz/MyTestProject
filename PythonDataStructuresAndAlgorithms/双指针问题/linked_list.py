# 链表
# 链表是用指针连接的用于存储数据的数组,它最大的优点在于可以有效利用零碎的内存空间.
# 在很多语言中,数组的大小要提前定义,定义后不能随便更改,而且数组中只能存储同一类型的变量
# 链表则不存在这些限制,链表可以改变数组的长度,并且可以再同一个数组中存储不同类型的元素(python中的列表的工作原理就是链表)
# python中没有指针,使用模拟指针的方式实现链表

# 1.单链表(由两个列表组成的单链表)


def single_linked_list(list_value, list_pointer):
    """list_value存储链表中的每个值,list_pointer存储链表中元素的指针"""
    head = 0  # head是指向链表的第一个元素的指针,需要自己定义
    print(list_value[head])  # 输出第一个元素的值
    next = list_pointer[head]  # 给next赋初始值
    while next != -1:  # next是指向下一个元素的指针,不等于-1表示后面还有元素
        print(list_value[next])  # 输出下一个元素中存储的值
        next = list_pointer[next]  # 把指针变为下一个元素中存储的值


list_value = [1, 5, 6, 2, 4, 3]
list_pointer = [3, 2, -1, 5, 1, 4]
single_linked_list(list_value, list_pointer)


# 2.单链表(数组中套数组)


def single_linked_list(list_linked):
    """大数组中每个小数组都是链表中的一个元素,每个小数组中的第一个数是这个元素存储的值,第二个数是指向下一个元素的指针"""
    value = 0  # 预先设置好值和指针在小数组中的位置(固定的)
    pointer = 1
    head = 0
    print(list_linked[head][value])  # 输出第一个元素的值
    next = list_linked[head][pointer]  # 给next赋初始值
    while next != -1:  # next是指向下一个元素的指针,不等于-1表示后面还有元素
        print(list_linked[next][value])  # 输出下一个元素中存储的值
        next = list_linked[next][pointer]


list_linked = [[1, 3], [5, 2], [6, -1], [2, 5], [4, 1], [3, 4]]
single_linked_list(list_linked)


# 双链表中的每个元素都由它的值和两个指针组成,一个指针指向上一个元素,一个指针指向下一个元素,好处是可以双向遍历
# 3.双链表(由三个列表组成的双链表)
def double_linked_list(list_value, list_right, list_left):
    """list_value:元素的值, list_right:元素的指向下一个元素的指针, list_left:元素的指向上一个元素的指针"""
    print("正向输出链表结果")
    head = list_left.index(-1)  # 头指针为-1在list_left中的位置
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]
    print("反向输出链表结果")
    head = list_right.index(-1)  # 头指针为-1在list_right中的位置
    print(list_value[head])
    next = list_left[head]
    while next != -1:
        print(list_value[next])
        next = list_left[next]


list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
list_left = [-1, 5, 1, 0, 2, 3]
double_linked_list(list_value, list_right, list_left)


# 3.双链表(数组中套数组)
def double_linked_list(double_list):
    # 首先定义三个固定值 1. 存储元素的位置 2. 存储上一个元素的指针的位置 3. 存储下一个元素指针的问题
    value = 0
    right = 1
    left = 2
    head = 0  # 提前设置头指针指向的问题
    print("双链表正序输出")
    print(double_list[head][value])
    next = double_list[head][right]
    while next != -1:
        print(double_list[next][value])
        next = double_list[next][right]


double_list = [[1, 3, -1], [5, 2, 5], [6, 4, 1], [2, 5, 0], [7, -1, 2], [3, 1, 3]]
double_linked_list(double_list)


# 4. 单向链表插入元素
def add_signal_element(list_value, list_right, head, element, prepos):
    """
    操作过程: 在吧上一个元素的指针指向新元素前,要把新元素的指针指向下一个元素,下一个元素的位置现在存储在上一个元素的指针中,也就是
        list_right数组中下标为prepos的变量中,把这个指针的值加在list_right的最后,就刚好和新添加到list_value中的值对应了.
        最后把上一个元素的指针赋值为新元素的位置,整个插入就完成了
    list_value: 存储元素的列表 list_right: 存储元素列表的指针 head: 链表的第一个元素的指针 element: 要添加的新元素的值
    prepos: 要插入未知的上一个元素的位置
    """
    print("插入前")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]
    list_value.append(element)  # 向数组末尾加上新元素的值4
    list_right.append(list_right[prepos])  # 加上新元素指针指向的位置(下一个元素)
    list_right[prepos] = len(list_value)-1
    print("插入后")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]


list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
head = 0
# element = 4
# prepos = 5
element = 9
prepos = 4
add_signal_element(list_value, list_right, head, element, prepos)


# 5. 向双链表中添加元素
def add_double_element(list_value, list_right, list_left, head, element, prepos):
    """
    操作过程: 在吧上一个元素的指针指向新元素前,要把新元素的指针指向下一个元素,下一个元素的位置现在存储在上一个元素的指针中,也就是
        list_right数组中下标为prepos的变量中,把这个指针的值加在list_right的最后,就刚好和新添加到list_value中的值对应了.
        最后把上一个元素的指针赋值为新元素的位置,整个插入就完成了
    list_value: 存储元素的列表 list_right: 存储下一个元素位置的指针 list_left: 存储上一个元素位置的指针
    head: 链表的第一个元素的指针 element: 要添加的新元素的值 prepos: 要插入未知的上一个元素的位置
    """
    print("插入前")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]

    # 知道要插入元素的上一个元素的位置
    # list_value.append(element)  # 向数组末尾加上新元素的值4
    # list_right.append(list_right[prepos])  # 加上新元素指针指向的位置(下一个元素)
    # list_left.append(prepos)
    # list_left[list_right[prepos]] = len(list_value)-1
    # list_right[prepos] = len(list_value)-1

    # 知道要插入元素的下一个元素的位置
    list_value.append(element)
    list_left.append(list_left[prepos])
    list_right.append(prepos)
    list_right[list_left[prepos]] = len(list_value)-1
    list_left[prepos] = len(list_value)-1


    print(list_value, list_right, list_left, sep="\n")
    print("插入后")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]


list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
list_left = [-1, 5, 1, 0, 2, 3]
head = 0
element = 4
# 要插入元素的上一个元素的位置
# prepos = 5
# 要插入元素下一个元素的位置
prepos = 1
# element = 9
# prepos = 4
add_double_element(list_value, list_right, list_left, head, element, prepos)


# 6. 删除单链表中的元素
def delete_signal_element(list_value, list_right, head, prepos):
    print("删除前")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]
    list_right[prepos] = list_right[list_right[prepos]]
    print("删除后")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]


list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
head = 0
element = 3  # 要删除的元素
prepos = 3  # 要删除元素的上一个元素的位置
delete_signal_element(list_value, list_right, head, prepos)


# 7. 删除双链表中的元素
def delete_double_element(list_value, list_right, list_left, head, prepos):
    print("删除前")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]

    # 知道要删除元素的上一个元素的位置的情况
    # # 要删除元素的上一个元素的右指针--->要删除元素的右指针
    # list_right[prepos] = list_right[list_right[prepos]]
    # # 要删除元素的下一个元素位置的左指针-->要删除元素的上一个元素的位置
    # list_left[list_right[list_right[prepos]]] = prepos

    # 知道要删除元素的下一个元素的位置的情况
    list_right[list_left[list_left[prepos]]] = prepos
    list_left[prepos] = list_left[list_left[prepos]]

    print("删除后")
    print(list_value[head])
    next = list_right[head]
    while next != -1:
        print(list_value[next])
        next = list_right[next]


list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
list_left = [-1, 5, 1, 0, 2, 3]
head = 0
# element = 5  # 要删除的元素
# prepos = 5  # 要删除元素的上一个元素的位置
element = 5  # 要删除的元素
prepos = 2  # 要删除元素的下一个元素的位置
delete_double_element(list_value, list_right, list_left, head, prepos)
