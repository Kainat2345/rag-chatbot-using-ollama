import wikipedia
import os

os.makedirs("data", exist_ok=True)

topics = [
    "Cricket",
    "History of cricket",
    "Cricket World Cup",
    "ICC Cricket World Cup",
    "Test cricket",
    "One Day International",
    "Twenty20",
    "Babar Azam",
    "Virat Kohli",
    "Sachin Tendulkar"
]

for topic in topics:
    try:
        text = wikipedia.page(topic).content

        filename = topic.replace(" ", "_") + ".txt"

        with open(
            f"data/{filename}",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(text)

        print(f"Saved: {filename}")

    except Exception as e:
        print(topic, e)

print("Done")