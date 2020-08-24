import re


# 你不⽤太关⼼这个函数
def parse(text):
# 使⽤正则表达式去除标点符号和换⾏符
    text = re.sub(r'[^\w ]', '', text)
# 转为⼩写
    text = text.lower()
# ⽣成所有单词的列表
    word_list = text.split(' ')
# 去除空⽩单词
    word_list = filter(None, word_list)
# ⽣成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
# 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_word_cnt


with open('in.txt', 'r') as fin:
    text = fin.read()


word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))
