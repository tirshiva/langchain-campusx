from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


chat_model = ChatOllama(model='llama3.2')

# 1st prompt -> Detailed report 
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> Summary 

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})

result = chat_model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result1 = chat_model.invoke(prompt2)

print(result1.content)
