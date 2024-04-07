import json
import os

import streamlit as st

# print(os.getcwd())
# st.code(os.getcwd())
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

st.code(os.getcwd())
st.code(os.listdir())
gua_list_ = os.listdir(f"{os.getcwd()}\\spages\\fk")
gua_list = list()

for i in gua_list_:
    gua_list.append(i)

which_one = st.selectbox("选择卦例", gua_list)

if which_one:
    context = open(
        f"{os.getcwd()}\\pages\\fk\\{which_one}", 'r', encoding='utf-8'
    )
    context = json.load(context)
    st.code(context['time'])
    three_num = context['gua']

    result = list(get_gua(int(three_num[0]),
                          int(three_num[1]),
                          int(three_num[2])))

    show = []
    for x in range(0, 2):
        zhu_gua = str(gua_to_images[result[0][x]])
        hu_gua = str(gua_to_images[result[1][x]])
        bian_gua = str(gua_to_images[result[2][x]])
        for m in range(0, 3):
            show.append('\n')
            show.append(zhu_gua.split('\n')[m])
            show.append('\t\t')
            show.append(hu_gua.split('\n')[m])
            show.append('\t\t')
            show.append(bian_gua.split('\n')[m])
    st.code("".join(show))
    st.text("占问:")

    st.code(context['qs'])
    st.text("反馈:")

    st.code(context['fankui'])
