from xpinyin import Pinyin


def words_to_pinyin(words):
    p = Pinyin()
    result = p.get_pinyin(words, tone_marks='numbers')
    temp = []
    for c in result:
        if c == '-':
            c = ' '
        temp.append(c)
    newText = ''.join(temp)
    return newText


# print(words_to_pinyin('我是你爹'))
