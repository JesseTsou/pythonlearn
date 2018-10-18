#Exercise10
#转义
#\t 制表符  \n回车  \\斜杠
# 三引号"""可以一组三引号间放入任意多行文字
# 三单引号也可以如上使用
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass"""

fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(fat_cat2)

# while True:
#     for i in ["/","-","|","\\","|"]:
#         print("%s\r" % i,)



#Exercise11
#输入
#python打印时不换行，需要指定end
print("How old are you ",end='')
#input输入
age = input()
print("How tall are you ",end='')
height = input()
print("How much do you weight ",end='')
weight = input()
print("so, you're %r old, %r tall and %r heavy." %(age,height,weight))

#Exercise12
#input输入中可加入提示语句
age = input("How old are you ")
height = input("How tall are you ")
weight = input("How much do you weight ")
print("so, you're %r old, %r tall and %r heavy." %(age,height,weight))

#Exercise13
#参数
from sys import argv
#argv参数第一个参数值为script本身
script, first, second, third = argv
print("The script is called:", argv)
print("first variable is:", first)
print("second variable is:",second)
print("third variable is:", third)

#Exercise14
#用变量作为input的提示语句
from sys import argv
script, user_name = argv
prompt = ">>>>>>>>>>>"

print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" %user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

#三个引号中的格式化字符
print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer))

#Exercise15
#读取文件
from sys import argv
script, filename = argv
#打开文件
txt = open(filename)

print("Here'is your file %r:" %filename)
#读取文件
print(txt.read())

print("input the filename again:")
file_again = input(">>")
txt_again = open(file_again)
print(txt_again.read())