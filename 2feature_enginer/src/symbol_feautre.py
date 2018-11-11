# coding=utf-8
import numpy as np
infile = open("../open_data/dat_symbol.txt", 'r')
outfile = open("../feature/dat_symbol_feature_2.txt",'w')
class_name = ['其他公司类',"互金公司","贷款类","网络标识","餐饮美食","快递送餐",
              "休闲娱乐","旅游出行","金融类","医疗健康","其他中介","房产类","教育类",
              "日常生活","购物","银行","酒店","法律","公安","不良习惯","运动健身",
              "信用卡","急救中心","征信"]
class2_name = ['其他公司类_其他','互金公司_p2p','网络标识_推销骚扰','网络标识_诈骗',
               '餐饮美食_快餐','餐饮美食_餐厅','餐饮美食_面包甜点','餐饮美食_烧烤',
               '快递送餐_送餐','快递送餐_快递','休闲娱乐_其他','旅游出行_出行',
               '旅游出行_其他','金融类_投资理财','医疗健康_其他','其他中介_其他中介',
               '房产类_其他','房产类_房产中介','教育类_其他','日常生活_其他','购物_超市',
               '购物_其他','购物_商场','银行_其他','酒店_其他','法律_律师','法律_其他',
               '法律_法院','公安_其他','不良习惯_赌博类','不良习惯_假证类','运动健身_其他',
               '贷款类_催收','贷款类_中介','贷款类_黑户贷款','贷款类_房贷','贷款类_车贷',
               '贷款类_其他','贷款类_抵押类','信用卡_套现','信用卡_银行客服','信用卡_提额',
               '急救中心_其他','征信_征信查询']
for line in infile:
    line = line.strip()
    symbol = line.split('\t')[1]
    data = set()
    if symbol == 'symbol':
        outfile.write(line + '\n')
        continue
    for c in symbol.split(','):
        data.add(c.split('_')[0])
    data = list(data)
    outline = ','.join(str(s) for s in data)
    outline = line.split('\t')[0] + '\t' + outline
    outfile.write(outline+'\n')
outfile.close()
infile.close()

