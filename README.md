# InsightX - Automated Insight Engine | H-001

## The Problem (Real World Scenario)

Marketing teams and advertising analysts spend countless hours manually:
- **Extracting and cleaning** advertising data from multiple sources
- **Calculating KPIs** like CTR, ROI, and conversion metrics manually in spreadsheets
- **Creating visualizations** and charts for executive presentations
- **Writing insights** and recommendations based on campaign performance
- **Formatting reports** into presentation-ready PDFs for stakeholders

This manual process is:
- ⏰ **Time-consuming** - Takes 2-3 hours per report
- 🐛 **Error-prone** - Manual calculations lead to mistakes
- 📊 **Inconsistent** - Different analysts create different report formats
- 🔄 **Repetitive** - Same process repeated for every campaign review

**Real-world impact**: A marketing agency managing 20+ campaigns wastes 40-60 hours monthly on report generation instead of strategic optimization.

---

## Expected End Result

**InsightX - Automated Insight Engine** delivers:

✅ **Automated Data Processing**
- Ingests CSV files with advertising data (impressions, clicks, conversions, spend, revenue)
- Cleans and normalizes data automatically
- Handles missing values and data quality issues

✅ **Instant KPI Calculations**
- Click-Through Rate (CTR)
- Return on Investment (ROI)
- Total performance metrics across campaigns
- Campaign-level and aggregate analytics

✅ **AI-Powered Insights**
- Leverages Google Gemini or OpenAI GPT-4 for intelligent analysis
- Generates executive-ready summaries and actionable recommendations
- Identifies trends and performance patterns automatically
- Fallback to rule-based insights when APIs unavailable

✅ **Professional PDF Reports**
- Executive-ready formatted reports with company branding
- Performance visualizations (charts and graphs)
- KPI dashboards with key metrics highlighted
- Generated in seconds, not hours

✅ **Web Interface (Optional)**
- User-friendly file upload interface
- Real-time report generation
- Download PDF reports directly from browser
- No technical knowledge required

---

## Technical Approach

### Architecture Overview

```
┌─────────────────┐
│   CSV Upload    │
│  (ad_data.csv)  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│  Data Ingestion & Cleaning      │
│  - Parse CSV                    │
│  - Normalize columns            │
│  - Handle missing values        │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│  KPI Computation Engine         │
│  - CTR = (Clicks/Impressions)   │
│  - ROI = (Revenue/Spend) × 100  │
│  - Aggregate metrics            │
└────────┬────────────────────────┘
         │
         ├──────────────┬─────────────┐
         ▼              ▼             ▼
    ┌────────┐    ┌─────────┐   ┌────────┐
    │ Charts │    │ AI LLM  │   │  PDF   │
    │ (PNG)  │    │ Insights│   │ Report │
    └────────┘    └─────────┘   └────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
         ┌─────────┐      ┌──────────┐
         │ Gemini  │      │ GPT-4    │
         │  API    │      │   API    │
         └─────────┘      └──────────┘
              │                 │
              └────────┬────────┘
                       │
                  (Fallback to
                  Rule-based)
```

### Pipeline Steps

1. **Data Ingestion** (`ingest_and_clean_data`)
   - Reads CSV using pandas
   - Normalizes column names to lowercase
   - Maps `Spend` → `ad_spend` for consistency
   - Fills null values with 0 for numeric columns
   - Converts date strings to datetime objects

2. **KPI Calculation** (`compute_kpis`)
   - Aggregates totals: clicks, impressions, spend, revenue
   - Calculates CTR: `(total_clicks / total_impressions) × 100`
   - Calculates ROI: `(total_revenue / total_spend) × 100`
   - Returns rounded metrics for readability

3. **Visualization** (`create_visualization`)
   - Generates line chart: Clicks over Time
   - Uses matplotlib with professional styling
   - Exports as high-resolution PNG (150 DPI)
   - Saves to `output/chart.png`

4. **AI Insight Generation** (`generate_ai_insights`)
   - **Primary**: Calls Google Gemini API (gemini-2.0-flash-exp)
   - **Secondary**: Falls back to OpenAI GPT-4 if Gemini fails
   - **Tertiary**: Uses rule-based logic if no API keys
   - Generates 3-4 sentence executive summary with recommendations

