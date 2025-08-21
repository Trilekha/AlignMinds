"""
Enhanced CSS styles for AlignMinds application
"""

ENHANCED_CSS = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated Background for Home Page */
    .home-page-background {
        position: fixed !important;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: #0f172a;
        z-index: -10 !important;
        pointer-events: none;
    }
    
    .home-page-background::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        z-index: -10;
    }
    
    .home-page-background::after {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.1) 0%, transparent 50%);
        animation: backgroundFlow 20s ease-in-out infinite;
        z-index: -9;
        pointer-events: none;
    }
    
    @keyframes backgroundFlow {
        0%, 100% {
            transform: translate(-50%, -50%) rotate(0deg) scale(1);
        }
        33% {
            transform: translate(-45%, -55%) rotate(120deg) scale(1.1);
        }
        66% {
            transform: translate(-55%, -45%) rotate(240deg) scale(0.9);
        }
    }
    
    /* Animated Gradient Orbs */
    .animated-bg-orbs {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .animated-bg-orbs::before {
        content: '';
        position: absolute;
        top: 10%;
        left: 10%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.4) 0%, transparent 70%);
        border-radius: 50%;
        animation: float1 15s ease-in-out infinite;
        filter: blur(40px);
    }
    
    .animated-bg-orbs::after {
        content: '';
        position: absolute;
        bottom: 10%;
        right: 10%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(236, 72, 153, 0.3) 0%, transparent 70%);
        border-radius: 50%;
        animation: float2 18s ease-in-out infinite reverse;
        filter: blur(50px);
    }
    
    @keyframes float1 {
        0%, 100% {
            transform: translate(0, 0) scale(1);
        }
        33% {
            transform: translate(30px, -30px) scale(1.1);
        }
        66% {
            transform: translate(-20px, 20px) scale(0.9);
        }
    }
    
    @keyframes float2 {
        0%, 100% {
            transform: translate(0, 0) scale(1);
        }
        50% {
            transform: translate(-40px, -20px) scale(1.2);
        }
    }
    
    /* Default styling for other pages */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        position: relative;
        z-index: 10;
    }
    
    /* Ensure main content is visible on home page */
    .main {
        position: relative;
        z-index: 10;
    }
    
    /* Header Styling - Home page version */
    body.home-page .main-header {
        background: transparent;
        backdrop-filter: none;
        border: 1px solid rgba(0, 0, 0, 0.3);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 0 0 2rem 0;
        box-shadow: none;
        position: relative;
        overflow: hidden;
        z-index: 12;
    }
    
    /* Header Styling - Other pages version */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 0 0 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-weight: 700;
        font-size: 2.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
    }
    
    /* Clean Professional Sidebar - No Gaps */
    section[data-testid="stSidebar"] {
        background: #2d3748 !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background: #2d3748 !important;
        padding-top: 50px !important; /* Minimal header space */
    }
    
    /* Tight AlignMinds header */
    section[data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 50px;
        background: #2d3748;
        border-bottom: 1px solid #4a5568;
        z-index: 10;
    }
    
    section[data-testid="stSidebar"]::after {
        content: "⚡ AlignMinds";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 50px;
        background: #2d3748;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        padding: 0 1rem;
        gap: 0.5rem;
        border-bottom: 1px solid #4a5568;
        z-index: 11;
    }
    
    /* Hide custom headers */
    .professional-sidebar-header {
        display: none !important;
    }
    
    /* Position the original close button above the header */
    section[data-testid="stSidebar"] button[data-testid="baseButton-header"],
    section[data-testid="stSidebar"] button[kind="header"],
    section[data-testid="stSidebar"] > div > div > button:first-child {
        position: absolute !important;
        top: 55px !important;
        right: 10px !important;
        z-index: 1000 !important;
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 6px !important;
        color: white !important;
        width: 30px !important;
        height: 30px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    section[data-testid="stSidebar"] button[data-testid="baseButton-header"]:hover,
    section[data-testid="stSidebar"] button[kind="header"]:hover,
    section[data-testid="stSidebar"] > div > div > button:first-child:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.3) !important;
    }
    
    /* Smooth navigation - no gaps */
    section[data-testid="stSidebar"] nav[role="navigation"] {
        padding: 0 !important;
        margin: 0 !important;
        background: #2d3748 !important;
    }
    
    /* Streamlined navigation links */
    section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] {
        background: transparent !important;
        border: none !important;
        border-radius: 8px !important;
        margin: 1px 1rem !important;
        padding: 12px 16px !important;
        color: #cbd5e1 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        text-decoration: none !important;
        transition: background 0.15s ease, color 0.15s ease !important;
        display: flex !important;
        align-items: center !important;
    }
    
    /* Smooth hover */
    section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"]:hover {
        background: #4a5568 !important;
        color: #ffffff !important;
    }
    
    /* Basic active highlighting */
    section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"][aria-current="page"] {
        background: #ffffff !important;
        color: #2d3748 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    
    /* Icons */
    section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] span {
        color: inherit !important;
        opacity: 1 !important;
    }
    
    section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] span:first-child {
        margin-right: 0.75rem !important;
        font-size: 1rem !important;
    }
    
    /* Make sure sidebar toggle button is visible */
    button[data-testid="collapsedControl"] {
        display: block !important;
        background: white !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        color: #64748b !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        position: fixed !important;
        top: 1rem !important;
        left: 1rem !important;
        z-index: 999 !important;
        width: 40px !important;
        height: 40px !important;
    }
    
    button[data-testid="collapsedControl"]:hover {
        background: #f8fafc !important;
        border-color: #cbd5e1 !important;
        color: #1e293b !important;
    }
    
            /* Card Components - Default for non-home pages */
    .custom-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e2e8f0;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }

    .custom-card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        transform: translateY(-2px);
    }

    /* Progress Bar Enhancements */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 50%, #ec4899 100%);
        border-radius: 10px;
    }
    
    .progress-container {
        background: #f1f5f9;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    /* Metrics Styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border: 1px solid #cbd5e1;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #1e293b;
        font-weight: 600;
    }
    
    /* Tab Enhancements */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #f8fafc;
        padding: 4px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 8px;
        padding: 0 20px;
        background: transparent;
        border: none;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(79, 70, 229, 0.1);
        transform: translateY(-1px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white !important;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
        transform: translateY(-2px);
    }
    
    /* Tab content transitions */
    .stTabs [data-baseweb="tab-panel"] {
        animation: fadeInTab 0.4s ease-out;
        opacity: 1;
        transform: translateY(0);
    }
    
    /* Tab content fade animation */
    @keyframes fadeInTab {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Smooth tab indicator */
    .stTabs [data-baseweb="tab"]::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"]::before {
        background: rgba(255, 255, 255, 0.3);
    }
    
    /* Enhanced tab text transitions */
    .stTabs [data-baseweb="tab"] span {
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] span {
        font-weight: 600;
    }
    
    /* Button Enhancements */
    .stButton > button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(79, 70, 229, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(79, 70, 229, 0.3);
    }
    
    /* File Uploader Enhancements */
    .uploadedFileInfos {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        border: 2px dashed #10b981;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .uploadedFileInfos:hover {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        transform: scale(1.02);
    }
    
    /* Success/Warning/Error Messages */
    .element-container div[data-testid="stMarkdownContainer"] div[data-testid="stAlert"] {
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Job Match Cards */
    .job-match-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 15px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .job-match-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 50%, #ec4899 100%);
    }
    
    .job-match-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    }
    
    /* Loading Animations */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .loading-pulse {
        animation: pulse 2s infinite;
    }
    
    /* Fade In Animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Statistics Cards */
    .stat-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        transform: translateY(-3px);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        color: #64748b;
        font-weight: 500;
        margin-top: 0.5rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .custom-card {
            padding: 1rem;
        }
    }
    
    /* Hide Streamlit Menu and Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Enhanced Animations for Modern Landing Page */
    
    /* Smooth scroll behavior */
    html {
        scroll-behavior: smooth;
    }
    
    /* Staggered fade-in animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes fadeInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    @keyframes glow {
        0%, 100% {
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }
        50% {
            box-shadow: 0 8px 40px rgba(79, 70, 229, 0.15);
        }
    }
    
    /* Apply animations to elements */
    .fade-in-up {
        animation: fadeInUp 0.8s ease-out;
    }
    
    .fade-in-left {
        animation: fadeInLeft 0.8s ease-out;
    }
    
    .fade-in-right {
        animation: fadeInRight 0.8s ease-out;
    }
    
    /* Floating animation for hero elements */
    .float-animation {
        animation: float 6s ease-in-out infinite;
    }
    
        @keyframes shimmer {
        0% {
            transform: translateX(-100%) translateY(-100%) rotate(45deg);
        }
        100% {
            transform: translateX(100%) translateY(100%) rotate(45deg);
        }
    }
    
        /* Home page specific styling using class selector */
    .home-page-content .custom-card {
        background: transparent !important;
        backdrop-filter: none !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: none !important;
        margin: 1rem 0;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        color: white !important;
        z-index: 15 !important;
    }

    .home-page-content .custom-card::before {
        display: none !important;
    }

    .home-page-content .custom-card:hover {
        box-shadow: 0 5px 20px rgba(255, 255, 255, 0.1) !important;
        transform: translateY(-5px);
        border-color: rgba(255, 255, 255, 0.4) !important;
        background: rgba(255, 255, 255, 0.05) !important;
    }

    .home-page-content .custom-card h3 {
        color: white !important;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    .home-page-content .custom-card p {
        color: rgba(255, 255, 255, 0.9) !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    }

    /* Ensure all text in home page content is white */
    .home-page-content * {
        color: white !important;
    }

    .home-page-content p, .home-page-content span {
        color: rgba(255, 255, 255, 0.9) !important;
    }

    .home-page-content strong {
        color: white !important;
    }

    /* Home page header styling */
    .home-page-content .main-header {
        background: transparent !important;
        backdrop-filter: none !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        padding: 2rem;
        border-radius: 20px;
        color: white !important;
        text-align: center;
        margin: 0 0 2rem 0;
        box-shadow: none !important;
        position: relative;
        overflow: hidden;
        z-index: 15 !important;
    }
    
            /* Feature cards - Home page only */
    .home-page-content .feature-card-1 {
        background: transparent !important;
        backdrop-filter: none !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-left: 4px solid #4f46e5 !important;
        transition: all 0.3s ease;
        color: white !important;
        position: relative;
        z-index: 15 !important;
        padding: 1rem;
        border-radius: 10px;
    }

    .home-page-content .feature-card-1:hover {
        background: rgba(79, 70, 229, 0.1) !important;
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
    }

    .home-page-content .feature-card-2 {
        background: transparent !important;
        backdrop-filter: none !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-left: 4px solid #7c3aed !important;
        transition: all 0.3s ease;
        color: white !important;
        position: relative;
        z-index: 15 !important;
        padding: 1rem;
        border-radius: 10px;
    }

    .home-page-content .feature-card-2:hover {
        background: rgba(124, 58, 237, 0.1) !important;
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(124, 58, 237, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
    }

    .home-page-content .feature-card-3 {
        background: transparent !important;
        backdrop-filter: none !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-left: 4px solid #ec4899 !important;
        transition: all 0.3s ease;
        color: white !important;
        position: relative;
        z-index: 15 !important;
        padding: 1rem;
        border-radius: 10px;
    }

    .home-page-content .feature-card-3:hover {
        background: rgba(236, 72, 153, 0.1) !important;
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(236, 72, 153, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
    }
    
    /* Pulse animation for interactive elements */
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    /* Smooth transitions for all interactive elements */
    * {
        transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    /* Loading pulse animation */
    .loading-pulse {
        animation: pulse 2s infinite;
    }
</style>
"""


def apply_enhanced_styles():
    """Apply enhanced CSS styles to the Streamlit app"""
    import streamlit as st
    st.markdown(ENHANCED_CSS, unsafe_allow_html=True) 