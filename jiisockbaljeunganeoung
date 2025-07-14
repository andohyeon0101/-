import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="기업의 경제적 지속발전 가능성",
    page_icon="📈",
    layout="wide"
)

# 메인 제목
st.title("📈 기업의 경제적 지속발전 가능성")
st.markdown("---")

# 사이드바 메뉴
st.sidebar.title("🎯 메뉴")
menu = st.sidebar.radio(
    "선택하세요:",
    ["개요", "핵심 전략", "성과 지표", "자가진단", "실행 계획", "성공 사례"]
)

# 메인 콘텐츠
if menu == "개요":
    st.header("🌟 경제적 지속발전 가능성이란?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 정의
        기업이 **장기적으로 수익성을 유지**하면서도 **혁신과 효율성**을 통해 
        지속적인 경쟁력을 확보하는 능력입니다.
        
        ### 핵심 원칙
        - 📊 **장기적 가치 창출**
        - 🔄 **지속가능한 비즈니스 모델**
        - 💡 **혁신과 적응력**
        - 🤝 **이해관계자 가치 균형**
        """)
    
    with col2:
        # 지속가능성 요소 파이 차트
        labels = ['경제적 성과', '혁신 역량', '운영 효율성', '리스크 관리', '이해관계자 관계']
        values = [25, 20, 20, 15, 20]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        
        fig = px.pie(values=values, names=labels, title="경제적 지속가능성 구성요소",
                     color_discrete_sequence=colors)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # 중요성 설명
    st.subheader("🎯 왜 중요한가?")
    
    importance_data = {
        "장점": [
            "장기적 수익성 확보",
            "경쟁 우위 유지",
            "투자자 신뢰 증대",
            "시장 변화 대응력 향상",
            "브랜드 가치 상승"
        ],
        "위험": [
            "단기적 수익 추구로 인한 장기 손실",
            "혁신 부족으로 인한 경쟁력 상실",
            "지속불가능한 비즈니스 모델",
            "이해관계자 불신",
            "시장 변화 적응 실패"
        ]
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("✅ 지속가능성 확보 시")
        for benefit in importance_data["장점"]:
            st.write(f"• {benefit}")
    
    with col2:
        st.error("❌ 지속가능성 부족 시")
        for risk in importance_data["위험"]:
            st.write(f"• {risk}")

elif menu == "핵심 전략":
    st.header("🚀 핵심 전략")
    
    strategies = {
        "혁신과 기술 개발": {
            "description": "지속적인 연구개발과 기술 혁신을 통한 경쟁력 확보",
            "methods": [
                "R&D 투자 확대",
                "디지털 전환 추진",
                "신기술 도입 및 활용",
                "혁신 문화 조성",
                "오픈 이노베이션 추진"
            ],
            "color": "#FF6B6B"
        },
        "운영 효율성 향상": {
            "description": "프로세스 최적화와 자원 활용 효율성 제고",
            "methods": [
                "프로세스 자동화",
                "린 경영 도입",
                "공급망 최적화",
                "에너지 효율성 개선",
                "비용 구조 개선"
            ],
            "color": "#4ECDC4"
        },
        "시장 다각화": {
            "description": "새로운 시장 진출과 제품 포트폴리오 다양화",
            "methods": [
                "신시장 개척",
                "제품 다양화",
                "서비스 확장",
                "글로벌 진출",
                "파트너십 구축"
            ],
            "color": "#45B7D1"
        },
        "인재 개발": {
            "description": "핵심 인재 확보와 역량 강화를 통한 조직 경쟁력 제고",
            "methods": [
                "교육 훈련 강화",
                "리더십 개발",
                "성과 관리 시스템",
                "조직 문화 개선",
                "인재 유치 및 유지"
            ],
            "color": "#FFA07A"
        }
    }
    
    for strategy, details in strategies.items():
        with st.expander(f"📋 {strategy}"):
            st.markdown(f"**개념:** {details['description']}")
            st.markdown("**주요 실행 방법:**")
            for method in details['methods']:
                st.write(f"• {method}")

elif menu == "성과 지표":
    st.header("📊 성과 지표 (KPI)")
    
    # 지표 카테고리
    kpi_categories = {
        "재무 지표": [
            {"name": "매출 성장률", "description": "지속적인 매출 증가율", "target": "연 5-10%"},
            {"name": "수익성 (ROE)", "description": "자기자본 수익률", "target": "15% 이상"},
            {"name": "현금 흐름", "description": "영업 현금 흐름", "target": "양수 유지"},
            {"name": "부채 비율", "description": "총 부채 / 총 자본", "target": "50% 이하"}
        ],
        "혁신 지표": [
            {"name": "R&D 투자율", "description": "매출 대비 R&D 투자 비율", "target": "3-5%"},
            {"name": "신제품 매출 비중", "description": "신제품 매출 / 총 매출", "target": "20% 이상"},
            {"name": "특허 출원 건수", "description": "연간 특허 출원 수", "target": "지속적 증가"},
            {"name": "디지털 성숙도", "description": "디지털 전환 수준", "target": "4점/5점"}
        ],
        "운영 지표": [
            {"name": "생산성 지수", "description": "생산량 / 투입 자원", "target": "전년 대비 증가"},
            {"name": "고객 만족도", "description": "고객 만족 점수", "target": "4.5점/5점"},
            {"name": "직원 만족도", "description": "직원 만족 점수", "target": "4.0점/5점"},
            {"name": "시장 점유율", "description": "해당 시장 내 점유율", "target": "유지 또는 증가"}
        ]
    }
    
    # KPI 대시보드
    st.subheader("🎯 핵심 성과 지표")
    
    for category, indicators in kpi_categories.items():
        st.markdown(f"### {category}")
        cols = st.columns(len(indicators))
        
        for i, indicator in enumerate(indicators):
            with cols[i]:
                st.metric(
                    label=indicator["name"],
                    value=indicator["target"],
                    help=indicator["description"]
                )
        st.markdown("---")
    
    # 성과 추이 시뮬레이션
    st.subheader("📈 성과 추이 시뮬레이션")
    
    # 샘플 데이터 생성
    dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='Q')
    
    # 재무 성과 데이터
    np.random.seed(42)
    revenue_growth = np.random.normal(7, 2, len(dates))
    roe = np.random.normal(16, 3, len(dates))
    rd_investment = np.random.normal(4, 0.5, len(dates))
    
    performance_df = pd.DataFrame({
        '날짜': dates,
        '매출성장률(%)': revenue_growth,
        'ROE(%)': roe,
        'R&D투자율(%)': rd_investment
    })
    
    # 성과 차트
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=performance_df['날짜'],
        y=performance_df['매출성장률(%)'],
        mode='lines+markers',
        name='매출성장률(%)',
        line=dict(color='#FF6B6B')
    ))
    
    fig.add_trace(go.Scatter(
        x=performance_df['날짜'],
        y=performance_df['ROE(%)'],
        mode='lines+markers',
        name='ROE(%)',
        line=dict(color='#4ECDC4')
    ))
    
    fig.add_trace(go.Scatter(
        x=performance_df['날짜'],
        y=performance_df['R&D투자율(%)'],
        mode='lines+markers',
        name='R&D투자율(%)',
        line=dict(color='#45B7D1')
    ))
    
    fig.update_layout(
        title='핵심 성과 지표 추이',
        xaxis_title='날짜',
        yaxis_title='비율(%)',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif menu == "자가진단":
    st.header("🔍 기업 지속가능성 자가진단")
    
    st.markdown("""
    다음 질문들에 답하여 귀하의 기업의 경제적 지속가능성 수준을 진단해보세요.
    각 항목을 1-5점으로 평가해주세요. (1: 매우 부족, 5: 매우 우수)
    """)
    
    # 진단 카테고리
    categories = {
        "재무 건전성": [
            "안정적인 수익 창출 능력",
            "건전한 재무 구조",
            "현금 흐름 관리",
            "투자 수익률"
        ],
        "혁신 역량": [
            "R&D 투자 수준",
            "신제품 개발 능력",
            "기술 혁신 문화",
            "디지털 전환 수준"
        ],
        "운영 효율성": [
            "생산성 수준",
            "품질 관리 시스템",
            "공급망 최적화",
            "비용 관리 효율성"
        ],
        "시장 적응력": [
            "시장 변화 대응 능력",
            "고객 만족도",
            "브랜드 인지도",
            "경쟁 우위 요소"
        ],
        "조직 역량": [
            "인재 관리 수준",
            "리더십 품질",
            "조직 문화",
            "변화 관리 능력"
        ]
    }
    
    scores = {}
    total_score = 0
    total_items = 0
    
    for category, items in categories.items():
        st.subheader(f"📋 {category}")
        category_scores = []
        
        for item in items:
            score = st.slider(
                f"{item}",
                min_value=1,
                max_value=5,
                value=3,
                key=f"{category}_{item}"
            )
            category_scores.append(score)
            total_score += score
            total_items += 1
        
        scores[category] = sum(category_scores) / len(category_scores)
        st.write(f"**{category} 평균 점수: {scores[category]:.1f}/5.0**")
        st.markdown("---")
    
    # 전체 진단 결과
    overall_score = total_score / total_items
    
    st.subheader("🎯 종합 진단 결과")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("전체 평균 점수", f"{overall_score:.1f}/5.0")
        
        if overall_score >= 4.0:
            st.success("🌟 우수: 경제적 지속가능성이 뛰어납니다!")
        elif overall_score >= 3.0:
            st.warning("⚠️ 보통: 개선이 필요한 영역이 있습니다.")
        else:
            st.error("🚨 부족: 전반적인 개선이 필요합니다.")
    
    with col2:
        # 레이더 차트
        fig = go.Figure()
        
        categories_list = list(scores.keys())
        values = list(scores.values())
        values += values[:1]  # 닫힌 도형을 위해 첫 값 추가
        categories_list += categories_list[:1]
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories_list,
            fill='toself',
            name='현재 수준'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=True,
            title="영역별 진단 결과"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # 개선 제안
    st.subheader("💡 개선 제안")
    
    weak_areas = [category for category, score in scores.items() if score < 3.0]
    
    if weak_areas:
        st.markdown("**우선 개선 필요 영역:**")
        for area in weak_areas:
            st.write(f"• {area}: {scores[area]:.1f}점")
    else:
        st.success("모든 영역에서 양호한 수준입니다!")

elif menu == "실행 계획":
    st.header("📋 지속가능성 실행 계획")
    
    st.markdown("""
    경제적 지속가능성 향상을 위한 단계별 실행 계획을 수립해보세요.
    """)
    
    # 실행 단계
    phases = {
        "1단계: 현황 분석 (1-2개월)": {
            "목표": "현재 상황 파악 및 개선 영역 식별",
            "활동": [
                "재무 현황 분석",
                "시장 포지션 평가",
                "내부 역량 진단",
                "경쟁사 벤치마킹",
                "이해관계자 의견 수렴"
            ],
            "결과물": "현황 분석 보고서, 개선 우선순위"
        },
        "2단계: 전략 수립 (2-3개월)": {
            "목표": "지속가능성 전략 및 로드맵 구축",
            "활동": [
                "비전 및 목표 설정",
                "핵심 전략 수립",
                "실행 계획 작성",
                "성과 지표 정의",
                "자원 배분 계획"
            ],
            "결과물": "지속가능성 전략서, 실행 로드맵"
        },
        "3단계: 실행 준비 (1-2개월)": {
            "목표": "실행을 위한 기반 구축",
            "활동": [
                "조직 체계 구축",
                "시스템 구축",
                "교육 및 훈련",
                "파트너십 구축",
                "예산 확보"
            ],
            "결과물": "실행 체계, 교육 프로그램"
        },
        "4단계: 본격 실행 (6-12개월)": {
            "목표": "전략의 본격적 실행",
            "활동": [
                "프로젝트 실행",
                "성과 모니터링",
                "정기 점검 및 조정",
                "이해관계자 소통",
                "개선 사항 반영"
            ],
            "결과물": "실행 성과, 개선 사항"
        },
        "5단계: 평가 및 개선 (지속적)": {
            "목표": "지속적 개선 및 발전",
            "활동": [
                "성과 평가",
                "차기 계획 수립",
                "베스트 프랙티스 공유",
                "시스템 고도화",
                "문화 정착"
            ],
            "결과물": "평가 보고서, 차기 계획"
        }
    }
    
    for phase, details in phases.items():
        with st.expander(f"📅 {phase}"):
            st.markdown(f"**목표:** {details['목표']}")
            st.markdown("**주요 활동:**")
            for activity in details['활동']:
                st.write(f"• {activity}")
            st.markdown(f"**예상 결과물:** {details['결과물']}")
    
    st.markdown("---")
    
    # 실행 계획 템플릿
    st.subheader("📝 실행 계획 템플릿")
    
    with st.form("action_plan"):
        st.markdown("### 우선 개선 영역 선택")
        
        priority_area = st.selectbox(
            "개선이 가장 시급한 영역을 선택하세요:",
            ["재무 건전성", "혁신 역량", "운영 효율성", "시장 적응력", "조직 역량"]
        )
        
        st.markdown("### 목표 설정")
        target_period = st.selectbox("목표 달성 기간:", ["3개월", "6개월", "1년", "2년"])
        target_description = st.text_area("구체적인 목표:", placeholder="예: ROE 15% 달성, 신제품 매출 비중 20% 증대 등")
        
        st.markdown("### 실행 방안")
        action_items = st.text_area(
            "주요 실행 항목 (한 줄씩 입력):",
            placeholder="예:\n• R&D 투자 확대\n• 디지털 전환 프로젝트 추진\n• 프로세스 혁신 TF 구성"
        )
        
        st.markdown("### 성과 지표")
        kpi = st.text_input("핵심 성과 지표 (KPI):", placeholder="예: 매출 성장률, ROE, 고객 만족도 등")
        
        st.markdown("### 필요 자원")
        resources = st.text_area("필요한 자원 (예산, 인력, 시스템 등):", placeholder="예: 예산 1억원, 전담 인력 5명, IT 시스템 구축")
        
        submitted = st.form_submit_button("실행 계획 생성")
        
        if submitted:
            st.success("✅ 실행 계획이 생성되었습니다!")
            
            st.markdown("### 📋 생성된 실행 계획")
            st.markdown(f"**우선 개선 영역:** {priority_area}")
            st.markdown(f"**목표 달성 기간:** {target_period}")
            st.markdown(f"**구체적 목표:** {target_description}")
            st.markdown(f"**주요 실행 항목:**\n{action_items}")
            st.markdown(f"**핵심 성과 지표:** {kpi}")
            st.markdown(f"**필요 자원:** {resources}")

elif menu == "성공 사례":
    st.header("🏆 성공 사례")
    
    st.markdown("""
    경제적 지속가능성을 성공적으로 달성한 기업들의 사례를 통해 
    실질적인 인사이트를 얻어보세요.
    """)
    
    # 성공 사례 데이터
    success_cases = {
        "기술 혁신 중심": {
            "company": "A 제조기업",
            "challenge": "전통적인 제조업에서 디지털 전환 필요성",
            "strategy": [
                "스마트 팩토리 구축",
                "AI 기반 품질 관리 시스템 도입",
                "IoT를 활용한 예측 정비",
                "데이터 기반 의사결정 체계 구축"
            ],
            "results": [
                "생산성 30% 향상",
                "품질 불량률 50% 감소",
                "운영 비용 20% 절감",
                "신제품 출시 시간 40% 단축"
            ],
            "lessons": "지속적인 기술 투자와 조직 문화 변화가 핵심"
        },
        "시장 다각화": {
            "company": "B 유통기업",
            "challenge": "온라인 시장 확산으로 인한 오프라인 매출 감소",
            "strategy": [
                "옴니채널 플랫폼 구축",
                "개인화된 고객 서비스 제공",
                "새로운 비즈니스 모델 개발",
                "글로벌 시장 진출"
            ],
            "results": [
                "온라인 매출 300% 증가",
                "고객 만족도 25% 향상",
                "시장 점유율 15% 확대",
                "수익성 40% 개선"
            ],
            "lessons": "고객 중심 사고와 빠른 시장 적응이 성공 요인"
        },
        "운영 효율성": {
            "company": "C 서비스기업",
            "challenge": "인건비 상승과 경쟁 심화로 인한 수익성 악화",
            "strategy": [
                "프로세스 자동화 추진",
                "린 경영 시스템 도입",
                "직원 생산성 향상 프로그램",
                "파트너십 기반 협업 모델"
            ],
            "results": [
                "운영 비용 25% 감소",
                "서비스 품질 향상",
                "직원 만족도 20% 증가",
                "고객 유지율 35% 향상"
            ],
            "lessons": "효율성과 품질을 동시에 추구하는 균형 잡힌 접근"
        }
    }
    
    for case_type, case_data in success_cases.items():
        with st.expander(f"📊 {case_type}: {case_data['company']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 🎯 도전 과제")
                st.write(case_data['challenge'])
                
                st.markdown("### 🚀 추진 전략")
                for strategy in case_data['strategy']:
                    st.write(f"• {strategy}")
            
            with col2:
                st.markdown("### 📈 주요 성과")
                for result in case_data['results']:
                    st.write(f"• {result}")
                
                st.markdown("### 💡 핵심 교훈")
                st.info(case_data['lessons'])
    
    st.markdown("---")
    
    # 성공 요인 분석
    st.subheader("🔍 성공 요인 분석")
    
    success_factors = {
        "리더십": ["강력한 의지", "변화 추진력", "장기적 관점"],
        "조직문화": ["혁신 마인드", "학습 조직", "협업 문화"],
        "전략 실행": ["명확한 목표", "체계적 접근", "지속적 모니터링"],
        "자원 활용": ["적절한 투자", "핵심 역량 집중", "파트너십 활용"],
        "시장 적응": ["고객 중심", "민첩한 대응", "지속적 혁신"]
    }
    
    cols = st.columns(len(success_factors))
    
    for i, (factor, elements) in enumerate(success_factors.items()):
        with cols[i]:
            st.markdown(f"### {factor}")
            for element in elements:
                st.write(f"• {element}")
    
    # 벤치마킹 체크리스트
    st.subheader("📋 벤치마킹 체크리스트")
    
    checklist = [
        "명확한 지속가능성 비전과 목표 설정",
        "최고 경영진의 강력한 의지와 지원",
        "체계적인 현황 분석과 개선 계획",
        "핵심 성과 지표(KPI) 설정 및 모니터링",
        "조직 문화 혁신과 변화 관리",
        "지속적인 혁신과 기술 투자",
        "이해관계자와의 효과적 소통",
        "단계적 실행과 지속적 개선"
    ]
    
    st.markdown("**우리 기업에 적용 가능한 요소들을 체크해보세요:**")
    
    for item in checklist:
        st.checkbox(item, key=f"check_{item}")

# 푸터
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px;'>
📈 기업의 경제적 지속발전 가능성 웹앱 | 지속가능한 경영을 위한 가이드
</div>
""", unsafe_allow_html=True)
