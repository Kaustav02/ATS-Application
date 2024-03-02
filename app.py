# from dotenv import load_dotenv
# import base64
# load_dotenv()

# import streamlit as st
# import io

# import os
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key = os.getenv("API_KEY"))


# def get_gemini_response(input,pdf_content,prompt):
#     model = genai.GenerativeModel('geminii-pro-vision')
#     res=model.generate_content([input,pdf_content[0],prompt])
#     return res.text

# def input_pdf_set(upload_file):
#     if upload_file is not None:
#         #converting pdf to image
    
#         images = pdf2image.convert_from_bytes(upload_file.read())
#         first_page = images[0]
    
#         img_byt_array = io.BytesIO()
#         first_page.save(img_byt_array,format='JPEG')
#         img_byt_array = img_byt_array.getvalue()
    
#         pdf_parts=[
#         {
#             "mime_type":"image/jpeg",
#             "data":base64.b64encode(img_byt_array).decode(),
#         }
#     ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file found")

# st.set_page_config(page_title="ATS")
# st.header("Resume score")

# input_text = st.text_area("Job description: ",key="input")
# uploaded_file = st.file_uploader("upload your resume in pdf",typr=["pdf"])

# if uploaded_file is not None:
#     st.write("file uploaded successfully")
    

# submit_1= st.button("About the resume")
# submit_2= st.button("Skills to be improved")  
# submit_3= st.button("Percent match")

# input_prompt1 = """

# you are an expert and experienced technical human resource manager in the field of Data Science
# , Full stack web development, Machine Learning , Data Anlyst and Devops , your task is to review
# the provided resume against the job description.
# please share your professional evaluation on whether the candidate's profile aligns with the job description.
# Highlight the strengths and weaknesses of the applicant for the specific job role.

# """

# input_prompt2 = """

# you are an expert and experienced technical human resource manager 
# in the field of Data Science
# , Full stack web development, Machine Learning , Data Anlyst and Devops, your task is to scrutinize the resume in against the job description provided
# please share your professional evaluation on whether the candidate's profile aligns with the job description.
# Addtionally offer on enhancing the candidate's skills and what skills need to be improved to fit for that role.

# """

# input_prompt3 = """

# you are an expert ATS system scanner with a deep understanding of ata Science
# , Full stack web development, Machine Learning , Data Anlyst and Devops
# evaluate the resume against the provided job description .
# Give me the percentage match. First the output should come as percentage and the keywords missing
# and suggesion for improvement of the resume.

# """

# if submit_1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_set(uploaded_file)
#         res = get_gemini_response(input_text,pdf_content,input_prompt1)
#         st.subheader("The response is ")
#         st.write(res)
#     else:
#         st.write("Please uploade a file")
# elif submit_2:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_set(uploaded_file)
#         res = get_gemini_response(input_text,pdf_content,input_prompt2)
#         st.subheader("The response is ")
#         st.write(res)
#     else:
#         st.write("Please uploade a file")
# elif submit_3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_set(uploaded_file)
#         res = get_gemini_response(input_text,pdf_content,input_prompt3)
#         st.subheader("The response is ")
#         st.write(res)
#     else:
#         st.write("Please uploade a file")
        

    
from dotenv import load_dotenv
import base64
load_dotenv()

import streamlit as st
import io

import os
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key = os.getenv("API_KEY"))


def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    res = model.generate_content([input, pdf_content[0], prompt])
    return res.text

def input_pdf_set(upload_file):
    if upload_file is not None:
        # Converting pdf to image
        images = pdf2image.convert_from_bytes(upload_file.read())
        first_page = images[0]
    
        img_byt_array = io.BytesIO()
        first_page.save(img_byt_array, format='JPEG')
        img_byt_array = img_byt_array.getvalue()
    
        pdf_parts = [{
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byt_array).decode(),
        }]
        return pdf_parts
    else:
        raise FileNotFoundError("No file found")

st.set_page_config(page_title="ATS")
st.header("Resume score")

input_text = st.text_area("Job description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume in pdf", type=["pdf"])

if uploaded_file is not None:
    st.write("File uploaded successfully")
    

submit_1 = st.button("About the resume")
submit_2 = st.button("Skills to be improved")  
submit_3 = st.button("Percent match")

input_prompt1 = """
You are an expert and experienced technical human resource manager in the field of Data Science,
Full stack web development, Machine Learning, Data Analyst, and DevOps. Your task is to review
the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the job description.
Highlight the strengths and weaknesses of the applicant for the specific job role.
"""

input_prompt2 = """
You are an expert and experienced technical human resource manager 
in the field of Data Science, Full stack web development, Machine Learning, Data Analyst, and DevOps.
Your task is to scrutinize the resume against the provided job description.
Please share your professional evaluation on whether the candidate's profile aligns with the job description.
Additionally, offer on enhancing the candidate's skills and what skills need to be improved to fit for that role.
"""

input_prompt3 = """
You are an expert ATS system scanner with a deep understanding of Data Science,
Full stack web development, Machine Learning, Data Analyst, and DevOps.
Evaluate the resume against the provided job description.
Give me the percentage match. First, the output should come as a percentage and the keywords missing
and suggestion for improvement of the resume.
"""

if submit_1:
    if uploaded_file is not None:
        pdf_content = input_pdf_set(uploaded_file)
        res = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is ")
        st.write(res)
    else:
        st.write("Please upload a file")
elif submit_2:
    if uploaded_file is not None:
        pdf_content = input_pdf_set(uploaded_file)
        res = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The response is ")
        st.write(res)
    else:
        st.write("Please upload a file")
elif submit_3:
    if uploaded_file is not None:
        pdf_content = input_pdf_set(uploaded_file)
        res = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is ")
        st.write(res)
    else:
        st.write("Please upload a file")


