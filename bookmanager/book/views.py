from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import F, Q, Avg
from book.models import PeopleInfo, BookInfo  # 导入模块报红是pycharm的bug，实际可执行


# 为书籍表添加数据
# BookInfo.objects.create(
#     name='三国演义'
#
# )
# # 为人物表添加数据
# PeopleInfo.objects.create(
#     name='刘备',
#     book_id='5'
# )
# PeopleInfo.objects.create(
#     name='关羽',
#     book_id=5
# )

# PeopleInfo.objects.filter(name='刘备').update(description='三顾茅庐')  # 为姓名是刘备的人物添加介绍
# PeopleInfo.objects.filter(name='关羽').update(description='温酒斩华雄')  # 为姓名是关羽的人物添加介绍
# BookInfo.objects.filter(id=7).delete()  # 删除id为7的书籍
# BookInfo.objects.filter(id=1).all()  # 查询id为1的所有书籍
# BookInfo.objects.all()  # 查询所有书籍
# PeopleInfo.objects.filter(name='关羽')  # 查询姓名为 关羽 的任务
# BookInfo.objects.filter(name__contains='三')  # 查询名字中含有 三 的书籍
# BookInfo.objects.filter(name__endswith='义')  # 查询名字中以 义 结尾的书籍
# BookInfo.objects.filter(name__startswith='三')  # 查询名字中以 三 开头的书籍
# BookInfo.objects.filter(pub_date__isnull=True)  # 查询发布时间为空的书籍
# BookInfo.objects.filter(id__in=range(1, 4))  # 查询ID为1-4的书籍，或id__in=[1,2,3,4]
# BookInfo.objects.filter(id__gte=3)  # 查询ID大于等于3的书籍，gt是等于，lt是小于，lte是小于等于
# BookInfo.objects.exclude(id__gt=3)  # 使用exclude()过滤，实际结果为ID小于等于3的书籍
# BookInfo.objects.filter(pub_date__year__gte=1986)  # 查询发布时间大于等于1986年的书籍
# BookInfo.objects.filter(commentcount__gt=F('readcount'))  # 查询点击量大于阅读量的书籍
# BookInfo.objects.filter(commentcount__gt=F('readcount') * 2)  # 查询点击量大于阅读量两倍的书籍
# BookInfo.objects.filter(readcount__gt=30, id__gt=2)  # 查询阅读量大于30且id大于2的书籍
# BookInfo.objects.filter(Q(readcount__gt=30) | Q(id__gt=3))  # 查询阅读量大于30或id大于3的书籍 &表示逻辑与，|表示逻辑或
# BookInfo.objects.filter(Q(readcount__gt=30) & Q(id__gt=3))  # 查询阅读量大于30且id大于3的书籍 &表示逻辑与，|表示逻辑或。~表示not非
# BookInfo.objects.filter(~Q(id=3))  # 查询id不等于3的书籍，&表示逻辑与，|表示逻辑或。~在Q前表示not非
# BookInfo.objects.filter(~Q(id=3) & ~Q(id=2))  # 查询id不等于3且不等于2的书籍 ~要和每个Q拼接使用
# BookInfo.objects.aggregate(Avg('readcount'))  # 使用Avg求阅读量的平均值 Avg平均，Count数量，Max最大，Min最小，Sum求和，需要在models模块中导入
# BookInfo.objects.all().order_by('readcount')  # 使用order_by进行排序，默认升序，加-为降序
# # 对应的模型类对象.多对应的模型类名小写_set
# BookInfo.objects.get(id=1).peopleinfo_set.all()  # 查询id为1的书籍所有的人物
#
# book = BookInfo.objects.get(id=1)  # 查询id为1的书籍赋值给book
# book.peopleinfo_set.all()  # 查询id为1的书籍所有的人物 先存储再调用会减少缓存占用
# # BookInfo.objects.filter(id__gt=3).peopleinfo_set.all() #BookInfo.objects.filter(id__gt=3)的结果为QuerySet类型，不支持
#
# PeopleInfo.objects.get(id=1).book  # 查询id为1的人物对应的书籍名称
# # 多对应的模型类对象.关联类属性_id
# person = PeopleInfo.objects.get(id=8)
#
# person.book_id  # 查询id为1的人物对应的书籍关联id
# # 关联模型类名小写__属性名__条件运算符=值
# book = BookInfo.objects.filter(peopleinfo__name='郭靖')
# book  # 查询图书，要求图书人物为"郭靖"
# book = BookInfo.objects.filter(peopleinfo__name__contains='刘')
# book  # 查询图书，要求图书中人物名称包含"刘"
#
# # 模型类关联属性名__模型类属性名__条件运算符=值
# people = PeopleInfo.objects.filter(book__name='天龙八部')
# people  # 查询书名为“天龙八部”的所有人物
#
# people = PeopleInfo.objects.filter(book__name__contains='八')
# people  # 查询书名包含“八”的书籍的所有人物


# 定义页面index界面返回内容
def index(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2020-1-1',
        readcount=10
    )
    return HttpResponse("OK")


def shop(request, city_id, shop_id):
    query_params = request.GET
    print(query_params)  # 获取查询字符串的查询字典
    order = query_params.get('order')  # 获取查询字符串字典的键值，一键多值用getlist
    return HttpResponse('城市的小店')
