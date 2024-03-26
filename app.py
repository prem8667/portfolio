

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
image = Image.open('IMG_20201014_182146_441.jpg') 
lottie_url = load_lottie_url("https://lottie.host/0c1681fb-be3d-41a9-a7ff-34dc62a7cc00/FJDEziS74b.json")
lottie_contact = load_lottie_url("https://lottie.host/17b287ce-cdda-4e32-8332-669e99cb6ecc/fWQkoX38oH.json")
lottie_Auto = load_lottie_url("https://lottie.host/b7c22a23-d0be-4789-b937-69f56b270b31/azRRDr4od3.json")
lottie_cyber = load_lottie_url("https://lottie.host/1f3e40a9-cccf-4a2e-b579-593c161a62af/oB3NUJ63sD.json")
lottie_cancer = load_lottie_url("https://lottie.host/1069f626-6944-4619-ae46-55f2cb0a314e/5F5eB4W7nI.json")
lottie_Chatbot = load_lottie_url("https://lottie.host/1adade21-2016-46af-8fdd-528c28bc6721/geW1l6x5pd.json")
lottie_sentiment = load_lottie_url("https://lottie.host/1d5412d0-0740-4441-b6ba-d75134deb657/AkXR9HT9EK.json")
lottie_qa = load_lottie_url("https://lottie.host/adddee58-687c-48e9-a78c-844be18b8857/6dfo9OLIQz.json")
lottie_blog = load_lottie_url("https://lottie.host/a1ffcf82-6fbd-467f-8595-fd7b210db647/mfZ9GjqBBu.json")
lottie_newsresearch = load_lottie_url("https://lottie.host/1e1fc41e-53df-4f62-9200-a7da5a3bc8b4/8tpjMFJMfb.json")
lottie_linkedin = load_lottie_url("https://lottie.host/ba1892ee-ed64-432a-ad04-4fc25435435b/zA5wtkxal0.json")
lottie_email = load_lottie_url("https://lottie.host/858252e7-bdce-4ace-a3a0-d86d1d28aa28/gnHmk0Ip0V.json")
lottie_phn = load_lottie_url("https://lottie.host/d216b690-b992-459c-9d99-6b373c3e06fb/JpXSt0i0eG.json")




# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown
with st.container():
        colu1, colu2 = st.columns(2)
        with colu1:
            st.write("##")
            st.subheader("Hey Guys  :wave:")
            st.title("My Portfolio Website")
            st.write(""" Prem Kumar Rasakonda""")
            st.write("[Read More](https://www.linkedin.com/in/prem-kumar-rasakonda-b54046177/)")
        with colu2:
            st.image(image, width = 200)
with st.container():
        colu3, colu4, colu5, colu6, colu7, colu8 = st.columns(6)
        with colu3:
            st_lottie(lottie_linkedin, height=30, width=30)
        with colu4:
            st.write("[Linkedin](https://www.linkedin.com/in/prem-kumar-rasakonda-b54046177/)")
            
        with colu5:
            st_lottie(lottie_email, height=50, width=50)
        with colu6:
            st.write("Premrasakonda@gmail.com")
        with colu7:
            st_lottie(lottie_phn, height=30, width=30)
        with colu8:
            st.write("+1 (945)900-3469")


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
            st_lottie(lottie_Chatbot, height = 150)
            # st.image(image)
        with col6:
            st.subheader("Chatbot-for-Ecommerce-using-PALM")
            st.write("Built a chatbot for E-commerce using PALM, Langchain")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/Chatbot-for-Ecommerce-using-PALM)")

    with st.container():
        st.write("##")
        col6, col7  = st.columns((1,2))
        with col6:
            st_lottie(lottie_sentiment, height = 150)
            # st.image(image)
        with col7:
            st.subheader("Sentiment Analysis Using Bert")
            st.write("Built a sentiment analysys for reviews of restaurent using BERT")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/BERT-Sentiment)")

    with st.container():
        st.write("##")
        col8, col9  = st.columns((1,2))
        with col8:
            st_lottie(lottie_newsresearch, height = 150)
            # st.image(image)
        with col9:
            st.subheader("News Research tool using OpenAI LLM")
            st.write("Built a News research tool using OpenAI")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/News-research-tool-using-LLM)")

    with st.container():
        st.write("##")
        col10, col11  = st.columns((1,2))
        with col10:
            st_lottie(lottie_qa, height = 150)
            # st.image(image)
        with col11:
            st.subheader("Conversational-Q-A-Chatbot")
            st.write("Built a Conversational Q-A  Chatbot using OpenAI")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/Conversational-Q-A-Chatbot)")

    with st.container():
        st.write("##")
        col12, col13  = st.columns((1,2))
        with col12:
            st_lottie(lottie_blog, height = 150)
            # st.image(image)
        with col13:
            st.subheader("Blog-Generation-Using-Langchain")
            st.write("Built a Blog generation webpage using Langchain")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/Blog-Generation-Using-Langchain)")

    

    with st.container():
        st.write("##")
        col14, col15  = st.columns((1,2))
        with col14:
            st_lottie(lottie_Auto, height = 150)
            # st.image(image)
        with col15:
            st.subheader("Automobile Price prediction")
            st.write("Predicted prices of automobile usinh different ML algorithms")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/Automobile-Price-Prediction)")
    with st.container():
        
        st.write("##")
        col16, col17  = st.columns((1,2))
        with col16:
            st_lottie(lottie_cancer, height = 150)

        with col17:
            st.subheader("Cancer Prediction")
            st.write("Predicted Cancer using Logistic KNN and Decision-Tree")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/Cancer-prediction-using-Logistic-KNN-and-Decision-Tree)")
    with st.container():
        
        st.write("##")
        col18, col19  = st.columns((1,2))
        with col18:
            st_lottie(lottie_cyber, height = 150)

        with col19:
            st.subheader("Attack Detection Using Autoencoders")
            st.write("Anomoly detection using Autoencoders")
            st.markdown("[Visit Github Repo](https://github.com/prem8667/Anomaly-detection-using-Autoencoders)")

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




