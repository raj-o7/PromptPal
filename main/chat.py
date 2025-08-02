from main.api_client import GroqClient

class ChatManager:
    """Class to manage chat interactions."""

    def __init__(self):
        self.client = GroqClient()  # Initialize the Groq client
        self.conversation_history = []  # Store conversation history

    def add_message(self, role, content):
        """Add a message to the conversation history."""
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, user_message):
        """
        Get a response based on user input and conversation history.

        :param user_message: The message input from the user.
        :return: AI response as a string.
        """
        # Add user's message to history
        self.add_message("user", user_message)

        # Prepare the history for the API call
        messages = self.conversation_history

        # Get AI response using the history
        ai_response = self.client.get_response(messages)

        # Add AI's response to the history
        self.add_message("assistant", ai_response)

        return ai_response
