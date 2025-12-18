import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 문학 캐릭터 추천",
    page_icon="📚",
    layout="centered"
)

# MBTI 데이터베이스 (16가지 유형 정의)
# 이미지 URL은 예시로 책 제목이 들어간 이미지를 자동 생성합니다. 
# 실제 사용 시에는 실제 표지 이미지 URL(예: 위키미디어, S3 등)로 교체하시면 됩니다.
mbti_data = {
    "ISTJ": {
        "character": "미스터 다아시 (Mr. Darcy)",
        "book": "오만과 편견 (Pride and Prejudice)",
        "desc": "당신은 책임감이 강하고 현실적이며, 전통과 질서를 중시합니다. 처음에는 차가워 보일 수 있지만, 내면에는 깊은 신의와 성실함을 간직한 '다아시'와 꼭 닮았네요.",
        "color": "#4298B4"
    },
    "ISFJ": {
        "character": "닉 캐러웨이 (Nick Carraway)",
        "book": "위대한 개츠비 (The Great Gatsby)",
        "desc": "타인에게 헌신적이고 조용히 관찰하며 주변을 챙기는 당신. 화려한 사건 속에서도 중심을 잃지 않고 차분하게 이야기를 서술해 나가는 '닉'과 비슷합니다.",
        "color": "#4298B4"
    },
    "INFJ": {
        "character": "제인 에어 (Jane Eyre)",
        "book": "제인 에어 (Jane Eyre)",
        "desc": "조용하지만 마음속에 뜨거운 열정과 확고한 신념을 가진 당신. 도덕적 가치를 중시하고 자신의 운명을 스스로 개척해 나가는 통찰력 있는 '제인'을 추천합니다.",
        "color": "#33A474"
    },
    "INTJ": {
        "character": "로스콜니코프 (Raskolnikov)",
        "book": "죄와 벌 (Crime and Punishment)",
        "desc": "논리적이고 분석적이며, 자신만의 철학이 확고한 당신. 때로는 너무 깊은 고뇌에 빠지기도 하지만, 세상을 꿰뚫어 보는 날카로운 지성을 가진 인물입니다.",
        "color": "#88619A"
    },
    "ISTP": {
        "character": "셜록 홈즈 (Sherlock Holmes)",
        "book": "셜록 홈즈 (Sherlock Holmes)",
        "desc": "뛰어난 관찰력과 논리적 사고로 문제를 해결하는 당신. 감정보다는 사실에 집중하며, 도구를 다루는 데 능숙한 천재 탐정 '셜록'이 당신의 소울메이트입니다.",
        "color": "#E4AE3A"
    },
    "ISFP": {
        "character": "해리 포터 (Harry Potter)",
        "book": "해리 포터 (Harry Potter)",
        "desc": "따뜻한 마음씨와 겸손함을 지녔지만, 자신의 가치관을 지키기 위해서라면 용감해지는 당신. 예술적 감각과 순간의 감정에 충실한 '해리'와 닮았습니다.",
        "color": "#E4AE3A"
    },
    "INFP": {
        "character": "앤 셜리 (Anne Shirley)",
        "book": "빨간 머리 앤 (Anne of Green Gables)",
        "desc": "풍부한 상상력과 낭만을 가진 당신. 세상의 아름다움을 발견하고 자신만의 이상적인 세계를 꿈꾸는, 사랑스러운 몽상가 '앤'을 추천합니다.",
        "color": "#33A474"
    },
    "INTP": {
        "character": "앨리스 (Alice)",
        "book": "이상한 나라의 앨리스 (Alice in Wonderland)",
        "desc": "호기심이 많고 논리적인 모순을 찾아내는 것을 즐기는 당신. 이해할 수 없는 세상 속에서도 끊임없이 '왜?'라는 질문을 던지는 '앨리스'와 비슷하군요.",
        "color": "#88619A"
    },
    "ESTP": {
        "character": "톰 소여 (Tom Sawyer)",
        "book": "톰 소여의 모험 (The Adventures of Tom Sawyer)",
        "desc": "모험을 즐기고 행동력이 넘치는 당신. 지루한 것은 딱 질색이며, 위기 상황에서도 재치 있게 문제를 해결하는 장난기 넘치는 '톰'이 떠오릅니다.",
        "color": "#E4AE3A"
    },
    "ESFP": {
        "character": "데이지 뷰캐넌 (Daisy Buchanan)",
        "book": "위대한 개츠비 (The Great Gatsby)",
        "desc": "사교적이고 낙천적이며, 순간의 즐거움을 사랑하는 당신. 사람들의 시선을 사로잡는 매력을 지녔으며, 인생을 축제처럼 즐길 줄 아는 인물입니다.",
        "color": "#E4AE3A"
    },
    "ENFP": {
        "character": "엘리자베스 베넷 (Elizabeth Bennet)",
        "book": "오만과 편견 (Pride and Prejudice)",
        "desc": "자유로운 영혼과 재치 있는 입담을 가진 당신. 편견에 얽매이지 않고 진정한 사랑과 자아를 찾아가는 열정적인 '리지'와 꼭 닮았습니다.",
        "color": "#33A474"
    },
    "ENTP": {
        "character": "돈 키호테 (Don Quixote)",
        "book": "돈 키호테 (Don Quixote)",
        "desc": "풍부한 아이디어와 지칠 줄 모르는 도전 정신을 가진 당신. 남들이 뭐라 하든 자신의 비전을 향해 돌진하는 유쾌한 발명가형 인물입니다.",
        "color": "#88619A"
    },
    "ESTJ": {
        "character": "보로미르 (Boromir)",
        "book": "반지의 제왕 (The Lord of the Rings)",
        "desc": "책임감이 강하고 조직을 이끄는 리더십이 있는 당신. 전통을 수호하고 자신의 사람들을 지키기 위해 앞장서는 현실적인 지도자입니다.",
        "color": "#4298B4"
    },
    "ESFJ": {
        "character": "메그 마치 (Meg March)",
        "book": "작은 아씨들 (Little Women)",
        "desc": "타인을 돕는 것을 좋아하고 조화를 중시하는 당신. 따뜻한 마음으로 주변을 챙기며, 사랑하는 사람들과의 관계를 가장 소중히 여기는 '메그'를 추천합니다.",
        "color": "#4298B4"
    },
    "ENFJ": {
        "character": "엠마 우드하우스 (Emma Woodhouse)",
        "book": "엠마 (Emma)",
        "desc": "사람들을 이끄는 카리스마와 따뜻함을 동시에 지닌 당신. 주변 사람들의 행복을 위해(때로는 참견일지라도) 적극적으로 나서는 사랑스러운 중재자입니다.",
        "color": "#33A474"
    },
    "ENTJ": {
        "character": "나폴레옹 (Napoleon)",
        "book": "동물농장 (Animal Farm)",
        "desc": "대담한 리더십과 전략적 사고를 가진 당신. 목표를 달성하기 위해 체계적으로 계획을 세우고 사람들을 지휘하는 타고난 사령관입니다.",
        "color": "#88619A"
    }
}

