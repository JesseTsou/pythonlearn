#-*-coding:utf-8-*-
#Exercise1
#打印
print("Hello world!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

#Exercise2
#注释
print("I could have code like this.") #and the comment after is ignored
print("This will run")

#Exercise3
#运算
print("I will now count my chickens:")
#python3会得到实际的值（小数）
print("Hens",25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print( 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7 ?")
print(3 + 2 < 5 - 7)
#表示式返回布尔值
print("What is 3 + 2 ? ", 3 + 2)
print("What is 5 - 7 ? ", 5 - 7)
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2)
print("Is it greater or equal ?", 5 >= -2)
print("Is it less or equal ?", 5 <= -2)

#Exercise4
#变量
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#多个字符串间会加个空格
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be",cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about",average_passengers_per_car, "in each car.")

#Exercise5
#格式化与打印
my_name = '邹亚杰'
my_age = 26.0
my_height = 75
my_weight = 176
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'Brown'
num = 1.777
#四舍五入
num1 = round(num)

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
#Python用一个tuple将多个值传递给模板，每个值对应一个格式符
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
print("If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight))
print("num1 %d." %num1)

#Exercise6
#字符串与文本
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said:%r" %x)
print("I also said:'%s'." %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side"

print(w + e)

#Exercise7
#更多打印
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1 + end2 + end3 + end4 + end5 + end6,
      end7 + end8 + end9 + end10 + end11 + end12)

#Exercise8
#打印，打印
#%r打印的是写出来的方式（或者近似方式），用来debug原始格式
formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter % (True,False,False,True))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % ("I had this thing",
                   "That you could type up right.",
                   "But it didn't sing.",
                   "So I said goodnight")
      )

formatter = "%s %s %s %s"
print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter % (True,False,False,True))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % ("I had this thing",
                   "That you could type up right.",
                   "But it didn't sing.",
                   "So I said goodnight"))

#Exercise9
#打印，打印
days = "Mon Tue Wed Thu Fri Sat Sun"
#字符串换行
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)
print("Here are the months:",months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

#打卡
import math
#input函数输入的是字符串格式
num_str = input("请输入：")
print("输入的半径是：%s" %num_str)
#将字符串强转为int
num = int(num_str)
print("以%d为半径的圆:\n周长:%f\n面积：%f" % (num, 2 * math.pi * num, math.pi * num * num))
