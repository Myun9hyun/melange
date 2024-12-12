import random
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import joblib
import seaborn as sns
from streamlit_option_menu import option_menu
import os
import openpyxl
from io import BytesIO
import base64
import datetime
import PyPDF2
import fitz
from bs4 import BeautifulSoup


st.set_page_config(page_title="Melange", page_icon=":gem:", layout="wide")
password = 1234
password_test = "1234"

image = Image.open("Cozem/image/jewelry_banner.png")

# # streamlit에 이미지 표시
st.image(image, use_column_width=True)

with st.sidebar:
    choice = option_menu("Menu", ["메인페이지", "길드페이지","작품페이지","피드백 남기기"],
                         icons=['house', 'bi bi-emoji-smile', 'bi bi-robot', 'bi bi-palette','bi bi-archive', 'bi bi-card-text'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#73B4EC"},
    }
    )

    data = {
        'Name': ['💾Google Docs','📫문의방', '📷Instagram'],
        'Link': ['[![GitHub](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://onedrive.live.com/edit.aspx?resid=221CE48C87202DCA!2450&ithint=file%2cxlsx&authkey=!ADKQOeLCxzQp_5o)',
         '[![GitHub](https://img.shields.io/badge/Kakao%20talk-FFBE00?style=for-the-badge&logo=kakaotalk&logoColor=white)](https://open.kakao.com/o/gUmZwuzd)',
         '[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://open.kakao.com/o/gUmZwuzd)']

    }
    df = pd.DataFrame(data)
    # st.sidebar.dataframe(df)
    st.write(df.to_markdown(index=False))
    # choice = st.sidebar.selectbox("메뉴를 선택해주세요", menu)
    bgms = ["나린","도원경", "차원의균열", "첫번째동행", "에오스탑외부", "오시리아대륙항해", "아쿠아리움필드",
                "오디움_신의창", "강림_괴력난신" , "아델의맹세", "아쉴롬_일리움", "악몽의시계탑", "시간의신전"]
    bgm = st.selectbox("🔈원하시는 배경음악을 골라주세용", bgms)
    st.write("음악은 다른 기능을 사용하면 정지됩니다.")


# 선택된 메뉴에 따라 다른 탭 출력
if choice == "메인페이지":
    st.header("MELANGE")
    st.write("### 멜랑주 화성점에 방문하신것을 환영합니다😊")
      
    st.write()
    '''
    ##### 멜랑주 화성점
    * 경기도 화성시
    * 혜경궁베이커리 내 수빈관 위치
    * 경기 화성시 정남면 보통내길 205-28
    '''

elif choice == "길드페이지":
    tab1, tab2= st.tabs(["😎Manager", "📋Rules"])
    with tab1:
        st.header("😎Manager")
        st.write()
        # col1, col2 = st.columns(2)
        # with col1:
        '''
        ---
        ### 길드 간부진 💪
        | 직책 | 이름  | 직업 | 간부진 1:1오픈채팅 | 메지지 프로필 |
        | :---: | :---: | :---: | :---: | :---:|
        | 길마👑 | 뱌닢 | 나이트로드 | [![Colab](https://img.shields.io/badge/kakaotalk-뱌닢-yellow)](https://open.kakao.com/o/spPPOAhc) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/뱌닢) |
        | 부마 | 릎샴  | 아크 | [![Colab](https://img.shields.io/badge/kakaotalk-릎샴-yellow)](https://open.kakao.com/o/s0FeFIee) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/릎샴) |
        | 부마 | 둥둥향 | 캐논슈터 | [![Colab](https://img.shields.io/badge/kakaotalk-둥둥향-yellow)](https://open.kakao.com/o/sl6WBJUc) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/둥둥향) |
        | 부마 | 영래곰  | 듀얼블레이드 | [![Colab](https://img.shields.io/badge/kakaotalk-영래곰-yellow)](https://open.kakao.com/o/sBK5y3md) |[![maple](https://img.shields.io/badge/maplestory%20-%2314354C.svg?style=for-the-badge&logo=maplestory&logoColor=white)](https://maple.gg/u/영래곰) |
        '''
# pdf_path = "Cozem/rule/아기자기_길드_규정_2023.pdf"
        # with col2:
        #     st.image("Cozem/image/elinel.jpg", use_column_width=True)
    with tab2:
        st.header("📋길드 규정집📋")
        # st.image("Cozem/read_me_image/guide_new_1.jpg", use_column_width=True)
        # st.image("Cozem/read_me_image/guide_new_2.jpg", use_column_width=True)
        st.image("Cozem/read_me_image/rule_new_1.jpg", use_column_width=True)
        st.image("Cozem/read_me_image/rule_new_2.jpg", use_column_width=True)



