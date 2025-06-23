from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/preview', methods=['POST'])
def preview():
    data = request.form
    template = data.get('template', 'resume_template1.html')
    return render_template(template, data=data)


@app.route('/generate', methods=['POST'])
def generate_resume():
    data = request.form
    template = data.get('template', 'resume_template1.html')
    rendered = render_template(template, data=data)
    pdf_file = 'generated/resume.pdf'
    pdfkit.from_string(rendered, pdf_file, configuration=config)

    return send_file(pdf_file, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('generated'):
        os.mkdir('generated')
    app.run(debug=True)
