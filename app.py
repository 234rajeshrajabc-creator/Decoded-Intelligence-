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

# 2. Institutional Bloomberg Dark CSS
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
        font-
