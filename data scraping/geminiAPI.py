import streamlit as st
def geminiApi(prompt):

    geminiAPI="AIzaSyBq9LmoCRSh9mEeGJcwIepPNshSi7k8bq0"

    from google import genai

    client = genai.Client(api_key=geminiAPI)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return(response.text)

st.header("Aamaey's Own LLM!")
prompt = st.text_input("Enter your prompt")
if st.button("Generate"):
    result = geminiApi(prompt)
    print(result)
    # result = ""
    st.write(result)
