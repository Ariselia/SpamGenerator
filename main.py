"""
Qzone spam generator
Created by CatMe0w
"""
import random

# Initialize variables
customTagsList = ['留空' for i in range(12)]
rankingList = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
random.shuffle(rankingList)
# print(rankingList)

inputArgs = input('请输入所需生成类型...\n【1】默认示例\n【2】自定义\n')

if inputArgs == '1':
    # Generate spam in default format
    print('【最近缺钱一定得转！星座运势排名 4天钱到账！】')
    for i in range(12):
        print('第 {0} 名：'.format(i + 1), rankingList[i])

if inputArgs == '2':
    customTitle = input('请输入自定义标题....\n')
    print('注：附加标签，即排名后括号内的内容，可不填')
    for i in range(12):
        customTags = input('请输入排名第 {0} 位的星座 附加标签内容: '.format(i + 1))
        if customTags == '':
            continue
        else:
            customTagsList[i] = customTags
    # Generate spam
    if customTagsList[0:12] == ['留空' for i in range(12)]:
        print('【{0}】'.format(customTitle))
        for i in range(12):
            print('第 {0} 名：'.format(i + 1), rankingList[i])
    else:
        print('【{0}】'.format(customTitle))
        for i in range(12):
            print('第 {0} 名：'.format(i + 1), rankingList[i], '（{0}）'.format(customTagsList[i]))
