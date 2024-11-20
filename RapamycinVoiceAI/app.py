from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from os import environ
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = environ["OPENAI_API_KEY"]


from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4")

try:
    storage_context = StorageContext.from_defaults(
        persist_dir="./storage/sorge"
    )
    sorge_index = load_index_from_storage(storage_context)

    storage_context = StorageContext.from_defaults(
        persist_dir="./storage/fischer"
    )
    fischer_index = load_index_from_storage(storage_context)

    index_loaded = True
except:
    index_loaded = False

if not index_loaded:
    # load data
    sorge_docs = SimpleDirectoryReader(
        input_files=["./10k/rapa_sorge_2014.pdf"]
    ).load_data()
    fischer_docs = SimpleDirectoryReader(
        input_files=["./10k/rapa_fischer_2015.pdf"]
    ).load_data()

    # build index
    sorge_index = VectorStoreIndex.from_documents(sorge_docs, show_progress=True)
    fischer_index = VectorStoreIndex.from_documents(fischer_docs, show_progress=True)

    # persist index
    sorge_index.storage_context.persist(persist_dir="./storage/sorge")
    fischer_index.storage_context.persist(persist_dir="./storage/fischer")

sorge_engine = sorge_index.as_query_engine(similarity_top_k=3, llm=llm)
fischer_engine = fischer_index.as_query_engine(similarity_top_k=3, llm=llm)

query_engine_tools = [
    QueryEngineTool(
        query_engine=sorge_engine,
        metadata=ToolMetadata(
            name="sorge_10k",
            description=(
                "Provides information about Rapamycin according to Sorge 2014 science paper."
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=fischer_engine,
        metadata=ToolMetadata(
            name="fischer_10k",
            description=(
                "Provides information about Rapamycin according to Fischer 2015 science paper."
            ),
        ),
    ),
]


agent = ReActAgent.from_tools(
    query_engine_tools,
    llm=llm,
    verbose=True,
    max_turns=10,
)

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return "Hello Worlds"

@app.route('/voice', methods=["POST"])
def voice():
    resp = VoiceResponse()

    gather = resp.gather(
        input='speech',
        max_length=30,
        action='/process_q',
        transcribe=True
    )

    gather.say("Hello, welcome to Twilio voice call. ", voice = 'alice')

    return str(resp)

@app.route('/process_q', methods=["POST"])
def process_question():
    resp = VoiceResponse()
    user_question = request.values.get('SpeechResult', '')

    if user_question:
        response = agent.chat(user_question)
        resp.say(response)
    else: resp.say('Sorry, question was unable to be processed')

    return str(resp)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5001)
