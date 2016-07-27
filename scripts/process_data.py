# -*- coding: utf-8 -*-
from pymongo import MongoClient
from re import *
from Store import Store
from heapq import *

client = MongoClient()
db = client.restaurants

baoshan = db.baoshan.find()
# print baoshan
changning = db.changning.find()
chongming = db.chongming.find()
fengxian = db.fengxian.find()
hongkou = db.hongkou.find()
huangpu = db.huangpu.find()
jiading = db.jiading.find()
jingan = db.jingan.find()
jinshan = db.jinshan.find()
luwan = db.luwan.find()
minhang = db.minhang.find()
pudong = db.pudong.find()
putuo = db.putuo.find()
qingpu = db.qingpu.find()
songjiang = db.songjiang.find()
xuhui = db.xuhui.find()
yangpu = db.yangpu.find()
zhabei = db.zhabei.find()

names = {
'宝山': 'Baoshan', 
'长宁': 'Changning', 
'崇明': 'Chongming', 
'奉贤': 'Fengxian', 
'虹口': 'Hongkou', 
'黄浦': 'Huangpu', 
'嘉定': 'Jiading', 
'静安': 'Jingan',
'金山': 'Jinshan', 
'卢湾': 'Luwan', 
'闵行': 'Minhang', 
'浦东': 'Pudong', 
'普陀': 'Putuo', 
'青浦': 'Qingpu', 
'松江': 'Songjiang', 
'徐汇': 'Xuhui', 
'杨浦': 'Yangpu', 
'闸北': 'Zhabei' }

all_districts = {
'宝山': baoshan, 
'长宁': changning, 
'崇明': chongming, 
'奉贤': fengxian, 
'虹口': hongkou, 
'黄浦': huangpu, 
'嘉定': jiading, 
'静安': jingan,
'金山': jinshan, 
'卢湾': luwan, 
'闵行': minhang, 
'浦东': pudong, 
'普陀': putuo, 
'青浦': qingpu, 
'松江': songjiang, 
'徐汇': xuhui, 
'杨浦': yangpu, 
'闸北': zhabei }


class ProcessData:

    #number of cafés in every district of Shanghai
    def cafe_count(self):
        global all_districts
        global names
        fo = open("cafe_count.csv", "wb")
        fo.write("Area (CN),Number of Cafés,Area (EN)\n")
        for district in all_districts:
          count = 0
          price = 0
          for store in all_districts[district]:
              if store['dish_type'] == u'咖啡厅' and store['price'] != '-':
                  count += 1
                  price += int(store['price'])
          fo.write(district + "," + str(count) + "," + names[district] + "\n")
    
    #list of top 5 restaurants in every district of Shanghai
    def best_restaurants(self): 
        global all_districts
        global names

        
        fo = open("best_restaurants.csv", "wb")
        fo.write("Area (CN),restaurant name, overall rate, average price, Area (EN)\n")
        for district in all_districts:
            heap = []
            for store in all_districts[district]:
                if store['dish_type'] == u'咖啡厅' and store['price'] != '-':
                    s = Store(store)
                    heappush(heap, s)
                    
            for i in range(0, 5):
                s = heappop(heap)
                title = u''.join(s.title).encode('utf-8').strip()
                price = u''.join(s.price).encode('utf-8').strip()
                fo.write (district + "," + title + "," + str("%.2f" %((float(s.flavor_rate) + float(s.env_rate) +float(s.srv_rate))/3.)) + "," + price + "," + names[district] + "\n")
                    


if __name__ == '__main__':
    pd = ProcessData()
    pd.best_restaurants()