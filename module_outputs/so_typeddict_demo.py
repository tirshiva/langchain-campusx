from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated

model = ChatOllama(model='llama3.2')

# schema

class Review(TypedDict):

    summary : Annotated[str, "A brief summary of the review"]
    sentiment : Annotated[str, "Return sentiment of the review either positive, negative or neutral"]

strucrured_model = model.with_structured_output(Review)

result = strucrured_model.invoke("""After using the OrionTech Aether Z9 Ultra as my primary device for over two months, I have mixed but mostly positive impressions. This is clearly a performance-oriented flagship, but it comes with some trade-offs that potential buyers should understand.

The device is powered by the HyperCore X3 chipset paired with 12GB LPDDR5 RAM. Day-to-day performance is excellent. App switching is instant, and I’ve rarely experienced lag. I tested it with heavy multitasking (Chrome with 20+ tabs, YouTube in PiP mode, Slack, and background music), and it handled everything smoothly.

Gaming performance is strong — I played BGMI and Genshin Impact on high settings. Frame rates were stable, but after about 25 minutes, the device gets noticeably warm near the camera module. It’s not alarming, but definitely noticeable.""")

print(result)



