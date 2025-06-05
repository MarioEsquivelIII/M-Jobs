import streamlit as st
import requests
from PIL import Image 

APP_ID = "a227e3af"
API_KEY = "97a32e9fc9cea6da99a8997dd56f1856"
st.set_page_config(page_title="M-Jobs", page_icon="Images/m-letter-icon.png")
img = Image.open("Images/m-letter-icon.png")
st.image(img,width=100) #NEW st.image
st.title('Mjobs - Job Searcher')
img1 = Image.open("Images/job-search.jpg")
st.sidebar.image(img1,width=200)
st.sidebar.header('Search for Jobs')

job_title = st.sidebar.text_input('Job Title', 'Software Engineer') #NEW st.text_input
location = st.sidebar.text_input('Location', 'New York')

base_URL = "http://api.adzuna.com/v1/api/jobs/us/search/1?app_id={}&app_key={}&results_per_page=10&what={}&where={}&content-type=application/json"

def get_jobs(title, location):
    response = requests.get(base_URL.format(APP_ID, API_KEY, title, location))
    return response.json()['results']
if st.sidebar.button('Search'): #NEW st.button
    st.subheader(f"Jobs for {job_title} in {location}:")
    jobs = get_jobs(job_title, location)
    if jobs:
        for job in jobs:
            st.write(f"**{job['title']}** at {job['company']['display_name']}")
            st.write(f"**Location:** {job['location']['display_name']}")
            st.write(f"**Description:** {job['description'][:150]}...")
            st.markdown("---")
    else:
        st.write("No jobs found. Try different keywords or location.")







