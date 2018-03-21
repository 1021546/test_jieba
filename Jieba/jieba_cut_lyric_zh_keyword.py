#encoding=utf-8
import jieba
import jieba.analyse

jieba.set_dictionary('dict.txt.big')

content = open('lyric.txt', 'rb').read()

print("Input：", content)

tags = jieba.analyse.extract_tags(content, 10)

print("Output：")
print(",".join(tags))