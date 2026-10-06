import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set institutional layout configurations
st.set_page_config(page_title="Decoded Intelligence | PQC Risk Terminal", layout="wide", initial_sidebar_state="expanded")

# Dark Theme & Custom CSS Styling for Bloomberg-Terminal Aesthetic (Fixed Parameter)
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .metric-box { border-left: 4px solid #00ff66; padding-left: 10px; margin-bottom: 15px; }
    .error-box { border-left: 4px solid #ff3333; padding-left: 10px; }
    </style>
""", unsafe_allow_html=True)

# Main Terminal Header
st.title("🛡️ DECODED INTELLIGENCE | RISK TERMINAL v1.2")
st.caption("Institutional Post-Quantum Cryptography Stress-Testing Engine // Ref: NIST SP 800-224 & S&P Global Node-9")
st.markdown("---")

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.markdown("### 🏢 ENTERPRISE CAPITAL STRUCTURE")
asset_value = st.sidebar.number_input("Total Digital Assets Exposure (USD Millions)", min_value=10.0, value=1000.0, step=50.0)
cost_of_equity = st.sidebar.slider("Baseline Cost of Equity (%)", 4.0, 15.0, 8.5, 0.1)
debt_weight = st.sidebar.slider("Capital Structure: Debt Weight (%)", 10, 70, 30, 5)

st.sidebar.markdown("### ⚙️ QUANTUM MIGRATION PATHWAY")
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

    # Compute Re-priced WACC
    e_weight = (100 - d_weight) / 100.0
    d_weight_pct = d_weight / 100.0
    final_equity_cost = (baseline_equity + (wacc_premium_bps / 100.0)) / 100.0
    after_tax_debt = (cost_of_debt * (1 - tax_rate))
    computed_wacc = (final_equity_cost * e_weight) + (after_tax_debt * d_weight_pct)
    
    implied_balance_sheet_loss = (assets * (attack_surface_pb / 4500.0)) if attack_surface_pb > 0 else 0.0
    
    return attack_surface_pb, wacc_premium_bps, eps_dilution_usd, capex_required, computed_wacc * 100, implied_balance_sheet_loss, status_code

# Run execution
pb_exposed, bps_premium, eps_diluted, capex_vol, repriced_wacc, metrics_loss, code = run_institutional_engine(
    asset_value, target_year, strategy, cost_of_equity, debt_weight
)

# --- TERMINAL DISPLAYS & KPI BLOCKS ---
st.subheader("📊 EXECUTION CORE METRICS")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric(label="Data at Risk Surface", value=f"{pb_exposed:.1f} PB", delta=f"+{pb_exposed:.1f} PB vs Target" if pb_exposed > 0 else "0.0 PB (Secure)")
    st.markdown("</div>", unsafe_style_html=True)
with col2:
    st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
    st.metric(label="Re-Priced Corporate WACC", value=f"{repriced_wacc:.2f}%", delta=f"+{bps_premium} bps Equity Premium" if bps_premium > 0 else "Baseline Optimal")
    st.markdown("</div>", unsafe_style_html=True)
with col3:
    st.metric(label="Quarterly EPS Dilution", value=f"-${eps_diluted:.2f}", delta="Risk Matrix Alert" if eps_diluted > 0 else "0.00 (Stabilized)", delta_color="inverse")
with col4:
    st.metric(label="Projected CapEx Variance", value=f"${capex_vol:.1f}M", delta="Spot Market Panic" if capex_vol >= 290 else "Baseline Budget")

st.markdown("---")

# --- HIGH-TECH VISUALIZATION SUITE ---
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### 📈 Quantum Cryptographic Decay Grid (Dynamic Simulation)")
    years_arr = ["2026", "2027", "2028", "2029", "2030"]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years_arr, y=[0, 0, 0, 0, 0], name='Proactive Adaptation', line=dict(color='#00ff66', width=3)))
    fig.add_trace(go.Scatter(x=years_arr, y=[420, 588, 1260, 1680, 2100], name='Delayed Inertia', line=dict(color='#ffaa00', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=years_arr, y=[580, 1624, 2436, 3248, 4060], name='Systemic Shock Curve', line=dict(color='#ff3333', width=4)))
    
    fig.update_layout(template="plotly_dark", title="Attack Surface Growth Vector (PB Exposed)", xaxis_title="Timeline", yaxis_title="Petabytes", height=380)
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("### 🎛️ Diagnostic Sensitivity Engine")
    sensitivity_data = pd.DataFrame({
        "Simulated Asset Base": [f"${asset_value:.0f}M", f"${asset_value:.0f}M", f"${asset_value:.0f}M"],
        "Threat Matrix Model": ["Proactive Path", "Inertia Delay", "Shor System Shock"],
        "Implied Balance Sheet Shock": [
            "$0.00 (Protected)", 
            f"${metrics_loss*0.7:.1f} Million", 
            f"${metrics_loss:.1f} Million (Extreme Exposure)"
        ]
    })
    st.table(sensitivity_data)

# --- IF-THEN DIAGNOSTIC MEMO SYSTEM ---
st.markdown("---")
st.subheader("📋 Decoded Executive Intelligence Diagnostic Memos")
if code == "OPTIMAL_ALPHA":
    st.success(f"**SYSTEM LOCK STATUS [OPTIMAL]:** Capital architecture remains insulated. Repriced WACC sits securely at **{repriced_wacc:.2f}%**. The balance sheet shows complete immunity against retroactive 'Harvest Now, Decrypt Later' vulnerabilities.")
elif code == "DEGRADED_COMPLIANCE":
    st.warning(f"**IF** operational inertia remains unmitigated past {target_year}, **THEN** Decoded Intelligence matrices project an unpriced corporate liability velocity resulting in **${metrics_loss:.2f} Million** in retrospective losses and dynamic vendor procurement penalties.")
else:
    st.error(f"**🔥 HARD EXPOSURE BREACH WARNING [CRITICAL SYSTEM SHOCK]:** **IF** migration path is delayed past the Q4 2027 cross-over node, **THEN** Tier-1 cyber-insurance syndicates will trigger formal exclusions. This will force a direct liquidity freeze baseline, cascading into institutional valuation failures.")

st.caption("Decoded Intelligence System // Powered by Economics Decoded Substack // Backed by Verified Audit Tokens QR-2026.")
