
def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1) - 1
    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 += 1
        p2 -= 1

def reversing_words_sentence_logic(string1):
    # 먼저 문장 전체를 반환한다
    reverser(string1)
    # print(string1)
    p = 0
    start = 0
    while p < len(string1):
        if string1[p] == u"\u0020": # 유니코드"공백" 을 의미함
            # 단어를 다시 반전(원위치)
            reverser(string1, start, p - 1)
            # print(string1)
            start = p + 1
        p += 1
    # 마지막 단어를 반전(원위치)
    reverser(string1, start, p - 1)
    # print(string1)
    return "".join(string1)

str1 = "파이썬 알고리즘 정말 재미있다"
str2 = reversing_words_sentence_logic(list(str1))
print(str2)