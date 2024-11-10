import re
import sys
def convert(word):
    newWord = ""
    for ele in word:
        if ele.isalpha():
            newWord += ele
    return newWord
if __name__ == '__main__':
    n = int(input())
    words = []
    input_data = sys.stdin.read().strip().lower()
    lines = input_data.split('\n')
    
    for s in lines:
        pattern = r'\d+'
        list_word = re.split(pattern, s)
        s = " ".join(list_word)
        pattern = r'\W+'
        list_word = re.split(pattern, s)
        list_word = [word for word in list_word if word]
        for ele in list_word:
            words.append(ele)
    
    dic = dict()
    for ele in words:
        if ele not in dic:
            dic[ele] = 1
        else:
            dic[ele] += 1
    
    sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    for word, fre in sorted_dic:
        print(f"{word} {fre}")