import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Page Configuration & Institutional Layout
st.set_page_config(
    page_title="Decoded Intelligence | PQC Risk Terminal", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. Hyper-Pro Custom CSS Engine (Bloomberg Terminal Aesthetics & Smooth Animations)
st.markdown("""
    <style>
    /* Full Dark Cyber Mode Background */
    body, .main, .reportview-container {
        background-color: #05070a !important;
        color: #e2e8f0 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Fade-in Animation for Ultra Smooth Presentation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .stApp {
        animation: fadeIn 0.8s ease-out-all;
    }

    /* Next-Gen KPI Metric Cards Styling */
    .kpi-container {
        background: linear-gradient(135deg, #0d1527 0%, #070a12 100%);
        border: 1px solid #1e293b;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .kpi-container:hover {
        transform: scale(1.02);
        border-color: #00ff66;
    }
    .kpi-title {
        color: #94a3b8;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 8px;
    }
    .kpi-value {
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    /* Custom Sidebar Aesthetics */
    .css-11v0wun, .css-6qob1r {
        background-color: #090d16 !important;
        border-right: 1px solid #1e293b !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Main Bloomberg-Style Terminal Header
st.markdown("""
    <div style='border-bottom: 2px solid #00ff66; padding-bottom: 10px; margin-bottom: 25px;'>
        <span style='background-color: #ff3333; color: white; padding: 3px 8px; font-size: 0.7rem; font-weight: bold; border-radius: 3px; vertical-align: middle;'>LIVE INTEL</span>
        <h1 style='display: inline; margin-left: 10px; color: #ffffff; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;'>DECODED INTELLIGENCE // RISK TERMINAL v1.2</h1>
        <p style='color: #475569; font-size: 0.8rem; margin-top: 5px; margin-left: 5px;'>QUANTITATIVE CRYPTOGRAPHIC DECAY ENGINE • DATA NODE COMPLIANCE: NIST SP 800-224 / S&P GLOBAL INDEX</p>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTROL PANEL (ADVANCED PARAMS) ---
st.sidebar.markdown("### 🏢 CORPORATE STRUCTURE")
asset_value = st.sidebar.number_input("Total Digital Assets Exposure (USD Millions)", min_value=10.0, value=1000.0, step=50.0)
cost_of_equity = st.sidebar.slider("Baseline Cost of Equity (%)", 4.0, 15.0, 8.5, 0.1)
debt_weight = st.sidebar.slider("Capital Structure: Debt Weight (%)", 10, 70, 30, 5)

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ RISK RADAR STRATEGY")
strategy = st.sidebar.selectbox(
    "Select Target Operational Posture",
    ("Proactive Transition (ML-KEM Secure)", "Delayed Inertia (Pushed to Q4 2028)", "Systemic Shock (No Active Mitigation)")
)
target_year = st.sidebar.slider("Stress-Test Target Horizon", 2026, 2030, 2027)

# --- BACKEND QUANTITATIVE LOGIC ENGINE ---
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
    else:  # Systemic Shock Case
        attack_surface_pb = 580.0 * t_factor
        wacc_premium_bps = int(120 * t_factor) if year < 2027 else int(180 * t_factor)
        eps_dilution_usd = 0.15 * t_factor if year < 2027 else 0.48 * t_factor
        capex_required = 290.0 if year >= 2029 else 0.0
        status_code = "CRITICAL_COMPROMISE"

    # Compute Re-priced WACC Formula (From Page 21 of Report)
    e_weight = (100 - d_weight) / 100.0
    d_weight_pct = d_weight / 100.0
    final_equity_cost = (baseline_equity + (wacc_premium_bps / 100.0)) / 100.0
    after_tax_debt = (cost_of_debt * (1 - tax_rate))
    computed_wacc = (final_equity_cost * e_weight) + (after_tax_debt * d_weight_pct)
    
    implied_balance_sheet_loss = (assets * (attack_surface_pb / 4500.0)) if attack_surface_pb > 0 else 0.0
    
    return attack_surface_pb, wacc_premium_bps, eps_dilution_usd, capex_required, computed_wacc * 100, implied_balance_sheet_loss, status_code

# Execute Data Logic
pb_exposed, bps_premium, eps_diluted, capex_vol, repriced_wacc, metrics_loss, code = run_institutional_engine(
    asset_value, target_year, strategy, cost_of_equity, debt_weight
)

# --- PROP LAYOUT DISPLAY: RAW MATRICES ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class='kpi-container'>
            <div class='kpi-title'>🛡️ Quantum Attack Surface</div>
            <div class='kpi-value' style='color: {"#00ff66" if pb_exposed == 0 else "#ff3333"};'>{pb_exposed:.1f} PB</div>
            <div style='font-size: 0.7rem; margin-top: 5px; color: #64748b;'>HNDL Vector Exposure Area</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class='kpi-container'>
            <div class='kpi-title'>📊 Re-Priced WACC Baseline</div>
            <div class='kpi-value' style='color: #00e5ff;'>{repriced_wacc:.2f}%</div>
            <div style='font-size: 0.7rem; margin-top: 5px; color: #ffaa00;'>+{bps_premium} bps Equity Add-on</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class='kpi-container'>
            <div class='kpi-title'>📉 Quarterly EPS Dilution</div>
            <div class='kpi-value' style='color: {"#00ff66" if eps_diluted == 0 else "#f43f5e"};'>-${eps_diluted:.2f}</div>
            <div style='font-size: 0.7rem; margin-top: 5px; color: #64748b;'>Impact on Asset Velocity</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class='kpi-container'>
            <div class='kpi-title'>⚡ Spot Procurement CapEx</div>
            <div class='kpi-value' style='color: #ffffff;'>${capex_vol:.1f}M</div>
            <div style='font-size: 0.7rem; margin-top: 5px; color: #64748b;'>Required Mitigation Capital</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- HIGH-TECH CHARTING SUITE ---
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem; letter-spacing: 0.05em;'>📈 CRYPTOGRAPHIC DECAY VELEOCITY CURVE</h3>", unsafe_allow_html=True)
    years_arr = ["2026", "2027", "2028", "2029", "2030"]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years_arr, y=[0, 0, 0, 0, 0], name='Proactive (ML-KEM)', line=dict(color='#00ff66', width=3)))
    fig.add_trace(go.Scatter(x=years_arr, y=[420, 890, 1280, 1500, 1900], name='Delayed Inertia', line=dict(color='#ffaa00', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=years_arr, y=[580, 1100, 2400, 3100, 4500], name='Systemic Shock', line=dict(color='#ff3333', width=4)))
    
    fig.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Timeline Target", 
        yaxis_title="Petabytes Exposed",
        margin=dict(l=20, r=20, t=20, b=20),
        height=340
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem; letter-spacing: 0.05em;'>🎛️ PORTFOLIO SENSITIVITY SHOCK GRID</h3>", unsafe_allow_html=True)
    sensitivity_data = pd.DataFrame({
        "Asset Group Base": [f"${asset_value:.0f}M", f"${asset_value:.0f}M", f"${asset_value:.0f}M"],
        "Threat Model Applied": ["Proactive Curve", "Inertia Delay Path", "Shor Matrix System Shock"],
        "Implied Balance Sheet Shock": [
            "$0.00 (Protected)", 
            f"${metrics_loss*0.65:.1f} Million", 
            f"${metrics_loss:.1f} Million (Extreme Risk)"
        ]
    })
    st.table(sensitivity_data)

# --- IF-THEN ADVANCED SYSTEM DIAGNOSTIC MEMOS ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem; letter-spacing: 0.05em;'>📋 EXECUTABLE DIAGNOSTIC MEMO</h3>", unsafe_allow_html=True)

if code == "OPTIMAL_ALPHA":
    st.markdown(f"""
        <div style='background-color: rgba(0, 255, 102, 0.05); border: 1px solid #00ff66; padding: 15px; border-radius: 6px;'>
            <strong style='color: #00ff66;'>[CRITICAL POSTURE: OPTIMAL LOCK]</strong> Capital architecture fully optimized. Repriced WACC settled at <strong>{repriced_wacc:.2f}%</strong>. System balance sheet reflects absolute immunity against legacy encryption compromises.
        </div>
    """, unsafe_allow_html=True)
elif code == "DEGRADED_COMPLIANCE":
    st.markdown(f"""
        <div style='background-color: rgba(255, 170, 0, 0.05); border: 1px solid #ffaa00; padding: 15px; border-radius: 6px;'>
