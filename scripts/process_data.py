# -*- coding: utf-8 -*-
from pymongo import MongoClient
from re import *
from Store import Store
from heapq import *

client = MongoClient()
db = client.restaurants

baoshan = db.baoshan.find()
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
              if (store['dish_type'] == u'咖啡厅' or store['dish_type'] == u'面包甜点') and store['price'] != '-':
                  count += 1
                  price += int(store['price'])
          fo.write(district + "," + str(count) + "," + names[district] + "\n")
        fo.close()    
    #list of top 5 restaurants in every district of Shanghai
    def best_restaurants(self): 
        global all_districts
        global names
        fo = open("best_restaurants.csv", "wb")
        fo.write("Area (CN),restaurant name, overall rate, average price, num of comments, Area (EN)\n")
        for district in all_districts:
            heap = []
            for store in all_districts[district]:
                if (store['dish_type'] == u'咖啡厅' or store['dish_type'] == u'面包甜点') and store['price'] != '-' and int(store['num_comment']) >= 600: 
                    s = Store(store)
                    heappush(heap, s)

            unique_stores = set([])      
            while len(unique_stores) < 5 and len(heap) > 0:
                s = heappop(heap)
                title = u''.join(s.title).encode('utf-8').strip()
                price = u''.join(s.price).encode('utf-8').strip()
                num_comment = u''.join(s.num_comment).encode('utf-8').strip()
                unique_stores.add(district + "," + title + "," + str("%.2f" %((float(s.flavor_rate) + float(s.env_rate) +float(s.srv_rate))/3.)) + "," + price + "," + num_comment + "," + names[district] + "\n")
            for entry in unique_stores:
                fo.write(entry)    
        fo.close()

    def avg_comments_rate(self):
        global all_districts
        global names
        fo = open("avg_comments_rate.csv", "wb")
        fo.write("Area (CN), average num of comments, average rate, Area (EN)\n")
        for district in all_districts:
            count = 0
            comments = 0
            rate = 0.
            for store in all_districts[district]:
                if (
                        (store['dish_type'] == u'咖啡厅' or store['dish_type'] == u'面包甜点') and 
                        store['price'] != '-' and store['srv_rate'] != '-' and 
                        store['env_rate'] != '-' and store['flavor_rate'] != '-'
                    ):
                    count += 1
                    comments += int(store['num_comment'])
                    rate += (float(store['flavor_rate']) + float(store['env_rate']) +float(store['srv_rate']))/3.
            print str(count) + district
            fo.write(district + "," + str(int(comments/count)) + "," + str("%.2f" % (rate/float(count))) + "," + names[district] + "\n")
        fo.close()


    def avg_price(self):
        global all_districts
        global names
        fo = open("avg_price.csv", "wb")
        fo.write("Area (CN), average price, Area (EN)\n")
        for district in all_districts:
            count = 0
            price = 0
            for store in all_districts[district]:
                if (store['dish_type'] == u'咖啡厅' or store['dish_type'] == u'面包甜点') and store['price'] != '-':
                    count += 1
                    price += int(store['price'])
                    # if district == "徐汇":
                        # print store['price'] + store['title']
            fo.write(district + "," + str(price/count) + "," + names[district] + "\n")
        fo.close()


    def ratio_diff_rate(self):
        global all_districts
        global names
        fo = open("ratio_diff_rate.csv", "wb")
        fo.write("Area (CN), avg flv ratio, avg srv ratio, avg env ratio, Area (EN)\n")
        for district in all_districts:
            count = 0
            # rate = 0.
            flv_rate = 0.
            srv_rate = 0.
            env_rate = 0.
            for store in all_districts[district]:
                if (
                        (store['dish_type'] == u'咖啡厅' or store['dish_type'] == u'面包甜点') and 
                        store['price'] != '-' and int(store['num_comment']) >= 200 and 
                        store['srv_rate'] != '-' and store['env_rate'] != '-' and store['flavor_rate'] != '-'
                    ):
                    count += 1
                    tmp = (float(store['flavor_rate']) + float(store['env_rate']) + float(store['srv_rate']))/3.
                    if tmp >= 0:
                        # rate += tmp
                        flv_rate += float(store['flavor_rate'])
                        env_rate += float(store['env_rate'])   
                        srv_rate += float(store['srv_rate']) 
            # print str(count) + district
            fo.write(district + "," + str("%.3f" %(flv_rate/float(count))) + "," 
                + str("%.3f" % (srv_rate/float(count))) + "," + str("%.3f" %(env_rate/float(count))) + "," 
                + names[district] + "\n")
        fo.close()

    def ratio_diff_rate_general(self):
        global all_districts
        global names
        fo = open("ratio_diff_rate_general.csv", "wb")
        fo.write("Area (CN), avg flv ratio, avg srv ratio, avg env ratio, Area (EN)\n")
        for district in all_districts:
            count = 0
            # rate = 0.
            flv_rate = 0.
            srv_rate = 0.
            env_rate = 0.
            for store in all_districts[district]:
                if (
                        store['price'] != '-' and int(store['num_comment']) >= 200 and 
                        store['srv_rate'] != '-' and store['env_rate'] != '-' and store['flavor_rate'] != '-'
                    ):
                    count += 1
                    tmp = (float(store['flavor_rate']) + float(store['env_rate']) + float(store['srv_rate']))/3.
                    if tmp >= 0:
                        # rate += tmp
                        flv_rate += float(store['flavor_rate'])
                        env_rate += float(store['env_rate'])   
                        srv_rate += float(store['srv_rate']) 
            # print str(count) + district
            fo.write(district + "," + str("%.3f" %(flv_rate/float(count))) + "," 
                + str("%.3f" % (srv_rate/float(count))) + "," + str("%.3f" %(env_rate/float(count))) + "," 
                + names[district] + "\n")
        fo.close()

if __name__ == '__main__':
    pd = ProcessData()
    # pd.cafe_count()
    # pd.best_restaurants()
    # pd.avg_comments_rate()
    # pd.avg_price()
    # pd.ratio_diff_rate()
    pd.ratio_diff_rate_general()