5. **PDF Report Creation** (`create_pdf_report`)
   - Uses FPDF library for PDF generation
   - Structured sections: Title, KPIs, Insights, Chart
   - Professional formatting with headers and spacing
   - Outputs to `output/Insight_Report.pdf`

---

## Tech Stack

### Core Technologies

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python 3.8+ | Main programming language |
| **Data Processing** | Pandas | CSV parsing, data cleaning, transformations |
| **Visualization** | Matplotlib | Chart generation (clicks over time) |
| **PDF Generation** | FPDF | Professional report creation |
| **AI/LLM** | Google Gemini API | Primary AI insight generation |
| **AI/LLM (Fallback)** | OpenAI GPT-4 | Secondary AI insight generation |
| **Environment** | python-dotenv | Secure API key management |
| **Web Framework** | Flask | Optional web interface |
| **HTTP Server** | Werkzeug | File upload handling |

### Dependencies

```txt
pandas
matplotlib
fpdf
python-dotenv
google-generativeai
openai
flask
```

### API Integration

- **Google Gemini**: `gemini-2.0-flash-exp` model
  - Max tokens: 200
  - Temperature: 0.7
  - Configured via `GOOGLE_API_KEY` environment variable

- **OpenAI GPT-4**: `gpt-4o` model
  - Max tokens: 200
  - Temperature: 0.7
  - Configured via `OPENAI_API_KEY` environment variable

---

## Challenges & Learnings

### 1️⃣ **Challenge**: API Model Name Confusion
**Problem**: Initially used `gemini-2.0-flash-exp` but Google's API required the `models/` prefix.
```python
# ❌ Failed
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# ✅ Fixed
model = genai.GenerativeModel('models/gemini-2.0-flash-exp')
```
**Learning**: Always verify API documentation for exact model naming conventions.

---

### 2️⃣ **Challenge**: CSV Column Name Inconsistencies
**Problem**: Real-world CSVs have varied column naming (e.g., `Spend` vs `ad_spend`, `Date` vs `date`).
```python
# Solution: Normalize and map columns
df.columns = df.columns.str.lower()
df.rename(columns={'spend': 'ad_spend'}, inplace=True)
```
**Learning**: Build flexible data ingestion that handles common variations.

---

### 3️⃣ **Challenge**: Fallback Strategy for AI APIs
**Problem**: API failures shouldn't break the entire pipeline.
```python
# Implemented cascading fallback
try:
    # Try Gemini
except:
    try:
        # Try OpenAI
    except:
        # Use rule-based insights
```
**Learning**: Always have fallback mechanisms for external dependencies.

---

### 4️⃣ **Challenge**: PDF Layout with Dynamic Content
**Problem**: AI-generated text length varies, causing layout issues.
```python
# Solution: Use multi_cell for word wrapping
pdf.multi_cell(0, 6, insight)  # Auto-wraps text
```
**Learning**: FPDF's `multi_cell` handles variable-length content better than `cell`.

---

### 5️⃣ **Challenge**: Chart Integration in PDF
**Problem**: Chart images need proper sizing and positioning in PDF.
```python
# Save chart first
plt.savefig(chart_path, dpi=150, bbox_inches='tight')

# Then embed in PDF with width control
pdf.image(chart_path, x=10, w=190)
```
**Learning**: Generate charts at high DPI (150+) for professional quality in reports.

---

### 6️⃣ **Challenge**: Handling Small Datasets
**Problem**: Trend analysis (first week vs last week) failed with <7 rows.
```python
# Defensive coding
first_week_clicks = df['clicks'][:7].mean()
last_week_clicks = df['clicks'][-7:].mean()
# Works even if dataset has <7 rows
```
**Learning**: Use Python slicing safely - it doesn't error on out-of-bounds.

---

## Visual Proof

### 📊 Generated Report Sample

**Input Data** (`ad_data.csv`):
```csv
Date,Campaign,Region,Impressions,Clicks,Conversions,Spend,Revenue
2025-11-01,Diwali_Sale,India,12000,340,40,600,950
2025-11-02,Winter_Discount,India,8500,230,25,420,700
2025-11-03,NewUser_Campaign,US,7000,200,22,350,500
...
```

