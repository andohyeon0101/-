import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="기업의 경제적 지속발전 가능성 - 위키",
    page_icon="📚",
    layout="wide"
)

# 위키피디아 스타일 CSS
st.markdown("""
<style>
    .main-title {
        font-family: "Linux Libertine", Georgia, Times, serif;
        font-size: 2.5rem;
        font-weight: normal;
        border-bottom: 3px solid #a2a9b1;
        padding-bottom: 10px;
        margin-bottom: 20px;
        color: #000;
    }
    
    .wiki-header {
        font-family: "Linux Libertine", Georgia, Times, serif;
        font-size: 1.8rem;
        font-weight: normal;
        border-bottom: 1px solid #a2a9b1;
        padding-bottom: 5px;
        margin-top: 30px;
        margin-bottom: 15px;
        color: #000;
    }
    
    .wiki-subheader {
        font-family: "Linux Libertine", Georgia, Times, serif;
        font-size: 1.4rem;
        font-weight: normal;
        margin-top: 25px;
        margin-bottom: 10px;
        color: #000;
    }
    
    .wiki-text {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 14px;
        line-height: 1.6;
        color: #202122;
        text-align: justify;
    }
    
    .wiki-toc {
        background-color: #f8f9fa;
        border: 1px solid #a2a9b1;
        padding: 15px;
        margin: 20px 0;
        border-radius: 3px;
    }
    
    .wiki-toc-title {
        font-family: "Linux Libertine", Georgia, Times, serif;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 10px;
        color: #000;
    }
    
    .wiki-infobox {
        background-color: #f8f9fa;
        border: 1px solid #a2a9b1;
        padding: 15px;
        margin: 20px 0;
        border-radius: 3px;
        width: 100%;
    }
    
    .wiki-infobox-title {
        font-family: "Linux Libertine", Georgia, Times, serif;
        font-size: 1.1rem;
        font-weight: bold;
        text-align: center;
        background-color: #ccccff;
        padding: 8px;
        margin: -15px -15px 15px -15px;
        border-radius: 3px 3px 0 0;
    }
    
    .wiki-reference {
        font-size: 11px;
        color: #0645ad;
        text-decoration: none;
    }
    
    .wiki-note {
        background-color: #f6f6f6;
        border-left: 4px solid #36c;
        padding: 10px 15px;
        margin: 15px 0;
        font-style: italic;
        border-radius: 0 3px 3px 0;
    }
    
    .wiki-table {
        border-collapse: collapse;
        width: 100%;
        background-color: #f8f9fa;
        border: 1px solid #a2a9b1;
        margin: 10px 0;
    }
    
    .wiki-table th {
        background-color: #ccccff;
        padding: 8px;
        border: 1px solid #a2a9b1;
        font-weight: bold;
    }
    
    .wiki-table td {
        padding: 8px;
        border: 1px solid #a2a9b1;
    }
    
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        border: 1px solid #a2a9b1;
        padding: 15px;
        border-radius: 3px;
    }
    
    .wiki-category {
        background-color: #f8f9fa;
        border: 1px solid #a2a9b1;
        padding: 10px;
        margin: 20px 0;
        border-radius: 3px;
        font-size: 12px;
    }
    
    .wiki-disambiguation {
        background-color: #f8f9fa;
        border: 1px solid #a2a9b1;
        padding: 10px;
        margin: 10px 0;
        border-radius: 3px;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# 메인 제목
st.markdown('<h1 class="main-title">기업의 경제적 지속발전 가능성</h1>', unsafe_allow_html=True)

# 위키 스타일 disambiguation
st.markdown("""
<div class="wiki-disambiguation">
이 문서는 <strong>기업의 경제적 지속발전 가능성</strong>에 관한 것입니다. 
다른 의미의 지속가능성에 대해서는 <a href="#" class="wiki-reference">지속가능성 (동음이의)</a>를 참조하십시오.
</div>
""", unsafe_allow_html=True)

# 사이드바 - 위키 스타일 네비게이션
st.sidebar.markdown("""
<div style="background-color: #f8f9fa; border: 1px solid #a2a9b1; padding: 15px; border-radius: 3px;">
<h3 style="margin-top: 0; color: #000; font-family: 'Linux Libertine', Georgia, Times, serif;">목차</h3>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "",
    ["1. 개요", "2. 핵심 전략", "3. 성과 지표", "4. 자가진단", "5. 실행 계획", "6. 성공 사례"],
    label_visibility="collapsed"
)

