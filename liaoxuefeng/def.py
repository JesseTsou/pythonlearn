def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

#默认参数
def enroll(name, gender,age=6,city='beijing'):
    print("name",name)
    print("gender",gender)
    print("age",age)
    print("city",city)

#默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L


#可变参数
#调用1：calc(1,2,3,5)
#调用2：a=[1,2,3,4]
#       calc(*a)
def calc(*num):
    sum=0
    for n in num:
        sum+=n*n
    return sum

#关键字参数
#调用1：person('Bob', 35, city='Beijing')
#调用2：extra = {'city': 'Beijing', 'job': 'Engineer'}
#       person('Jack', 24, **extra)
#调用3：extra = {'city': 'Beijing', 'job': 'Engineer'}
#       person('Jack', 24, city=extra['city'], job=extra['job'])
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)

#命名关键字参数，参数必然包含指定的参数名（若命名关键字有默认值时可不包含）
#调用:person('Jack', 24, city='Beijing', job='Engineer')
def info(name, age, *, city, job):
    print(name, age, city, job)

def info1(name, age, *, city="beijing", job):
    print(name, age, city, job)
    
def info1(name, age, *args, city, job):
    print(name, age, args,city, job)
    
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数