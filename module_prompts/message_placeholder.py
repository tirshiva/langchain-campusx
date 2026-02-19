"""
In LangChain, a MessagesPlaceholder is a class used within a ChatPromptTemplate to dynamically insert a list of chat messages at a specific point in the prompt.
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage

# chat template

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history

with open('prompts\chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
chat_template.invoke({
    'chat_history': chat_history, 
    'query': HumanMessage(content='What is the status of my refund?')
})