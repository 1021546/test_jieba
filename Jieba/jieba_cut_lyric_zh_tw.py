#encoding=utf-8
import jieba

jieba.set_dictionary('dict.txt.big')

content = open('lyric_tw.txt', 'rb').read()

print("Input：", content)

words = jieba.cut(content, cut_all=False)

print("Output 精確模式 Full Mode：")
for word in words:
    print(word)