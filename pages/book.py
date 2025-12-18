import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 세계문학 추천소",
    page_icon="📚",
    layout="centered"
)

# ---------------------------------------------------------
# 데이터베이스 (MBTI별 추천 도서, 이유, ISBN)
# 이미지 출처: Open Library Cover API (별도 키 필요 없음)
# ---------------------------------------------------------
mbti_books = {
    "ISTJ": {
        "mbti_name": "청렴결백한 논리주의자",
        "title": "1984",
        "author": "조지 오웰",
        "reason": "사실과 논리, 질서를 중시하는 ISTJ에게 추천합니다. 전체주의 사회의 모순과 그 속에서 진실을 찾으려는 주인공의 고군분투는 당신의 분석적인 성향을 자극할 것입니다.",
        "isbn": "9780451524935"
    },
    "ISFJ": {
        "mbti_name": "용감한 수호자",
        "title": "앵무새 죽이기",
        "author": "하퍼 리",
        "reason": "타인을 향한 따뜻한 마음과 도덕적 책임감이 강한 ISFJ에게, 정의와 양심, 그리고 약자에 대한 보호를 다룬 이 책은 깊은 울림을 줄 것입니다.",
        "isbn": "9780061120084"
    },
    "INFJ": {
        "mbti_name": "통찰력 있는 선지자",
        "title": "제인 에어",
        "author": "샬럿 브론테",
        "reason": "내면의 신념이 확고하고 이상을 추구하는 INFJ에게, 억압적인 환경 속에서도 자존감을 지키며 주체적인 삶을 개척해 나가는 제인의 이야기는 큰 영감이 될 것입니다.",
        "isbn": "9780141441146"
    },
    "INTJ": {
        "mbti_name": "용의주도한 전략가",
        "title": "이방인",
        "author": "알베르 카뮈",
        "reason": "독립적이고 논리적이며 관습에 얽매이지 않는 INTJ에게, 실존과 부조리에 대해 냉철하게 질문을 던지는 뫼르소의 이야기는 지적 흥미를 불러일으킬 것입니다.",
        "isbn": "9780679720201"
    },
    "ISTP": {
        "mbti_name": "만능 재주꾼",
        "title": "노인과 바다",
        "author": "어니스트 헤밍웨이",
        "reason": "군더더기 없는 실용주의와 행동을 중시하는 ISTP에게, 거대한 자연에 맞서 묵묵히 자신의 기술과 의지로 사투를 벌이는 노인의 모습은 강렬한 인상을 남길 것입니다.",
        "isbn": "9780684801223"
    },
    "ISFP": {
        "mbti_name": "호기심 많은 예술가",
        "title": "어린 왕자",
        "author": "앙투안 드 생텍쥐페리",
        "reason": "감수성이 풍부하고 현재의 아름다움을 즐길 줄 아는 ISFP에게, 순수한 시선으로 세상을 바라보며 진정한 관계의 의미를 묻는 이 책은 마음의 안식처가 될 것입니다.",
        "isbn": "9780156012195"
    },
    "INFP": {
        "mbti_name": "열정적인 중재자",
        "title": "데미안",
        "author": "헤르만 헤세",
        "reason": "자아 탐구와 내면의 성장을 중요시하는 INFP에게, '알'을 깨고 나와 진정한 자신을 찾아가는 싱클레어의 여정은 마치 자신의 이야기처럼 다가올 것입니다.",
        "isbn": "9780143106784"
    },
    "INTP": {
        "mbti_name": "논리적인 사색가",
        "title": "이상한 나라의 앨리스",
        "author": "루이스 캐럴",
        "reason": "지적 호기심이 넘치고 추상적인 개념을 즐기는 INTP에게, 언어 유희와 논리적 수수께끼로 가득 찬 이 기발하고 환상적인 세계는 최고의 놀이터입니다.",
        "isbn": "9780141439761"
    },
    "ESTP": {
        "mbti_name": "모험을 즐기는 사업가",
        "title": "위대한 개츠비",
        "author": "F. 스콧 피츠제럴드",
        "reason": "행동력이 넘치고 현실 감각이 뛰어난 ESTP에게, 화려한 재즈 시대의 욕망과 성취, 그리고 그 이면의 덧없음을 다룬 이 소설은 흥미진진하게 읽힐 것입니다.",
        "isbn": "9780743273565"
    },
    "ESFP": {
        "mbti_name": "자유로운 영혼의 연예인",
        "title": "마담 보바리",
        "author": "귀스타브 플로베르",
        "reason": "열정적이고 미적 감각이 뛰어난 ESFP에게, 권태로운 일상을 거부하고 낭만과 사랑을 쫓아 불꽃처럼 살다 간 엠마의 이야기는 깊은 공감을 줄 수 있습니다.",
        "isbn": "9780140449129"
    },
    "ENFP": {
        "mbti_name": "재기발랄한 활동가",
        "title": "빨간 머리 앤",
        "author": "루시 모드 몽고메리",
        "reason": "상상력이 풍부하고 긍정적인 에너지를 가진 ENFP에게, 낭만적인 상상으로 세상을 아름답게 물들이며 사람들의 마음을 여는 앤은 최고의 소울메이트입니다.",
        "isbn": "9780141321592"
    },
    "ENTP": {
        "mbti_name": "뜨거운 논쟁을 즐기는 변론가",
        "title": "돈 키호테",
        "author": "미겔 데 세르반테스",
        "reason": "기존 체제에 도전하고 새로운 가능성을 보는 ENTP에게, 남들은 미쳤다고 해도 자신의 신념을 향해 거침없이 돌진하는 돈 키호테는 유쾌한 동지애를 느끼게 합니다.",
        "isbn": "9780060934347"
    },
    "ESTJ": {
        "mbti_name": "엄격한 관리자",
        "title": "동물 농장",
        "author": "조지 오웰",
        "reason": "현실적이고 조직 체계를 중시하는 ESTJ에게, 잘못된 리더십과 시스템이 어떻게 조직을 부패시키는지 날카롭게 풍자한 이 우화는 깊은 통찰을 제공합니다.",
        "isbn": "9780451526342"
    },
    "ESFJ": {
        "mbti_name": "사교적인 외교관",
        "title": "작은 아씨들",
        "author": "루이자 메이 올콧",
        "reason": "타인과의 조화와 공동체를 소중히 여기는 ESFJ에게, 네 자매가 서로를 보듬으며 성장해가는 따뜻한 가족애와 사랑 이야기는 큰 감동을 선사할 것입니다.",
        "isbn": "9780147514011"
    },
    "ENFJ": {
        "mbti_name": "정의로운 사회운동가",
        "title": "레미제라블",
        "author": "빅토르 위고",
        "reason": "사람에 대한 믿음과 인류애를 가진 ENFJ에게, 법보다 위대한 사랑과 용서, 그리고 사회 정의를 향한 장발장의 숭고한 여정은 가슴을 뜨겁게 할 것입니다.",
        "isbn": "9780451419439"
    },
    "ENTJ": {
        "mbti_name": "대담한 통솔자",
        "title": "군주론",
        "author": "니콜로 마키아벨리",
        "reason": "목표 지향적이고 전략적인 리더십을 가진 ENTJ에게, 냉철한 현실 인식과 권력의 속성을 다룬 이 고전은 리더로서의 통찰력을 한층 더 날카롭게 해줄 것입니다.",
        "isbn": "9780553212270"
    }
}

