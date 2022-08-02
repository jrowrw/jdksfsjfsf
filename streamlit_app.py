from email.mime import image
from nbformat import write
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title= "my webpage", page_icon=":tada:", layout="wide")

 
def load_lottieurl(url):
      r = requests.get(url)
      if r.status_code != 200:
          return None
      return r.json()


lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_0whtym8p.json")


with st.container():
    st.subheader("hi , im mohamed  :wave:")
    st.title("a begginer python dev from egypt")
    st.write("my dream is to shopping website like amazon")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write("##")
        st.write("me do some projects in furture")
with right_column:
     st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        
      with text_column:
          st.subheader("some python tutorial videos but not MINE" )
          
          st.subheader("and some python projects but not mine")

          st.markdown("[Watch Video...](https://www.youtube.com/watch?v=WTRKeSoynKI&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=3")
          st.markdown("[Watch Video...](https://www.youtube.com/watch?v=OlZoEMdM530&list=PLuXY3ddo_8nzCVqXcTFqwcM5R0gZiMRiW")


    


