from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated

model = ChatOllama(model='llama3.2')

# schema

class Review(TypedDict):

    summary : Annotated[str, "A brief summary of the review"]
    sentiment : Annotated[str, "Return sentiment of the review either positive, negative or neutral"]

strucrured_model = model.with_structured_output(Review)

result = strucrured_model.invoke("""After using the OrionTech Aether Z9 Ultra as my primary device for over two months, I have mixed but mostly positive impressions. This is clearly a performance-oriented flagship, but it comes with some trade-offs that potential buyers should understand.

Performance & Multitasking:

The device is powered by the HyperCore X3 chipset paired with 12GB LPDDR5 RAM. Day-to-day performance is excellent. App switching is instant, and I’ve rarely experienced lag. I tested it with heavy multitasking (Chrome with 20+ tabs, YouTube in PiP mode, Slack, and background music), and it handled everything smoothly.

Gaming performance is strong — I played BGMI and Genshin Impact on high settings. Frame rates were stable, but after about 25 minutes, the device gets noticeably warm near the camera module. It’s not alarming, but definitely noticeable.

Display:

The 6.8-inch AMOLED panel is one of the highlights. Colors are vibrant, blacks are deep, and the 120Hz refresh rate makes scrolling fluid. However, auto-brightness calibration feels slightly aggressive indoors.

Camera System:

This is where things get interesting.

Daylight shots are sharp with good dynamic range.

Portrait mode edge detection works well most of the time.

Low-light photography is inconsistent — sometimes excellent with Night Mode, sometimes noisy.

The 3x telephoto lens produces decent results but struggles in artificial lighting.

Video recording at 4K 60fps is stable thanks to strong OIS, but HDR processing occasionally overexposes highlights.

Battery & Charging:

The 5000mAh battery comfortably lasts one day with moderate usage (social media, 1–2 hours video streaming, messaging). On heavy gaming days, it drops to around 20% by evening.

Fast charging (65W) takes about 40–45 minutes for a full charge, which is impressive. However, the device does heat up slightly during fast charging.

Software Experience:

This is my biggest concern. The custom UI has useful features, but there are occasional bugs:

Random app refreshes

Delayed notifications for Gmail twice

Minor animation stutters after recent updates

Security patches seem slightly delayed compared to competitors.

Build & Ergonomics:

Premium glass back, aluminum frame, solid tactile buttons. Slightly heavy at 212g, which may not suit everyone.

Pros:

Excellent performance

Beautiful AMOLED display

Fast charging

Strong daylight photography

Premium build quality

Cons:

Noticeable heating under heavy load

Inconsistent low-light camera

Software bugs and delayed updates

Slightly heavy

Final Verdict:

The OrionTech Aether Z9 Ultra is a performance powerhouse with a stunning display and solid camera hardware. However, software optimization and thermal management need improvement. If you prioritize performance and display over perfect software polish, this is a strong contender in the flagship segment.""")

print(result)



