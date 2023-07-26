import os
from io import BytesIO
from flask import Flask, render_template, request, redirect, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_files = request.files.getlist('images')

    pdf = FPDF()
    pdf_bytes = BytesIO()

    for file in uploaded_files:
        if file.filename != '':
            image_data = file.read()
            pdf.add_page()
            pdf.image(image_data, 10, 10, 190)

    pdf.output(pdf_bytes)  
    pdf_bytes.seek(0)

    return send_file(
        pdf_bytes,
        as_attachment=True,
        download_name = 'output.pdf',
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
