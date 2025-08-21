# AlignMinds - Home Page
import streamlit as st
from ui.styles import apply_enhanced_styles

# Configure Streamlit page
st.set_page_config(
    page_title="AlignMinds - AI Recruitment System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply enhanced styles
apply_enhanced_styles()


def main():
    # Add custom home icon to sidebar using JavaScript
    st.markdown(
        """
        <script>
        // Wait for sidebar to load and add home icon
        function addHomeIcon() {
            const sidebarLinks = document.querySelectorAll('[data-testid="stSidebarNavLink"]');
            sidebarLinks.forEach(link => {
                if (link.textContent.trim() === 'Home') {
                    link.innerHTML = 'Home';
                }
            });
        }

        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        if (sidebar) {
            observer.observe(sidebar, { childList: true, subtree: true });
        }
        </script>
        """,
        unsafe_allow_html=True,
    )
    
    # Add animated background for home page
    st.markdown('<div class="home-page-background"></div>', unsafe_allow_html=True)
    
    # Wrap all content in home-page-content class
    st.markdown('<div class="home-page-content">', unsafe_allow_html=True)
    
    # Welcome page content with floating animation
    st.markdown(
        """
        <div class="main-header fade-in-up float-animation">
            <h1 style="color: white; margin: 0;">🤖 Welcome to AlignMinds</h1>
            <p style="color: rgba(255, 255, 255, 0.9); margin: 0.5rem 0 0 0;">AI-Powered Recruitment Analysis System</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Getting started section with clickable cards - using container approach
    st.markdown(
        """
        <div class="custom-card fade-in-left" style="animation-delay: 0.2s; background: transparent !important; border: 1px solid rgba(255, 255, 255, 0.2) !important; box-shadow: none !important; color: white !important;">
            <h3 style="color: white !important; margin-bottom: 1rem;">🚀 Getting Started</h3>
            <p style="color: rgba(255, 255, 255, 0.8) !important;">Choose from the navigation menu to:</p>
            <div style="padding: 1rem 0;">
                <div id="upload-card" style="margin: 1rem 0; padding: 1rem; border-radius: 10px; background: rgba(79, 70, 229, 0.4); border: 1px solid rgba(255, 255, 255, 0.2); border-left: 4px solid #4f46e5; transition: all 0.3s ease; color: white; cursor: pointer;" onmouseover="this.style.background='rgba(79, 70, 229, 0.5)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(79, 70, 229, 0.4)'; this.style.transform='translateX(0)'" onclick="navigateToUpload()">
                    <strong style="color: white;">📄 Upload Resume</strong> - <span style="color: rgba(255, 255, 255, 0.9);">Analyze PDF resumes with AI-powered insights</span>
                </div>
                <div id="analytics-card" style="margin: 1rem 0; padding: 1rem; border-radius: 10px; background: rgba(236, 72, 153, 0.4); border: 1px solid rgba(255, 255, 255, 0.2); border-left: 4px solid #ec4899; transition: all 0.3s ease; color: white; cursor: pointer;" onmouseover="this.style.background='rgba(236, 72, 153, 0.5)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(236, 72, 153, 0.4)'; this.style.transform='translateX(0)'" onclick="navigateToAnalytics()">
                    <strong style="color: white;">📊 Analytics Dashboard</strong> - <span style="color: rgba(255, 255, 255, 0.9);">View comprehensive recruitment analytics</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Use session state to handle navigation
    if "navigate_to" not in st.session_state:
        st.session_state.navigate_to = None
    
    if st.session_state.navigate_to == "upload":
        st.switch_page("pages/1_📄_Upload_Resume.py")
    elif st.session_state.navigate_to == "analytics":
        st.switch_page("pages/3_📊_Analytics_Dashboard.py")
    
    # Add JavaScript to handle navigation via session state
    st.markdown(
        """
        <script>
        function navigateToUpload() {
            // Use Streamlit's component communication
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                key: 'navigate_to',
                value: 'upload'
            }, '*');
            // Trigger a rerun
            window.parent.postMessage({type: 'streamlit:rerun'}, '*');
        }
        
        function navigateToAnalytics() {
            // Use Streamlit's component communication
            window.parent.postMessage({
                type: 'streamlit:setComponentValue', 
                key: 'navigate_to',
                value: 'analytics'
            }, '*');
            // Trigger a rerun
            window.parent.postMessage({type: 'streamlit:rerun'}, '*');
        }
        </script>
        """,
        unsafe_allow_html=True,
    )
    
    # Features overview with staggered animations
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class="custom-card fade-in-left" style="animation-delay: 0.4s; background: transparent !important; border: 1px solid rgba(255, 255, 255, 0.2) !important; box-shadow: none !important; color: white !important;">
                <h3 style="color: white !important; margin-bottom: 1rem;">🎯 AI-Powered Analysis</h3>
                <p style="color: rgba(255, 255, 255, 0.8) !important;">Our multi-agent system provides:</p>
                <ul style="color: rgba(255, 255, 255, 0.9) !important; line-height: 1.8; list-style: none; padding-left: 0;">
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(79, 70, 229, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(79, 70, 229, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(79, 70, 229, 0.2)'; this.style.transform='translateX(0)'">
                        ⚡ Intelligent resume parsing
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(79, 70, 229, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(79, 70, 229, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(79, 70, 229, 0.2)'; this.style.transform='translateX(0)'">
                        🎯 Skills assessment and scoring
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(79, 70, 229, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(79, 70, 229, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(79, 70, 229, 0.2)'; this.style.transform='translateX(0)'">
                        🔍 Job matching algorithms
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(79, 70, 229, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(79, 70, 229, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(79, 70, 229, 0.2)'; this.style.transform='translateX(0)'">
                        👥 Candidate screening automation
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(79, 70, 229, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(79, 70, 229, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(79, 70, 229, 0.2)'; this.style.transform='translateX(0)'">
                        💡 Actionable recommendations
                    </li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            """
            <div class="custom-card fade-in-right" style="animation-delay: 0.6s; background: transparent !important; border: 1px solid rgba(255, 255, 255, 0.2) !important; box-shadow: none !important; color: white !important;">
                <h3 style="color: white !important; margin-bottom: 1rem;">⚡ Quick & Efficient</h3>
                <p style="color: rgba(255, 255, 255, 0.8) !important;">Experience fast, accurate analysis:</p>
                <ul style="color: rgba(255, 255, 255, 0.9) !important; line-height: 1.8; list-style: none; padding-left: 0;">
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(236, 72, 153, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(236, 72, 153, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(236, 72, 153, 0.2)'; this.style.transform='translateX(0)'">
                        📤 Upload PDF resumes instantly
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(236, 72, 153, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(236, 72, 153, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(236, 72, 153, 0.2)'; this.style.transform='translateX(0)'">
                        ⏱️ Real-time processing pipeline
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(236, 72, 153, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(236, 72, 153, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(236, 72, 153, 0.2)'; this.style.transform='translateX(0)'">
                        📊 Comprehensive result reporting
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(236, 72, 153, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(236, 72, 153, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(236, 72, 153, 0.2)'; this.style.transform='translateX(0)'">
                        🎨 Modern, intuitive interface
                    </li>
                    <li style="margin: 0.5rem 0; padding: 0.5rem; background: rgba(236, 72, 153, 0.2); border-radius: 8px; transition: all 0.3s ease; color: white !important;" onmouseover="this.style.background='rgba(236, 72, 153, 0.3)'; this.style.transform='translateX(5px)'" onmouseout="this.style.background='rgba(236, 72, 153, 0.2)'; this.style.transform='translateX(0)'">
                        💾 Export and save results
                    </li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    # Close home-page-content wrapper
    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main() 