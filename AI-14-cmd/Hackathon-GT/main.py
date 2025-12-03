"""
InsightX - Automated Insight Engine
Main script for data ingestion, analysis, visualization, and PDF report generation.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def ingest_and_clean_data(csv_path):
    """
    Ingest CSV data and clean it.
    
    Args:
        csv_path: Path to the CSV file
        
    Returns:
        Cleaned pandas DataFrame
    """
    print("[INFO] Ingesting data...")
    df = pd.read_csv(csv_path)
    
    # Handle nulls - fill numeric columns with 0
    numeric_columns = ['clicks', 'impressions', 'ad_spend', 'revenue']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].fillna(0)
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    print(f"[SUCCESS] Loaded {len(df)} rows of data")
    return df


def compute_kpis(df):
    """
    Compute key performance indicators.
    
    Args:
        df: DataFrame with advertising data
        
    Returns:
        Dictionary with KPI values
    """
    print("[INFO] Computing KPIs...")
    
    total_clicks = df['clicks'].sum()
    total_impressions = df['impressions'].sum()
    total_spend = df['ad_spend'].sum()
    total_revenue = df['revenue'].sum()
    
    # Calculate CTR and ROI
    ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
    roi = (total_revenue / total_spend * 100) if total_spend > 0 else 0
    
    kpis = {
        'ctr': round(ctr, 2),
        'roi': round(roi, 2),
        'total_clicks': int(total_clicks),
        'total_impressions': int(total_impressions),
        'total_spend': round(total_spend, 2),
        'total_revenue': round(total_revenue, 2)
    }
    
    print(f"[SUCCESS] CTR: {kpis['ctr']}% | ROI: {kpis['roi']}%")
    return kpis


def create_visualization(df, output_dir):
    """
    Create a line chart of Clicks vs Date.
    
    Args:
        df: DataFrame with advertising data
        output_dir: Directory to save the chart
        
    Returns:
        Path to the saved chart image
    """
    print("[INFO] Creating visualization...")
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['clicks'], marker='o', linewidth=2, color='#2563eb')
    plt.title('Campaign Performance: Clicks Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Date', fontsize=11)
    plt.ylabel('Clicks', fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart_path = os.path.join(output_dir, 'chart.png')
    plt.savefig(chart_path, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"[SUCCESS] Chart saved to {chart_path}")
    return chart_path


def generate_ai_insights(kpis, df):
    """
    Generate AI-powered insights using OpenAI or Google Gemini, with fallback.
    
    Args:
        kpis: Dictionary of KPI values
        df: DataFrame with advertising data
        
    Returns:
        Insight text string
    """
    print("[INFO] Generating insights...")
    
    # Prepare data summary for AI
    first_week_clicks = df['clicks'][:7].mean()
    last_week_clicks = df['clicks'][-7:].mean()
    trend = "improving" if last_week_clicks > first_week_clicks else "declining"
    
    prompt = f"""Analyze this advertising campaign performance data and provide a concise 3-4 sentence executive summary:

- CTR (Click-Through Rate): {kpis['ctr']}%
- ROI (Return on Investment): {kpis['roi']}%
- Total Clicks: {kpis['total_clicks']:,}
- Total Impressions: {kpis['total_impressions']:,}
- Total Ad Spend: ${kpis['total_spend']:,.2f}
- Total Revenue: ${kpis['total_revenue']:,.2f}
- Trend: {trend}

