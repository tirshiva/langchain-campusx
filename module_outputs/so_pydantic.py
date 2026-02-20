from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing import Literal, Optional

model = ChatOllama(model='llama3.2')

# schema

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "description": "write down all the key themes discussed in the review in a list",
      "items": {
        "type": "string"
      }
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "description": "Return sentiment of the review either negative or positive",
      "enum": ["positive", "negative"]
    },
    "pros": {
      "type": ["array", "null"],
      "description": "write down all the pros inside a list",
      "items": {
        "type": "string"
      }
    },
    "cons": {
      "type": ["array", "null"],
      "description": "Write down all the cons inside a list",
      "items": {
        "type": "string"
      }
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"],
  "additionalProperties": False
}

  

strucrured_model = model.with_structured_output(Review)

result = strucrured_model.invoke("""After using the OrionTech Aether Z9 Ultra as my primary device for over two months, I have mixed but mostly positive impressions. This is clearly a performance-oriented flagship, but it comes with some trade-offs that potential buyers should understand.

The device is powered by the HyperCore X3 chipset paired with 12GB LPDDR5 RAM. Day-to-day performance is excellent. App switching is instant, and I’ve rarely experienced lag. I tested it with heavy multitasking (Chrome with 20+ tabs, YouTube in PiP mode, Slack, and background music), and it handled everything smoothly.

Gaming performance is strong — I played BGMI and Genshin Impact on high settings. Frame rates were stable, but after about 25 minutes, the device gets noticeably warm near the camera module. It’s not alarming, but definitely noticeable.""")

print(result.name)



