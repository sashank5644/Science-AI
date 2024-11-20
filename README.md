# Welcome to Science AI!

This project was developed during the Open Source for AI Hackathon hosted at Microsoft's headquarters. Within just 6 hours, our team designed and built this innovative voice-enabled AI system, which placed 2nd in the Hackathon.

The Science AI project is a testament to our ability to tackle complex challenges, leverage cutting-edge AI tools, and deliver impactful solutions under tight deadlines.

Feel free to explore the code and learn more about how we built this system!

# Project Overview

The Rapamycin Invoice AI project is an AI-powered voice-enabled application that leverages cutting-edge AI technologies to provide detailed scientific insights about Rapamycin (anti-aging drug) by querying and retrieving relevant information from indexed research papers. By integrating Twilio, OpenAI's GPT-4, LlamaIndex, and ngrok, the project demonstrates the effective combination of AI, telephone, and web technologies to deliver a seamless user experience.

Technology Stack
The project leverages the following technologies:

* Twilio Voice API: Enables real-time voice interactions by transcribing spoken queries and delivering AI-generated responses.
* Flask: Powers the backend, handling RESTful API endpoints for routing voice interactions and processing user queries.
* Python: Implements the AI models and server-side logic for document indexing, querying, and dynamic response generation.
* LlamaIndex: Facilitates the creation and management of vector-based document indexes for efficient information retrieval.
* OpenAI GPT-4: Processes user queries and generates conversational, evidence-based answers.
* ngrok: Provides a secure and publicly accessible URL for the Flask application, enabling integration with Twilio Webhooks.


# Project Functionalities

1. User Interaction: A user calls the system via a Twilio phone number and interacts using voice commands.
2. Ngrok Tunnel: Twilio forwards Webhook requests to the public ngrok URL, which securely connects to the local Flask application.
3. Query Transcription: Twilio transcribes the user's question and sends it to the Flask backend via the ngrok tunnel.
4. AI Query Resolution: The backend uses the ReAct Agent and LlamaIndex to process the question and retrieve answers.
5. Response Delivery: The system vocalizes the response via Twilio, ensuring a conversational experience.
6. Adding ngrok ensures the Flask application is accessible externally during development without deploying to a server, streamlining integration and testing.


# Getting Started

For this project you will need **Python version 3.11.10**

To test this project locally you will need access to an OpenAI API Key, a free Twilio account, and a free Ngrok account.

**OpenAI API Key**

Have your API key ready, or create one [here](https://platform.openai.com/docs/overview)

**Free Twilio Account**

Log into you Twilio account or create one [here](https://www.twilio.com/en-us)

Create a new free phone number

**Free Ngrok Account**

Please hve you Ngrok account authtoken or get one [here](https://ngrok.com/)

Set up your ngrok auth token: ngrok config add-authtoken "Your Token"


It is best to create a virtual environment to manage the required dependencies and framework versions for this project. To initialize and set up a virtual environment, first clone this repository to your local development environment.


      git clone <repository-url>


**Create a Virtual Environment**


      python3 -m venv venv

**Activate the Virtual Environment**

* MacOS/Linux:

    source venv/bin/activate

* Windows:

    venv\Scripts\activate
  

**Install Dependencies**

    pip install -r requirements.txt


**Navigte to Directory**

    cd RapamycinVoiceAI

**Please create an .env file inside the current directory and add the following**

* OPENAI_API_KEY = "Your OpenAI API Key"

**In the terminal run**

    python3 app.py

**Open a new terminal, and run**

    ngrok http 5001

Copy the Forwarding url and navigate to your twilio account. 
Go to you Account Dashboard -> Develop -> # Phone Numbers -> Manage -> Active Numbers

Then under Voice Configurations, where it says "A call comes in". Paste you copied forwarding url in the "URL" section with a /voice at the end of the url

For example if you forwarding url was: http://forwarding add /voice to make it http://forwarding/voice

Then scroll down and click save configuration.

Now you can use your phone to call your twilio free phone number and chat with the voice agent about Rapamycin



      

