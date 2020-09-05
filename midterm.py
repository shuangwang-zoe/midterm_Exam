f = open('exercise\marks.txt',encoding='utf-8')
lines = f.readlines()
f.close()

#个人成绩集合
score_and_name = {}
score_collect = []
item = lines[0].split()
item.append("总分")
item.append("平均分")
#print(item) # 标签列
for line in lines[1:]:
    personal_record = line.split()
    element = personal_record[1:]
    sum = 0
    for i in range(1,len(element)):#计算总分
        sum += int(element[i])
    personal_record.append(sum) #把总数加进去
    average = sum/int(len(element))
    personal_record.append(float('%.2f'%average))#把平均数加进列表
    score_collect.append(personal_record)

#按平均分重新排序并添加名次
def order(personal_record):
    return personal_record[-1]

score_collect.sort(key = order, reverse=True)
for personal_record in score_collect:
    rank = score_collect.index(personal_record) + 1
    personal_record.insert(0,rank)
#print(score_collect)

#每科平均分
item_average = [0,'平均']
sum_average = 0
for j in range(2,len(element)+2):
    sum_course = 0
    for personal_record in score_collect:
        sum_course += int(personal_record[j])
    average = sum_course/len(score_collect)
    item_average.append(float('%.2f'%average))
    sum_average += average
average_all = sum_average/len(element)
item_average.append(float('%.2f' % average_all))
#print(item_average)

#合并
score_collect.insert(0,item_average)
score_collect.insert(0,item)
for n in score_collect[2:]: #把列表里原本为字符串格式的分数全部转化为数字
    n[2:-2]=[int(x) for x in n[2:-2]]
#print(score_collect)

#替换不及格
for n in score_collect[1:]:
    for j in range(2,len(n)):
        if n[j] < 60:
            n[j] = '不及格'

#把列表转化成字符串



    #写入新文件
score_all = []
for record in score_collect:
    new_record = " ".join('%s' % id for id in record)   
    score_all.append(new_record)
    score_all.append('\n')
output = open('score_all.txt', 'w', encoding='utf-8')
output.writelines(score_all)
output.close()
        



