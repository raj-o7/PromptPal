import os
from groq import Groq
from logger import CustomLogger
from dotenv import load_dotenv

load_dotenv

class GroqClient:
    # Class to interact with the groq api

    def __init__(self):
        self.api_key=os.getenv('API_KEY') #get the api key from the evironment
        self.client=Groq(api_key=self.api_key)
        self.logger=CustomLogger().get_logger()

    def get_response(self,messages):
        # Send messages to the groq api and return the response
        # Send: List of messages for the sconversation
        # Return: AI response as a string

        try: 
            self.logger.info("Sending message to the Groq API")
            chat_completion=self.client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192"
            )
            response=chat_completion.choices[0].message.content
            self.logger.info("Recieved the response from the Groq API")
            return response
        except Exception as e:
            self.logger.error(f"Error communicating with the Groq API: {e}")
            return "Sorry i couldn't get a response at this time"

