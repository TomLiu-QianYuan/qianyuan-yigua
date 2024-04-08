import datetime
# import os
import random
from resources import *
import pytz
import streamlit as st
import borax.calendars as bc

dy_c = 0

di_zhi = {
    "子": 1,
    "丑": 2,
    "寅": 3,
    "卯": 4,
    "辰": 5,
    "巳": 6,
    "午": 7,
    "未": 8,
    "申": 9,
    "酉": 10,
    "戌": 11,
    "亥": 12,
}
di_zhi_list = [

    "子",
    "丑",
    "寅",
    "卯",
    "辰",
    "巳",
    "午",
    "未",
    "申",
    "酉",
    "戌",
    "亥"]
gua_to_images = {
    "乾": "▀▀▀▀▀▀\n▀▀▀▀▀▀\n▀▀▀▀▀▀",
    "兑": "▀▀  ▀▀\n▀▀▀▀▀▀\n▀▀▀▀▀▀",
    "离": "▀▀▀▀▀▀\n▀▀  ▀▀\n▀▀▀▀▀▀",
    "震": "▀▀  ▀▀\n▀▀  ▀▀\n▀▀▀▀▀▀",
    "巽": "▀▀▀▀▀▀\n▀▀▀▀▀▀\n▀▀  ▀▀",
    "坎": "▀▀  ▀▀\n▀▀▀▀▀▀\n▀▀  ▀▀",
    "艮": "▀▀▀▀▀▀\n▀▀  ▀▀\n▀▀  ▀▀",
    "坤": "▀▀  ▀▀\n▀▀  ▀▀\n▀▀  ▀▀",

}
# simple version
xian_tian_gua = [
    '111',
    '011',
    '101',
    '001',
    '110',
    '010',
    '100',
    '000'
]
gua_ming = {
    '111': "乾",
    '011': "兑",
    '101': "离",
    '001': "震",
    '110': "巽",
    '010': "坎",
    '100': "艮",
    '000': "坤"
}


def get_gua(a: int, b: int, c: int):
    # get bin gua
    global dy_c
    if a == 0:
        a = 8
    if b == 0:
        b = 8
    if c == 0:
        c = 6
    a = (a + 8) % 8 - 1
    b = (b + 8) % 8 - 1
    c = (c + 6) % 6
    zhu_gua = [
        xian_tian_gua[a], xian_tian_gua[b]
    ]
    hu_gua = [xian_tian_gua[a][1] + xian_tian_gua[a][2] + xian_tian_gua[b][0],
              xian_tian_gua[a][2] + xian_tian_gua[b][0] + xian_tian_gua[b][1]
              ]
    temp = list(xian_tian_gua[a] + xian_tian_gua[b])
    # print('x',c)
    # print('xz', 6-c)
    print(temp)
    if temp[-c] == '0':
        # print('动阴')
        temp[-c] = '1'
    else:
        # print('动阳')
        temp[-c] = '0'
        # print("-c:",-c)
    dy_c = -c
    # print(temp)
    bian_gua = [temp[0] + temp[1] + temp[2], temp[3] + temp[4] + temp[5]]
    return ([gua_ming[zhu_gua[0]], gua_ming[zhu_gua[1]]],
            [gua_ming[hu_gua[0]], gua_ming[hu_gua[1]]],
            [gua_ming[bian_gua[0]], gua_ming[bian_gua[1]]]
            )


def get_shi(time: int):
    # 获取时辰
    print('current hour:', time)
    if 1 <= time < 3:
        return di_zhi_list[1]
    elif 3 <= time < 5:
        return di_zhi_list[2]
    elif 5 <= time < 7:
        return di_zhi_list[3]
    elif 7 <= time < 9:
        return di_zhi_list[4]
    elif 9 <= time < 11:
        return di_zhi_list[5]
    elif 11 <= time < 13:
        return di_zhi_list[6]
    elif 13 <= time < 15:
        return di_zhi_list[7]
    elif 15 <= time < 17:
        return di_zhi_list[8]
    elif 17 <= time < 19:
        return di_zhi_list[9]
    elif 19 <= time < 21:
        return di_zhi_list[10]
    elif 21 <= time < 23:
        return di_zhi_list[11]
    elif 23 <= time or time < 1:
        return di_zhi_list[0]

def get_gua(a: int, b: int, c: int):
    global dy_c
    if a == 0:
        a = 8
    if b == 0:
        b = 8
    if c == 0:
        c = 6
    a = (a + 8) % 8 - 1
    b = (b + 8) % 8 - 1
    c = (c + 6) % 6
    zhu_gua = [
        xian_tian_gua[a], xian_tian_gua[b]
    ]
    hu_gua = [xian_tian_gua[a][1] + xian_tian_gua[a][2] + xian_tian_gua[b][0],
              xian_tian_gua[a][2] + xian_tian_gua[b][0] + xian_tian_gua[b][1]
              ]
    temp = list(xian_tian_gua[a] + xian_tian_gua[b])
    # print('x',c)
    # print('xz', 6-c)
    print(temp)
    if temp[-c] == '0':
        # print('动阴')
        temp[-c] = '1'
    else:
        # print('动阳')
        temp[-c] = '0'
        # print("-c:",-c)
    dy_c = -c
    # print(temp)
    bian_gua = [temp[0] + temp[1] + temp[2], temp[3] + temp[4] + temp[5]]
    return ([gua_ming[zhu_gua[0]], gua_ming[zhu_gua[1]]],
            [gua_ming[hu_gua[0]], gua_ming[hu_gua[1]]],
            [gua_ming[bian_gua[0]], gua_ming[bian_gua[1]]]
            )


