# 猜词游戏(Bulls and Cows)
# 出题者给出几个数字,猜题者猜测出题者给出的数字,出题者会告诉猜题者猜测中又多少位数字和数字的确切位置都猜对了(成为"Bulls",公牛),
# 还有多少位数字猜对了但是位置不对(称为"Cows",奶牛),答题方根据出题方给出的答案继续猜,知道猜出所有数字和位置都正确为止
# 例: 我们将公牛记做A,母牛记做B, 假如出题者给出的数字为1123,猜题者给出数字为9111,第二个数字相同,位置相同,所以他算一只公牛(A)
# 其他两个1只能算是数字猜对了一个,但是位置不对,所以只能算是一只母牛(B),返回1A1B
# 1 1 2 3
#   |
# 9 1 1 1


def word_guessing(secret, guess):
    secret_dict = {}
    guess_dict = {}
    A = 0
    B = 0
    for x in range(len(secret)):
        if secret[x] == guess[x]:
            A += 1
        else:
            if secret[x] in secret_dict:
                secret_dict[secret[x]] += 1
            else:
                secret_dict[secret[x]] = 1
            if guess[x] in guess_dict:
                guess_dict[guess[x]] += 1
            else:
                guess_dict[guess[x]] = 1
    for num in secret_dict:
        if num in guess_dict:
            B += min(secret_dict[num], guess_dict[num])
    return "%dA%dB" % (A, B)


secret = '1133'
guess = '9111'
print(word_guessing(secret, guess))
