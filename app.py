import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="DECODED INTELLIGENCE | Institutional PQC Risk Terminal", 
    page_icon="🛡️",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Custom CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
    
    html, body, .stApp {
        background-color: #06090e !important;
        color: #e2e8f0 !important;
        font-family: 'Inter', sans-serif !important;
    }

    code, .mono-font {
        font-family: 'JetBrains Mono', monospace !important;
    }

    .brand-container {
        background: #0b111c;
        border: 1px solid #1e293b;
        border-left: 4px solid #00ff66;
        padding: 16px 20px;
        border-radius: 6px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 10px;
    }
    
    .brand-title {
        color: #ffffff;
        font-size: 1.25rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    .brand-tag {
        color: #00ff66;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        background: rgba(0, 255, 102, 0.1);
        padding: 6px 12px;
        border-radius: 4px;
        border: 1px solid rgba(0, 255, 102, 0.2);
    }

    .kpi-card {
        background: #0b111c;
        border: 1px solid #1e293b;
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .kpi-label {
        color: #64748b;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 6px 0;
        word-break: break-all;
    }
    .kpi-foot {
        font-size: 0.72rem;
        color: #94a3b8;
    }

    div[data-testid="stSidebar"] {
        background-color: #080d16 !important;
        border-right: 1px solid #1e293b;
    }

    /* Custom Stylish SUBMIT Button */
    div.stButton > button {
        background: linear-gradient(135deg, #00ff66 0%, #00cc52 100%) !important;
        color: #06090e !important;
        font-size: 1rem !important;
        font-weight: 800 !important;
        border: none !important;
        width: 100% !important;
        padding: 12px 20px !important;
        border-radius: 6px !important;
        letter-spacing: 0.08em !important;
        box-shadow: 0px 4px 15px rgba(0, 255, 102, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(0, 255, 102, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("""
    <div class="brand-container">
        <div>
            <span class="brand-title">DECODED INTELLIGENCE</span>
            <span style="color: #475569; margin: 0 8px;">/</span>
            <span style="color: #94a3b8; font-size: 0.85rem; font-weight: 600;">QUANTUM DECAY & STOCHASTIC PROJECTION ENGINE</span>
        </div>
        <div>
            <span class="brand-tag">NIST SP 800-224 COMPLIANT</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Clean Sidebar Form
st.sidebar.markdown("### 🏢 **INSTITUTIONAL PARAMS**")
with st.sidebar.form(key='input_form'):
    asset_val = st.number_input("Total Asset Exposure ($M)", min_value=10.0, value=1250.0, step=50.0)
    cost_equity = st.slider("Cost of Equity (%)", 4.0, 15.0, 9.9, 0.1)
    debt_wt = st.slider("Debt Weight (%)", 10, 70, 30, 5)

    st.markdown("---")
    st.markdown("### 🎯 **TIMELINE HORIZON**")
    target_yr = st.slider("Target Horizon Year", 2026, 2035, 2030)
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="SUBMIT")

def format_currency(value_millions):
    if value_millions >= 1000:
        return f"${value_millions/1000:.2f}B"
    return f"${value_millions:.1f}M"

# 5. Calculation Logic
years = np.arange(2026, 2036)

d_wt = debt_wt / 100.0
e_wt = (100 - debt_wt) / 100.0
after_tax_debt = 0.05 * (1 - 0.25)
wacc_base = ((cost_equity / 100.0) * e_wt) + (after_tax_debt * d_wt)

baseline_exposure = np.full_like(years, asset_val, dtype=float)
moderate_shock = asset_val * (1 + 0.15)**(years - 2025)
severe_shock = asset_val * (1 + 0.24)**(years - 2025)

index_target = target_yr - 2026
var_loss = moderate_shock[index_target] - asset_val
cvar_loss = severe_shock[index_target] - asset_val

# 6. KPI Dashboard Cards
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Baseline WACC</div>
            <div class="kpi-value" style="color: #38bdf8;">{wacc_base * 100:.2f}%</div>
            <div class="kpi-foot">Weighted Average Capital Cost</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Expected VaR</div>
            <div class="kpi-value" style="color: #fba518;">{format_currency(var_loss)}</div>
            <div class="kpi-foot">Moderate Risk ({target_yr})</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Tail-Risk CVaR</div>
            <div class="kpi-value" style="color: #f43f5e;">{format_currency(cvar_loss)}</div>
            <div class="kpi-foot">Severe Worst Case ({target_yr})</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">CRQC Horizon</div>
            <div class="kpi-value" style="color: #00ff66;">{max(0, 2030 - target_yr)} Yrs</div>
            <div class="kpi-foot">Shor Algorithm Window</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. High-Performance Full Interactive Graph
st.markdown("##### 📈 **QUANTUM RISK EXPOSURE PROJECTION (2026 - 2035)**")

fig = go.Figure()

# Line 1: Base Exposure
fig.add_trace(go.Scatter(
    x=years, 
    y=baseline_exposure, 
    mode='lines+markers',
    name='Base Capital Exposure',
    line=dict(color='#38bdf8', width=2, dash='dot'),
    marker=dict(size=6),
    hovertemplate='Year: %{x}<br>Base Asset: $%{y:.1f}M<extra></extra>'
))

# Line 2: Moderate Risk
fig.add_trace(go.Scatter(
    x=years, 
    y=moderate_shock, 
    mode='lines+markers',
    name='Moderate Risk Exposure',
    line=dict(color='#fba518', width=3),
    marker=dict(size=7),
    hovertemplate='Year: %{x}<br>Moderate Exposure: $%{y:.1f}M<extra></extra>'
))

# Line 3: Severe Tail Risk
fig.add_trace(go.Scatter(
    x=years, 
    y=severe_shock, 
    mode='lines+markers',
    name='Severe Tail Risk (CVaR)',
    line=dict(color='#f43f5e', width=3, dash='dash'),
    marker=dict(size=7),
    hovertemplate='Year: %{x}<br>Severe Exposure: $%{y:.1f}M<extra></extra>'
))

# Target Year Highlight Vertical Marker
fig.add_vline(
    x=target_yr, 
    line_width=2, 
    line_dash="solid", 
    line_color="#00ff66",
    annotation_text=f"Target {target_yr}",
    annotation_position="top left",
    annotation_font=dict(color="#00ff66", size=12, family="JetBrains Mono")
)

# Smooth Responsive Layout & Interactive Zoom Controls Enabled
fig.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(11, 17, 28, 0.8)',
    height=420,
    autosize=True,
    margin=dict(l=10, r=10, t=30, b=10),
    hovermode="x unified",
    hoverlabel=dict(
        bgcolor="#0b111c",
        font_size=11,
        font_family="JetBrains Mono",
        font_color="#ffffff"
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.03,
        xanchor="center",
        x=0.5,
        font=dict(size=11)
    )
)

# Full Year Range (2026 to 2035)
fig.update_xaxes(
    title_text="Year", 
    showgrid=True, 
    gridcolor='#1e293b', 
    dtick=1, 
    range=[2025.5, 2035.5]
)
fig.update_yaxes(title_text="Asset Exposure ($M)", showgrid=True, gridcolor='#1e293b')

# Interactive controls enabled for zoom/pan
st.plotly_chart(
    fig, 
    use_container_width=True, 
    config={
        'displayModeBar': True,
        'scrollZoom': True,
        'displaylogo': False
    }
)

# 8. Selected Target Year Summary Table
st.markdown(f"##### 📊 **RISK BREAKDOWN FOR SELECTED HORIZON ({target_yr})**")
breakup_df = pd.DataFrame({
    "Exposure Scenario": ["Base Capital Exposure", "Moderate Risk (Expected VaR)", "Severe Risk (Tail CVaR)"],
    "Total Exposure Value ($M)": [f"${asset_val:.1f}M", format_currency(moderate_shock[index_target]), format_currency(severe_shock[index_target])],
    "Net Risk Impact ($M)": ["$0.0M", format_currency(var_loss), format_currency(cvar_loss)]
})
st.dataframe(breakup_df, hide_index=True, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# 9. NIST Roadmap & Executive Audit Memo
col_tbl, col_audit = st.columns([1, 1])

with col_tbl:
    st.markdown("##### 🛡️ **RECOMMENDED NIST MIGRATION**")
    roadmap_df = pd.DataFrame({
        "Asset Layer": ["Key Stores", "PKI Infrastructure", "API/TLS Comm"],
        "Target Standard": ["ML-KEM (Kyber)", "ML-DSA (Dilithium)", "SLH-DSA"],
        "Status": ["CRITICAL", "HIGH", "MEDIUM"]
    })
    st.dataframe(roadmap_df, hide_index=True, use_container_width=True)

with col_audit:
    st.markdown("##### 📋 **DECODED INTELLIGENCE AUDIT**")
    st.info(f"**[EXECUTIVE SUMMARY]:** Selected target horizon **{target_yr}** projects an expected capital loss of **{format_currency(var_loss)}** under Moderate Risk and **{format_currency(cvar_loss)}** under Severe Tail Risk scenarios.")

# Footer
st.markdown("""
    <hr style="border-color: #1e293b; margin-top: 30px;">
    <div style="text-align: center; color: #475569; font-size: 0.75rem;">
        DECODED INTELLIGENCE © 2026 • QUANTITATIVE RISK SYSTEM FOR INSTITUTIONAL ASSET MANAGEMENT
    </div>
""", unsafe_allow_html=True)