def get_shi(time: int):
    print('tt', time)
    if 1 <= time < 3:
        return di_zhi_list[1]
    elif 3 <= time < 5:
        return di_zhi_list[2]
    elif 5 <= time < 7:
        return di_zhi_list[3]
    elif 7 <= time < 9:
        return di_zhi_list[4]
    elif 9 <= time < 11:
        return di_zhi_list[5]
    elif 11 <= time < 13:
        return di_zhi_list[6]
    elif 13 <= time < 15:
        return di_zhi_list[7]
    elif 15 <= time < 17:
        return di_zhi_list[8]
    elif 17 <= time < 19:
        return di_zhi_list[9]
    elif 19 <= time < 21:
        return di_zhi_list[10]
    elif 21 <= time < 23:
        return di_zhi_list[11]
    elif 23 <= time or time < 1:
        return di_zhi_list[0]


st.set_page_config(page_title="乾元易卦",
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

# 导航栏
# 设置初始页面为Home
session_state = st.session_state
session_state['page'] = '起卦'

# page = st.sidebar.radio('导航', ['起卦', '书籍'])
# if page == "起卦":
st.code('''
观物吟
一物从来有一身，一身还有一乾坤。
能知百物备与我，肯把三才别立根。
天向一中分造化，人与心上起经纶。
仙人亦有两般话，道不虚传只在人。
''')
time = st.date_input("日期", value=datetime.datetime.now(pytz.timezone("ASIA/ShangHai")).date())
time2 = st.time_input("时间", value=datetime.datetime.now(pytz.timezone("ASIA/ShangHai")))
time2 = time2.hour
# time = st.time_input("选择时间:",datetime)
qs = st.text_input("占问:", placeholder="占问何事")
mode_to_select = st.selectbox('起卦方式', ['时间起卦', '报数起卦', '随机起卦'])
# print(mode_to_select)
if mode_to_select == '报数起卦':
    three_num = st.text_input(label='请输入三个整数', placeholder="321")
    if len(three_num) < 3 and three_num != []:
        st.warning("你需要填写3个数字，格式如:123")
    elif len(three_num) == 3:
        c = int(three_num[2])
        if c > 6:
            c = c % 6
        elif c == 6 or c <= 0:
            c = 6

        three_num = [int(three_num[0]), int(three_num[1]), int(three_num[2])]
    elif len(three_num) > 3:
        st.warning("你暂时只能填写三个数字哦")

if mode_to_select == '随机起卦':
    c = random.randint(1, 64)
    three_num = [random.randint(1, 64), random.randint(1, 64), c]

start = st.button(label="开始起卦")

if start:
    st.code(bc.LunarDate.from_solar_date(
        time.year,
        time.month,
        time.day,
    ).strftime('%G') + get_shi(time2) + "时")
    # print(functions.di_zhi.values()[0])
    if mode_to_select == '时间起卦':
        time_ = bc.LunarDate.from_solar_date(
            time.year,
            time.month,
            time.day,
        ).strftime('%G')
        year_gz = di_zhi[time_[1]]
        # yue_gz = functions.di_zhi[time_[4]]
        # ri_gz = functions.di_zhi[time_[7]]
        yue = bc.LunarDate.from_solar_date(
            time.year,
            time.month,
            time.day,
        ).month
        # print(yue)
        ri = bc.LunarDate.from_solar_date(
            time.year,
            time.month,
            time.day,
        ).day
        # print(ri)

        shi = (time2 + 1) // 2 + 1
        # print(year_gz, yue_gz, ri_gz)
        a = year_gz + yue + ri
        b = year_gz + yue + ri + shi
        c = b
        if c > 6:
            c = c % 6
        elif c == 6:
            c = 6

        print(a, b, c)
        three_num = [a, b, c]
    # 开始起卦
    result = list(get_gua(three_num[0], three_num[1], three_num[2]))
    show = []
    for x in range(0, 2):

        zhu_gua = str(gua_to_images[result[0][x]])
        hu_gua = str(gua_to_images[result[1][x]])
        bian_gua = str(gua_to_images[result[2][x]])

        # print(zhu_gua, '\n')
        # print(hu_gua, '\n')
        # print(bian_gua)
        for m in range(0, 3):
            show.append('\n')
            show.append(zhu_gua.split('\n')[m])
            # .replace(
            #             '1', ''))
            #             .replace('1', '')
            #             .replace('1', '')
            #             .replace('1', '')
            #             .replace('1', '')
            #             .replace('1', '')
            #             .replace('1', '')
            #
            #             )
            show.append('\t\t')
            show.append(hu_gua.split('\n')[m])
            show.append('\t\t')
            show.append(bian_gua.split('\n')[m])

            # print(x * 3 + m)
            print("动爻:", dy_c)
            if dy_c < 0:
                dy_c = 6 + dy_c
            print((x * 3 + m), dy_c)
            if (x * 3 + m) == dy_c:
                show.append('\tO')

        # print(show)
    st.code("".join(show))
    st.text("若需将此卦分享请复制:")
    st.code(bc.LunarDate.from_solar_date(
        time.year,
        time.month,
        time.day,
    ).strftime('%G') + get_shi(time2) + "时" + str(three_num)+"-"+qs)
