import os

from dotenv import load_dotenv
from ollama import Client

from AI.context_func import get_data_retrieval_context, get_data_retrieval_question_context, get_system_context
from services.mysql.MySQL_Connector import Mysql_connector

load_dotenv()

ai_url = os.getenv("AI_URL")
client = Client(host=ai_url)

question = "How much does the client of domicilio Neuquen 1234 consume until now"

stream = client.chat(model=os.getenv("AI_MODEL"), messages=[
    {"role": "system", "content": get_data_retrieval_context()},
    {"role": "user", "content": get_data_retrieval_question_context(question)}
], stream=True)

full_answer = ''
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
    full_answer = ''.join([full_answer, chunk['message']['content']])

mysql_conn = Mysql_connector()
result = mysql_conn.execute_query(query=full_answer)

for x in result:
    print(x)

stream = client.chat(model=os.getenv("AI_MODEL"), messages=[
    {"role": "system", "content": get_system_context(result)},
    {"role": "user", "content": get_data_retrieval_question_context(question)}
], stream=True)

full_answer = ''
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
    full_answer = ''.join([full_answer, chunk['message']['content']])