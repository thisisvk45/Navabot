import streamlit as st
import requests
import json

# API endpoint and headers
API_ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDwsxg_tXmaRmvRTGoiCvPq4mPHV9PDDTE'
HEADERS = {'Content-Type': 'application/json'}

# Function to generate response from the API
def generate_response(input_text):
    payload = {
        'contents': [
            {
                'parts': [
                    {
                        'text': input_text
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                content = result['candidates'][0]['content']['parts'][0]['text']
                return content
            else:
                return "Error: No valid response from API"
        else:
            return f"Error: API request failed with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to API - {e}"

# Streamlit app UI
def main():
    st.title('AI Chatbot using Streamlit')

    input_counter = 0  # Initialize a counter for generating unique keys

    while True:
        user_input = st.text_input(f'You {input_counter}:', key=f'input_{input_counter}')  # Use unique key

        if st.button(f'Send {input_counter}'):
            if user_input:
                response = generate_response(user_input)
                st.text_area(f'Chatbot {input_counter}:', response, height=200)

        input_counter += 1  # Increment counter for the next iteration

if __name__ == '__main__':
    main()
