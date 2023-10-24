# Chatbox - An Online Chat Website

Chatbox is a Django-based online chat website that leverages the OpenAI GPT-turbo-3.5 model to provide interactive conversations. It also connects to a Google Cloud MySQL database for data persistence.
## Live Demo

Experience the live demo of Chatbox at [http://www.jackliaomatsuyama.org:8864/](http://www.jackliaomatsuyama.org:8864/).

## Setup

1. **Configure Google Cloud Database:**
   - Navigate to `chatbox/settings.py`.
   - Set your Google Cloud Database credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'HOST': 'your-gcloud-db-host',
             'PORT': 'your-port',
             'NAME': 'your-db-name',
             'USER': 'your-username',
             'PASSWORD': 'your-password',
         }
     }
     ```

2. **Configure OpenAI API:**
   - Navigate to `chat/views.py`.
   - Set your OpenAI API key and specify the model you want to use:
     ```python
     openai.api_key = 'your-openai-api-key'
     res = openai.ChatCompletion.create(
            model="MODEL_YOU_WANT_TO_USE",
     ```


3. **Run the Server:**
   - Execute the following command to start the Django server:
     ```bash
     python manage.py runserver
     ```

## Usage

1. **Access the Website:**
   - Open your web browser and navigate to `http://127.0.0.1:8000/` to access the chat interface.

2. **Interact with Chatbox:**
   - Type your message in the input box and click "Send" to initiate a conversation.
   - The responses from the GPT-turbo-3.5 model will appear in the chat area.

3. **Search Messages:**
   - Use the search box to enter text and filter the messages displayed in the chat area based on your search query.

4. **Clear Chat:**
   - Click "Clear Chat" to erase the conversation history.

## Features

- Real-time chat interaction with GPT-turbo-3.5.
- Message history persistence using Google Cloud MySQL database.
- Message search functionality to easily find relevant conversations.

## Dependencies

- Django
- OpenAI GPT-turbo-3.5
- Google Cloud MySQL

## Contributing

Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

## License

[MIT License](LICENSE)

