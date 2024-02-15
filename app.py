import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
import requests

st.set_page_config(layout="wide")
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = load_lottie_url("https://lottie.host/0c1681fb-be3d-41a9-a7ff-34dc62a7cc00/FJDEziS74b.json")
lottie_contact = load_lottie_url("https://lottie.host/17b287ce-cdda-4e32-8332-669e99cb6ecc/fWQkoX38oH.json")
lottie_Auto = load_lottie_url("https://lottie.host/b7c22a23-d0be-4789-b937-69f56b270b31/azRRDr4od3.json")
lottie_cancer = load_lottie_url("https://lottie.host/1069f626-6944-4619-ae46-55f2cb0a314e/5F5eB4W7nI.json")
#image = Image.open("C:/Users/PREMR/Downloads/Desktop/Streamlit/Red-Dead-Redemption-2.jpg")


# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown

st.write("##")
st.subheader("Hey Guys  :wave:")
st.title("My Portfolio Website")
st.write(""" Prem Kumar Rasakonda""")
st.write("[Read More](https://www.linkedin.com/in/prem-kumar-rasakonda-b54046177/)")
st.write("___")
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        icons = ['person' , 'code-slash', 'chat-left-text-fill'],
        orientation = 'horizontal'
    )
    
if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Prem Kumar Rasakonda")
            st.title("Graduate from Texas A&M University - Commerce")
        with col2:
            st_lottie(lottie_url)
    st.write("___")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education:
            MASTER OF SCIENCE (M.S.) IN 
            COMPUTER SCIENCE at 
            Texas A&M University-Commerce
            Aug  2022 to May 2024
        """)
            
        with col4:
            st.header("""
            Expereince:
            Graduated Research Assistant at TAMUC, 
            co-authoring "Evaluating Unbalanced Network Data for Attack Detection" with extensive analysis. 
            Professional experience includes a Data Science Intern Trainee role at BEPEC SOLUTION and an Assistant Systems Engineer position at Tata Consultancy Services. 
            Led various personal projects, including a restaurant chatbot, deep learning-based face recognition, and contributions to conversational AI and image recognition projects.""")
            
if selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6  = st.columns((1,2))
        with col5:
            st_lottie(lottie_Auto, height = 150)
            # st.image(image)
        with col6:
            st.subheader("Automobile Price prediction")
            st.write("Predicted prices of automobile usinh different ML algorithms")
            st.markdown("[Visit Github Repo](https://github.com/prem8667)")
    with st.container():
        
        st.write("##")
        col7, col8  = st.columns((1,2))
        with col7:
            st_lottie(lottie_cancer, height = 150)

        with col8:
            st.subheader("Cancer Prediction")
            st.write("Predicted Cancer using Logistic KNN and Decision-Tree")
            st.markdown("[Visit Github Repo](https://github.com/prem8667)")

if selected== "Contact":
    st.header("Get in touch!")
    st.write("##")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/premrasakonda@email.com" method="POST">
     <input type="hidden" name="_captcha" value ="false">
     <input type="text" name="name" placeholder = "your name" required>
     <input type="email" name="email" placeholder =  "your email" required>
     <button type="submit">Send</button>
</form>
"""

    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html= True )
    with right_col:
        st_lottie(lottie_contact, height = 300)




