"""
Enhanced UI Components for AlignMinds
"""
import streamlit as st
from typing import Dict, Any, List


def render_header():
    """Render enhanced main header with custom logo"""
    st.markdown(
        """
        <div class="main-header fade-in-up">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
                <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGRlZnM+CiAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJyYWluR3JhZGllbnQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdHlsZT0ic3RvcC1jb2xvcjojM2I4MmY2O3N0b3Atb3BhY2l0eToxIiAvPgogICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0eWxlPSJzdG9wLWNvbG9yOiM4YjVjZjY7c3RvcC1vcGFjaXR5OjEiIC8+CiAgICA8L2xpbmVhckdyYWRpZW50PgogICAgPGxpbmVhckdyYWRpZW50IGlkPSJhcnJvd0dyYWRpZW50IiB4MT0iMCUiIHkxPSIwJSIgeDI9IjEwMCUiIHkyPSIwJSI+CiAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0eWxlPSJzdG9wLWNvbG9yOiMxMGI5ODE7c3RvcC1vcGFjaXR5OjEiIC8+CiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3R5bGU9InN0b3AtY29sb3I6IzA1OTY2OTtzdG9wLW9wYWNpdHk6MSIgLz4KICAgIDwvbGluZWFyR3JhZGllbnQ+CiAgPC9kZWZzPgogIDwhLS0gQnJhaW4gb3V0bGluZSAtLT4KICA8cGF0aCBkPSJNMjUgMzUgQzI1IDI1LCAzNSAxNSwgNTAgMTUgQzY1IDE1LCA3NSAyNSwgNzUgMzUgQzc1IDQ1LCA3MCA1MCwgNzAgNjAgQzcwIDcwLCA2NSA3NSwgNjAgNzUgQzU1IDc1LCA1MCA3MCwgNTAgNzAgQzUwIDcwLCA0NSA3NSwgNDAgNzUgQzM1IDc1LCAzMCA3MCwgMzAgNjAgQzMwIDUwLCAyNSA0NSwgMjUgMzUgWiIgCiAgICAgICAgZmlsbD0ibm9uZSIgc3Ryb2tlPSJ1cmwoI2JyYWluR3JhZGllbnQpIiBzdHJva2Utd2lkdGg9IjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogIDwhLS0gTmV1cmFsIGNvbm5lY3Rpb24gbm9kZXMgLS0+CiAgPGNpcmNsZSBjeD0iMzUiIGN5PSI0MCIgcj0iMyIgZmlsbD0idXJsKCNicmFpbkdyYWRpZW50KSIvPgogIDxjaXJjbGUgY3g9IjQ1IiBjeT0iMzAiIHI9IjIuNSIgZmlsbD0idXJsKCNicmFpbkdyYWRpZW50KSIvPgogIDxjaXJjbGUgY3g9IjU1IiBjeT0iMzUiIHI9IjIuNSIgZmlsbD0idXJsKCNicmFpbkdyYWRpZW50KSIvPgogIDxjaXJjbGUgY3g9IjY1IiBjeT0iNDUiIHI9IjMiIGZpbGw9InVybCgjYnJhaW5HcmFkaWVudCkiLz4KICA8Y2lyY2xlIGN4PSI0MCIgY3k9IjU1IiByPSIyIiBmaWxsPSJ1cmwoI2JyYWluR3JhZGllbnQpIi8+CiAgPGNpcmNsZSBjeD0iNjAiIGN5PSI2MCIgcj0iMiIgZmlsbD0idXJsKCNicmFpbkdyYWRpZW50KSIvPgogIDwhLS0gQ2VudHJhbCB0YXJnZXRpbmcgY3Jvc3NoYWlyIC0tPgogIDxjaXJjbGUgY3g9IjUwIiBjeT0iNDUiIHI9IjEyIiBmaWxsPSJub25lIiBzdHJva2U9IiMxZTQwYWYiIHN0cm9rZS13aWR0aD0iMyIvPgogIDxsaW5lIHgxPSI0MiIgeTE9IjQ1IiB4Mj0iNTgiIHkyPSI0NSIgc3Ryb2tlPSIjMWU0MGFmIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8bGluZSB4MT0iNTAiIHkxPSIzNyIgeDI9IjUwIiB5Mj0iNTMiIHN0cm9rZT0iIzFlNDBhZiIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPGNpcmNsZSBjeD0iNTAiIGN5PSI0NSIgcj0iMyIgZmlsbD0iIzFlNDBhZiIvPgogIDwhLS0gQWxpZ25tZW50IGFycm93IC0tPgogIDxwYXRoIGQ9Ik03MCA1MCBMODU1MCBMODA0NSBNODUgNTAgTDgwIDU1IiAKICAgICAgICBmaWxsPSJub25lIiBzdHJva2U9InVybCgjYXJyb3dHcmFkaWVudCkiIHN0cm9rZS13aWR0aD0iNCIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+Cjwvc3ZnPg==" 
                     style="width: 60px; height: 60px;" alt="AlignMinds Logo">
                <h1 style="margin: 0;">AlignMinds</h1>
            </div>
            <p>AI-Powered Recruitment Analysis System</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar():
    """Render enhanced sidebar with modern styling"""
    with st.sidebar:
        st.markdown(
            """
            <div class="professional-sidebar-header">
                <div class="sidebar-logo">
                    <div class="sidebar-logo-icon">⚡</div>
                    <div class="sidebar-logo-text">AlignMinds</div>
                </div>
            </div>
            <div class="nav-section">
                <div class="nav-section-title">MAIN MENU</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_file_uploader():
    """Render enhanced file uploader with better styling"""
    st.markdown(
        """
        <div class="custom-card fade-in-up">
            <h3>📄 Upload Resume for Analysis</h3>
            <p>Upload a PDF resume to get comprehensive AI-powered insights, job matching, and recommendations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    uploaded_file = st.file_uploader(
        "Choose PDF Resume File",
        type=["pdf"],
        help="Select a PDF resume file to analyze",
        label_visibility="collapsed"
    )
    return uploaded_file


def render_pipeline_progress(current_stage: str = "extraction", completed_stages: list = []):
    """Render multi-stage progress indicator using Streamlit native components"""
    stages = [
        {"key": "extraction", "icon": "📄", "title": "Extraction", "desc": "Reading resume"},
        {"key": "analysis", "icon": "🔍", "title": "Analysis", "desc": "Analyzing profile"},
        {"key": "matching", "icon": "🎯", "title": "Matching", "desc": "Finding jobs"},
        {"key": "screening", "icon": "👥", "title": "Screening", "desc": "Evaluating fit"},
        {"key": "recommendation", "icon": "💡", "title": "Complete", "desc": "Results ready"},
    ]
    
    # Title
    st.markdown("### 🔄 AI Processing Pipeline")
    
    # Create columns for each stage
    cols = st.columns(len(stages))
    
    for i, (col, stage) in enumerate(zip(cols, stages)):
        with col:
            is_completed = stage["key"] in completed_stages
            is_current = stage["key"] == current_stage
            
            if is_completed:
                # Completed stage - green with checkmark
                st.markdown(
                    f"""
                    <div style="text-align: center; padding: 1rem;">
                        <div style="background: #10b981; color: white; width: 50px; height: 50px; 
                                   border-radius: 50%; display: flex; align-items: center; 
                                   justify-content: center; margin: 0 auto 0.5rem auto; 
                                   font-size: 1.2rem; font-weight: bold;">
                            ✓
                        </div>
                        <div style="color: #10b981; font-weight: 600; font-size: 0.9rem;">{stage['title']}</div>
                        <div style="color: #64748b; font-size: 0.8rem;">{stage['desc']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif is_current:
                # Current stage - blue with icon
                st.markdown(
                    f"""
                    <div style="text-align: center; padding: 1rem;">
                        <div style="background: #3b82f6; color: white; width: 50px; height: 50px; 
                                   border-radius: 50%; display: flex; align-items: center; 
                                   justify-content: center; margin: 0 auto 0.5rem auto; 
                                   font-size: 1.2rem; animation: pulse 1.5s infinite;">
                            {stage['icon']}
                        </div>
                        <div style="color: #3b82f6; font-weight: 600; font-size: 0.9rem;">{stage['title']}</div>
                        <div style="color: #64748b; font-size: 0.8rem;">{stage['desc']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                # Pending stage - gray with number
                st.markdown(
                    f"""
                    <div style="text-align: center; padding: 1rem;">
                        <div style="background: #e5e7eb; color: #9ca3af; width: 50px; height: 50px; 
                                   border-radius: 50%; display: flex; align-items: center; 
                                   justify-content: center; margin: 0 auto 0.5rem auto; 
                                   font-size: 1rem; font-weight: bold;">
                            {i + 1}
                        </div>
                        <div style="color: #6b7280; font-size: 0.9rem;">{stage['title']}</div>
                        <div style="color: #64748b; font-size: 0.8rem;">{stage['desc']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    
    # Add simple progress bar
    current_progress = 0
    if current_stage == "extraction":
        current_progress = 20
    elif current_stage == "analysis":
        current_progress = 40
    elif current_stage == "matching":
        current_progress = 60
    elif current_stage == "screening":
        current_progress = 80
    elif current_stage == "recommendation":
        current_progress = 100
    
    # Add completed stages to progress
    progress_value = len(completed_stages) * 20 + (20 if current_stage != "extraction" else 0)
    if current_stage == "recommendation":
        progress_value = 100
        
    st.progress(progress_value / 100)
    
    # Add some breathing room
    st.markdown("<br>", unsafe_allow_html=True)


def render_job_match_card(job: Dict[str, Any], index: int):
    """Render individual job match card with enhanced styling"""
    match_score = job.get('match_score', 'N/A')
    location = job.get('location', 'Remote')
    title = job.get('title', 'Position')
    
    # Color code based on match score
    if isinstance(match_score, (int, float)):
        if match_score >= 80:
            score_color = "#10b981"  # Green
            score_bg = "#ecfdf5"
        elif match_score >= 60:
            score_color = "#f59e0b"  # Orange
            score_bg = "#fffbeb"
        else:
            score_color = "#ef4444"  # Red
            score_bg = "#fef2f2"
    else:
        score_color = "#6b7280"
        score_bg = "#f9fafb"
    
    st.markdown(
        f"""
        <div class="job-match-card fade-in-up" style="animation-delay: {index * 0.1}s;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="flex: 1;">
                    <h4 style="margin: 0; color: #1e293b; font-weight: 600;">{title}</h4>
                    <p style="margin: 0.5rem 0; color: #64748b;">📍 {location}</p>
                </div>
                <div style="text-align: center; padding: 0.75rem; background: {score_bg}; border-radius: 10px; min-width: 80px;">
                    <div style="font-size: 1.2rem; font-weight: 700; color: {score_color};">{match_score}</div>
                    <div style="font-size: 0.8rem; color: {score_color}; opacity: 0.8;">Match</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_analysis_metrics(analysis_results: Dict[str, Any]):
    """Render analysis metrics with enhanced cards"""
    confidence_score = analysis_results.get('confidence_score', 0)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            f"""
            <div class="stat-card fade-in-up">
                <div class="stat-number">{confidence_score:.0%}</div>
                <div class="stat-label">Confidence Score</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        skills_count = len(analysis_results.get('extracted_skills', []))
        st.markdown(
            f"""
            <div class="stat-card fade-in-up" style="animation-delay: 0.1s;">
                <div class="stat-number">{skills_count}</div>
                <div class="stat-label">Skills Identified</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col3:
        experience_years = analysis_results.get('years_experience', 0)
        st.markdown(
            f"""
            <div class="stat-card fade-in-up" style="animation-delay: 0.2s;">
                <div class="stat-number">{experience_years}</div>
                <div class="stat-label">Years Experience</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_screening_score(screening_score: int):
    """Render screening score with visual indicator"""
    # Determine color based on score
    if screening_score >= 80:
        color = "#10b981"
        bg_color = "#ecfdf5"
        status = "Excellent"
    elif screening_score >= 70:
        color = "#3b82f6"
        bg_color = "#eff6ff"
        status = "Good"
    elif screening_score >= 60:
        color = "#f59e0b"
        bg_color = "#fffbeb"
        status = "Fair"
    else:
        color = "#ef4444"
        bg_color = "#fef2f2"
        status = "Needs Improvement"
    
    st.markdown(
        f"""
        <div class="custom-card fade-in-up">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0; color: #1e293b;">Screening Results</h3>
                    <p style="margin: 0.5rem 0; color: #64748b;">Candidate evaluation score</p>
                </div>
                <div style="text-align: center; padding: 1rem; background: {bg_color}; border-radius: 15px; min-width: 120px;">
                    <div style="font-size: 2.5rem; font-weight: 700; color: {color};">{screening_score}%</div>
                    <div style="font-size: 0.9rem; color: {color}; font-weight: 500;">{status}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_recommendation_card(recommendation: str):
    """Render final recommendation with enhanced styling"""
    st.markdown(
        f"""
        <div class="custom-card fade-in-up">
            <div style="padding: 1rem;">
                <h3 style="margin: 0 0 1rem 0; color: #1e293b; display: flex; align-items: center;">
                    💡 Final Recommendation
                </h3>
                <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
                           padding: 1.5rem; border-radius: 12px; border-left: 4px solid #0ea5e9;">
                    <p style="margin: 0; color: #0c4a6e; line-height: 1.6; font-size: 1.05rem;">
                        {recommendation}
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_about_page():
    """Render enhanced about page"""
    st.markdown(
        """
        <div class="main-header fade-in-up">
            <h1>About AlignMinds</h1>
            <p>Revolutionizing recruitment with AI-powered intelligence</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Feature cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class="custom-card fade-in-up">
                <h3>🎯 How It Works</h3>
                <div style="padding: 1rem 0;">
                    <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px; border-left: 4px solid #4f46e5;">
                        <strong>1. Extract</strong> - Parse PDF resumes and extract structured data
                    </div>
                    <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px; border-left: 4px solid #7c3aed;">
                        <strong>2. Analyze</strong> - AI-powered analysis of skills and experience
                    </div>
                    <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px; border-left: 4px solid #ec4899;">
                        <strong>3. Match</strong> - Find the best job opportunities
                    </div>
                    <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px; border-left: 4px solid #10b981;">
                        <strong>4. Recommend</strong> - Provide actionable insights
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            """
            <div class="custom-card fade-in-up" style="animation-delay: 0.2s;">
                <h3>🚀 Technology Stack</h3>
                <div style="padding: 1rem 0;">
                    <div style="margin: 0.75rem 0; display: flex; align-items: center;">
                        <span style="background: #4f46e5; color: white; padding: 0.5rem; border-radius: 8px; margin-right: 1rem; min-width: 60px; text-align: center;">AI</span>
                        <span>Ollama (llama3.2) for intelligent processing</span>
                    </div>
                    <div style="margin: 0.75rem 0; display: flex; align-items: center;">
                        <span style="background: #7c3aed; color: white; padding: 0.5rem; border-radius: 8px; margin-right: 1rem; min-width: 60px; text-align: center;">Web</span>
                        <span>Streamlit for modern interface</span>
                    </div>
                    <div style="margin: 0.75rem 0; display: flex; align-items: center;">
                        <span style="background: #ec4899; color: white; padding: 0.5rem; border-radius: 8px; margin-right: 1rem; min-width: 60px; text-align: center;">PDF</span>
                        <span>Advanced text extraction</span>
                    </div>
                    <div style="margin: 0.75rem 0; display: flex; align-items: center;">
                        <span style="background: #10b981; color: white; padding: 0.5rem; border-radius: 8px; margin-right: 1rem; min-width: 60px; text-align: center;">Async</span>
                        <span>Multi-agent architecture</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_upload_success(filename: str):
    """Render upload success message that disappears automatically with CSS"""
    st.markdown(
        f"""
        <div class="upload-success-toast">
            <div class="toast-content">
                <span class="toast-icon">✅</span>
                <div class="toast-text">
                    <strong>Upload Successful!</strong>
                    <br><span>File: {filename}</span>
                </div>
            </div>
        </div>
        
        <style>
            .upload-success-toast {{
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 1000;
                animation: toast-lifecycle 4s ease-in-out forwards;
                pointer-events: none;
            }}
            
            @keyframes toast-lifecycle {{
                0% {{ 
                    opacity: 0; 
                    transform: translateX(100%); 
                }}
                15% {{ 
                    opacity: 1; 
                    transform: translateX(0); 
                }}
                85% {{ 
                    opacity: 1; 
                    transform: translateX(0); 
                }}
                100% {{ 
                    opacity: 0; 
                    transform: translateX(100%);
                    visibility: hidden;
                }}
            }}
            
            .toast-content {{
                display: flex;
                align-items: center;
                background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
                padding: 1rem 1.5rem;
                border-radius: 12px;
                border-left: 4px solid #10b981;
                box-shadow: 0 4px 20px rgba(16, 185, 129, 0.2);
                gap: 0.75rem;
            }}
            
            .toast-icon {{
                font-size: 1.2rem;
            }}
            
            .toast-text {{
                color: #065f46;
            }}
            
            .toast-text strong {{
                color: #065f46;
            }}
            
            .toast-text span {{
                color: #047857;
                font-size: 0.9rem;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_loading_status(stage: str, progress: int):
    """Render loading status with enhanced progress indicator"""
    stages = {
        "extraction": {"icon": "📄", "text": "Extracting information from resume"},
        "analysis": {"icon": "🔍", "text": "Analyzing candidate profile"},
        "matching": {"icon": "🎯", "text": "Finding job matches"},
        "screening": {"icon": "👥", "text": "Screening candidate"},
        "recommendation": {"icon": "💡", "text": "Generating recommendations"},
    }
    
    current_stage = stages.get(stage, {"icon": "⚙️", "text": "Processing"})
    
    st.markdown(
        f"""
        <div class="progress-container loading-pulse">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem; margin-right: 1rem;">{current_stage['icon']}</span>
                <span style="font-weight: 500; color: #1e293b;">{current_stage['text']}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_progress_section():
    """Render progress section header"""
    st.markdown(
        """
        <div class="custom-card fade-in-up">
            <h3>🔄 Processing Resume</h3>
            <p>Our AI agents are analyzing your resume. This may take a few moments...</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_results_header():
    """Render results section header"""
    st.markdown(
        """
        <div class="custom-card fade-in-up" style="background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); border-color: #10b981;">
            <div style="display: flex; align-items: center;">
                <span style="background: #10b981; color: white; padding: 0.75rem; border-radius: 50%; margin-right: 1rem;">✅</span>
                <div>
                    <h3 style="margin: 0; color: #065f46;">Analysis Complete!</h3>
                    <p style="margin: 0; color: #047857;">Your resume has been successfully processed and analyzed.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_celebration_animation():
    """Render clean analysis complete toast notification"""
    st.markdown(
        """
        <div class="analysis-complete-toast">
            <div class="toast-content">
                <span class="toast-icon">🎉</span>
                <div class="toast-text">
                    <strong>Analysis Complete!</strong>
                    <br><span>Results are ready to view</span>
                </div>
            </div>
        </div>
        
        <style>
            .analysis-complete-toast {{
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 1000;
                animation: toast-lifecycle 4s ease-in-out forwards;
                pointer-events: none;
            }}
            
            @keyframes toast-lifecycle {{
                0% {{ 
                    opacity: 0; 
                    transform: translateX(100%); 
                }}
                15% {{ 
                    opacity: 1; 
                    transform: translateX(0); 
                }}
                85% {{ 
                    opacity: 1; 
                    transform: translateX(0); 
                }}
                100% {{ 
                    opacity: 0; 
                    transform: translateX(100%);
                    visibility: hidden;
                }}
            }}
            
            .analysis-complete-toast .toast-content {{
                display: flex;
                align-items: center;
                background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
                padding: 1rem 1.5rem;
                border-radius: 12px;
                border-left: 4px solid #3b82f6;
                box-shadow: 0 4px 20px rgba(59, 130, 246, 0.2);
                gap: 0.75rem;
            }}
            
            .analysis-complete-toast .toast-icon {{
                font-size: 1.2rem;
            }}
            
            .analysis-complete-toast .toast-text {{
                color: #1e40af;
            }}
            
            .analysis-complete-toast .toast-text strong {{
                color: #1e40af;
            }}
            
            .analysis-complete-toast .toast-text span {{
                color: #1d4ed8;
                font-size: 0.9rem;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state(message: str, icon: str = "📝"):
    """Render empty state with friendly message"""
    st.markdown(
        f"""
        <div style="text-align: center; padding: 3rem; color: #64748b;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{icon}</div>
            <h3 style="color: #475569; font-weight: 500;">{message}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_analytics_dashboard():
    """Render analytics dashboard placeholder"""
    st.markdown(
        """
        <div class="main-header fade-in-up">
            <h1>📊 Analytics Dashboard</h1>
            <p>Coming Soon - Comprehensive recruitment analytics</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="custom-card fade-in-up">
            <h3>🚀 Planned Features</h3>
            <div style="padding: 1rem 0;">
                <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px;">
                    📈 <strong>Resume Processing Stats</strong> - Track analysis volume and success rates
                </div>
                <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px;">
                    🎯 <strong>Job Match Analytics</strong> - Success rates and matching patterns
                </div>
                <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px;">
                    👥 <strong>Candidate Insights</strong> - Skills trends and market analysis
                </div>
                <div style="margin: 1rem 0; padding: 1rem; background: #f8fafc; border-radius: 10px;">
                    💡 <strong>Performance Metrics</strong> - Agent performance and optimization insights
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    ) 


def render_structured_analysis(skills_analysis_data):
    """Render skills analysis data in a structured, user-friendly format"""
    # Handle both string and dict data
    if isinstance(skills_analysis_data, str):
        try:
            # Try to parse if it's a string representation of a dict
            import ast
            skills_analysis_data = ast.literal_eval(skills_analysis_data)
        except:
            # If parsing fails, just display the string
            st.markdown(skills_analysis_data)
            return
    
    if isinstance(skills_analysis_data, dict):
        # Technical Skills Section - with border
        if 'technical_skills' in skills_analysis_data:
            skills = skills_analysis_data['technical_skills']
            if skills:
                with st.container():
                    st.markdown(
                        """
                        <div style="border: 2px solid #e5e7eb; border-radius: 12px; padding: 0.75rem; margin: 1rem 0; background: #f8fafc;">
                            <h4 style="margin: 0; color: #1e293b;">💻 Technical Skills</h4>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    # Use Streamlit columns for skills display
                    cols_per_row = 4
                    for i in range(0, len(skills), cols_per_row):
                        cols = st.columns(cols_per_row)
                        for j, skill in enumerate(skills[i:i+cols_per_row]):
                            with cols[j % cols_per_row]:
                                st.markdown(
                                    f"""<div style="background: #e0f2fe; color: #0c4a6e; padding: 0.4rem 0.8rem; 
                                        border-radius: 20px; text-align: center; margin: 0.25rem 0; font-weight: 500;">
                                        {skill}</div>""", 
                                    unsafe_allow_html=True
                                )
        
        # Experience, Education, and Level with borders - side by side
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if 'years_of_experience' in skills_analysis_data:
                years = skills_analysis_data['years_of_experience']
                with st.container():
                    st.markdown(
                        """
                        <div style="border: 2px solid #e5e7eb; border-radius: 12px; padding: 0.75rem; margin: 1rem 0; background: #f8fafc;">
                            <h4 style="margin: 0; color: #1e293b;">📅 Experience</h4>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.metric(label="Years", value=f"{years} years")
        
        with col2:
            if 'experience_level' in skills_analysis_data:
                level = skills_analysis_data['experience_level']
                with st.container():
                    st.markdown(
                        """
                        <div style="border: 2px solid #e5e7eb; border-radius: 12px; padding: 0.75rem; margin: 1rem 0; background: #f8fafc;">
                            <h4 style="margin: 0; color: #1e293b;">📊 Level</h4>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.info(level)
        
        with col3:
            if 'education' in skills_analysis_data:
                education = skills_analysis_data['education']
                if isinstance(education, dict):
                    level = education.get('level', 'Not specified')
                    field = education.get('field', 'Not specified')
                    with st.container():
                        st.markdown(
                            """
                            <div style="border: 2px solid #e5e7eb; border-radius: 12px; padding: 0.75rem; margin: 1rem 0; background: #f8fafc;">
                                <h4 style="margin: 0; color: #1e293b;">🎓 Education</h4>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                        st.write(f"**{level}**")
                        st.write(f"*{field}*")
        
        # Key Achievements Section - with border
        if 'key_achievements' in skills_analysis_data:
            achievements = skills_analysis_data['key_achievements']
            if achievements:
                with st.container():
                    st.markdown(
                        """
                        <div style="border: 2px solid #e5e7eb; border-radius: 12px; padding: 0.75rem; margin: 1rem 0; background: #f8fafc;">
                            <h4 style="margin: 0; color: #1e293b;">🏆 Key Achievements</h4>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    for achievement in achievements:
                        st.info(achievement)
        
        # Domain Expertise Section - with border
        if 'domain_expertise' in skills_analysis_data:
            domains = skills_analysis_data['domain_expertise']
            if domains:
                with st.container():
                    st.markdown(
                        """
                        <div style="border: 2px solid #e5e7eb; border-radius: 12px; padding: 0.75rem; margin: 1rem 0; background: #f8fafc;">
                            <h4 style="margin: 0; color: #1e293b;">🎯 Domain Expertise</h4>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    # Use Streamlit columns for domains display
                    cols_per_row = 3
                    for i in range(0, len(domains), cols_per_row):
                        cols = st.columns(cols_per_row)
                        for j, domain in enumerate(domains[i:i+cols_per_row]):
                            with cols[j % cols_per_row]:
                                st.markdown(
                                    f"""<div style="background: #ddd6fe; color: #581c87; padding: 0.4rem 0.8rem; 
                                        border-radius: 20px; text-align: center; margin: 0.25rem 0; font-weight: 500;">
                                        {domain}</div>""", 
                                    unsafe_allow_html=True
                                ) 