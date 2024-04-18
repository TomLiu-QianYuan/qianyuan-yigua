import streamlit as st

liu_ren_gong = ["大安（木）：开始安静之意", "留连（土）：留恋纠缠之意", "速喜（火）：好事很快来临之意",
                "赤口（金）：争执口角斗争之意", "小吉（水）：事情逐渐实现之意", "空亡（土）:事情变成空缺之意"]


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
    st.code(f"天宫|开始:{liu_ren_gong[first_number_c]}")
    st.code(f"地宫|过程:{liu_ren_gong[second_number_c]}")
    st.code(f"重点关注-人宫|结果:{liu_ren_gong[third_number_c]}")


three_number = st.text_input(label="请输入三个数字", placeholder="如:123")
if three_number:
    try:
        xiao_liu_ren(int(
            three_number[0]),
            int(three_number[1]),
            int(three_number[2]))

    except Exception as error:
        st.error("请确保格式正确!")
        st.error(error)