# 목차 (Table of Contents)
if menu == "1. 개요":
    st.markdown("""
    <div class="wiki-toc">
        <div class="wiki-toc-title">목차</div>
        <div class="wiki-text">
        <strong>1.</strong> 개요<br>
        <strong>1.1</strong> 정의<br>
        <strong>1.2</strong> 핵심 원칙<br>
        <strong>1.3</strong> 구성 요소<br>
        <strong>1.4</strong> 중요성<br>
        <strong>2.</strong> 핵심 전략<br>
        <strong>3.</strong> 성과 지표<br>
        <strong>4.</strong> 자가진단<br>
        <strong>5.</strong> 실행 계획<br>
        <strong>6.</strong> 성공 사례
        </div>
    </div>
    """, unsafe_allow_html=True)

# 메인 콘텐츠
if menu == "1. 개요":
    # 인포박스
    st.markdown("""
    <div class="wiki-infobox">
        <div class="wiki-infobox-title">기업의 경제적 지속발전 가능성</div>
        <table class="wiki-table">
            <tr><th>분야</th><td>경영학, 경제학</td></tr>
            <tr><th>관련 개념</th><td>지속가능경영, ESG, 기업가치</td></tr>
            <tr><th>주요 지표</th><td>ROE, 매출성장률, 혁신지수</td></tr>
            <tr><th>관련 이론</th><td>이해관계자 이론, 자원기반이론</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="wiki-header">1. 개요</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-text">
    <strong>기업의 경제적 지속발전 가능성</strong>(Corporate Economic Sustainability)은 기업이 
    장기적으로 수익성을 유지하면서도 혁신과 효율성을 통해 지속적인 경쟁력을 확보하는 능력을 
    의미한다. 이는 단순한 단기적 이익 추구가 아닌, 장기적 가치 창출에 중점을 두는 경영 철학이다.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="wiki-subheader">1.1 정의</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-text">
    경제적 지속가능성은 기업이 현재의 경제적 성과를 달성하면서도 미래 세대의 필요를 충족할 수 있는 
    능력을 손상시키지 않는 방식으로 사업을 운영하는 것을 의미한다. 이는 다음과 같은 특징을 갖는다:
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="wiki-text">
        <ul>
        <li><strong>장기적 관점</strong>: 단기적 이익보다 장기적 가치 창출 우선</li>
        <li><strong>혁신 중심</strong>: 지속적인 혁신을 통한 경쟁력 확보</li>
        <li><strong>효율성 추구</strong>: 자원의 최적 활용과 운영 효율성 극대화</li>
        <li><strong>이해관계자 고려</strong>: 모든 이해관계자의 가치 균형 추구</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # 지속가능성 요소 파이 차트
        labels = ['경제적 성과', '혁신 역량', '운영 효율성', '리스크 관리', '이해관계자 관계']
        values = [25, 20, 20, 15, 20]
        colors = ['#e8f4f8', '#d4edda', '#fff3cd', '#f8d7da', '#e2e3e5']
        
        fig = px.pie(values=values, names=labels, 
                     title="<b>구성 요소</b>",
                     color_discrete_sequence=colors)
        fig.update_layout(
            font=dict(family="Helvetica Neue, Helvetica, Arial, sans-serif", size=12),
            title_font_size=14,
            width=400,
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<h3 class="wiki-subheader">1.2 핵심 원칙</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-text">
    기업의 경제적 지속발전 가능성은 다음과 같은 핵심 원칙들에 기반한다:
    </div>
    """, unsafe_allow_html=True)
    
    principles_data = {
        "원칙": ["장기적 가치 창출", "지속가능한 비즈니스 모델", "혁신과 적응력", "이해관계자 가치 균형"],
        "설명": [
            "단기적 이익보다 장기적 가치 창출을 우선시하는 경영 철학",
            "환경 변화에 적응할 수 있는 유연하고 견고한 비즈니스 모델 구축",
            "지속적인 혁신을 통해 변화하는 시장 환경에 적응하는 능력",
            "주주뿐만 아니라 모든 이해관계자의 가치를 고려하는 균형 잡힌 접근"
        ]
    }
    
    principles_df = pd.DataFrame(principles_data)
    st.markdown("""
    <div class="wiki-text">
    <table class="wiki-table">
        <tr><th>원칙</th><th>설명</th></tr>
        <tr><td>장기적 가치 창출</td><td>단기적 이익보다 장기적 가치 창출을 우선시하는 경영 철학</td></tr>
        <tr><td>지속가능한 비즈니스 모델</td><td>환경 변화에 적응할 수 있는 유연하고 견고한 비즈니스 모델 구축</td></tr>
        <tr><td>혁신과 적응력</td><td>지속적인 혁신을 통해 변화하는 시장 환경에 적응하는 능력</td></tr>
        <tr><td>이해관계자 가치 균형</td><td>주주뿐만 아니라 모든 이해관계자의 가치를 고려하는 균형 잡힌 접근</td></tr>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="wiki-subheader">1.3 중요성</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-note">
    <strong>주의:</strong> 경제적 지속가능성의 부족은 기업의 장기적 생존을 위협할 수 있다.
    </div>
    """, unsafe_allow_html=True)
    
    importance_data = {
        "지속가능성 확보 시": [
            "장기적 수익성 확보",
            "경쟁 우위 유지",
            "투자자 신뢰 증대",
            "시장 변화 대응력 향상",
            "브랜드 가치 상승"
        ],
        "지속가능성 부족 시": [
            "단기적 수익 추구로 인한 장기 손실",
            "혁신 부족으로 인한 경쟁력 상실",
            "지속불가능한 비즈니스 모델",
            "이해관계자 불신",
            "시장 변화 적응 실패"
        ]
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="wiki-text">
        <h4>✓ 확보 시 장점</h4>
        <ul>
        <li>장기적 수익성 확보</li>
        <li>경쟁 우위 유지</li>
        <li>투자자 신뢰 증대</li>
        <li>시장 변화 대응력 향상</li>
        <li>브랜드 가치 상승</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="wiki-text">
        <h4>✗ 부족 시 위험</h4>
        <ul>
        <li>단기적 수익 추구로 인한 장기 손실</li>
        <li>혁신 부족으로 인한 경쟁력 상실</li>
        <li>지속불가능한 비즈니스 모델</li>
        <li>이해관계자 불신</li>
        <li>시장 변화 적응 실패</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu == "2. 핵심 전략":
    st.markdown('<h2 class="wiki-header">2. 핵심 전략</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-text">
    기업의 경제적 지속발전 가능성을 확보하기 위한 핵심 전략은 크게 네 가지 영역으로 구분할 수 있다. 
    각 전략은 상호 연관성을 가지며, 통합적으로 접근할 때 최대의 효과를 발휘한다.
    </div>
    """, unsafe_allow_html=True)
    
    strategies = {
        "2.1 혁신과 기술 개발": {
            "description": "지속적인 연구개발과 기술 혁신을 통한 경쟁력 확보",
            "methods": [
                "R&D 투자 확대",
                "디지털 전환 추진",
                "신기술 도입 및 활용",
                "혁신 문화 조성",
                "오픈 이노베이션 추진"
            ],
            "details": "혁신과 기술 개발은 기업의 장기적 경쟁력 확보를 위한 핵심 전략이다. 이는 단순한 기술 도입이 아닌, 조직 전체의 혁신 역량을 강화하는 포괄적 접근을 의미한다."
        },
        "2.2 운영 효율성 향상": {
            "description": "프로세스 최적화와 자원 활용 효율성 제고",
            "methods": [
                "프로세스 자동화",
                "린 경영 도입",
                "공급망 최적화",
                "에너지 효율성 개선",
                "비용 구조 개선"
            ],
            "details": "운영 효율성 향상은 기업의 비용 경쟁력 확보와 수익성 개선을 위한 필수 요소이다. 이는 기술적 개선뿐만 아니라 조직 운영 방식의 전반적인 혁신을 포함한다."
        },
        "2.3 시장 다각화": {
            "description": "새로운 시장 진출과 제품 포트폴리오 다양화",
            "methods": [
                "신시장 개척",
                "제품 다양화",
                "서비스 확장",
                "글로벌 진출",
                "파트너십 구축"
            ],
            "details": "시장 다각화는 기업의 리스크를 분산하고 새로운 성장 동력을 확보하는 전략이다. 이는 기존 사업 영역의 확장과 새로운 영역으로의 진출을 모두 포함한다."
        },
        "2.4 인재 개발": {
            "description": "핵심 인재 확보와 역량 강화를 통한 조직 경쟁력 제고",
            "methods": [
                "교육 훈련 강화",
                "리더십 개발",
                "성과 관리 시스템",
                "조직 문화 개선",
                "인재 유치 및 유지"
            ],
            "details": "인재 개발은 기업의 모든 전략 실행의 기반이 되는 핵심 요소이다. 우수한 인재 없이는 어떤 전략도 성공할 수 없다는 점에서 그 중요성이 더욱 크다."
        }
    }
    
    for strategy, details in strategies.items():
        st.markdown(f'<h3 class="wiki-subheader">{strategy}</h3>', unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="wiki-text">
        <p><strong>개념:</strong> {details['description']}</p>
        <p>{details['details']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="wiki-text">
        <strong>주요 실행 방법:</strong>
        <ul>
        """, unsafe_allow_html=True)
        
        for method in details['methods']:
            st.markdown(f"<li>{method}</li>", unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)

elif menu == "3. 성과 지표":
    st.markdown('<h2 class="wiki-header">3. 성과 지표</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-text">
    기업의 경제적 지속발전 가능성을 측정하고 관리하기 위해서는 적절한 성과 지표(Key Performance Indicators, KPI)의 
    설정과 모니터링이 필수적이다. 이러한 지표들은 재무적 성과뿐만 아니라 비재무적 성과까지 포괄하여 
    기업의 지속가능성을 다각도로 평가할 수 있도록 한다.
    </div>
    """, unsafe_allow_html=True)
    
    # 지표 카테고리
    kpi_categories = {
        "3.1 재무 지표": [
            {"name": "매출 성장률", "description": "지속적인 매출 증가율", "target": "연 5-10%", "formula": "(당기매출 - 전기매출) / 전기매출 × 100"},
            {"name": "수익성 (ROE)", "description": "자기자본 수익률", "target": "15% 이상", "formula": "당기순이익 / 평균자기자본 × 100"},
            {"name": "현금 흐름", "description": "영업 현금 흐름", "target": "양수 유지", "formula": "영업활동현금흐름 / 매출액 × 100"},
            {"name": "부채 비율", "description": "총 부채 / 총 자본", "target": "50% 이하", "formula": "총부채 / 총자본 × 100"}
        ],
        "3.2 혁신 지표": [
            {"name": "R&D 투자율", "description": "매출 대비 R&D 투자 비율", "target": "3-5%", "formula": "R&D 투자액 / 매출액 × 100"},
            {"name": "신제품 매출 비중", "description": "신제품 매출 / 총 매출", "target": "20% 이상", "formula": "신제품매출 / 총매출 × 100"},
            {"name": "특허 출원 건수", "description": "연간 특허 출원 수", "target": "지속적 증가", "formula": "당해연도 특허출원건수"},
            {"name": "디지털 성숙도", "description": "디지털 전환 수준", "target": "4점/5점", "formula": "디지털전환지수 (5점척도)"}
        ],
        "3.3 운영 지표": [
            {"name": "생산성 지수", "description": "생산량 / 투입 자원", "target": "전년 대비 증가", "formula": "총생산량 / 총투입자원"},
            {"name": "고객 만족도", "description": "고객 만족 점수", "target": "4.5점/5점", "formula": "고객만족도조사 평균점수"},
            {"name": "직원 만족도", "description": "직원 만족 점수", "target": "4.0점/5점", "formula": "직원만족도조사 평균점수"},
            {"name": "시장 점유율", "description": "해당 시장 내 점유율", "target": "유지 또는 증가", "formula": "기업매출 / 전체시장규모 × 100"}
        ]
    }
    
    # KPI 대시보드
    st.markdown('<h3 class="wiki-subheader">3.1 핵심 성과 지표 체계</h3>', unsafe_allow_html=True)
    
    for category, indicators in kpi_categories.items():
        st.markdown(f'<h4 class="wiki-subheader">{category}</h4>', unsafe_allow_html=True)
        
        # 테이블 형태로 표시
        st.markdown("""
        <table class="wiki-table">
            <tr><th>지표명</th><th>설명</th><th>목표치</th><th>산식</th></tr>
        """, unsafe_allow_html=True)
        
        for indicator in indicators:
            st.markdown(f"""
            <tr>
                <td><strong>{indicator["name"]}</strong></td>
                <td>{indicator["description"]}</td>
                <td>{indicator["target"]}</td>
                <td><code>{indicator["formula"]}</code></td>
            </tr>
            """, unsafe_allow_html=True)
        
        st.markdown("</table>", unsafe_allow_html=True)
    
    # 성과 추이 시뮬레이션
    st.markdown('<h3 class="wiki-subheader">3.2 성과 추이 분석</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-text">
    다음은 대표적인 기업의 경제적 지속가능성 지표들의 추이를 보여주는 시뮬레이션 결과이다. 
    이러한 데이터를 통해 기업의 지속가능성 수준을 파악할 수 있다.
    </div>
    """, unsafe_allow_html=True)
    
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
        line=dict(color='#0645ad', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=performance_df['날짜'],
        y=performance_df['ROE(%)'],
        mode='lines+markers',
        name='ROE(%)',
        line=dict(color='#cc0000', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=performance_df['날짜'],
        y=performance_df['R&D투자율(%)'],
        mode='lines+markers',
        name='R&D투자율(%)',
        line=dict(color='#00aa00', width=2)
    ))
    
    fig.update_layout(
        title='<b>핵심 성과 지표 추이</b>',
        xaxis_title='날짜',
        yaxis_title='비율(%)',
        height=500,
        font=dict(family="Helvetica Neue, Helvetica, Arial, sans-serif", size=12),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif menu == "4. 자가진단":
    st.markdown('<h2 class="wiki-header">4. 자가진단</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="wiki-text">
    기업의 경제적 지속발전 가능성을 객관적으로 평가하기 위한 자가진단 도구이다. 
    이 진단은 5개 핵심 영역에 대한 20개 항목으로 구성되며
