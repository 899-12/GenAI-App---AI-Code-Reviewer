import google.generativeai as genai
import streamlit as st

#setting up the API key
f = open("C:/Users/aarsh/gemini_api_key.txt")
key = f.read()
genai.configure(api_key = key)


st.title("AI CODE REVIEWER")
st.subheader('Submit your Python code for review and receive feedback.')

#taking user input
user_prompt = st.text_area("Enter your code...")

#if the button is clicked, generate responses
if st.button("Review") == True:
    model = genai.GenerativeModel(model_name='models/gemini-1.5-flash',
                              system_instruction="""
                              Code Review:
                                1. Bug Report:
                                - Identify all potential bugs, errors, or issues in the code. Be specific and concise.
                                - Highlight any areas for improvement, including logic, syntax, or best practices.

                                2. Fixed Code:
                                - Provide a corrected version of the code that resolves all identified issues.
                                - Ensure the code follows Python's best practices and is optimized for readability and efficiency.

                            If the input is not valid Python code, politely inform the user that you are only designed to review Python code and cannot analyze other languages or inputs.
                                """
                )
    
    #if the prompt is provided
    if user_prompt:
        response = model.generate_content(user_prompt)
            
    #printing the response on the webpage
        st.write(response.text)