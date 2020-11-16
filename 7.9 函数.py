def add(num1,num2):
    result = num1 + num2
    return result
add(num1=1,num2=2)
result = add(1,2)
print(result)


def add_name(first_name,last_name):
    fullname = first_name + last_name
    return fullname

full_name = add_name('Loborn','James')
print(full_name)


#可变参数组

def multi_values(*args):
    # print(args)
    return args
a = multi_values('E',29,180)
print(a)

name,age,height = multi_values('E',30,179)
print(name,age,height)


def num_student(*args):
    print('学生总数：{}个'.format(len(args)))
    for student in args:
        print('他们是：',student)
num_student('小明','小红','小白')

##第一种情况--传入按照列表多元素传入
nums = [1,2,3,4,5,6,7,8,9,10]

def addup1(*args):
    print(args)
    return sum(args)
b = addup1(*nums)
print(b)


##第二种情况--列表作为一个整体元素传入
def addup2(*args):
    print(args)
    # return sum(args[0])
c = addup2(nums,12,12,12,0)
print(c)               # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12, 12, 12, 0)


# 关键字参数与*args参数（可变参数）混合使用
def multi_values_1(num1,*args):
    print(num1)
    print(args)
multi_values_1(1,234,3,4,5)


dict_data = {1:1,2:2}  # 可变
int_data =100   #不可变
def g_fun():
    # global dict_data
    dict_data[1] = 123  #直接引用
    # dict_data = {}
    print('函数内： ',dict_data)
    # global int_data  #不可变。 修改需要声明
    int_data=1000
    print('函数内： ',int_data)
g_fun()
print('全局变量dict->',dict_data,'全局变量int->',int_data,sep=' ')


list_test = [('王强',583),('李阳',575),('徐帆',569),('齐飞',557)]
print(len(list_test))
print(list_test[-1])
for x in list_test[0:10]:
    print(x)


