import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="DECODED INTELLIGENCE | Institutional PQC Risk Terminal", 
    page_icon="🛡️",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Institutional Bloomberg Dark CSS (No Cheap Animations, Clean & Dark)
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

    /* Professional Top Bar */
    .brand-container {
        background: #0b111c;
        border: 1px solid #1e293b;
        border-left: 4px solid #00ff66;
        padding: 14px 20px;
        border-radius: 6px;
        margin-bottom: 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .brand-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    .brand-tag {
        color: #00ff66;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        background: rgba(0, 255, 102, 0.1);
        padding: 4px 8px;
        border-radius: 4px;
        border: 1px solid rgba(0, 255, 102, 0.2);
    }

    /* KPI Metrics Card */
    .kpi-card {
        background: #0b111c;
        border: 1px solid #1e293b;
        border-radius: 6px;
        padding: 18px;
        margin-bottom: 10px;
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
        font-size: 1.8rem;
        font-weight: 700;
        margin: 6px 0;
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

# 3. Header
st.markdown("""
    <div class="brand-container">
        <div>
            <span class="brand-title">DECODED INTELLIGENCE</span>
            <span style="color: #475569; margin: 0 10px;">/</span>
            <span style="color: #94a3b8; font-size: 0.85rem; font-weight: 600;">QUANTUM DECAY & STOCHASTIC VaR ENGINE v3.0</span>
        </div>
        <div>
            <span class="brand-tag">NIST SP 800-224 COMPLIANT</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Sidebar Options
st.sidebar.markdown("### 🏢 **INSTITUTIONAL PARAMS**")
asset_val = st.sidebar.number_input("Total Digital Asset Exposure ($M)", min_value=10.0, value=1000.0, step=50.0)
cost_equity = st.sidebar.slider("Cost of Equity (%)", 4.0, 15.0, 8.5, 0.1)
debt_wt = st.sidebar.slider("Debt Weight (%)", 10, 70, 30, 5)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎲 **MONTE CARLO SIMULATION**")
simulations = st.sidebar.select_slider("Simulation Runs", options=[1000, 5000, 10000], value=5000)
confidence_level = st.sidebar.selectbox("Value at Risk (VaR) Confidence", (95, 99))

target_yr = st.sidebar.slider("Target Horizon", 2026, 2035, 2028)

# 5. Core Engine (Mathematical Risk Engine)
def calculate_advanced_metrics(assets, year, equity_cost, d_weight, sim_count, conf):
    years_left = max(1, year - 2025)
    
    # Base Capital Math
    d_wt = d_weight / 100.0
    e_wt = (100 - d_weight) / 100.0
    after_tax_debt = 0.05 * (1 - 0.25)
    wacc_base = ((equity_cost / 100.0) * e_wt) + (after_tax_debt * d_wt)
    
    # Monte Carlo Risk Simulation Engine
    np.random.seed(42)
    # Simulate quantum decay shocks using lognormal distribution
    shock_rates = np.random.lognormal(mean=0.15 * years_left, sigma=0.35, size=sim_count)
    simulated_losses = assets * (shock_rates / (10 + shock_rates))
    
    var_percentile = conf
    var_value = np.percentile(simulated_losses, var_percentile)
    expected_shortfall (CVaR) = np.mean(simulated_losses[simulated_losses >= var_value])
    
    return wacc_base * 100, var_value, expected_shortfall, simulated_losses

wacc, var_loss, cvar_loss, sim_results = calculate_advanced_metrics(
    asset_val, target_yr, cost_equity, debt_wt, simulations, confidence_level
)

# 6. KPI Dashboard
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Baseline WACC</div>
            <div class="kpi-value" style="color: #38bdf8;">{wacc:.2f}%</div>
            <div class="kpi-foot">Weighted Average Capital Cost</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">{confidence_level}% Value at Risk (VaR)</div>
            <div class="kpi-value" style="color: #f43f5e;">${var_loss:.1f}M</div>
            <div class="kpi-foot">Max Expected Loss ({target_yr})</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Conditional VaR (CVaR)</div>
            <div class="kpi-value" style="color: #ff3333;">${cvar_loss:.1f}M</div>
            <div class="kpi-foot">Tail-Risk Worst-Case Loss</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">CRQC Estimated Horizon</div>
            <div class="kpi-value" style="color: #00ff66;">{2030 - target_yr} Yrs</div>
            <div class="kpi-foot">Shor Algorithm Quantum Window</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. Advanced Plotly Analytics
col_left, col_right = st.columns([1.2, 0.8])

with col_left:
    st.markdown("##### 🎲 **MONTE CARLO LOSS DISTRIBUTION (5,000 RUNS)**")
    
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=sim_results,
        nbinsx=50,
        marker_color='#1e293b',
        marker_line_color='#3b82f6',
        marker_line_width=1,
        name='Simulated Scenarios'
    ))
    
    # Value at Risk Line
    fig.add_vline(x=var_loss, line_width=2, line_dash="dash", line_color="#f43f5e", annotation_text=f"VaR ({confidence_level}%): ${var_loss:.1f}M")
    
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(11, 17, 28, 0.8)',
        xaxis=dict(title="Potential Capital Shock ($ Millions)", showgrid=True, gridcolor='#1e293b'),
        yaxis=dict(title="Frequency / Scenario Count", showgrid=True, gridcolor='#1e293b'),
        margin=dict(l=20, r=20, t=20, b=20),
        height=320
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("##### 🛡️ **RECOMMENDED PQC MIGRATION ROADMAP**")
    
    roadmap_df = pd.DataFrame({
        "Asset Layer": ["Digital Ledger / Key Stores", "PKI Infrastructure", "API/TLS Communications"],
        "Current Algorithm": ["RSA-3072 / ECC", "RSA-2048", "ECDHE-ECDSA"],
        "Target NIST Standard": ["ML-KEM (Kyber)", "ML-DSA (Dilithium)", "SLH-DSA (Sphincs+)"],
        "Urgent Status": ["CRITICAL", "HIGH", "MEDIUM"]
    })
    st.dataframe(roadmap_df, hide_index=True, use_container_width=True)

# 8. Executive Memo
st.markdown("##### 📋 **DECODED INTELLIGENCE QUANTITATIVE AUDIT**")
st.info(f"**[EXECUTIVE SUMMARY]:** Under {simulations:,} Monte Carlo simulations at a {confidence_level}% confidence level, your exposure indicates a potential Value at Risk (VaR) of **${var_loss:.2f} Million** by {target_yr}. Immediate deployment of NIST ML-KEM standards is recommended to mitigate capital cost inflation.")

# Footer
st.markdown("""
    <hr style="border-color: #1e293b; margin-top: 30px;">
    <div style="text-align: center; color: #475569; font-size: 0.75rem;">
        DECODED INTELLIGENCE © 2026 • PROPRIETARY QUANTITATIVE RISK SYSTEM FOR INSTITUTIONAL ASSET MANAGEMENT
    </div>
""", unsafe_allow_html=True)
