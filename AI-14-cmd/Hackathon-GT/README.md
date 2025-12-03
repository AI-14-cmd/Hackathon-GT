# 📈 InsightX - Automated Insight Engine | H-001

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




**For Google Gemini:**
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

**No API Key?** No problem! The system automatically falls back to intelligent rule-based insights.

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
📊 Ingesting data...
✅ Loaded 30 rows of data
📈 Computing KPIs...
✅ CTR: 2.54% | ROI: 338.76%
📉 Creating visualization...
✅ Chart saved to output/chart.png
🤖 Generating insights...
✅ AI insights generated
📄 Creating PDF report...
✅ PDF saved to output/Insight_Report.pdf

✅ Report Generated Successfully
```

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


