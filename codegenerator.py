import os
import logging
import openai

from openai import OpenAI

# Set your OpenAI API key
api_key = ''


client = OpenAI(api_key=api_key)



def generate_code(prompt, content):
    try:
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": content}
            ]
        )
        code = response.choices[0].text.strip()
        logging.info("Code generated successfully")
        return code
    except Exception as e:
        logging.error(f"Error generating code: {e}")
        return "Error generating code"