Provide actionable insights focusing on performance and recommendations."""

    # Try OpenAI first
    openai_key = os.getenv('OPENAI_API_KEY')
    if openai_key:
        try:
            import openai
            openai.api_key = openai_key
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert advertising analyst."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            insight = response.choices[0].message.content.strip()
            print("[SUCCESS] AI insights generated (OpenAI)")
            return insight
        except Exception as e:
            print(f"[WARNING] OpenAI failed: {e}")
    
    # Try Google Gemini
    google_key = os.getenv('GOOGLE_API_KEY')
    if google_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=google_key)
            # Use models/ prefix for model names
            model = genai.GenerativeModel('models/gemini-2.0-flash-exp')
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=200,
                    temperature=0.7,
                )
            )
            insight = response.text.strip()
            print("[SUCCESS] AI insights generated (Gemini)")
            return insight
        except Exception as e:
            print(f"[WARNING] Gemini failed: {e}")
    
    # Fallback to rule-based insights
    print("[SUCCESS] Using rule-based insights (no API key found)")
    insight = f"""The campaign achieved a CTR of {kpis['ctr']}% and an ROI of {kpis['roi']}%, indicating {'strong' if kpis['roi'] > 200 else 'moderate'} performance. With {kpis['total_clicks']:,} total clicks from {kpis['total_impressions']:,} impressions, the engagement trend is {trend} week over week. Total revenue of ${kpis['total_revenue']:,.2f} was generated from ${kpis['total_spend']:,.2f} in ad spend. {'Continue scaling investment to capitalize on positive momentum.' if trend == 'improving' else 'Consider optimizing targeting and creative to improve engagement.'}"""
    
    return insight


def create_pdf_report(kpis, insight, chart_path, output_dir):
    """
    Create a professional PDF report with KPIs, insights, and chart.
    
    Args:
        kpis: Dictionary of KPI values
        insight: AI-generated insight text
        chart_path: Path to the chart image
        output_dir: Directory to save the PDF
        
    Returns:
        Path to the generated PDF
    """
    print("[INFO] Creating PDF report...")
    
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, 'Automated Insight Report', ln=True, align='C')
    pdf.ln(5)
    
    # Date
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", ln=True, align='C')
    pdf.ln(10)
    
    # KPI Section
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Key Performance Indicators', ln=True)
    pdf.ln(2)
    
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 8, f"Click-Through Rate (CTR): {kpis['ctr']}%", ln=True)
    pdf.cell(0, 8, f"Return on Investment (ROI): {kpis['roi']}%", ln=True)
    pdf.cell(0, 8, f"Total Clicks: {kpis['total_clicks']:,}", ln=True)
    pdf.cell(0, 8, f"Total Impressions: {kpis['total_impressions']:,}", ln=True)
    pdf.cell(0, 8, f"Total Ad Spend: ${kpis['total_spend']:,.2f}", ln=True)
    pdf.cell(0, 8, f"Total Revenue: ${kpis['total_revenue']:,.2f}", ln=True)
    pdf.ln(10)
    
    # Insights Section
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Executive Summary', ln=True)
    pdf.ln(2)
    
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 6, insight)
    pdf.ln(10)
    
    # Chart Section
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Performance Visualization', ln=True)
    pdf.ln(5)
    
    # Add chart image
    if os.path.exists(chart_path):
        pdf.image(chart_path, x=10, w=190)
    
    # Save PDF
    pdf_path = os.path.join(output_dir, 'Insight_Report.pdf')
    pdf.output(pdf_path)
    
    print(f"[SUCCESS] PDF saved to {pdf_path}")
    return pdf_path


def generate_report(csv_path='data/sample_data.csv'):
    """
    Main function to orchestrate the entire report generation pipeline.
    
    Args:
        csv_path: Path to the input CSV file
    """
    # Create output directory if it doesn't exist
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Step 1: Ingest and clean data
        df = ingest_and_clean_data(csv_path)
        
        # Step 2: Compute KPIs
        kpis = compute_kpis(df)
        
        # Step 3: Create visualization
        chart_path = create_visualization(df, output_dir)
        
        # Step 4: Generate AI insights
        insight = generate_ai_insights(kpis, df)
        
        # Step 5: Create PDF report
        pdf_path = create_pdf_report(kpis, insight, chart_path, output_dir)
        
        print("\n[SUCCESS] Report Generated Successfully")
        print(f"[INFO] Output saved to: {output_dir}/")
        
        return pdf_path
        
    except Exception as e:
        print(f"\n[ERROR] Error generating report: {e}")
        raise


if __name__ == '__main__':
    generate_report()
