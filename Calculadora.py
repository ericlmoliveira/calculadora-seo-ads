import streamlit as st
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Calculadora SEO Técnico x Google Ads",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS customizado com identidade visual
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Montserrat', sans-serif;
    }
    
    .main {
        background: linear-gradient(180deg, #00cc66 0%, #000000 100%);
        padding: 2rem;
    }
    
    .stApp {
        background: linear-gradient(180deg, #00cc66 0%, #000000 100%);
    }
    
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 700;
    }
    
    .subtitle {
        color: #ffffff;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        border-left: 5px solid #00cc66;
    }
    
    .metric-title {
        color: #1a1a1a;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        color: #00cc66;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .metric-comparison {
        color: #666;
        font-size: 0.95rem;
        margin-top: 0.5rem;
    }
    
    .improvement {
        color: #00cc66;
        font-weight: 600;
    }
    
    .insight-box {
        background: rgba(26, 26, 26, 0.9);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 2px solid #00cc66;
        color: #ffffff;
    }
    
    .insight-title {
        color: #00cc66;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .insight-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #ffffff;
    }
    
    .footer {
        text-align: center;
        color: #ffffff;
        margin-top: 3rem;
        padding: 2rem;
        font-size: 0.9rem;
    }
    
    .stNumberInput, .stSlider {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 0.5rem;
    }
    
    label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    .arrow-up {
        color: #00cc66;
        font-size: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h1>⚙️ Calculadora de Impacto SEO Técnico x Google Ads</h1>
    <p class='subtitle'>Desenvolvido por <strong>Eric Lima</strong> — Sites mais rápidos, anúncios mais rentáveis.</p>
    <p style='color: #ffffff; font-size: 0.95rem; max-width: 800px; margin: 0 auto;'>
        Descubra quanto você pode economizar e lucrar otimizando a performance técnica do seu site.
        Esta ferramenta calcula o impacto real do SEO Técnico no ROI das suas campanhas Google Ads.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Seção de inputs
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📊 Dados da Campanha Atual")
    investimento = st.number_input(
        "Investimento Mensal (R$)",
        min_value=100.0,
        value=5000.0,
        step=100.0,
        help="Quanto você investe por mês em Google Ads"
    )
    
    cpc_atual = st.number_input(
        "CPC Médio Atual (R$)",
        min_value=0.10,
        value=2.50,
        step=0.10,
        help="Custo por clique atual da sua campanha"
    )

with col2:
    st.markdown("### 🎯 Métricas de Conversão")
    taxa_conversao = st.number_input(
        "Taxa de Conversão Atual (%)",
        min_value=0.1,
        value=3.0,
        step=0.1,
        help="Percentual de visitantes que convertem"
    )
    
    ticket_medio = st.number_input(
        "Ticket Médio (R$)",
        min_value=10.0,
        value=500.0,
        step=10.0,
        help="Valor médio de cada conversão/venda"
    )

with col3:
    st.markdown("### 💼 Investimento em SEO")
    custo_servico = st.number_input(
        "Valor do Serviço de SEO (R$)",
        min_value=100.0,
        value=2000.0,
        step=100.0,
        help="Investimento no serviço de otimização técnica"
    )

st.markdown("---")

# Sliders de ajuste
st.markdown("### 🎚️ Ajustes de Projeção")

# Guia de orientação
st.markdown("""
<div style='background: rgba(0, 204, 102, 0.1); border-left: 4px solid #00cc66; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem;'>
    <strong style='color: #00cc66;'>📊 Guia de Valores Realistas (baseado no LCP atual do site):</strong><br>
    <span style='color: #ffffff; font-size: 0.9rem;'>
    🔴 <strong>Site Lento (LCP > 4s):</strong> CPC -20% a -30% | Conversão +25% a +40%<br>
    🟡 <strong>Site Regular (LCP 2.5s - 4s):</strong> CPC -10% a -20% | Conversão +15% a +25%<br>
    🟢 <strong>Site Bom (LCP < 2.5s):</strong> CPC -5% a -10% | Conversão +5% a +10%
    </span>
</div>
""", unsafe_allow_html=True)

col_slider1, col_slider2 = st.columns(2)

with col_slider1:
    reducao_cpc = st.slider(
        "Redução Esperada no CPC (%)",
        min_value=5,
        max_value=40,
        value=20,
        help="Sites mais rápidos têm melhor Quality Score no Google Ads, reduzindo o custo por clique"
    )

with col_slider2:
    aumento_conversao = st.slider(
        "Aumento Esperado na Taxa de Conversão (%)",
        min_value=5,
        max_value=50,
        value=25,
        help="Performance técnica melhora a experiência do usuário e reduz a taxa de rejeição"
    )

st.markdown("---")

# Cálculos
cpc_novo = cpc_atual * (1 - reducao_cpc / 100)
cliques_atuais = investimento / cpc_atual
cliques_novos = investimento / cpc_novo
conversao_nova = taxa_conversao * (1 + aumento_conversao / 100)
leads_atuais = cliques_atuais * (taxa_conversao / 100)
leads_novos = cliques_novos * (conversao_nova / 100)
receita_atual = leads_atuais * ticket_medio
receita_nova = leads_novos * ticket_medio
ganho_estimado = receita_nova - receita_atual
roi_estimado = (ganho_estimado / custo_servico) * 100

# Cálculo de perda por lentidão (assumindo 2s de diferença)
segundos_lentidao = 2
perda_conversao_lentidao = segundos_lentidao * 7  # 7% por segundo

# Resultados
st.markdown("## 📈 Resultados da Otimização")

# Métricas principais
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>CPC Médio</div>
        <div class='metric-value'>R$ {cpc_novo:.2f}</div>
        <div class='metric-comparison'>
            Atual: R$ {cpc_atual:.2f}<br>
            <span class='improvement'>↓ {reducao_cpc}% de redução</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_m2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>Cliques/Mês</div>
        <div class='metric-value'>{int(cliques_novos)}</div>
        <div class='metric-comparison'>
            Atual: {int(cliques_atuais)}<br>
            <span class='improvement'>↑ {int(cliques_novos - cliques_atuais)} cliques adicionais</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_m3:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>Leads/Mês</div>
        <div class='metric-value'>{int(leads_novos)}</div>
        <div class='metric-comparison'>
            Atual: {int(leads_atuais)}<br>
            <span class='improvement'>↑ {int(leads_novos - leads_atuais)} leads adicionais</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_m4:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>Taxa de Conversão</div>
        <div class='metric-value'>{conversao_nova:.2f}%</div>
        <div class='metric-comparison'>
            Atual: {taxa_conversao:.2f}%<br>
            <span class='improvement'>↑ {aumento_conversao}% de aumento</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Métricas financeiras
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>Receita Mensal</div>
        <div class='metric-value'>R$ {receita_nova:,.2f}</div>
        <div class='metric-comparison'>
            Atual: R$ {receita_atual:,.2f}<br>
            <span class='improvement'>↑ R$ {ganho_estimado:,.2f} de ganho</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>Ganho Estimado</div>
        <div class='metric-value'>R$ {ganho_estimado:,.2f}</div>
        <div class='metric-comparison'>
            Por mês após otimização<br>
            <span class='improvement'>Em 12 meses: R$ {ganho_estimado * 12:,.2f}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_f3:
    cor_roi = "#00cc66" if roi_estimado > 100 else "#ff6b6b"
    st.markdown(f"""
    <div class='metric-card'>
        <div class='metric-title'>ROI do Investimento em SEO</div>
        <div class='metric-value' style='color: {cor_roi};'>{roi_estimado:.1f}%</div>
        <div class='metric-comparison'>
            Investimento: R$ {custo_servico:,.2f}<br>
            <span class='improvement'>Retorno em {(custo_servico / ganho_estimado):.1f} meses</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Insight sobre lentidão
st.markdown(f"""
<div class='insight-box' style='background: rgba(255, 107, 107, 0.1); border-color: #ff6b6b;'>
    <div class='insight-title' style='color: #ff6b6b;'>⚠️ Impacto da Lentidão</div>
    <div class='insight-text'>
        Estudos mostram que <strong>cada segundo adicional de carregamento reduz as conversões em 7%</strong>.
        Se seu site carregar 2s mais lento que o ideal, você pode estar perdendo até <strong>{perda_conversao_lentidao}%</strong> das suas conversões.
        <br><br>
        <strong>Isso significa {int(leads_atuais * (perda_conversao_lentidao/100))} leads perdidos por mês</strong>, equivalente a 
        <strong>R$ {(leads_atuais * (perda_conversao_lentidao/100) * ticket_medio):,.2f}</strong> em receita.
    </div>
</div>
""", unsafe_allow_html=True)

# Resumo executivo
st.markdown(f"""
<div class='insight-box'>
    <div class='insight-title'>💡 Resumo Executivo</div>
    <div class='insight-text'>
        Com a <strong>otimização técnica do seu site</strong>, você pode:
        <br><br>
        ✅ Reduzir seu CPC de <strong>R$ {cpc_atual:.2f}</strong> para <strong>R$ {cpc_novo:.2f}</strong><br>
        ✅ Aumentar de <strong>{int(leads_atuais)}</strong> para <strong>{int(leads_novos)}</strong> leads por mês 
        (<strong>+{int(leads_novos - leads_atuais)} leads</strong>)<br>
        ✅ Gerar <strong>R$ {ganho_estimado:,.2f}</strong> adicionais por mês<br>
        ✅ Obter um ROI de <strong>{roi_estimado:.1f}%</strong> sobre o investimento em SEO<br>
        ✅ Recuperar o investimento em aproximadamente <strong>{(custo_servico / ganho_estimado):.1f} meses</strong>
        <br><br>
        <strong>Em 12 meses, o ganho acumulado seria de R$ {ganho_estimado * 12:,.2f}</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# Gráfico de comparação
st.markdown("### 📊 Comparação Visual")

fig = go.Figure()

categorias = ['CPC (R$)', 'Cliques', 'Leads', 'Receita (R$)']
valores_atuais = [cpc_atual, cliques_atuais, leads_atuais, receita_atual/100]
valores_novos = [cpc_novo, cliques_novos, leads_novos, receita_nova/100]

fig.add_trace(go.Bar(
    name='Cenário Atual',
    x=categorias,
    y=valores_atuais,
    marker_color='rgba(255, 255, 255, 0.3)',
    text=[f'{v:.1f}' for v in valores_atuais],
    textposition='auto',
))

fig.add_trace(go.Bar(
    name='Com Otimização',
    x=categorias,
    y=valores_novos,
    marker_color='#00cc66',
    text=[f'{v:.1f}' for v in valores_novos],
    textposition='auto',
))

fig.update_layout(
    barmode='group',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white', family='Montserrat'),
    title='Comparação: Antes x Depois da Otimização',
    height=400,
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

st.plotly_chart(fig, use_container_width=True)

# Rodapé
st.markdown("""
<div class='footer'>
    <strong>Eric Lima</strong> | Especialista em SEO Técnico<br>
    Otimização de Performance • Core Web Vitals • Google Ads ROI<br>
    <br>
    <a href='https://www.linkedin.com/in/ericlmoliveira' target='_blank' style='color: #00cc66; text-decoration: none; font-weight: 600;'>
        🔗 Conecte-se no LinkedIn
    </a>
    <br><br>
    <span style='font-size: 0.8rem; color: rgba(255,255,255,0.6);'>
        Esta calculadora usa fórmulas baseadas em dados reais de mercado e estudos de performance web.
    </span>
</div>

""", unsafe_allow_html=True)


