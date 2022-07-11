import streamlit as st
import math

def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_triagle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2

def is_valid_quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4):
    # check if it has the same point
    if ((x1, y1) == (x2, y2) or (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4) or
        (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4) or (x3, y3) == (x4, y4)):
        return False
    # check if three points are on a line
    if (get_triagle_area(x1, y1, x2, y2, x3, y3) == 0 or get_triagle_area(x1, y1, x3, y3, x4, y4) == 0
        and get_triagle_area(x2, y2, x3, y3, x4, y4) == 0):
        return False
    # check intersectoin
    for _ in range(2):
        sign11 = (x1 - x2)*(y3 - y1) + (y1 - y2)*(x1 - x3)
        sign12 = (x1 - x2)*(y4 - y1) + (y1 - y2)*(x1 - x4)
        sign21 = (x3 - x4)*(y1 - y3) + (y3 - y4)*(x3 - x1)
        sign22 = (x3 - x4)*(y2 - y3) + (y3 - y4)*(x3 - x2)
        if sign11*sign12 < 0 and sign21*sign22 < 0:
            return False
        x1, x2, x3, x4 = x4, x1, x2, x3
        y1, y2, y3, y4 = y4, y1, y2, y3
    return True


st.markdown("# Math Solver")
st.markdown("このページでは便利な数学計算がおこなえます。")


st.markdown("### ２次方程式の解")
st.markdown("以下のxに関する２次方程式を解きます。")
st.latex(r"""
ax^2 + bx + c = 0
""")
st.text("ただし a > 0 とします。")

st.markdown("#### 使っている公式")
st.latex(r"""
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
""")

with st.form(key="quadratic_eq"):
    a = st.text_input("a")
    b = st.text_input("b")
    c = st.text_input("c")
    submit_btn_quadratic_eq = st.form_submit_button("Calculate")
    if submit_btn_quadratic_eq:
        if a and b and c and is_num(a) and float(a) != 0 and is_num(b) and is_num(c):
            a, b, c = float(a), float(b), float(c)
            D = b**2 - 4*a*c
            if D < 0:
                ans1 = (-b - math.sqrt(-D)*1j)/(2*a)
                ans2 = (-b + math.sqrt(-D)*1j)/(2*a)
                st.text(f"x = {str(ans1)} or x = {str(ans2)}")
            elif D == 0:
                ans = -b/(2*a)
                st.text(f"x = {str(ans)}")
            else:
                ans1 = (-b - math.sqrt(D))/(2*a)
                ans2 = (-b + math.sqrt(D))/(2*a)
                st.text(f"x = {str(ans1)} or x = {str(ans2)}")
        else:
            st.text("正しい数字を入力してください！")


st.markdown("### 座標平面上の三角形の面積")
st.markdown("座標平面上の3点(x1, y1), (x2, y2), (x3, y3)から成る三角形の面積を計算します。")

st.markdown("#### 使っている公式")
st.latex(r"""
area = \frac{|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|}{2}
""")

with st.form(key="triangle_area"):
    x1 = st.text_input("x1")
    y1 = st.text_input("y1")
    x2 = st.text_input("x2")
    y2 = st.text_input("y2")
    x3 = st.text_input("x3")
    y3 = st.text_input("y3")
    submit_btn_triangle_area = st.form_submit_button("Calculate")
    if submit_btn_triangle_area:
        if (x1 and x2 and x3 and y1 and y2 and y3 and
        is_num(x1) and is_num(x2) and is_num(x3) and is_num(y1) and is_num(y2) and is_num(y3)):
            x1, x2, x3 = float(x1), float(x2), float(x3)
            y1, y2, y3 = float(y1), float(y2), float(y3)
            area = get_triagle_area(x1, y1, x2, y2, x3, y3)
            st.text(f"面積: {area}")
        else:
            st.text("正しい数字を入力してください！")

st.markdown("### 座標平面上の四角形の面積")
st.text("座標平面上の4点(x1, y1), (x2, y2), (x3, y3), (x4, y4)から成る四角形の面積を計算します。\nただし上記4点の順番でたどったときに構成される四角形が対象です。")

st.markdown("### 使っている公式")
st.markdown("2つの三角形に分割して面積和を求めます。")
st.markdown("凹四角形の場合は(x3, y3)で凹部を作るとします。")
st.latex(r"""
area1  = \frac{|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|}{2}
""")
st.latex(r"""
area2 = \frac{|x_1(y_4 - y_3) + x_4(y_3 - y_1) + x_3(y_1 - y_4)|}{2}
""")
st.latex(r"""
area = area1 + area2
""")

with st.form(key="quadrilateral_area"):
    x1 = st.text_input("x1")
    y1 = st.text_input("y1")
    x2 = st.text_input("x2")
    y2 = st.text_input("y2")
    x3 = st.text_input("x3")
    y3 = st.text_input("y3")
    x4 = st.text_input("x4")
    y4 = st.text_input("y4")
    submit_btn_quadrilateral_area = st.form_submit_button("Calculate")
    if submit_btn_quadrilateral_area:
        if (x1 and x2 and x3 and x4 and y1 and y2 and y3 and y4
        and is_num(x1) and is_num(x2) and is_num(x3) and is_num(x4)
        and is_num(y1) and is_num(y2) and is_num(y3) and is_num(y4)):
            x1, x2, x3, x4 = float(x1), float(x2), float(x3), float(x4)
            y1, y2, y3, y4 = float(y1), float(y2), float(y3), float(y4)
            if is_valid_quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4):
                area1 = get_triagle_area(x1, y1, x2, y2, x3, y3)
                area2 = get_triagle_area(x1, y1, x3, y3, x4, y4)
                area3 = get_triagle_area(x2, y2, x3, y3, x4, y4)
                # concave
                if area1 + area2 == area3:
                    area = area1 + area2
                elif area1 + area3 == area2:
                    area = area1 + area3
                elif area2 + area3 == area1:
                    area = area2 + area3
                # convex
                else:
                    area = area1 + area2
                st.text(f"面積: {area}")
            else:
                st.text("正しい四角形の座標を入力してください！")
        else:
            st.text("正しい数字を入力してください！")
