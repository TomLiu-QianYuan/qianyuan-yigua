import streamlit as st

wu_xing_list = ["金", "水", "木", "火", "土"]
gua_wixing_dict = {
    '乾': '金',
    '兑': '金',
    '离': '火',
    '震': '木',
    '巽': '木',
    '坎': '水',
    '艮': '土',
    '坤': '土',

}

zhu_index = 0

hu_index = 0

bian_index = 0


def wuxing_duan(ti, yong):
    global wu_xing_list
    ti_position = wu_xing_list.index(ti)
    yong_position = wu_xing_list.index(yong)

    # print("体位:", ti_position)
    # print("用位:", yong_position)

    if ti_position + 1 or ti_position + 2 or ti_position + 3 or ti_position + 4 > 4:
        ti_position -= 5

    if wu_xing_list[ti_position + 1] == yong:
        # 体生用
        # st.write("体生用")
        return 2

    elif wu_xing_list[ti_position + 2] == yong:
        # 体克用
        # st.write("体克用")
        return 3
    elif wu_xing_list[ti_position + 3] == yong:
        # 用克体
        # st.write("用克体")
        return 1
    elif wu_xing_list[ti_position + 4] == yong:
        # 用生体
        # st.write("用生体")
        return 4
    else:
        # st.write("比和")
        return 3


gua_table = st.session_state
# gua_table = (['艮', '离'], ['震', '坎'], ['艮', '震'])
zhu_gua = gua_table[0]
hu_gua = gua_table[1]
bian_gua = gua_table[2]

# 辨别体用
ti_gua = ''
if zhu_gua[0] == bian_gua[0]:
    # 体卦在上

    ti_gua = zhu_gua[0]
    # print(f"体为{ti_gua}")

    zhu_ti_wuxing = gua_wixing_dict[ti_gua]
    zhu_yong_wuxing = gua_wixing_dict[zhu_gua[1]]
    hu_ti_wuxing = gua_wixing_dict[hu_gua[0]]
    hu_yong_wuxing = gua_wixing_dict[hu_gua[1]]
    bian_ti_wuxing = gua_wixing_dict[bian_gua[0]]
    bian_yong_wuxing = gua_wixing_dict[bian_gua[1]]


else:
    # 体卦在下
    ti_gua = zhu_gua[1]
    # print(f"体为{ti_gua}")

    zhu_ti_wuxing = gua_wixing_dict[ti_gua]
    zhu_yong_wuxing = gua_wixing_dict[zhu_gua[0]]
    hu_ti_wuxing = gua_wixing_dict[hu_gua[1]]
    hu_yong_wuxing = gua_wixing_dict[hu_gua[0]]
    bian_ti_wuxing = gua_wixing_dict[bian_gua[1]]
    bian_yong_wuxing = gua_wixing_dict[bian_gua[0]]

zhu_index = wuxing_duan(zhu_ti_wuxing, zhu_yong_wuxing)
hu_index = wuxing_duan(hu_ti_wuxing, hu_yong_wuxing)
bian_index = wuxing_duan(bian_ti_wuxing, bian_yong_wuxing)
st.write("智能断卦助手为你解答:\n")
st.text("系数越高越吉,反之越凶")
st.code(f"主卦吉凶系数:{zhu_index}\n"
        f"互卦吉凶系数:{hu_index}\n"
        f"变卦吉凶系数:{bian_index}")
if zhu_index > bian_index:
    st.write("变比主凶,事情常不顺利")
    if zhu_index - bian_index > 2:
        st.code("此次吉凶变化较大,甚至于失败")
    else:
        st.code("此次吉凶变化较小,不容易失败")
if zhu_index < bian_index:
    st.write("变比主吉,事情常顺利")
    if bian_index - zhu_index > 2:
        st.code("此次吉凶变化较大,甚至于成功")
    else:
        st.code("此次吉凶变化较小,不容易成功")
if zhu_index <= 2:
    st.code("开始不顺利")
else:
    st.code("开始顺利")
if zhu_index < hu_index:
    st.code("过程中会比开始吉利")
elif zhu_index > hu_index:
    st.code("过程中会比开始凶险")
else:
    st.code("过程和开始一样")
if hu_index < bian_index:
    st.code("结果会比过程吉利")
else:
    st.code("结果会比过程凶险")

st.page_link(page="home.py", label="回到主页面")
