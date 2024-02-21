import requests  # Import the requests library to make HTTP requests
import streamlit as st  # Import the Streamlit library
from streamlit_lottie import st_lottie  # Import the st_lottie module from streamlit_lottie package
from PIL import Image  # Import the Image module from the Python Imaging Library (Pillow)

# Set Streamlit page configuration settings
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Function to load Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load local CSS file
local_css("style/style.css")

# ---- LOAD ASSETS ----
# Load Lottie animation from URL
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Load images
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
# Display header section with a container
with st.container():
    # Display subheader and title
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    # Display description
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    # Add link
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
# Display "What I do" section with a container
with st.container():
    st.write("---")
    # Split the page into two columns
    left_column, right_column = st.columns(2)
    with left_column:
        # Display header
        st.header("What I do")
        st.write("##")
        # Display description
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        # Add link
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        # Display Lottie animation
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
# Display "My Projects" section with a container
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    # Split the page into two columns
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # Display image
        st.image(img_lottie_animation)
    with text_column:
        # Display project details
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        # Add link
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")

# Display "My Projects" section with a container
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # Display image
        st.image(img_contact_form)
    with text_column:
        # Display project details
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        # Add link
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
# Display "Get In Touch With Me!" section with a container
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Form for contact
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
        # Display contact form
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        # Empty column
        st.empty()
