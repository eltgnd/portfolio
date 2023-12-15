from info_txt import home_txt
import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(layout='wide', initial_sidebar_state="expanded")

my_font = 'Open Sans'
title_size = 40
heading_size = 28
caption_size = 12
content_size = 16

# Colors
color_ds = '#3ead20'
color_sc = '#1d67c2'
color_gd = '#f73e77'


def write(s, font=my_font, size=40, color='black', weight='light'):
    to_markdown = f"""<span style= "font-family:{my_font} ; font-size:{size}px ; color:{color} ; font-weight:{weight} ; ">{s}</span>"""
    st.markdown(to_markdown, unsafe_allow_html=True)

# Photo
st.image('https://scontent.xx.fbcdn.net/v/t1.15752-9/407069039_919924335639929_1048753321996585183_n.png?_nc_cat=109&ccb=1-7&_nc_sid=510075&_nc_eui2=AeEMrg_JmTL_5N0e-Zh4cN5ZCnjAALAC8EMKeMAAsALwQzjrvnpaRxs20IQqoOSbUJiLBrlg8CoWb8APvvBCU5su&_nc_ohc=d3jf3esaDfYAX_IOjIj&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&cb_e2o_trans=q&oh=03_AdRlv6K__pQ1vA6k8cVDi2l1nmQr_1kwPjIGHWPLsB2dSg&oe=65A34463', width=125)
st.write('')

# Title
title = f"""
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">Hi, I'm Val and I love </span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:#3ead20 ; font-weight:600 ; ">data science</span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">, </span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:#1d67c2 ; font-weight:600 ; ">science communication</span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">, and </span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:#f73e77 ; font-weight:600 ; ">graphic design</span>
<span style="  font-family:{my_font} ; font-size:{title_size}px ; color:black ; font-weight:light ; ">. 👋</span>
"""
st.markdown(title, unsafe_allow_html=True)
st.write('')

# About
with st.container(border=True):
    write('ABOUT ME', size=caption_size, color='gray')
    write(home_txt['about'], size=content_size)
    st.write('')

st.write('')
st.write('')

# col1, col2 = st.columns(2, gap='medium')
# with col1:
#     st.image('https://scontent.fcrk3-1.fna.fbcdn.net/v/t39.30808-6/410353355_851624143814966_7245468193696776366_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=3635dc&_nc_eui2=AeETa1stRtct-4jI6TXDlLfNHowdPapDmAsejB09qkOYC87qAuyO_vF8fKVw4f9g4i43w-fQ4tO6m0SkKr8LBqQV&_nc_ohc=dK2-mpglss8AX9S-9zH&_nc_ht=scontent.fcrk3-1.fna&cb_e2o_trans=q&oh=00_AfC2Ac1jUOkR4W1oVZ3NLyKtO4z1iidk2SD2nUbxasMzDQ&oe=657F8907')
# with col2:
#     with st.container(border=True):
#         st.radio('CHOOSE A VAL',['Data Scientist Val', 'Science Communicator Val', 'Graphic Designer Val'])

# Choose your Val
def chooseyourval(quote, quote_highlight, description, img_link, emoji, quote_color='#000000'):
    st.write('')
    col1, col2 = st.columns(2, gap='medium')
    with col1:
        # rain(emoji=emoji,font_size=40, falling_speed=7, animation_length=7)

        # Heading
        title = f"""
        <span style="  font-family:{my_font} ; font-size:{heading_size}px ; color:black ; font-weight:light ; ">{quote}</span>
        <span style="  font-family:{my_font} ; font-size:{heading_size}px ; color:{quote_color} ; font-style:italic; font-weight:600 ; ">{quote_highlight}</span>
        <span style="  font-family:{my_font} ; font-size:{heading_size}px ; color:black ; font-weight:light ; ">.</span>
        """
        st.write('')
        st.markdown(title, unsafe_allow_html=True)
        # Subheading
        write(description, size=content_size)
    with col2:
        st.image(img_link)

ds, sc, gd = st.tabs(['📊 Data Scientist Val', '💡 Science Communicator Val', '🖌️ Graphic Designer Val'])
with ds:
    chooseyourval(quote='I want to use data science to unravel patterns that ',
        quote_highlight = 'derive actionable insights',
        quote_color = color_ds,
        description = home_txt['ds'],
        img_link = 'images/Data Scientist Val.png',
        emoji='📊')
with sc:
    chooseyourval(quote='I believe knowing complex ideas isn\'t enough —',
        quote_highlight = 'it needs to be accessible to the public too',
        quote_color = color_sc,
        description = home_txt['sc'],
        img_link = 'images/Science Communicator Val.png',
        emoji='💡') 
with gd:
    chooseyourval(quote='I love graphic design because it lets me ',
        quote_highlight = 'tell visually compelling stories',
        quote_color = color_gd,
        description = home_txt['gd'],
        img_link = 'images/Graphic Designer Val.png',
        emoji='🖌️')     

# Timeline