# ---------------------------------------------------------
# UI 구성
# ---------------------------------------------------------

st.title("📚 당신을 위한 세계문학 처방전")
st.markdown("""
당신의 **MBTI**를 선택해주세요.  
성향에 딱 맞는 세계문학 고전 한 권을 표지와 함께 추천해 드립니다.
""")

st.divider() # 구분선

# 1. MBTI 선택 입력
# selectbox를 사용하여 MBTI 선택
col1, col2 = st.columns([1, 2]) # 레이아웃 조정

with col1:
    st.subheader("MBTI 선택")
    option = st.selectbox(
        '당신의 MBTI 유형은 무엇인가요?',
        list(mbti_books.keys())
    )
    
    # 추천하기 버튼
    if st.button('추천 도서 확인하기 🔍', type="primary"):
        st.session_state['selected_mbti'] = option
    else:
        # 처음 실행 시나 버튼 누르기 전 상태
        if 'selected_mbti' not in st.session_state:
             st.session_state['selected_mbti'] = None

# 2. 결과 출력
if st.session_state['selected_mbti']:
    mbti = st.session_state['selected_mbti']
    book_info = mbti_books[mbti]
    
    st.divider()
    
    # 결과 보여주는 컨테이너
    with st.container():
        st.markdown(f"### 🎯 {mbti} ({book_info['mbti_name']})를 위한 추천")
        
        res_col1, res_col2 = st.columns([1, 1.5])
        
        with res_col1:
            # Open Library Covers API를 사용하여 이미지 표시
            # L: Large size
            image_url = f"https://covers.openlibrary.org/b/isbn/{book_info['isbn']}-L.jpg"
            st.image(image_url, caption=f"{book_info['title']} - {book_info['author']}", use_container_width=True)
            
        with res_col2:
            st.subheader(f"📖 {book_info['title']}")
            st.markdown(f"**저자**: {book_info['author']}")
            st.success("💡 **추천 이유**")
            st.write(book_info['reason'])
            
            st.info("""
            *이 추천은 MBTI의 일반적인 성향을 바탕으로 선정되었습니다.*
            """)
