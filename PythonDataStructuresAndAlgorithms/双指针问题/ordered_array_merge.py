# 有序数组合并
# 指针的意思是内存空间的地址. 我们可以通过一个数组中每个元素的下标来找出它的值,所以存储这个元素下标位置的元素的下标值变量可以看做一个指针
# python中没有明确意义上的指针,我们叫它"模拟指针问题"

# 假设我们有两个有序数组 arr1 = [1, 3, 4, 6, 10], arr2 = [2, 5, 8, 11]


def array_merge(arr1, arr2):
    ind = 0  # 初始化下标
    arr = arr1.copy()  # 复制 arr1 为 arr,用来存储排序的数组
    for i in range(len(arr2)):
        while ind < len(arr1):
            if arr2[i] <= arr1[ind]:  # ind的范围不能超过数组元素下标的最大值
                arr.insert(ind+i, arr2[i])  # 向第一个数组中的合适位置(ind+i)插入第二个数组的数
                break
            else:
                ind += 1
        else:
            arr.extend(arr2[i:])  # 当arr2[i]的值大于arr1中的任何一个值时,将剩下的arr2拼接到arr1结尾
            break
    return arr


arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11]
array_merge(arr1, arr2)
