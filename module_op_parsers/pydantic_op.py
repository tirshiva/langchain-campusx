from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatOllama(model='llama3.2')

class Person(BaseModel):

    name : str = Field(description='Name of the person')
    age : int = Field(gt=18, description='age of the person')
    city : str = Field(description='city of the person')


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generarte the name, age and city of a fictional {place} person \n {format_ins}',
    input_variables=['place'],
    partial_variables={'format_ins': parser.get_format_instructions}
)

prompt = template.invoke({'place':'indian'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)