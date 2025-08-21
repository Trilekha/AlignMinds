# Enhanced Streamlit Web Application for AlignMinds
import streamlit as st
import asyncio
import os
from datetime import datetime
from pathlib import Path
from agents.orchestrator import OrchestratorAgent
from utils.logger import setup_logger
from utils.exceptions import ResumeProcessingError
from ui.styles import apply_enhanced_styles
from ui.components import (
    render_header,
    render_sidebar,
    render_file_uploader,
    render_progress_section,
    render_job_match_card,
    render_analysis_metrics,
    render_screening_score,
    render_recommendation_card,
    render_upload_success,
    render_loading_status,
    render_results_header,
    render_empty_state,
    render_analytics_dashboard,
    render_structured_analysis,
)

# Configure Streamlit page
st.set_page_config(
    page_title="AlignMinds",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize logger
logger = setup_logger()

# Apply enhanced styles
apply_enhanced_styles()


async def process_resume(file_path: str) -> dict:
    """Process resume through the AI recruitment pipeline"""
    try:
        orchestrator = OrchestratorAgent()
        resume_data = {
            "file_path": file_path,
            "submission_timestamp": datetime.now().isoformat(),
        }
        return await orchestrator.process_application(resume_data)
    except Exception as e:
        logger.error(f"Error processing resume: {str(e)}")
        raise


def save_uploaded_file(uploaded_file) -> str:
    """Save uploaded file and return the file path"""
    try:
        # Create uploads directory if it doesn't exist
        save_dir = Path("uploads")
        save_dir.mkdir(exist_ok=True)

        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = save_dir / f"resume_{timestamp}_{uploaded_file.name}"

        # Save the file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return str(file_path)
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        raise


def main():
    # Render sidebar navigation
    selected = render_sidebar()

    if selected == "Upload Resume":
        # Main header
        render_header()
        
        # File upload section
        uploaded_file = render_file_uploader()

        if uploaded_file:
            try:
                # Show upload success
                render_upload_success(uploaded_file.name)
                
                with st.spinner("Saving uploaded file..."):
                    file_path = save_uploaded_file(uploaded_file)

                # Create progress tracking
                render_progress_section()
                progress_bar = st.progress(0)
                status_placeholder = st.empty()

                # Process resume with enhanced UI
                try:
                    # Stage 1: Extraction
                    with status_placeholder.container():
                        render_loading_status("extraction", 20)
                    progress_bar.progress(20)
                    
                    # Run analysis asynchronously
                    result = asyncio.run(process_resume(file_path))

                    if result["status"] == "completed":
                        progress_bar.progress(100)
                        
                        # Show completion header
                        render_results_header()

                        # Enhanced results display
                        tab1, tab2, tab3, tab4 = st.tabs(
                            [
                                "📊 Analysis Results",
                                "💼 Job Matches",
                                "🎯 Screening Report",
                                "💡 Final Recommendation",
                            ]
                        )

                        with tab1:
                            st.markdown("### Skills & Profile Analysis")
                            
                            # Enhanced metrics display
                            render_analysis_metrics(result["analysis_results"])
                            
                            # Structured analysis sections
                            render_structured_analysis(result["analysis_results"]["skills_analysis"])

                        with tab2:
                            st.markdown("### 🎯 Matched Job Opportunities")
                            
                            if not result["job_matches"]["matched_jobs"]:
                                render_empty_state("No suitable positions found at this time", "🔍")
                            else:
                                seen_titles = set()
                                job_count = 0
                                
                                for job in result["job_matches"]["matched_jobs"]:
                                    if job["title"] in seen_titles:
                                        continue
                                    seen_titles.add(job["title"])
                                    render_job_match_card(job, job_count)
                                    job_count += 1

                        with tab3:
                            st.markdown("### 📋 Candidate Screening")
                            
                            # Enhanced screening display
                            screening_score = result["screening_results"]["screening_score"]
                            render_screening_score(screening_score)
                            
                            # Screening report in a card
                            st.markdown(
                                f"""
                                <div class="custom-card fade-in-up">
                                    <h4>📝 Detailed Report</h4>
                                    <div style="background: #f8fafc; padding: 1.5rem; border-radius: 10px; margin-top: 1rem; line-height: 1.6;">
                                        {result["screening_results"]["screening_report"]}
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True,
                            )

                        with tab4:
                            st.markdown("### 🎯 Hiring Recommendation")
                            render_recommendation_card(
                                result["final_recommendation"]["final_recommendation"]
                            )

                        # Save results with success message
                        output_dir = Path("results")
                        output_dir.mkdir(exist_ok=True)
                        output_file = (
                            output_dir
                            / f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                        )

                        with open(output_file, "w") as f:
                            f.write(str(result))

                    else:
                        st.markdown(
                            f"""
                            <div class="custom-card" style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border-color: #ef4444;">
                                <div style="display: flex; align-items: center;">
                                    <span style="background: #ef4444; color: white; padding: 0.75rem; border-radius: 50%; margin-right: 1rem;">⚠️</span>
                                    <div>
                                        <h4 style="margin: 0; color: #dc2626;">Processing Failed</h4>
                                        <p style="margin: 0; color: #b91c1c;">Stage: {result['current_stage']}</p>
                                        <p style="margin: 0; color: #b91c1c;">Error: {result.get('error', 'Unknown error')}</p>
                                    </div>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                except Exception as e:
                    st.markdown(
                        f"""
                        <div class="custom-card" style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border-color: #ef4444;">
                            <div style="text-align: center; padding: 1rem;">
                                <h4 style="color: #dc2626;">❌ Processing Error</h4>
                                <p style="color: #b91c1c;">{str(e)}</p>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    logger.error(f"Processing error: {str(e)}", exc_info=True)

                finally:
                    # Cleanup uploaded file
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        logger.error(f"Error removing temporary file: {str(e)}")

            except Exception as e:
                st.markdown(
                    f"""
                    <div class="custom-card" style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); border-color: #ef4444;">
                        <div style="text-align: center; padding: 1rem;">
                            <h4 style="color: #dc2626;">❌ Upload Error</h4>
                            <p style="color: #b91c1c;">{str(e)}</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                logger.error(f"Upload error: {str(e)}", exc_info=True)

    elif selected == "Analytics Dashboard":
        render_analytics_dashboard()


if __name__ == "__main__":
    main() 