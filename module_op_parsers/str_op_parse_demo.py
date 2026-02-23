from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

chain = template1 | chat_model | parser | template2 | chat_model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)