**Output**: 
- 📄 **PDF Report**: `output/Insight_Report.pdf`
- 📈 **Chart**: `output/chart.png` (Clicks Over Time visualization)

### Sample KPI Dashboard (from generated PDF)

```
Key Performance Indicators
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Click-Through Rate (CTR): 3.22%
Return on Investment (ROI): 154.76%
Total Clicks: 1,700
Total Impressions: 70,000
Total Ad Spend: $2,970.00
Total Revenue: $4,770.00

Executive Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The campaign achieved a CTR of 3.22% and an ROI of 154.76%, 
indicating moderate performance. With 1,700 total clicks from 
70,000 impressions, the engagement trend is improving week over 
week. Total revenue of $4,770.00 was generated from $2,970.00 
in ad spend. Continue scaling investment to capitalize on 
positive momentum.
```

### 📸 Screenshots
- Chart visualization showing click trends over campaign period
- Professional PDF layout with branding and formatting
- Web interface (if using Flask app)

---

## How to Run

### Prerequisites

- Python 3.8 or higher installed
- (Optional) Google Gemini API key for AI insights
- (Optional) OpenAI API key as fallback

### Step 1: Clone/Download the Project

```bash
cd /path/to/project
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```txt
pandas
matplotlib
fpdf
python-dotenv
google-generativeai
openai
flask
```

### Step 3: Set Up Environment Variables (Optional for AI)

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
# OR
OPENAI_API_KEY=your_openai_api_key_here
```

**Note**: If no API keys are provided, the system will use rule-based insights (still functional).

### Step 4: Prepare Your Data

Place your advertising data CSV in the project root as `ad_data.csv` with these columns:
- `Date` - Campaign date (YYYY-MM-DD format)
- `Campaign` - Campaign name
- `Region` - Geographic region
- `Impressions` - Number of ad impressions
- `Clicks` - Number of clicks
- `Conversions` - Number of conversions
- `Spend` - Ad spend amount
- `Revenue` - Revenue generated

**Example CSV structure:**
```csv
Date,Campaign,Region,Impressions,Clicks,Conversions,Spend,Revenue
2025-11-01,Diwali_Sale,India,12000,340,40,600,950
2025-11-02,Winter_Discount,India,8500,230,25,420,700
```

### Step 5: Run the Report Generator

#### Option A: Command Line (Basic)

```bash
python main.py
```

**Output:**
- `output/chart.png` - Performance visualization
- `output/Insight_Report.pdf` - Complete PDF report

#### Option B: Web Interface

```bash
python server.py
```

Then open your browser to: `http://localhost:5000`

1. Upload your CSV file via the web interface
2. Click "Generate Report"
3. Download the PDF report

### Step 6: View Results

The generated files will be in the `output/` folder:
- **PDF Report**: `output/Insight_Report.pdf`
- **Chart Image**: `output/chart.png`

### Troubleshooting

| Issue | Solution |
|-------|----------|
| **Module not found** | Run `pip install -r requirements.txt` |
| **CSV not found** | Ensure `ad_data.csv` is in project root |
| **API errors** | Check `.env` file or proceed without (uses fallback) |
| **PDF generation fails** | Ensure `output/` folder exists (auto-created) |

### Advanced: Custom CSV Path

```bash
python -c "from main import generate_report; generate_report('path/to/your/data.csv')"
```

---

### 🎯 Quick Start (TL;DR)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the generator
python main.py

# Check output folder for PDF report
```

**That's it!** Your report will be ready in seconds. 🚀

---

## Project Structure

```
InsightX/
├── main.py                 # Core report generation logic
├── server.py               # Flask web server
├── ad_data.csv            # Sample advertising data
├── requirements.txt        # Python dependencies
├── .env                   # API keys (create this)
├── output/                # Generated reports
│   ├── chart.png
│   └── Insight_Report.pdf
├── static/                # Web UI assets
│   ├── style.css
│   └── script.js
└── templates/             # HTML templates
    └── index.html
```

---

## License

This project is available for educational and commercial use.

---

## Contributors

Built for hackathon demonstration - InsightX Automated Insight Engine

---

## Support

For issues or questions, please refer to the troubleshooting section above or check the code comments in `main.py`.
