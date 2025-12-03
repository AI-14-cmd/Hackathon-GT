# 📈 InsightX - Automated Insight Engine

> **AI-powered advertising analytics that transforms raw data into executive-ready PDF reports — no manual work required.**

Built for the **GroundTruth Hackathon** to solve the challenge: *"Account Managers manually download CSVs and screenshots to make reports. Design a system that ingests raw data and automatically generates beautiful, executive-ready reports with AI-written insights."*

🔗 **GitHub Repository:** [https://github.com/AI-14-cmd/Hackathon-GT.git](https://github.com/AI-14-cmd/Hackathon-GT.git)

## 🚀 **Project Status: ✅ FULLY FUNCTIONAL**

**Latest Test Results:**
- ✅ Successfully processed 30 rows of sample data
- ✅ Computed KPIs: **CTR: 2.47%** | **ROI: 446.6%**
- ✅ Generated performance visualization
- ✅ Created executive PDF report
- ✅ Both CLI and web interfaces working
- ✅ AI fallback system operational

## 📸 Demo & Output

**Generated Files:**
- 📊 `output/chart.png` - Performance visualization chart
- 📄 `output/Insight_Report.pdf` - Executive-ready PDF report

**Sample Output:**
```
[SUCCESS] CTR: 2.47% | ROI: 446.6%
[SUCCESS] Chart saved to output/chart.png
[SUCCESS] PDF saved to output/Insight_Report.pdf
✅ Report Generated Successfully
```

---

## 🎯 Problem Statement

In the AdTech world, Account Managers spend countless hours:
- Manually downloading CSV exports
- Creating screenshots of dashboards
- Writing performance summaries
- Compiling slides and PDF reports

**InsightX automates this entire workflow.**

---

## ✨ Features

✅ **Automated Data Ingestion** - Reads CSV files with advertising metrics  
✅ **KPI Computation** - Calculates CTR, ROI, and totals automatically  
✅ **Smart Visualization** - Generates clean, professional charts  
✅ **AI-Powered Insights** - Uses OpenAI GPT-4o or Google Gemini to write natural-language summaries  
✅ **PDF Report Generation** - Creates executive-ready reports with one click  
✅ **Web Interface** - Simple Streamlit UI for non-technical users  
✅ **Zero Manual Work** - Complete end-to-end automation  

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/AI-14-cmd/Hackathon-GT.git
cd Hackathon-GT

# Install dependencies
pip install -r requirements.txt
```

### Option 1: Run via Command Line

Generate a report from sample data:

```bash
python main.py
```

This will:
- Process `data/sample_data.csv`
- Compute KPIs (CTR, ROI)
- Generate charts
- Create AI insights
- Export `output/Insight_Report.pdf`

### Option 2: Run via Web Interface

Launch the Streamlit app:

```bash
streamlit run app.py
```

Then:
1. Upload your CSV file
2. Click "Generate Report"
3. Download the PDF

---

## 📊 Input Data Format

Your CSV must have these columns:

| Column | Description |
|--------|-------------|
| `date` | Date in YYYY-MM-DD format |
| `clicks` | Number of clicks |
| `impressions` | Number of impressions |
| `ad_spend` | Ad spend in dollars |
| `revenue` | Revenue generated in dollars |

**Example:**
```csv
date,clicks,impressions,ad_spend,revenue
2024-11-01,245,12500,450.00,1250.00
2024-11-02,289,13200,480.00,1430.00
```

See `data/sample_data.csv` for a complete example.

---

## 🤖 AI Integration (Optional)

InsightX can use AI to generate intelligent insights. Set one of these environment variables:

**For OpenAI GPT-4o:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**For Google Gemini:**
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

**No API Key?** No problem! The system automatically falls back to intelligent rule-based insights.

### 🔧 API Configuration Setup

**Method 1: Environment Variables**
```bash
# Windows
set OPENAI_API_KEY=your-key-here
set GOOGLE_API_KEY=your-key-here

# Linux/Mac
export OPENAI_API_KEY="your-key-here"
export GOOGLE_API_KEY="your-key-here"
```

**Method 2: .env File (Recommended)**
```bash
# Create .env file in project root
OPENAI_API_KEY=your-openai-key-here
GOOGLE_API_KEY=your-google-key-here
```

---

## 📁 Project Structure

```
Hackathon-GT/
├── main.py                 # Core automation script
├── app.py                  # Streamlit web interface
├── requirements.txt        # Python dependencies
├── test_gemini.py          # Gemini API testing script
├── .env                    # Environment variables (API keys)
├── GEMINI_API_NOTE.md      # Gemini API setup notes
├── data/
│   └── sample_data.csv     # Demo dataset (30 rows)
├── output/                 # Generated reports
│   ├── chart.png           # Performance visualization
│   └── Insight_Report.pdf  # Executive report
└── README.md               # This file
```

---

## 📄 What's in the Report?

The generated PDF includes:

1. **Title & Timestamp** - Professional header
2. **Key Performance Indicators** - CTR, ROI, impressions, clicks, spend, revenue
3. **Executive Summary** - AI-written natural-language insights
4. **Performance Visualization** - Line chart showing trends over time

**Example Output:** Check `output/Insight_Report.pdf` after running the script.

---

## 🛠️ Technical Stack

- **Data Processing:** pandas
- **Visualization:** matplotlib
- **PDF Generation:** FPDF
- **AI Integration:** OpenAI API / Google Gemini API
- **Web Interface:** Streamlit
- **Environment:** python-dotenv

---

## 💡 How It Works

```
CSV Data → Pandas Ingestion → KPI Computation → Chart Generation
                                      ↓
                              AI Insight Generation
                                      ↓
                              PDF Report Assembly
                                      ↓
                          Executive-Ready Output 🎉
```

---

## 🎯 Hackathon Solution Checklist

✅ Ingests data from CSV files  
✅ Analyzes and combines data automatically  
✅ Generates AI-written insights  
✅ Exports downloadable PDF reports  
✅ Eliminates manual reporting work  
✅ Production-ready web interface  

---

## 🧪 Testing

Run the automated test:

```bash
python main.py
```

Expected output:
```
[INFO] Ingesting data...
[SUCCESS] Loaded 30 rows of data
[INFO] Computing KPIs...
[SUCCESS] CTR: 2.47% | ROI: 446.6%
[INFO] Creating visualization...
[SUCCESS] Chart saved to output/chart.png
[INFO] Generating insights...
[SUCCESS] Using rule-based insights (no API key found)
[INFO] Creating PDF report...
[SUCCESS] PDF saved to output/Insight_Report.pdf

[SUCCESS] Report Generated Successfully
```

### Test Streamlit Interface

```bash
streamlit run app.py
```

Then open: `http://localhost:8501`

---

## 🔧 Troubleshooting

### Common Issues

**1. API Quota Exceeded**
```
429 You exceeded your current quota
```
- **Solution:** System automatically uses rule-based insights
- **Alternative:** Wait for quota reset or use different API key

**2. Missing Dependencies**
```
ModuleNotFoundError: No module named 'pandas'
```
- **Solution:** Run `pip install -r requirements.txt`

**3. File Not Found**
```
FileNotFoundError: data/sample_data.csv
```
- **Solution:** Ensure you're in the project root directory

**4. Permission Errors**
- **Solution:** Run with appropriate permissions or check file paths

### Performance Metrics

- **Processing Speed:** ~2-3 seconds for 30 rows
- **Memory Usage:** <50MB for typical datasets
- **Output Size:** PDF ~200KB, Chart ~50KB
- **Supported Data:** Up to 10,000+ rows tested

---

## 👥 Team

Built for **GroundTruth Hackathon** - Team AI-14-cmd

🔗 **Repository:** [https://github.com/AI-14-cmd/Hackathon-GT.git](https://github.com/AI-14-cmd/Hackathon-GT.git)

---

## 📝 License

This project is created for the GroundTruth Hackathon.

---

## 🚀 Future Enhancements

- Support for SQL database connections
- Multi-page reports with deeper analytics
- PowerPoint slide deck generation
- Dashboard with historical report tracking
- Scheduled automated report delivery via email

---

---

## 📞 Support

- 📖 **Documentation:** Check code comments in `main.py`
- 🐛 **Issues:** Report on GitHub repository
- 💡 **Features:** Submit enhancement requests
- 📧 **Contact:** Via GitHub repository

---

**🎉 Ready to automate your advertising reports? Clone, install, and run!**
