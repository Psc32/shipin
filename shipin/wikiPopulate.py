import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shipin.settings')
import django
django.setup()
from wiki.models import Category, Page
import random


def populate():
    # 游戏视频
    category = addCategory('游戏视频')
    addPage(category, '多玩游戏视频', 'http://www.duowan.com/')
    addPage(category, '17173游戏视频', 'http://v.17173.com/')
    addPage(category, '太平洋游戏网', 'http://v.pcgames.com.cn/')
    # 现代电影
    category = addCategory('现代电影')
    addPage(category, '优酷电影', 'http://movie.youku.com/')
    addPage(category, '奇摩电影', 'https://tw.movies.yahoo.com/')
    addPage(category, 'youtube电影','https://www.youtube.com/playlist?list=PLCB8PNVqPO58yms2lTW2FFD9vpl7Bfdy-')
    # 古装剧
    category = addCategory('电视剧')
    addPage(category, '虎扑体育','http://v.opahnet.com/')
    addPage(category, '搜狐体育', 'http://tv.sohu.com/sports/')
    addPage(category, '爱奇艺体育', 'http://sports.iqiyi.com/')
    # 娱乐
    category = addCategory('娱乐视频')
    addPage(category, '腾讯视频', 'http://v.qq.com/ent/')
    addPage(category, '搜狗娱乐', 'http://kan.sogou.com/yule/')
    addPage(category,'新浪视频','http://video.sina.com.cn/ent/#250369637')
    #其他
    category = addCategory('其他')
    addPage(category, '优酷记录片', 'http://jilupian.youku.com/')
    addPage(category, '动物世界', 'http://v.baidu.com/show/1630.html')
    addPage(category, '荒野求生', 'http://v.baidu.com/show/6046.html')
    
    # 印出所輸入的資料
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(category.name, '--', page.title)
            
            
def addCategory(name):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = random.randint(0, 20)
    category.likes = random.randint(0, 20)
    category.save()
    return category
def addPage(category, title, url):
    Page.objects.get_or_create(category=category, title=title, url=url)


if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。') 