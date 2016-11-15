# -*-coding:utf-8 -*-
import re
print "你要查找什么内容？请输入："
pattern = raw_input()
text = "今天双11我给儿子买了2个玩具在淘宝上。"
match = re.search(pattern, text)
s = match.start()
e = match.end()
print '发现 "%s"\n在这句话中 "%s"\n %d 到 %d 的位置->(%s)' % (match.re.pattern, match.string, s, e, text[s:e])
