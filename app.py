import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title='My webpage', layout= 'wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


# ---- Load ASSETS ---
lottie_coding = load_lottieurl("https://lottie.host/f3d8cb31-b098-45ca-bd6e-3a5594442567/Bew1fwSqxU.json")
lottie_coding_2 = load_lottieurl("https://lottie.host/057da749-488c-490a-bd9c-c12a1b040458/pdws0OnMfS.json")
img_cnn = Image.open("images/image1.png")

# Use local Css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

# --- HEADER Section ----
with st.container():
    st.subheader("Hi, I am Ruzan :wave")
    st.title("A Data Scientist From India")
    st.write("I am passionate about finding ways to use Python, Machine learning , Deeplearning, Tableau, Power BI ,databases like MongoDb & SQL to grow business effectively")

# --- What do I DO --
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How can I contribute ?")
        st.write("##")
        st.write(
            """
            Efficient Automation and Seamless Data Integration:
             Adept in Alteryx, Xceptor, and Python automation, I've achieved 97% automation in margin calls across 20+ projects. 
             Successfully transferred MySQL data to MongoDB and integrated social media data, enhancing workflows and decision-making.

            Innovative AI Solutions and Predictive Models:
             Employing SVM, Random Forest, LSTM, and more, I've crafted advanced models. Published a research paper on predicting phishing attacks. 
             Elevating cybersecurity through ADA Boost, Random Forest, and LSTM.

            Engaging Dashboards and Visual Insights:
             Using Tableau, Power BI, and Streamlit, I've created dynamic dashboards that visualize complex data. 
             Built customer prediction models and collaborated globally with Singapore, Buenos Aires, and more.

            Global Collaboration and Multifaceted Expertise:
             Collaborated across Singapore, Buenos Aires, and more, bringing diverse insights. 
             Seeking roles in Mumbai, Pune, Bangaluru, Canada, and Norway, with extensive skills in data science and analytics.

            """
        )

        with right_column:
            st_lottie(lottie_coding, height=200, key="coding")
            st_lottie(lottie_coding_2, height=200, key="Data Visualization")

# -- Projects --
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cnn)
    # insert image
    with text_column:
        st.subheader("Convolutional Neural Network for Fashion Trends")
        st.write(
            """
            The Virtual assistant can help the retailer like Jabong Flipkart and Amazon detect and forecast fashion trends and target marketing a camping’s.
            Retailer has hired you to build a virtual stylist assistant that looks a Instagram and Facebook images and Classifies the ongoing trends and this story we're going to use the fashionmnist data. It's a data set that contains images of bags shoes and dresses. And we're asking the deep network to classify the images into 10 classes.
            So we wanted to build kind of an app per se or a model. They can look at images and can tell us exactly what category in this image. 
            Is it like a short. Is it a bag. Is it like a hat. And so on.
            That's the whole objective.
            The data again they are divided into 28 by 28 greyscale images and the target class is actually No. 1 out of 10 which is kind of a target label which can be categorized as you can see into either like maybe a shoe maybe like like pants. Basically these are the target classes. 
            We have the t shirts trousers pullovers ankle boots sneakers and so on so forth.
            """
        )

        st.markdown("[Github link] (https://github.com/FinancialCoder5/Convolutional-Neural-Network)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


