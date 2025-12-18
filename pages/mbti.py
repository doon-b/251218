import streamlit as st

# 1. 데이터 구성 (MBTI별 진로 2개와 추천 도서 1권)
mbti_data = {
    "ISTJ": {"jobs": ["회계사", "금융 분석가"], "book": "지적 대화를 위한 넓고 얕은 지식 (채사장)"},
    "ISFJ": {"jobs": ["사회복지사", "초등교사"], "book": "나미야 잡화점의 기적 (히가시노 게이코)"},
    "INFJ": {"jobs": ["상담심리사", "작가"], "book": "데미안 (헤르만 헤세)"},
    "INTJ": {"jobs": ["소프트웨어 개발자", "전략 기획자"], "book": "사피엔스 (유발 하라리)"},
    "ISTP": {"jobs": ["엔지니어", "데이터 분석가"], "book": "월든 (헨리 데이비드 소로)"},
    "ISFP": {"jobs": ["디자이너", "예술가"], "book": "어린 왕자 (생텍쥐페리)"},
    "INFP": {"jobs": ["예술 치료사", "에디터"], "book": "호밀밭의 파수꾼 (J.D. 샐린저)"},
    "INTP": {"jobs": ["연구원", "철학자"], "book": "코스모스 (칼 세이건)"},
    "ESTP": {"jobs": ["사업가", "기자"], "book": "부의 추월차선 (엠제이 드마코)"},
    "ESFP": {"jobs": ["연예인", "홍보 전문가"], "book": "그리스인 조르바 (니코스 카잔차키스)"},
    "ENFP": {"jobs": ["크리에이티브 디렉터", "홍보 컨설턴트"], "book": "연금술사 (파울로 코엘료)"},
    "ENTP": {"jobs": ["발명가", "벤처 사업가"], "book": "생각에 관한 생각 (대니얼 카너먼)"},
    "ESTJ": {"jobs": ["경영자", "군 장교"], "book": "원칙 (레이 달리오)"},
    "ESFJ": {"jobs": ["호텔 지배인", "승무원"], "book": "데일 카네기 인간관계론 (데일 카네기)"},
    "ENFJ": {"jobs": ["아나운서", "정치인"], "book": "모리와 함께한 화요일 (미치 앨봄)"},
    "ENTJ": {"jobs": ["경영 컨설턴트", "변호사"], "book": "손자병법 (손무)"},
}

# 2. 웹 앱 인터페이스 구성
st.set_page_config(page_title="MBTI 진로 & 도서 추천", page_icon="📚")

st.title("✨ MBTI 맞춤 진로 & 도서 추천")
st.write("자신의 MBTI를 선택하면 어울리는 진로와 책을 추천해 드립니다.")

# 3. 사용자 입력 (선택 상자)
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_list)

# 4. 결과 출력
if selected_mbti:
    result = mbti_data[selected_mbti]
    
    st.divider()
    
    st.subheader(f"🔍 {selected_mbti} 유형을 위한 추천")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("**🚀 추천 진로**")
        for job in result["jobs"]:
            st.write(f"- {job}")
            
    with col2:
        st.success("**📖 추천 도서**")
        st.write(f"_{result['book']}_")

    st.balloons() # 축하 효과
