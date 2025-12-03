"""
InsightX - Flask Web Server
Serves the HTML/CSS web interface and handles report generation.
"""

from flask import Flask, render_template, request, send_file, jsonify
import os
from werkzeug.utils import secure_filename
from main import generate_report
import traceback

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create necessary directories
os.makedirs('uploads', exist_ok=True)
os.makedirs('output', exist_ok=True)

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle CSV upload and generate report."""
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Only CSV files are allowed.'}), 400
        
        # Save the uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Generate the report
        pdf_path = generate_report(filepath)
        
        return jsonify({
            'success': True,
            'message': 'Report generated successfully!',
            'pdf_path': pdf_path
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': f'Error generating report: {str(e)}'}), 500

@app.route('/download-report')
def download_report():
    """Download the generated PDF report."""
    try:
        pdf_path = os.path.join('output', 'Insight_Report.pdf')
        if os.path.exists(pdf_path):
            return send_file(pdf_path, as_attachment=True, download_name='InsightX_Report.pdf')
        else:
            return jsonify({'error': 'Report not found. Please generate a report first.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate-sample')
def generate_sample():
    """Generate a report using the sample data."""
    try:
        pdf_path = generate_report('data/sample_data.csv')
        return jsonify({
            'success': True,
            'message': 'Sample report generated successfully!',
            'pdf_path': pdf_path
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        traceback.print_exc()
        return jsonify({'error': f'Error generating sample report: {str(e)}'}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("InsightX - Automated Insight Engine")
    print("="*60)
    print("\nWeb server starting...")
    print("Open your browser and go to: http://localhost:5000")
    print("\n" + "="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
