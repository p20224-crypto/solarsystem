import streamlit as st

st.title('태양계 행성들의 위성')

# 사용자 입력 받기
selected_planet = st.selectbox('행성을 선택해주세요:', [
    '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성'
])

# 위성 설명 (더 자세히)
planet_data = {
    '수성': {
        '특징': '태양에서 가장 가깝고 태양계에서 가장 작은 행성이다.',
        '대표적인_위성': '없다.',
    },
    '금성': {
        '특징': '지구와 유사한 크기이지만, 두꺼운 이산화탄소 대기와 그로 인한 극단적인 온실효과가 있다.',
        '대표적인_위성': '없다.',
    },
    '지구': {
        '특징': '생명체가 존재하며 대기가 질소와 산소로 구성되어 있다.',
        '대표적인_위성': '달',
        '위성_특징': {
            '달': {
                '설명': '지구에서 가장 가까운 천체이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg'
            },
        },
    },
    '화성': {
        '특징': '매우 희박한 이산화탄소 대기, 낮은 중력, 물의 흔적이 있다.',
        '대표적인_위성': '포보스, 데이모스',
        '위성_특징': {
            '포보스': {
                '설명': '화성을 공전하고 있는 두 위성 중 가까이 있는 위성이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/0/02/Phobos_colour_2008.jpg'
            },
            '데이모스': {
                '설명': '미국의 천문학자인 아사프 홀이 발견했다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/1/16/Deimos-MRO.jpg'
            },
        },
    },
    '목성': {
        '특징': '태양계에서 가장 큰 거대 가스 행성으로, 강력한 자기장과 빠른 자전, 거대한 폭풍 대적점이 특징이다.',
        '대표적인_위성': '이오, 유로파, 가니메데, 칼리스토',
        '위성_특징': {
            '이오': {
                '설명': '평균 반지름이 약 1,800km로 달과 비슷한 크기이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Io_highest_resolution_true_color.jpg'
            },
            '유로파': {
                '설명': '표면 아래 거대한 지하 바다가 존재할 가능성이 높아 생명체 후보지로 주목받는다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/1/1e/Europa-moon.jpg'
            },
            '가니메데': {
                '설명': '반지름 2,634km로 태양계에서 가장 큰 위성이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Ganymede_g1_true-edit1.jpg'
            },
            '칼리스토': {
                '설명': '태양계에서 세 번째로 큰 위성으로, 표면 충돌구가 많다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/8/83/Callisto.jpg'
            },
        },
    },
    '토성': {
        '특징': '거대한 고리와 많은 위성을 가진 행성이다.',
        '대표적인_위성': '타이탄, 엔셀라두스, 미마스',
        '위성_특징': {
            '타이탄': {
                '설명': '토성의 가장 큰 위성으로, 소형 천체망원경으로 관찰할 수 있다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Titan_in_true_color.jpg'
            },
            '엔셀라두스': {
                '설명': '지름이 504km밖에 되지 않은 매우 작은 위성으로, 얼음 기둥이 분출되는 현상이 있다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Enceladus_from_Cassini_Orbit_114.jpg'
            },
            '미마스': {
                '설명': '토성의 7번째로 큰 자연 위성으로, 표면의 거대한 충돌구가 특징이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Mimas_Cassini.jpg'
            },
        },
    },
    '천왕성': {
        '특징': '푸른색을 띠는 가스 행성으로, 자전축이 거의 옆으로 누워있다.',
        '대표적인_위성': '세토보스, 티타니아, 미란다',
        '위성_특징': {
            '세토보스': {
                '설명': '천왕성의 가장 바깥쪽 불규칙 위성 중 하나이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Setebos_Uranus_moon.jpg'
            },
            '티타니아': {
                '설명': '천왕성의 위성들 중 가장 크다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Titania_%28moon%29_color.jpg'
            },
            '미란다': {
                '설명': '천왕성의 둥근 다섯 개의 위성 중 가장 작고 가장 안쪽에 위치한다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/0/0d/Miranda.jpg'
            },
        },
    },
    '해왕성': {
        '특징': '푸른색을 띠는 가스 행성으로, 강력한 바람과 폭풍이 특징이다.',
        '대표적인_위성': '트리톤, 나이아드, 탈라사',
        '위성_특징': {
            '트리톤': {
                '설명': '해왕성의 가장 큰 위성으로, 역행 공전을 한다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Triton_moon_mosaic_Voyager_2_%28large%29.jpg'
            },
            '나이아드': {
                '설명': '해왕성에 가까운 궤도를 가진 작은 위성이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/2/2d/Naiad_moon_of_Neptune.png'
            },
            '탈라사': {
                '설명': '불규칙한 모양이며, 위성들의 파편이 뭉쳐 만들어졌을 가능성이 있다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Thalassa_moon.png'
            },
        },
    },
}

if st.button('특징 생성'):
    if selected_planet in planet_data:
        특징 = planet_data[selected_planet].get('특징', '정보 없음')
        대표적인_위성 = planet_data[selected_planet].get('대표적인_위성', '정보 없음')
        위성_특징 = planet_data[selected_planet].get('위성_특징', None)

        st.write(f"**특징**: {특징}")
        st.write(f"**대표적인 위성**: {대표적인_위성}")

        # 위성_특징이 dict이면 문단 나누어 표시
        if isinstance(위성_특징, dict):
            for 위성, 설명 in 위성_특징.items():
                st.markdown(f"**{위성}**  \n{설명}\n")
        else:
            st.write(위성_특징 or "위성 관련 상세 정보가 없습니다.")
    else:
        st.write(f"{selected_planet}에 대한 정보가 없습니다.")
