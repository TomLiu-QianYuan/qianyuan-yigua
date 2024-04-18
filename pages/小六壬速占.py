liu_ren_gong = ["大安（木）：开始安静之意", "留连（土）：留恋纠缠之意", "速喜（火）：好事很快来临之意",
                "赤口（金）：争执口角斗争之意", "小吉（水）：事情逐渐实现之意", "空亡（土）:事情变成空缺之意"]

import streamlit as st

three_num = []

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


def xiao_liu_ren(first_number: int = 0, second_number: int = 0, third_number: int = 0):
    # global first_number_c, second_number_c, third_number_c
    first_number_c = (first_number + 6) % 6
    second_number_c = (second_number + 6) % 6
    third_number_c = (third_number + 6) % 6
    first_number_c = first_number_c - 1
    second_number_c = (first_number_c + second_number_c) % 6 - 1
    third_number_c = (second_number_c + third_number) % 6 - 1

    # print(f"数1:{first_number_c + 1} 数2:{second_number_c} 数3:{third_number_c}")
    print(f"天宫|开始:{liu_ren_gong[first_number_c]}")
    print(f"地宫|过程:{liu_ren_gong[second_number_c]}")
    print(f"重点关注-人宫|结果:{liu_ren_gong[third_number_c]}")
    st.text(f"天宫|开始:{liu_ren_gong[first_number_c]}")
    st.text(f"地宫|过程:{liu_ren_gong[second_number_c]}")
    st.text(f"重点关注-人宫|结果:{liu_ren_gong[third_number_c]}")


three_number = st.text_input(label="请输入第一个数字", placeholder="如:1")
three_number_2 = st.text_input(label="请输入第二数字", placeholder="如:2")
three_number_3 = st.text_input(label="请输入第三个数字", placeholder="如:3")
start = st.button(label="开始计算")
mh = st.button(label="起梅花卦")
if three_number and three_number_2 and three_number_3 and start:
    try:
        xiao_liu_ren(
            int(three_number),
            int(three_number_2),
            int(three_number_3))

    except Exception as error:
        st.error("请确保格式正确!")
        st.error(error)
if three_number and three_number_2 and three_number_3 and mh:
    result = list(get_gua(int(three_number),
                          int(three_number_2),
                          int(three_number_3)))
    # st.text("占问:")
    # st.code(qs)
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
