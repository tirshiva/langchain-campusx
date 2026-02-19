"""The ChatPromptTemplate in LangChain is a structured tool designed for creating and managing prompts in multi-turn, conversational interactions with chat-based Large Language Models (LLMs)."""


from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({
    'domain': 'cricket',
    'topic': 'doosra'
})

print(prompt)