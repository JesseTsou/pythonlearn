def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

#Ĭ�ϲ���
def enroll(name, gender,age=6,city='beijing'):
    print("name",name)
    print("gender",gender)
    print("age",age)
    print("city",city)

#Ĭ�ϲ�������ָ�򲻱����
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L


#�ɱ����
#����1��calc(1,2,3,5)
#����2��a=[1,2,3,4]
#       calc(*a)
def calc(*num):
    sum=0
    for n in num:
        sum+=n*n
    return sum

#�ؼ��ֲ���
#����1��person('Bob', 35, city='Beijing')
#����2��extra = {'city': 'Beijing', 'job': 'Engineer'}
#       person('Jack', 24, **extra)
#����3��extra = {'city': 'Beijing', 'job': 'Engineer'}
#       person('Jack', 24, city=extra['city'], job=extra['job'])
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)

#�����ؼ��ֲ�����������Ȼ����ָ���Ĳ��������������ؼ�����Ĭ��ֵʱ�ɲ�������
#����:person('Jack', 24, city='Beijing', job='Engineer')
def info(name, age, *, city, job):
    print(name, age, city, job)

def info1(name, age, *, city="beijing", job):
    print(name, age, city, job)
    
def info1(name, age, *args, city, job):
    print(name, age, args,city, job)
    
#���������˳������ǣ���ѡ������Ĭ�ϲ������ɱ�����������ؼ��ֲ����͹ؼ��ֲ���