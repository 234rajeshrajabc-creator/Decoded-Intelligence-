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

# 2. Institutional Dark Theme CSS
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

    /* Top Header Bar */
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

    /* KPI Cards */
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
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("""
    <div class="brand-container">
        <div>
            <span class="brand-title">DECODED INTELLIGENCE</span>
            <span style="color: #475569; margin: 0 8px;">/</span>
            <span style="color: #94a3b8; font-size: 0.85rem; font-weight: 600;">QUANTUM DECAY & RISK PROJECTION ENGINE</span>
        </div>
        <div>
            <span class="brand-tag">NIST SP 800-224 COMPLIANT</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Sidebar Controls
st.sidebar.markdown("### 🏢 **INSTITUTIONAL PARAMS**")
asset_val = st.sidebar.number_input("Total Asset Exposure ($M)", min_value=10.0, value=1000.0, step=50.0)
cost_equity = st.sidebar.slider("Cost of Equity (%)", 4.0, 15.0, 8.5, 0.1)
debt_wt = st.sidebar.slider("Debt Weight (%)", 10, 70, 30, 5)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎯 **TIMELINE HORIZON**")
target_yr = st.sidebar.slider("Target Horizon Year", 2026, 2035, 2028)

def format_currency(value_millions):
    if value_millions >= 1000:
        return f"${value_millions/1000:.2f}B"
    return f"${value_millions:.1f}M"

# 5. Risk Computation Engine
years = np.arange(2026, 2036)
years_left = max(1, target_yr - 2025)

d_wt = debt_wt / 100.0
e_wt = (100 - debt_wt) / 100.0
after_tax_debt = 0.05 * (1 - 0.25)
wacc_base = ((cost_equity / 100.0) * e_wt) + (after_tax_debt * d_wt)

decay_rate = 0.18
quantum_risk_projection = asset_val * (1 + decay_rate)**(years - 2025) - asset_val
baseline_exposure = np.full_like(years, asset_val, dtype=float)

index_target = target_yr - 2026
var_loss = quantum_risk_projection[index_target]
cvar_loss = var_loss * 1.25

# 6. KPI Dashboard
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
            <div class="kpi-label">Value at Risk (VaR)</div>
            <div class="kpi-value" style="color: #f43f5e;">{format_currency(var_loss)}</div>
            <div class="kpi-foot">Max Expected Loss ({target_yr})</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Conditional VaR (CVaR)</div>
            <div class="kpi-value" style="color: #ff3333;">{format_currency(cvar_loss)}</div>
            <div class="kpi-foot">Tail-Risk Worst-Case Loss</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">CRQC Estimated Horizon</div>
            <div class="kpi-value" style="color: #00ff66;">{max(0, 2030 - target_yr)} Yrs</div>
            <div class="kpi-foot">Shor Algorithm Window</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. Safe Plotly Analytics
col_left, col_right = st.columns([1.3, 0.7])

with col_left:
    st.markdown("##### 📈 **QUANTUM RISK DECAY PROJECTION (2026 - 2035)**")
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years, 
        y=baseline_exposure, 
        mode='lines',
        name='Base Capital Exposure',
        line=dict(color='#38bdf8', width=2, dash='dot')
    ))

    fig.add_trace(go.Scatter(
        x=years, 
        y=quantum_risk_projection + asset_val, 
        mode='lines+markers',
        name='Quantum Risk Exposure',
        line=dict(color='#f43f5e', width=3),
        marker=dict(size=6, color='#f43f5e')
    ))

    # Simplified Layout Parameters
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(11, 17, 28, 0.8)',
        height=340,
        margin=dict(l=10, r=10, t=10, b=10)
    )
    
    fig.update_xaxes(title_text="Year", showgrid=True, gridcolor='#1e293b', dtick=1)
    fig.update_yaxes(title_text="Asset Value ($M)", showgrid=True, gridcolor='#1e293b')

    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("##### 🛡️ **RECOMMENDED NIST MIGRATION**")
    
    roadmap_df = pd.DataFrame({
        "Asset Layer": ["Key Stores", "PKI Infrastructure", "API/TLS Comm"],
        "Target Standard": ["ML-KEM (Kyber)", "ML-DSA (Dilithium)", "SLH-DSA"],
        "Status": ["CRITICAL", "HIGH", "MEDIUM"]
    })
    st.dataframe(roadmap_df, hide_index=True, use_container_width=True)

# 8. Audit Memo
st.markdown("##### 📋 **DECODED INTELLIGENCE AUDIT SUMMARY**")
st.info(f"**[EXECUTIVE SUMMARY]:** Projected risk analysis shows potential capital impact reaching **{format_currency(var_loss)}** by **{target_yr}**. Transitioning to NIST Post-Quantum Cryptography standards recommended immediately.")

# Footer
st.markdown("""
    <hr style="border-color: #1e293b; margin-top: 30px;">
    <div style="text-align: center; color: #475569; font-size: 0.75rem;">
        DECODED INTELLIGENCE © 2026 • QUANTITATIVE RISK SYSTEM FOR INSTITUTIONAL ASSET MANAGEMENT
    </div>
""", unsafe_allow_html=True)
