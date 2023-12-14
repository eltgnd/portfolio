from info_txt import about_txt
import streamlit as st

st.set_page_config(layout='wide', initial_sidebar_state="expanded")

my_font = 'Open Sans'


def write(s, font=my_font, size=40, color='black', weight='light'):
    to_markdown = f"""<span style= "font-family:{my_font} ; font-size:{size}px ; color:{color} ; font-weight:{weight} ; ">{s}</span>"""
    st.markdown(to_markdown, unsafe_allow_html=True)

# Title
title_size = '40'
title = f"""
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">Hi, I'm Val and I love </span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:#3ead20 ; font-weight:600 ; ">data science</span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">, </span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:#1d67c2 ; font-weight:600 ; ">science communication</span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">, and </span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:#f73e77 ; font-weight:600 ; ">graphic design</span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">.</span>
"""
st.markdown(title, unsafe_allow_html=True)

# About

st.write('')
write('ABOUT ME', size=14, color='gray')
write(about_txt, size=16)

st.write('')
st.write('')

col1, col2 = st.columns(2, gap='medium')
with col1:
    st.image('https://scontent.fcrk3-1.fna.fbcdn.net/v/t39.30808-6/410353355_851624143814966_7245468193696776366_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeETa1stRtct-4jI6TXDlLfNHowdPapDmAsejB09qkOYC87qAuyO_vF8fKVw4f9g4i43w-fQ4tO6m0SkKr8LBqQV&_nc_ohc=dK2-mpglss8AX9S-9zH&_nc_ht=scontent.fcrk3-1.fna&cb_e2o_trans=q&oh=00_AfC2Ac1jUOkR4W1oVZ3NLyKtO4z1iidk2SD2nUbxasMzDQ&oe=657F8907')
with col2:
    st.radio('CHOOSE A VAL',['Data Scientist Val', 'Science Communicator Val', 'Graphic Designer Val'])

# Buttons
st.write('')
st.write('')
write('LET\'S CONNECT', size='18', color='gray')