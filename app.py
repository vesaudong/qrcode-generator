import eel
import pyqrcode
import io
import base64

eel.init('www')

@eel.expose
def generate(data):
    code = pyqrcode.create(data, encoding='utf-8')
    buffers = io.BytesIO()
    code.png(buffers, scale=10)
    encoded = base64.b64encode(buffers.getvalue()).decode('utf-8')
    return 'data:image/png;base64,' + encoded

eel.start('home.html', size=(600, 250))
