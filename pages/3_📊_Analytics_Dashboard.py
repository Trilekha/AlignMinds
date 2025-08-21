# Analytics Dashboard Page for AlignMinds
import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from ui.styles import apply_enhanced_styles
from ui.components import render_analytics_dashboard

# Configure page
st.set_page_config(
    page_title="Analytics Dashboard - AlignMinds",
    page_icon="📊",
    layout="wide",
)

# Apply enhanced styles
apply_enhanced_styles()

# Render analytics dashboard content
render_analytics_dashboard() 