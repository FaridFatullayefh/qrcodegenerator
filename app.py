from flask import Flask, render_template, request, url_for
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_data = None

    if request.method == 'POST':
        data = request.form['data']
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img_byte_arr = BytesIO()
        img.save(img_byte_arr)
        img_byte_arr.seek(0)

        img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

        qr_code_data = img_base64

    return render_template('index.html', qr_code_data=qr_code_data)

if __name__ == '__main__':
    app.run(debug=True)