# --- UI 구현 ---

st.title("📚 나의 문학적 도플갱어 찾기")
st.markdown("당신의 **MBTI**를 선택하면, 세계 문학 속에서 당신과 가장 닮은 등장인물을 찾아드립니다.")

st.write("---")

# 1. 사용자 입력 (MBTI 선택)
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### MBTI 선택")
    mbti_list = list(mbti_data.keys())
    selected_mbti = st.selectbox("당신의 유형을 알려주세요:", mbti_list)

# 선택된 데이터 가져오기
result = mbti_data[selected_mbti]

# 이미지 URL 생성 (플레이스홀더 서비스 사용 - 별도 파일 업로드 불필요)
# 책 제목의 공백을 '+'로 치환하여 URL 생성
safe_title = result['book'].split('(')[0].strip().replace(" ", "+")
image_url = f"https://placehold.co/400x600/png?text={safe_title}&font=roboto"

# 2. 결과 출력
with col2:
    st.markdown(f"### 결과: {selected_mbti}")
    
    # 카드 형태의 디자인
    st.success(f"**{result['character']}**")
    st.caption(f"출처: {result['book']}")
    
    st.image(image_url, caption=f"{result['book']} 표지", use_container_width=True)
    
    st.markdown("#### 💡 추천 이유")
    st.info(result['desc'])

st.write("---")
st.markdown("Created with ❤️ by Streamlit | [이미지 출처: Generated Placeholder]")
