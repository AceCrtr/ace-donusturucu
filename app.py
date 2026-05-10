from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import io
import os

app = Flask(__name__)
# Sitemizin bu sunucuya bağlanıp dosya göndermesine izin veriyoruz
CORS(app) 

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "Dosya seçilmedi", 400
    
    file = request.files['file']
    img = Image.open(file)
    
    # Resmi PDF'e çevirme işlemi
    img = img.convert('RGB')
    pdf_io = io.BytesIO()
    img.save(pdf_io, 'PDF')
    pdf_io.seek(0)
    
    return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name='ace-donusturucu.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

