from flask import Flask, render_template, request, send_file, redirect, url_for
import os
from main import generate_report

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file and file.filename.endswith('.csv'):
        filepath = f"temp_{file.filename}"
        file.save(filepath)
        
        try:
            pdf_path = generate_report(filepath)
            os.remove(filepath)
            return render_template('result.html', success=True)
        except Exception as e:
            return render_template('result.html', success=False, error=str(e))
    
    return redirect(url_for('index'))

@app.route('/download')
def download():
    return send_file('output/Insight_Report.pdf', as_attachment=True)

@app.route('/demo')
def demo():
    try:
        generate_report()
        return render_template('result.html', success=True)
    except Exception as e:
        return render_template('result.html', success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5000)