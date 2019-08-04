# 神奇的词根
# 词根(root): 它可以跟其他一些词组组成另一个较长的单词,我们成这个单词为继承词(successor)
# 规则: 给定一个有许多词根组成的字典和一个句子,需要将句子中的所有继承词用词根替换掉,如果继承词中有许多形成它的词根,则用最短的词根替换它
# 示例: 字典为["cat", "bat", "rat"],句子为"the cattle was rattled by the battery",经过替换,输出"the cat was rat by the bat"


import collections


# 方案一: 暴力查找,进行替换(时间复杂度O(n^2))
def replace_words(roots, sentence):
    sentence = sentence.split(' ')
    for root in roots:
        root_len = len(root)
        for x in range(len(sentence)):
            if root == sentence[x][:root_len]:
                sentence[x] = root
    return " ".join(sentence)


roots = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(replace_words(roots, sentence))


# 方案二: 哈希查找优化
def replace_words(roots, sentence):
    d = collections.defaultdict(set)
    s = collections.defaultdict(int)
    sentence = sentence.split(" ")
    for root in roots:
        print(root[0])
        d[root[0]].add(root)  # 将词根按照{首字母:{词根, 词根}}存储到d中
        s[root[0]] = max(s[root[0]], len(root))  # 将词根字符串的长度存储到s中,{首字母: 首字母为..的词根的最大长度}
    for i, word in enumerate(sentence):
        for j in range(s[word[0]]):
            if word[:j+1] in d[word[0]]:  # 如果单词的开头j位存在于d的首字母的value集合中,则进行替换
                sentence[i] = word[:j+1]
                break
    return " ".join(sentence)


roots = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(replace_words(roots, sentence))
