import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="DECODED INTELLIGENCE | Bloomberg Risk Terminal", 
    page_icon="⚡",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Ultra-Pro Custom CSS (Bloomberg Dark Mode Aesthetic)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&display=swap');
    
    html, body, .stApp {
        background-color: #04060a !important;
        color: #d1d5db !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track { background: #080d1a; }
    ::-webkit-scrollbar-thumb { background: #00ff66; border-radius: 3px; }

    /* Top Bloomberg Banner */
    .bloomberg-bar {
        background: #0d1322;
        border-bottom: 2px solid #00ff66;
        padding: 10px 18px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 4px;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.15);
    }
    .brand-title {
        color: #00ff66;
        font-weight: 800;
        font-size: 1.4rem;
        letter-spacing: 2px;
    }
    .brand-subtitle {
        color: #38bdf8;
        font-size: 0.75rem;
        letter-spacing: 1px;
    }

    /* KPI Cards */
    .kpi-card {
        background: rgba(13, 19, 34, 0.85);
        border: 1px solid #1e293b;
        border-left: 4px solid #00ff66;
        border-radius: 6px;
        padding: 16px;
        transition: all 0.25s ease-in-out;
    }
    .kpi-card:hover {
        border-color: #00e5ff;
        box-shadow: 0 0 20px rgba(0, 229, 255, 0.2);
        transform: translateY(-2px);
    }
    .kpi-header {
        color: #64748b;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .kpi-num {
        font-size: 1.7rem;
        font-weight: 800;
        color: #ffffff;
        margin: 5px 0;
    }
    .kpi-sub {
        font-size: 0.68rem;
        color: #94a3b8;
    }

    div[data-testid="stSidebar"] {
        background-color: #070b14 !important;
        border-right: 1px solid #1e293b;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Live Moving Ticker Header
st.markdown("""
    <div style="background-color: #020408; border-bottom: 1px solid #1e293b; overflow: hidden; whitespace: nowrap; box-sizing: border-box; padding: 6px 0; font-size: 0.75rem;">
        <div style="display: inline-block; padding-left: 100%; animation: ticker 28s linear infinite;">
            <span style="color: #00ff66; font-weight: bold;">[DECODED INTEL FEED]</span>
            <span style="color: #94a3b8; margin: 0 15px;">BTC/USD: <b style="color: #00ff66;">$94,250.00 ▲ +2.4%</b></span>
            <span style="color: #94a3b8; margin: 0 15px;">ETH/USD: <b style="color: #00ff66;">$3,420.50 ▲ +1.8%</b></span>
            <span style="color: #94a3b8; margin: 0 15px;">PQC THREAT INDEX: <b style="color: #ff3333;">482.10 ▼ -3.2%</b></span>
            <span style="color: #94a3b8; margin: 0 15px;">US10Y YIELD: <b style="color: #00e5ff;">4.25%</b></span>
            <span style="color: #94a3b8; margin: 0 15px;">S&P 500: <b style="color: #00ff66;">5,890.12 ▲ +0.5%</b></span>
            <span style="color: #94a3b8; margin: 0 15px;">SHOR VECTOR THREAT: <b style="color: #ffaa00;">ELEVATED</b></span>
        </div>
    </div>

    <style>
    @keyframes ticker {
        0% { transform: translate3d(0, 0, 0); }
        100% { transform: translate3d(-100%, 0, 0); }
    }
    </style>

    <div class="bloomberg-bar" style="margin-top: 10px;">
        <div>
            <span class="brand-title">DECODED INTELLIGENCE</span>
            <span style="color: #64748b; margin: 0 8px;">|</span>
            <span class="brand-subtitle">QUANTITATIVE RISK & PQC DECAY TERMINAL v2.5</span>
        </div>
        <div>
            <span style="background: #ff3333; color: white; padding: 3px 8px; font-size: 0.65rem; font-weight: bold; border-radius: 2px;">WALL STREET INTEL</span>
            <span style="color: #00ff66; font-size: 0.75rem; margin-left: 10px;">● NODE ACTIVE</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Sidebar Controls
st.sidebar.markdown("### 🏢 **DECODED INTELLIGENCE // PARAMS**")
asset_value = st.sidebar.number_input("Total Digital Assets Exposure ($M)", min_value=10.0, value=1000.0, step=50.0)
cost_of_equity = st.sidebar.slider("Baseline Cost of Equity (%)", 4.0, 15.0, 8.5, 0.1)
debt_weight = st.sidebar.slider("Capital Structure: Debt Weight (%)", 10, 70, 30, 5)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ **WALL STREET THREAT MODEL**")
strategy = st.sidebar.selectbox(
    "Target Posture Strategy",
    ("Proactive Transition (ML-KEM Secure)", "Delayed Inertia (Pushed to Q4 2028)", "Systemic Shock (No Active Mitigation)")
)
target_year = st.sidebar.slider("Stress-Test Target Horizon", 2026, 2030, 2027)

# 5. Backend Engine
def run_institutional_engine(assets, year, path, baseline_equity, d_weight):
    t_factor = max(0.1, (year - 2025) * 1.4)
    tax_rate = 0.25
    cost_of_debt = 0.05
    
    if path == "Proactive Transition (ML-KEM Secure)":
        attack_surface_pb = 0.0
        wacc_premium_bps = 0
        eps_dilution_usd = 0.00
        capex_required = 12.0 if year == 2026 else 3.0
        status_code = "OPTIMAL_ALPHA"
    elif path == "Delayed Inertia (Pushed to Q4 2028)":
        attack_surface_pb = 420.0 * t_factor
        wacc_premium_bps = int(35 * t_factor)
        eps_dilution_usd = 0.04 * t_factor
        capex_required = 45.0 if year >= 2028 else 18.0
        status_code = "DEGRADED_COMPLIANCE"
    else:
        attack_surface_pb = 580.0 * t_factor
        wacc_premium_bps = int(120 * t_factor) if year < 2027 else int(180 * t_factor)
        eps_dilution_usd = 0.15 * t_factor if year < 2027 else 0.48 * t_factor
        capex_required = 290.0 if year >= 2029 else 0.0
        status_code = "CRITICAL_COMPROMISE"

    e_weight = (100 - d_weight) / 100.0
    d_weight_pct = d_weight / 100.0
    final_equity_cost = (baseline_equity + (wacc_premium_bps / 100.0)) / 100.0
    after_tax_debt = (cost_of_debt * (1 - tax_rate))
    computed_wacc = (final_equity_cost * e_weight) + (after_tax_debt * d_weight_pct)
    
    implied_balance_sheet_loss = (assets * (attack_surface_pb / 4500.0)) if attack_surface_pb > 0 else 0.0
    
    return attack_surface_pb, wacc_premium_bps, eps_dilution_usd, capex_required, computed_wacc * 100, implied_balance_sheet_loss, status_code

pb_exposed, bps_premium, eps_diluted, capex_vol, repriced_wacc, metrics_loss, code = run_institutional_engine(
    asset_value, target_year, strategy, cost_of_equity, debt_weight
)

# 6. KPI Grid
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
        <div class="kpi-card" style="border-left-color: {'#00ff66' if pb_exposed == 0 else '#ff3333'};">
            <div class="kpi-header">Quantum Surface Exposure</div>
            <div class="kpi-num" style="color: {'#00ff66' if pb_exposed == 0 else '#ff3333'};">{pb_exposed:.1f} PB</div>
            <div class="kpi-sub">HNDL Vector Data Threat</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="kpi-card" style="border-left-color: #00e5ff;">
            <div class="kpi-header">Re-Priced WACC Risk</div>
            <div class="kpi-num" style="color: #00e5ff;">{repriced_wacc:.2f}%</div>
            <div class="kpi-sub">+{bps_premium} bps Equity Risk Add-on</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="kpi-card" style="border-left-color: {'#00ff66' if eps_diluted == 0 else '#ffaa00'};">
            <div class="kpi-header">Quarterly EPS Dilution</div>
            <div class="kpi-num" style="color: {'#00ff66' if eps_diluted == 0 else '#ffaa00'};">-${eps_diluted:.2f}</div>
            <div class="kpi-sub">Impact on Capital Velocity</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
        <div class="kpi-card" style="border-left-color: #ffffff;">
            <div class="kpi-header">Required CapEx Allocation</div>
            <div class="kpi-num">${capex_vol:.1f}M</div>
            <div class="kpi-sub">Spot Mitigation Capital</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. Analytics & Charts
col_left, col_right = st.columns([1.2, 0.8])

with col_left:
    st.markdown("##### 📈 **DECODED INTELLIGENCE // RISK CURVE VELOCITY**")
    years_arr = ["2026", "2027", "2028", "2029", "2030"]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years_arr, y=[0, 0, 0, 0, 0], name='Proactive (ML-KEM)', line=dict(color='#00ff66', width=3)))
    fig.add_trace(go.Scatter(x=years_arr, y=[420, 890, 1280, 1280, 1280], name='Delayed Inertia', line=dict(color='#ffaa00', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=years_arr, y=[420, 1100, 2400, 3100, 4500], name='Systemic Shock', line=dict(color='#ff3333', width=3)))
    
    fig.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(7, 11, 20, 0.8)',
        xaxis=dict(showgrid=True, gridcolor='#1e293b'),
        yaxis=dict(title="Petabytes Exposed", showgrid=True, gridcolor='#1e293b'),
        margin=dict(l=20, r=20, t=20, b=20),
        height=320,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("##### 🎛️ **SENSITIVITY MATRIX SHOCK GRID**")
    sensitivity_data = pd.DataFrame({
        "Asset Base": [f"${asset_value:.0f}M", f"${asset_value:.0f}M", f"${asset_value:.0f}M"],
        "Threat Vector": ["Proactive Curve", "Inertia Delay Path", "Shor Matrix System Shock"],
        "Implied Loss": [
            "$0.00 (Immune)", 
            f"${metrics_loss*0.65:.1f} Million", 
            f"${metrics_loss:.1f} Million"
        ]
    })
    st.dataframe(sensitivity_data, hide_index=True, use_container_width=True)

# 8. Diagnostic Memo
st.markdown("##### 📋 **EXECUTIVE MEMORANDUM // DECODED INTELLIGENCE AUDIT**")

if code == "OPTIMAL_ALPHA":
    st.success(f"**[DECODED INTEL - OPTIMAL ALPHA LOCK]** Capital architecture is fully optimized against quantum decryption vectors. Repriced WACC: {repriced_wacc:.2f}%. Zero balance sheet risk recorded.")
elif code == "DEGRADED_COMPLIANCE":
    st.warning(f"**[DECODED INTEL - DEGRADED COMPLIANCE]** Infrastructure inertia active for horizon {target_year}. Projected unpriced corporate asset vulnerability accumulation: **${metrics_loss:.2f} Million**.")
else:
    st.error(f"**[DECODED INTEL - CRITICAL SYSTEMIC SHOCK]** ZERO mitigation strategy exposes total corporate assets. Projected balance sheet exposure: **${metrics_loss:.2f} Million** by {target_year}.")

# 9. Institutional Footer
st.markdown("""
    <div style="border-top: 1px solid #1e293b; padding-top: 15px; margin-top: 30px; text-align: center; color: #475569; font-size: 0.7rem;">
        POWERED BY <strong>DECODED INTELLIGENCE</strong> INSTITUTIONAL QUANT ENGINE • COMPLIANT WITH NIST SP 800-224 STANDARDS
    </div>
""", unsafe_allow_html=True)
