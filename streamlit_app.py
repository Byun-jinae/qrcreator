import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

st.title('QR 코드 생성기')

data = st.text_input('QR 코드에 인코딩할 데이터를 입력하세요:')

if st.button('QR 코드 생성'):
    if data:
        img = generate_qr_code(data)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        st.image(buffered, caption='생성된 QR 코드')
    else:
        st.error('데이터를 입력해 주세요.')
