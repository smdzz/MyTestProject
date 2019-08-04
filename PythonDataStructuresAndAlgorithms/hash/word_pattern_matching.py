# 单词模式匹配
# 给定两个字符串,一个是单词模式字符串,一个是目标字符串,检查目标字符串是否为给定的单词模式,
# 即求目标字符串中单词出现的规律是否符合单词模式字符串中的规律
# 例:单词模式字符串为"一二二一", 目标字符串中为"苹果 香蕉 香蕉 苹果"二者规律一样,匹配成功
# 目标字符串为"苹果 香蕉 香蕉 橘子",匹配失败


def word_pattern_match(word_pattern, word_str):
    word = word_str.split(" ")  # 首先将目标字符串隔开
    if len(word_pattern) != len(word):  # 如果目标字符串的列表和单词模式字符串的长度不一样,则肯定不匹配
        return False
    hash_word = {}  # 记录模式字符串和目标字符串的对应关系
    used = {}  # 记录已经使用过的目标字符串
    for x in range(len(word_pattern)):
        if word_pattern[x] in hash_word:  # 检查模式字符串中的字符是否已经被记录过映射关系
            if hash_word[word_pattern[x]] != word[x]:  # 如果不是第一次出现的话,则判断映射关系是否一致
                return False
        else:
            if word[x] in used:  # 检查这个单词是否已经使用过,使用过但是模式字符串没有命中则说明不匹配
                return False
            hash_word[word_pattern[x]] = word[x]  # 第一次出现,则创建映射关系,加入哈希表
            used[word[x]] = True  # 在used中保存该单词被使用过
    return True


word_pattern = "一二二一"
word_str = "苹果 香蕉 香蕉 苹果"
print(word_pattern_match(word_pattern, word_str))
