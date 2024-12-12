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
    # st.header("작품 살펴보기")
    # options = st.selectbox(
    # '원하는 종류를 골라주세요',
    # ('윤아트', '문아트', '검색하기'))
    # if options=='윤아트':
    #     st.write("윤아트 작품 아카이브🎨")
    #     st.write("윤아트 작품 목록입니다")
    #     option = st.selectbox(
    #     '원하는 작품을 골라주세요',
    #     ('집으로가는길', '풍요로운오후', '3', '4', '5', '6', '7','8','9','10','11','12','13','14','15','16','17','18','19'))
    #     if option == '집으로가는길':
    #         st.image("Cozem/yoon_pictures/집으로가는길.jpeg", width=500)
    #         st.write("집으로 가는길")
    #         st.write("박덕 작가 작품")
    #         st.write("캔버스에 유화")
    #         st.write("2024년 작품")
    #         '''
    #         ### 집으로 가는 길
    #         #### 박덕 작가 작품
    #         | 작품명 | 작가 | 크기 | 작품 설명 | 
    #         | :---: | :---: | :---: | :---: | 
    #         | 집으로 가는 길 | 박덕 | 10호 | 작은 점으로 그림을 그리는 작가로 알려진 박 덕작가의 집으로가는길작은 행복과 희망이 가득한 집으로 향하는 길에 동글동글한 나무들은 소소한 행복이 모여 큰나무를 이룬다는 작가의 작품의도 입니다.집으로 가는길은 꿈과 희망이 가득한 행복한 길이 바랍니다.|
    #         '''
    #     elif option == '풍요로운오후':
    #         st.write("풍요로운 오후")
    #         st.image("Cozem/yoon_pictures/풍요로운오후.jpeg", width=500)
    #     elif option == '3':
    #         st.write("여심")
    #         st.image("Cozem/yoon_pictures/3.jpeg", width=500)
    #     elif option == '4':
    #         st.write("모정")
    #         st.image("Cozem/yoon_pictures/4.jpeg", width=500)    
    #     elif option == '5':
    #         st.write("모정")
    #         st.image("Cozem/yoon_pictures/5.jpeg", width=500)
    #     elif option == '6':
    #         st.write("동심")
    #         st.image("Cozem/yoon_pictures/6.jpeg", width=500)
    #     elif option == '7':
    #         st.write("통영항")
    #         st.image("Cozem/yoon_pictures/7.jpeg", width=500)    
    

    # elif options=='문아트':
    #     st.write("길드 사진 아카이브입니다.")
    #     col1, col2=st.columns(2)
    #     with col1:
    #         st.write("**리나와 한컷**")
    #         st.image("Cozem/image/guild1.jpg", use_column_width=True)
    #     with col2:
    #         st.write("**왕의 쉼터**")
    #         st.image("Cozem/image/guild2.jpg", use_column_width=True)
    #     col3, col4 = st.columns(2)
    #     with col3:
    #         st.write("**옷맞춤**")
    #         st.image("Cozem/image/guild3.jpg", use_column_width=True)
    #     with col4:
    #         st.write("**엘리넬**")
    #         st.image("Cozem/image/elinel.jpg", use_column_width=True)

    # elif options=='검색하기':
    #     # 검색 상자
    #     st.title("작품 검색 및 아카이브")
    #     search_query = st.text_input("검색어를 입력하세요", placeholder="작가, 작품명, 크기, 설명 등")

    #     # 검색 결과 처리
    #     if search_query:
    #         search_results = []
    #         for name, info in artworks.items():
    #             if any(search_query.lower() in str(value).lower() for value in info.values()):
    #                 search_results.append({"작품명": name, **info})

    #         if search_results:
    #             st.write(f"'{search_query}'에 대한 검색 결과:")
    #             for result in search_results:
    #                 st.image(result["이미지"], width=500)
    #                 st.write(f"**작품명**: {result['작품명']}")
    #                 st.write(f"**작가**: {result['작가']}")
    #                 st.write(f"**크기**: {result['크기']}")
    #                 st.write(f"**설명**: {result['설명']}")
    #                 st.write(f"**연도**: {result['연도']}")
    #                 st.write(f"**매체**: {result['매체']}")
    #                 st.write("---")
    #         else:
    #             st.write("검색 결과가 없습니다.")
    #     else:
    #         st.write("검색어를 입력하면 결과가 표시됩니다.")
            # import streamlit as st

        # 작품 정보 데이터
        artworks = {
            "집으로 가는 길": {
                "작가": "박덕",
                "크기": "10호",
                "설명": "작은 점으로 그림을 그리는 작가로 알려진 박덕 작가의 집으로가는길. "
                    "작은 행복과 희망이 가득한 집으로 향하는 길에 동글동글한 나무들은 "
                    "소소한 행복이 모여 큰나무를 이룬다는 작가의 작품의도입니다. "
                    "집으로 가는길은 꿈과 희망이 가득한 행복한 길이 바랍니다.",
                "이미지": "Cozem/yoon_pictures/집으로가는길.jpeg",
                "연도": "2024",
                "매체": "캔버스에 유화",
            },
            "풍요로운 오후": {
                "작가": "서정애",
                "크기": "8호",
                "설명": "캔버스 밑바탕에 석채를 깔아놓고 배경을 까칠까칠하게 만들어 채색을하는 석채화 작품입니다. 유화물감의 채도를 투명하게 최대한 섬세하고 곱게 칠하여 수채화처럼 작품이 표현되었습니다.꽃밭안에 탁자를 보며 멀리있는 집 마음의 여유와 사랑이 가득한 풍경을 보면서 마음이 풍요로워지는 작품입니다.",
                "이미지": "Cozem/yoon_pictures/풍요로운오후.jpeg",
                "연도": "2023",
                "매체": "캔버스에 유화",
            },
            "여심": {
                "작가": "김길상",
                "크기": "12호",
                "설명": "모래를 이용하여 바탕을 만들고 상상력을 동원하여 이상향 을 그려내는 서양화가.작품해석> 달항아리 속의 가족의 화목한 모습을 표현한 따뜻한 마음이 느껴지는 작품입니다.파랑새는 사랑의 전령사, 사랑과 행복을 상징하는 가족을 뜻하고, 붉은 해는 꿈과 이상향을 상징합니다.해바라기꽃은 가족의 온기, 사랑 등을 뜻합니다",
                "이미지": "Cozem/yoon_pictures/여심.jpeg",
                "연도": "모름",
                "매체": "캔버스(유화 and 돌가루),석채",
            },
            "모정_1": {
                "작가": "김길상",
                "작가" : "",
                "크기" : "",
                "설명" : "사실적인 형태를 왜곡시켜 두터운 형태의 선으로 함축함으로 중간색조의 톤에 조밀한 점의 점묘법을 쓰고 안료에 모래를 섞어 바탕을 검게 하고 그 위에 밝은 색을 덧칠하여 뚜렷한 형상의 윤곽선을 끌어내는 표현방법을 구축하고 있습니다.(네거티브방식-흑색선을 선명하게 남기는 방법. 음화, 반전을 뜻하는 말.)모정 - 엄마와 아이가 주고받는 눈빛의 온도가 느껴집니다. 엄마의 무한한 사랑과 넘치는 행복을 주고 싶은 부모의 소망을 그린 작품입니다.파랑새 사랑의 전령사 의미하고 태양은 꿈을 뜻합니다.솟떼는 천운을 상징합니다.",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화 and 돌가루),석채",
            },
            "모정_2": {
                "작가" : "김길상",
                "크기" : "",
                "설명" : "모정- 엄마와 아이가 주고받는 눈빛의 온도가 느껴집니다. 엄마의 무한한 사랑과 넘치는 행복을 주고 싶은 부모의 소망을 그린 작품입니다.따뜻한 엄마의 품의 온도를 느끼게 해주는 정말 좋은 작품입니다",
                "이미지" : "Cozem/yoon_pictures/모정_2.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화 and 돌가루),석채",
            },
            "동심": {
                "작가" : "김길상",
                "크기" : "",
                "설명" : "동심 우리에게 잊혀진 꿈을 심어주는 매력을 갖고 있습니다.인간의 본능을 아름답게 표현하여 추상적인 이미지로 옛날 어린 시절로 돌아가 꿈과 낭만이 가득한 시간을 갖게 해주는 작품입니다.",
                "이미지" : "Cozem/yoon_pictures/동심.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화 and 돌가루),석채",
            },
            "통영항": {
                "작가" : "김길상",
                "크기" : "",
                "설명" : "통영의 시원한 바다를 그린작품으로 선착장의 많은 배들이일렬로 정박되어 있는 모습이 외국과 비교해도 그경치가 뒤지지 않는 통영 나포리를 그린 작품입니다.바다의 물은 돈의 흐름을 뜻하여 내앞에 넓게 펼쳐진 바다는 내가 앞으로 벌게되는 돈을 뜻합니다. 넓은 바다일수록 재물이 많이 모인다는 풍수적의미를 갖고있는 좋은 작품입니다.",
                "이미지" : "Cozem/yoon_pictures/통영항.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화 and 돌가루),석채",
            },
            "산토리니_지중해에 보이는 마을": {
                "작가" : "이강필",
                "크기" : "15호",
                "설명" : "주로 외국 풍경을 그리는 작가나이프로 표현된 작품으로 산토리니의 시원한 바다와 마을의 아름다운풍경이 조화롭게 아주 잘 표현된 작품 산토리니작품의 매력은 계단식으로 이어지는 이색적인 집의 모습과 섬과 사이로 보이는 지중해의 시원한 바다의 모습을 표현한 청량한 색채감이 일품인 작품입니다.",
                "이미지" : "Cozem/yoon_pictures/산토리니_지중해에보이는마을.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화)",
            },
            "들꽃의합창(꽃의합창)": {
                "작가" : "박상호",
                "크기" : "10호",
                "설명" : "다채로운 꽃을 표현한 작품으로 정형화된 우리가 아는 꽃명이 아닌 들꽃과 야생화를 추상적으로 표현하고자 꽃명을 모른상태로 표현한 그림 작가님의 고유 표현기법으로 그림의 배경처리가 매우 독특합니다. 연두색과 화이트유화물감을 캔버스에 순차적으로 칠하고 테레핀오일을 떨어뜨려 두가지 색상이 서로 마르기전 오일과 함께 색이 녹으면서 번지는 표현기법입니다.",
                "이미지" : "Cozem/yoon_pictures/들꽃의합창(꽃의합창).jpeg",
                "연도" : "",
                "매체" : "10호",
            },
            "홍매화가활짝핀날": {
                "작가" : "박덕",
                "크기" : "40호",
                "설명" : "작은 점으로 물방울처럼 큰점 작은점을 찍어서 그림을 완성하는 점묘법 채색도 점으로 표현하고 그림의 원근 밝고 어둠 명암도 점으로 표현하는 한국에서 점묘법으로 작품을 그리신지 40년이 넘으신 작가님입니다. 홍매화는 사랑과 사랑의 고백을 의미하는데 가족이 지나가는 모든기 날이 사랑이 되고 항상 꽃길만 걷자는 작가의 의미를 담고 있습니다.",
                "이미지" : "Cozem/yoon_pictures/홍매화가활짝핀날.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화, 점묘법)",
            },
            "행복이가득한나무": {
                "작가" : "서정애",
                "크기" : "40호",
                "설명" : "꽃밭과 아름다운 풍경을 주로 그리는 작가님 세필붓으로 섬세하게 그림의 마무리에 라인을 정교화게 다시 그리는 꼼꼼한 작품의 표현력이 일품인 서정적 따뜻한 화풍의 최고의 작가 이십니다. 행복이 가득 담긴 자작나무를 섬세하게 표현한 작품으로 나무 뒤에 보이는 작은 집속으로 행복이 넘치는 가족이 되길 바라는 작가의 작품의도가 보입니다.",
                "이미지" : "Cozem/yoon_pictures/행복이가득한나무.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "빨강사과나무": {
                "작가" : "이사연",
                "크기" : "10호",
                "설명" : "사과나무의 실제 모습을 스케치하여 표현한 사실화작품 빨강사과는 계약과 결실을 뜻하는 과일로 나에게 오는 좋은계약과 내게 뜻하고자하는 관직의 오르는 승진의 의미를 담고있습니다. 과일이 열리고 빨갛게 익어가는건 좋은 결실이 나에게 온다는 뜻도 있습니다. 세필붓으로 사과의 물방울까지 섬세하게 그려낸 작품입니다.",
                "이미지" : "Cozem/yoon_pictures/빨강사과나무.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화)",
            },
            "정원에서(그림작성)아름다운정원(설명표)": {
                "작가" : "김두식",
                "크기" : "12호",
                "설명" : "캔버스 밑바탕을 수성 코킹 재료로 불큐칙하게 표면을 질감처리를 한후 약5일간 건조후 셋소로 하얗게 유화작품하기전 베이스작업을 합니다. 그후에 정원에서의 아름다운 테이블과 꽃의 조화 그리고 멋찐 강가의 풍경 동화처럼 그려낸 작품입니다. 섬세한 꽃의 표현도 일품이지만 꼭 벽지에 그린듯한 캔버스의 밑작업이 작가고유의 표현기법으로 정말 힘들여 그린작품 입니다.",
                "이미지" : "Cozem/yoon_pictures/정원에서(그림작성)아름다운정원(설명표).jpeg",
                "연도" : "",
                "매체" : "캔버스(유화)",
            },
            "바구니가득빨강사과": {
                "작가" : "최진홍",
                "크기" : "20호",
                "설명" : "2023년6월 작고하신 최진홍 작가님의 유작입니다. 사실적인 묘사로 사과를 그리셨지만 그림체가 너무 부드럽고 풀밭위에 바구니 가득 담길 탐스런 사과의 모습이 예쁘고 아름답습니다. 초록사과가 빨강사과로 익어가듯 시간이 흐름에따라 일의 진행에 결과가 나타나고 결실이 된다고 하여 사업을 하는 분의 대표실에 사과를 걸어두면 일의성과 결과 결실이 맺힌다고하여 사업운에 대박 기운이 있는 사과그림입니다.",
                "이미지" : "Cozem/yoon_pictures/바구니가득빨강사과.jpeg",
                "연도" : "",
                "매체" : "캔버스(유화)",
            },
            "야생화": {
                "작가" : "박상호",
                "크기" : "10호",
                "설명" : "시간의 차이에서 오는 색감이 서로 다른 빛으로 다채로운 색으로 변하는 같은 공간에서 시간의 흐름의 격차를 두고 표현된 실험적 정물화입니다. 꽃뒤에 커튼색 표현이 시간에 따라 보랏빛과 푸른빛으로 반사되어 보이고 꽃병도 빛의 반사로 서로 다른 각도에서 다른 빛으로 색을 표현한 굉장히 생각을 많이 하며 그린 작품입니다.",
                "이미지" : "Cozem/yoon_pictures/야생화.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "여유있는하루": {
                "작가" : "박상호",
                "크기" : "10호",
                "설명" : "애견과 동행하는 카페에 앉아서 서로 사랑하는 강아지와 마주보고 차를 마시는 여인의 여유를 작품한 만화같은 일러스트 작품입니다. 쇼파와 탁자 창밖의 은행나무 모든 그림의 선과 색채감이 지나가는 시선을 다시 잡을정도로 잘표현된 작품입니다. 행복과 여유는 멀리있는게 아닌 삶의 휴식과 쉼속에서 찾아오는걸 알려주고 싶은 작가의 작품입니다.",
                "이미지" : "Cozem/yoon_pictures/여유있는하루.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "화려한날들(화려한인생)": {
                "작가" : "박상호",
                "크기" : "10호",
                "설명" : "다채로운 꽃을 표현한 작품으로 정형화된 우리가 아는 꽃명이 아닌 들꽃과 야생화를 추상적으로 표현하고자 꽃명을 모른상태로 표현한 그림 작가님의 고유 표현기법으로 그림의 배경처리가 매우 독특합니다. 연두색과 화이트유화물감을 캔버스에 순차적으로 칠하고 테레핀오일을 떨어뜨려 두가지 색상이 서로 마르기전 오일과 함께 색이 녹으면서 번지는 표현기법입니다.",
                "이미지" : "Cozem/yoon_pictures/화려한날들(화려한인생).jpeg",
                "연도" : "",
                "매체" : "",
            },
            "화려한외출(명동거리)": {
                "작가" : "박상호",
                "크기" : "10호",
                "설명" : "비가 내리는 명동에 퇴근하며 서로 오가는 사람들의 모습을 보며 카페에 앉아 스케치를 하고 자연스럽게 작품을 완성한 그림 높은 건물 사이로 걸어가는 사람과 마주하는 차들 빗방울로 바닥에 반사되는 조명들이 서로의 빛이 되어 아름다운 색감을 연출하는 회화적인 작품입니다.",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "2020년",
                "매체" : "",
            },
            "행복이가득한나무": {
                "작가" : "서정애",
                "크기" : "10호",
                "설명" : "동화처럼 아름다운 작품을 하는 서정애 작가의 행복이 가득한 나무 그림을 자세히 보면 꽃씨를 뿌리고 있는여인과 나무아래 등을 기대고 휴식을 취하고 있는 여인이 있습니다. 평화롭고 아름다운 동산에서 여유와 평온한 오후를 즐기는 모습이 마음까지 안정과 행복이 가득차게 해줍니다.",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "2024",
                "매체" : "캔버스(유화)",
            },
            "HappyTree": {
                "작가" : "서정애",
                "크기" : "40호",
                "설명" : "2019년 프랑스 여행중 루브르 박물관에서 여러 작가의 작품을 관람후 좋은 감명을 받은 작가, 한국에 돌아가면 나도 이런 작가들처럼 내그림을통해 행복한 느낌을 받았으면 좋겠다 는 생각을 하고 돌아오는길에 노트에 간단한 스케치를 하였습니다. 처음엔 아주 작은 캔버스에 행복이 가득담긴 나무를 표현하였습니다. 그후에 나무아래 집도 추가해서 그려보고 또다시 나비도 추가해서 그리면서 여러해에 걸쳐 다듬고다듬어 완성된 작품입니다. 정교하게 표현된 집이 모여 마을을 이루고 있는 그림속 아주 큰 나무는 "해피트리" 나무입니다. 나무 가운데 포도송이(행복의 결과)와 나비 (사랑의신저) 하트열매 (사랑의표현)가 보입니다. 서 작가님의 작품속에는 나무에 기대앉은 사람이 자주 등장하는데 나무는 내가 믿고 기대거나 의지하는 대상을 뜻하고 그로인해 안식을 느끼는 상징성을 의미합니다. 이그림을 통해 평안과 안식을 느끼시길 바랍니다..",
                "이미지" : "Cozem/yoon_pictures/HappyTree.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },
            "모정1": {
                "작가" : "",
                "크기" : "",
                "설명" : "",
                "이미지" : "Cozem/yoon_pictures/모정_1.jpeg",
                "연도" : "",
                "매체" : "",
            },


            # 다른 작품 정보를 추가할 수 있습니다.
        }

        # 페이지 헤더
        st.header("작품 살펴보기")

        # 옵션 선택
        options = st.selectbox(
            '원하는 종류를 골라주세요',
            ('윤아트', '문아트', '검색하기')
        )

        if options == '윤아트':
            st.write("윤아트 작품 아카이브🎨")
            st.write("윤아트 작품 목록입니다")
            option = st.selectbox(
                '원하는 작품을 골라주세요',
                tuple(artworks.keys())
            )

            # 검색어 입력
            search_query = st.text_input("검색어를 입력하세요", placeholder="작가, 작품명, 크기, 설명 등")

            if search_query:
                search_results = []
                for name, info in artworks.items():
                    if any(search_query.lower() in str(value).lower() for value in info.values()):
                        search_results.append({"작품명": name, **info})

                if search_results:
                    st.write(f"'{search_query}'에 대한 검색 결과:")
                    for result in search_results:
                        st.image(result["이미지"], width=500)
                        st.write(f"**작품명**: {result['작품명']}")
                        st.write(f"**작가**: {result['작가']}")
                        st.write(f"**크기**: {result['크기']}")
                        st.write(f"**설명**: {result['설명']}")
                        st.write(f"**연도**: {result['연도']}")
                        st.write(f"**매체**: {result['매체']}")
                        st.write("---")
                else:
                    st.write("검색 결과가 없습니다.")
            else:
                # 검색어가 없을 때 선택된 작품 표시
                artwork = artworks[option]
                st.image(artwork["이미지"], width=500)
                st.write(f"**작품명**: {option}")
                st.write(f"**작가**: {artwork['작가']}")
                st.write(f"**크기**: {artwork['크기']}")
                st.write(f"**설명**: {artwork['설명']}")
                st.write(f"**연도**: {artwork['연도']}")
                st.write(f"**매체**: {artwork['매체']}")

        elif options == '문아트':
            st.write("문아트 사진 아카이브입니다.")
            col1, col2 = st.columns(2)
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

        elif options == '검색하기':
            st.title("작품 검색 및 아카이브")

            # 검색어 입력
            search_query = st.text_input("검색어를 입력하세요", placeholder="작가, 작품명, 크기, 설명 등")

            if search_query:
                search_results = []
                for name, info in artworks.items():
                    if any(search_query.lower() in str(value).lower() for value in info.values()):
                        search_results.append({"작품명": name, **info})

                if search_results:
                    st.write(f"'{search_query}'에 대한 검색 결과:")
                    for result in search_results:
                        st.image(result["이미지"], width=500)
                        st.write(f"**작품명**: {result['작품명']}")
                        st.write(f"**작가**: {result['작가']}")
                        st.write(f"**크기**: {result['크기']}")
                        st.write(f"**설명**: {result['설명']}")
                        st.write(f"**연도**: {result['연도']}")
                        st.write(f"**매체**: {result['매체']}")
                        st.write("---")
                else:
                    st.write("검색 결과가 없습니다.")
            else:
                st.write("검색어를 입력하면 결과가 표시됩니다.")


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