elif choice == "작품페이지":
    st.header("작품 살펴보기")
    options = st.selectbox(
    '원하는 종류를 골라주세요',
    ('윤아트', '문아트'))
    if options=='윤아트':
        st.write("윤아트 작품 아카이브🎨")
        st.write("윤아트 작품 목록입니다")
        option = st.selectbox(
        '원하는 작품을 골라주세요',
        ('1', '2', '3', '4', '5', '6', '7','8','9','10','11','12','13','14','15','16','17','18','19'))
        if option == '1':
            st.write("집으로 가는길")
            st.image("Cozem/poster/1.jpeg", width=500)
        elif option == '2':
            st.write("풍요로운 오후")
            st.image("Cozem/poster/orange.jpg", width=500)
        elif option == '3':
            st.write("여심")
            st.image("Cozem/poster/red.jpg", width=500)
        elif option == '4':
            st.write("모정")
            st.image("Cozem/poster/blue.jpg", width=500)    
        elif option == '5':
            st.write("모정")
            st.image("Cozem/poster/odium.jpg", width=500)
        elif option == '6':
            st.write("동심")
            st.image("Cozem/poster/gray.jpg", width=500)
        elif option == '7':
            st.write("통영항")
            st.image("Cozem/poster/spring.jpg", width=500)    
    elif options=='문아트':
        st.write("길드 사진 아카이브입니다.")
        col1, col2=st.columns(2)
        with col1:
            st.write("**리나와 한컷**")
            st.image("Cozem/image/guild1.jpg", use_column_width=True)
        with col2:
            st.write("**왕의 쉼터**")
            st.image("Cozem/image/guild2.jpg", use_column_width=True)
        col3, col4 = st.columns(2)
        with col3:
            st.write("**옷맞춤**")
            st.image("Cozem/image/guild3.jpg", use_column_width=True)
        with col4:
            st.write("**엘리넬**")
            st.image("Cozem/image/elinel.jpg", use_column_width=True)

elif choice == "피드백 남기기":
    st.header("둥둥에게 피드백을 남겨주세요!")
    FILE_PATH10 = 'data10.csv'
    options = ["피드백 남기기➕", "피드백 내용 조회🔎", "피드백 내용 삭제✂", "피드백 초기화💣" ]
    option = st.selectbox("기능 선택", options, key='select3')
    # 파일에서 데이터 불러오기
    def load_data10():
        try: 
            data10 = pd.read_csv(FILE_PATH10)
        except FileNotFoundError:
            data10 = pd.DataFrame(columns=['Name', 'Comment', 'Day'])
        return data10

    # 데이터를 파일에 저장하기
    def save_data10(data10):
        data10.to_csv(FILE_PATH10, index=False)

    # 데이터 초기화 함수
    def clear_data10():
        global data10
        data10 = pd.DataFrame(columns=['Name', 'Comment', 'Day'])
        # 파일 삭제
        os.remove(FILE_PATH10)

    # 데이터 삭제 함수
    def delete_data10(row_index):
        global data10
        data10 = data10.drop(index=row_index).reset_index(drop=True)

    # 불러온 데이터를 전역 변수로 저장
    data10 = load_data10()
    def add_data10(name, comment, day):
        global data10
        # data10 = data10.append({
        # data10 = data10.concat({
        #     'Name': name, 
        #     'Comment' : comment,
        #     'Day' : day

        # }, ignore_index=True)
        new_data10 = pd.DataFrame({'Name': [name], 'Comment': [comment], 'Day': [day]})
        data10 = pd.concat([data10, new_data10], ignore_index=True)
    def main():
        if option == "피드백 내용 삭제✂":
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
            password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0, key='pass14')
            if password_input == password:
                st.success('접근을 허용합니다')
                st.write(data10[['Name','Comment', 'Day']])
                row_index = st.number_input('삭제하고 싶은 데이터의 번호를 입력해주세요', min_value=0, max_value=data10.shape[0]-1)
                st.write("Enter를 입력하면 삭제됩니다.")
                if st.button('데이터 삭제'):
                    # 해당 행이 존재할 경우, 행을 삭제
                    if row_index >= 0 and row_index < data10.shape[0]:
                        delete_data10(row_index)
                        save_data10(data10)  # 데이터를 파일에 저장
                        st.success('입력하신 행이 삭제되었습니다.')
            else:
                st.warning('비밀번호가 틀렸습니다.')
        elif option == "피드백 남기기➕":
            name = st.text_input("피드백 하시는 분의 이름을 입력해주세요")
            comment = st.text_input("피드백 내용을 적어주세요")
            day = st.date_input(
                "피드백 남기는 날짜를 설정해주세요",
                datetime.date.today())
            if st.button('피드백 남기기'):
                add_data10(name, comment, day)
                save_data10(data10)
                st.success("피드백 감사합니다!!ヾ(•ω•`)o")

        elif option == "피드백 내용 조회🔎":
            if st.button('피드백 확인'):
                st.write("피드백 내용입니다.")
                st.write(data10)

        elif option == "피드백 초기화💣":
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
            password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0,key='pass16')
            if password_input == password:
                st.success('접근을 허용합니다')
                # 데이터 전부 삭제
                st.write("⚠️버튼을 누르면 데이터가 다 날아갑니다!⚠️")
                st.write("⚠️신중하게 누르세요!!⚠️")
                if st.button('초기화'):
                    clear_data10()
                    st.warning('초기화 되었습니다')
            else:
                st.warning('비밀번호가 틀렸습니다.')
    if __name__ == "__main__":
        main()