import streamlit as st
# from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout='wide', initial_sidebar_state="expanded")

my_font = 'Open Sans'
title_size = 40
heading_size = 28
caption_size = 12
content_size = 16
color_ds = '#3ead20'

def write(s, font=my_font, size=40, color='black', weight='light'):
    to_markdown = f"""<span style= "font-family:{my_font} ; font-size:{size}px ; color:{color} ; font-weight:{weight} ; ">{s}</span>"""
    st.markdown(to_markdown, unsafe_allow_html=True)

# Title
write('Data Science Projects', size=title_size)

# with st.sidebar:
#     st.radio(label='hi',options=['1','2','3'])
# # tab1, tab2, tab3 = st.tabs(['','2','3'])
# # with tab1:
# #     st.write('hi')

# want_to_contribute = st.button("I want to contribute!")
# if want_to_contribute:
#     switch_page("")