# AlignMinds 🤖

An AI-powered recruitment analysis system that uses specialized AI agents to analyze resumes, match candidates with job opportunities, and provide intelligent recommendations.

## Features ✨

- **📄 Resume Extraction**: Automatically extract information from PDF resumes
- **🔍 Intelligent Analysis**: AI-powered analysis of candidate profiles and skills
- **🎯 Job Matching**: Smart matching with suitable job positions
- **👥 Candidate Screening**: Automated screening with scoring
- **💡 Recommendations**: Detailed insights and hiring recommendations
- **🌐 Modern Web Interface**: Beautiful Streamlit-based UI with real-time progress

## Demo 🎬

📹 **[Watch the Demo Video](https://drive.google.com/file/d/15IZ8kDSqYc-iVNSi3M6s5XZL0HleIlrF/view?usp=sharing)**

See AlignMinds in action with a complete walkthrough of the AI recruitment analysis system.

## Architecture 🏗️

AlignMinds uses a **multi-agent architecture** where specialized AI agents work together:

- **Orchestrator Agent**: Coordinates the entire workflow
- **Extractor Agent**: Extracts structured data from PDF resumes
- **Analyzer Agent**: Analyzes candidate profiles and skills
- **Matcher Agent**: Matches candidates with job opportunities
- **Screener Agent**: Performs candidate screening with scoring
- **Recommender Agent**: Generates final recommendations

## Tech Stack 🛠️

- **Frontend**: Streamlit with custom styling
- **AI Engine**: Ollama (llama3.2 model)
- **PDF Processing**: pdfminer.six
- **Language**: Python 3.x
- **Architecture**: Async/await multi-agent system

## Prerequisites 📋

- Python 3.8+ 
- [Ollama](https://ollama.ai/) installed and running
- llama3.2 model pulled in Ollama

## Installation & Setup 🚀

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AlignMinds
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Ollama**
   ```bash
   # Install Ollama (if not already installed)
   # Visit https://ollama.ai/ for installation instructions
   
   # Start Ollama service
   ollama serve
   
   # Pull the required model
   ollama pull llama3.2
   ```

4. **Configure environment (optional)**
   ```bash
   # Create .env file if you need custom Ollama settings
   echo "OLLAMA_BASE_URL=http://localhost:11434/v1" > .env
   echo "OLLAMA_API_KEY=ollama" >> .env
   ```

## Usage 🎯

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload a resume**
   - Click on "Upload Resume" in the sidebar
   - Select a PDF resume file
   - Wait for the AI analysis to complete

4. **View results** across four tabs:
   - **📊 Analysis**: Skills analysis and confidence scores
   - **💼 Job Matches**: Matched job positions with scores
   - **🎯 Screening**: Screening results and scores
   - **💡 Recommendation**: Final AI recommendations

## Project Structure 📁

```
AlignMinds/
├── agents/                 # AI agent implementations
│   ├── orchestrator.py    # Main workflow coordinator
│   ├── extractor_agent.py # PDF text extraction
│   ├── analyzer_agent.py  # Profile analysis
│   ├── matcher_agent.py   # Job matching
│   ├── screener_agent.py  # Candidate screening
│   └── recommender_agent.py # Recommendations
├── utils/                 # Utility modules
├── uploads/              # Temporary file storage
├── results/              # Analysis results
├── resumes/              # Sample resumes
├── app.py               # Main Streamlit application
└── requirements.txt     # Dependencies
```

## Sample Results 📊

The system provides comprehensive analysis including:
- Extracted candidate information
- Skills assessment with confidence scores
- Matched job positions with compatibility scores
- Screening evaluation and recommendations
- Final hiring recommendations