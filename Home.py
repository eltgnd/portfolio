from info_txt import home_txt
import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.metric_cards import style_metric_cards

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

col1, col2 = st.columns([0.5,3])
with col1:
    st.button('Download my resumé', type='primary')
with col2:
    st.button('Contact me', type='primary')

st.write('')

# About
with st.container(border=True):
    write('ABOUT ME', size=caption_size, color='gray')
    write(home_txt['about'], size=content_size)

st.write('')
st.write('')

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

curr_color = color_ds
options = ['📊 Data Scientist Val', '💡 Science Communicator Val', '🖌️ Graphic Designer Val']
c = st.radio(label='Choose a Val!', options=options, horizontal=False)
st.divider()
if c == options[0]:
    curr_color = color_ds
    chooseyourval(quote='I want to use data science to unravel patterns that ',
        quote_highlight = 'derive actionable insights',
        quote_color = color_ds,
        description = home_txt['ds'],
        img_link = 'images/Data Scientist Val.png',
        emoji='📊')
elif c == options[1]:
    curr_color = color_sc
    chooseyourval(quote='I believe knowing complex ideas isn\'t enough —',
        quote_highlight = 'it needs to be accessible to the public too',
        quote_color = color_sc,
        description = home_txt['sc'],
        img_link = 'images/Science Communicator Val.png',
        emoji='💡') 
elif c == options[2]:
    curr_color = color_gd
    chooseyourval(quote='I love graphic design because it lets me ',
        quote_highlight = 'tell visually compelling stories',
        quote_color = color_gd,
        description = home_txt['gd'],
        img_link = 'images/Graphic Designer Val.png',
            emoji='🖌️')     
st.divider()

# ds, sc, gd = st.tabs(['📊 Data Scientist Val', '💡 Science Communicator Val', '🖌️ Graphic Designer Val'])
# with ds:
#     chooseyourval(quote='I want to use data science to unravel patterns that ',
#         quote_highlight = 'derive actionable insights',
#         quote_color = color_ds,
#         description = home_txt['ds'],
#         img_link = 'images/Data Scientist Val.png',
#         emoji='📊')
# with sc:
#     chooseyourval(quote='I believe knowing complex ideas isn\'t enough —',
#         quote_highlight = 'it needs to be accessible to the public too',
#         quote_color = color_sc,
#         description = home_txt['sc'],
#         img_link = 'images/Science Communicator Val.png',
#         emoji='💡') 
# with gd:
#     chooseyourval(quote='I love graphic design because it lets me ',
#         quote_highlight = 'tell visually compelling stories',
#         quote_color = color_gd,
#         description = home_txt['gd'],
#         img_link = 'images/Graphic Designer Val.png',
#         emoji='🖌️')     

# Metric cards
st.write('')

col1, col2, col3 = st.columns(3)
col1.metric(label="Data Science Projects", value=5000, delta=1000)
col2.metric(label="New Content Posts", value=5000, delta=-1000)
col3.metric(label="Graphic Design Projects", value=5000, delta=0)

style_metric_cards(border_left_color=curr_color,box_shadow=False)

# Timeline
st.divider()
