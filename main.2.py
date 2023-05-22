import streamlit as st 
from PIL import Image
import html
import streamlit as st
import base64
from PIL import Image
import io

#set title image
img = Image.open('logo.png')

st.set_page_config(page_title='Tahu Abah Ismail', page_icon = img)


#set config
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html = True)

img3 = Image.open("header (1).png")

st.image(img3)
#st.text('Jl. Masjid Cibuluh No.130, RT.03/RW.03, Cibuluh, Kec. Bogor Utara, Bogor')
st.markdown("---")



taba_img = Image.open('tahu baso.jpg')
keripik_img = Image.open('keripik tahu.jpg')
tofu_img = Image.open('tahu putih.jpg')
bulat_img = Image.open('tahu bulat.jpg')

col1,col2 = st.columns([2,2])

with col1:
    st.image(taba_img)
with col2:
    st.subheader('1.Tahu Baso Abah')
    st.write("\tTahu baso setengah matang yang sudah siap dikonsumsi \n tetapi lebih nikmat jika dihangatkan")


col1_1,col2_1 = st.columns([2,2])

with col1_1:
    st.image(keripik_img)
with col2_1:
    st.subheader('2.Keripik Tahu Abah')
    st.write('Camilan Keripik Tahu Abah cocok untuk dijadikan camilan keluarga dan teman minum kopi')


col1_2,col2_2 = st.columns([2,2])

with col1_2:
    st.image(tofu_img)
with col2_2:
    st.subheader('3.Tahu Susu Abah')
    st.write('Tahu Susu Abah cocok sebagai tambahan soup ataupun dijadikan tahu goreng, lembut dan nikmat!')


col1_3,col2_3 = st.columns([2,2])

with col1_3:
    st.image(bulat_img)
with col2_3:
    st.subheader('4.Tahu Bulat Abah')
    st.write('Tahu Bulat Abah cocoks sebagai camilan, dengan rasa yang gurih dan kopong memberikan sensasi tahu bulat yang otentik')

st.markdown("---")





st.subheader('Contact Us:')

wa = Image.open('whatsapp.png')
mail = Image.open('mail.png')
ig = Image.open('ig.png')
fb = Image.open('fb.png')

col1_c,col2_c= st.columns([1,8])

with col1_c:
    # Load the image from local storage using PIL
    image_path = 'whatsapp.png'
    image = Image.open(image_path)

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()

    # Convert the bytes to base64 string
    image_base64 = base64.b64encode(image_bytes).decode()

    # Generate the link URL
    link_url = 'https://api.whatsapp.com/send?phone=6281283287360'  # Ganti dengan URL yang sesuai

    # Generate the HTML code with the linked image
    link_html = f'<a href="{html.escape(link_url)}"><img src="data:image/png;base64,{image_base64}" alt="gambar"></a>'

    # Display the linked image in Streamlit
    st.markdown(link_html, unsafe_allow_html=True)


with col2_c:
    st.image(mail)


col3_c,col4_c = st.columns([1,8])
with col3_c:
    st.image(ig)
    
with col4_c:
    st.image(fb)




