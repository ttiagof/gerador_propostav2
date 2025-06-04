from flask import Flask, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

FORM_HTML = '''
<!doctype html>
<title>Gerador de PDF</title>
<h1>Preencha o Formul\u00e1rio</h1>
<form method="post">
  <label>Nome: <input type="text" name="nome"></label><br>
  <label>Email: <input type="email" name="email"></label><br>
  <label>Mensagem:<br><textarea name="mensagem" rows="4" cols="40"></textarea></label><br>
  <input type="submit" value="Gerar PDF">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome', '')
        email = request.form.get('email', '')
        mensagem = request.form.get('mensagem', '')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt="Dados do formul\u00e1rio", ln=True, align='C')
        pdf.ln(5)
        pdf.cell(0, 10, txt=f"Nome: {nome}", ln=True)
        pdf.cell(0, 10, txt=f"Email: {email}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Mensagem: {mensagem}")

        pdf_bytes = pdf.output(dest='S').encode('latin1')
        return send_file(
            io.BytesIO(pdf_bytes),
            as_attachment=True,
            download_name='formulario.pdf',
            mimetype='application/pdf'
        )
    return FORM_HTML

if __name__ == '__main__':
    app.run(debug=True)
