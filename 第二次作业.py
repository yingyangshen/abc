# 作业
# 简单版1
family_member = ["father", "mother", "sister", "brother"]
print(family_member)
family_member.append("girlfriend")
print(family_member)
family_member.insert(0, "boyfriend")
print(family_member)
del family_member[0]
print(family_member)
family_member.pop()
print(family_member)

# 进阶版2
relatives = []
relative = input("请输入你的家庭成员:(如果退出请按q!)")
while relative != 'q':
    print("我的家人", relative, "!")
    relatives.insert(0, relative)
    print("我的家庭成员有：", relatives)
    relative = input("请输入你的家庭成员:(如果退出请按q!)")
print("我的家庭成员有：", relatives)
n = int(input("请输入你要删除的列表中的第几个数"))
del relatives[n - 1]
print(relatives)

#1、列表
    #列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有
    #任何关系。鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters 、digits 或names ）是个不错的主意。
#举例 ： bicycles = ['trek', 'cannondale', 'redline', 'specialized']
      # print(bicycles)

#2、列表索引
#  列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
    #举例：bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    # print(bicycles[0])

#3、修改列表中的元素
#修改列表元素的语法与访问列表元素的语法类似。要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
#举例：motorcycles = ['honda', 'yamaha', 'suzuki']
        #print(motorcycles)
        #motorcycles[0] = 'ducati'
        #print(motorcycles)

#4、在列表中添加元素
#举例：motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)
# motorcycles.append('ducati')
#print(motorcycles)

#5、在列表中插入元素
#使用方法insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。
#举例：motorcycles = ['honda', 'yamaha', 'suzuki']
    #motorcycles.insert(0, 'ducati')
    #print(motorcycles)

#6、从表中删除元素
#6.1 del的运用
    #motorcycles = ['honda', 'yamaha', 'suzuki']
    #print(motorcycles)
    #del motorcycles[0]
    #print(motorcycles)
#6.2 pop() 删除元素
    #motorcycles = ['honda', 'yamaha', 'suzuki']
    #print(motorcycles)
    #popped_motorcycle = motorcycles.pop()
    # #print(motorcycles)
    # print(popped_motorcycle)

#7、序列类型
#7.1使用方法sort() 对列表进行永久性排序
    #cars = ['bmw', 'audi', 'toyota', 'subaru']
    # cars.sort()
    #print(cars)
#7.2使用函数sorted() 对表进行临时排序
    #cars = ['bmw', 'audi', 'toyota', 'subaru']
    #print("Here is the original list:")
    #print(cars)
    #print("\nHere is the sorted list:")
    #print(sorted(cars))
    #print("\nHere is the original list again:")
    #print(cars)

#8、元组
#8.1添加元素
#举例：alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#alien_0['x_position'] = 0
# alien_0['y_position'] = 25
#print(alien_0)

#8.2修改元素
#alien_0 = {'color': 'green'}
#print("The alien is " + alien_0['color'] + ".")
#alien_0['color'] = 'yellow'
#print("The alien is now " + alien_0['color'] + ".")

#8.3删除元素
#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#del alien_0['points']
#print(alien_0)

#favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
#print("Sarah's favorite language is " +  favorite_languages['sarah'].title() + ".")

#遍历
#ser_0 = {'username': 'efermi','first': 'enrico','last': 'fermi',}
#for key, value in user_0.items():
# print("\nKey: " + key)
# print("Value: " + value)

#favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
# for name, language in favorite_languages.items():
# print(name.title() + "'s favorite language is " +language.title() + ".")

#favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
#for name in favorite_languages.keys():
#print(name.title())

#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'yellow', 'points': 10}
#alien_2 = {'color': 'red', 'points': 15}
#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
#print(alien)




