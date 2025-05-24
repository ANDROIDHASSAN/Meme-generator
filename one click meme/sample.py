import streamlit as st
import requests
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

st.set_page_config(page_title="🤡 Ultimate Meme Generator", layout="wide")

st.title("MemeBanao.Ai")
st.header("Aalu dalo to sona niklega")  # Hinglish meme header

USERNAME = os.getenv("IMGFLIP_USERNAME")
PASSWORD = os.getenv("IMGFLIP_PASSWORD")

caption_templates = [
    "When you realize {topic} is just a social experiment.",
    "Nobody: Absolutely nobody: Me after {topic}.",
    "That awkward moment when {topic} happens.",
    "If I had a dollar for every time {topic}...",
    "Keep calm and pretend {topic} is normal.",
    "POV: You and {topic} on a Monday morning.",
    "Why does {topic} always happen to me?",
    "Expectation: {topic}. Reality: Crying in the shower.",
    "How it started: {topic}. How it's going: Chaos.",
    "When you try to explain {topic} to your parents.",
    "Me: I won't talk about {topic} today. Also me: {topic}!",
    "If only {topic} could solve my problems.",
    "{topic}? That's my villain origin story.",
    "Breaking news: {topic} officially out of control.",
    "When {topic} is the plot twist no one asked for.",
    "Therapist: {topic} isn't real. {topic}:",
    "My plans: {topic}. 2025: LOL, no.",
    "When you Google {topic} and regret it instantly.",
    "Trying to avoid {topic} like...",
    "When you finally accept {topic} is your destiny.",
    "Me explaining {topic} to my dog.",
    "When {topic} is the answer to every question.",
    "The face you make when {topic} shows up.",
    "If {topic} was a person, I'd sue.",
    "When life gives you {topic}, make memes.",
    "Plot twist: {topic} was the culprit all along.",
    "When your last brain cell is thinking about {topic}.",
    "Me after surviving another day of {topic}.",
    "When you realize {topic} is trending again.",
    "If {topic} had a theme song, it would be a scream.",
    "When your WiFi is slower than {topic}.",
    "When {topic} is the final boss.",
    "When you pretend {topic} doesn't bother you.",
    "When {topic} is the only thing on your mind.",
    "When you see {topic} in your dreams.",
    "When you thought {topic} was a good idea.",
    "When your friend brings up {topic} at a party.",
    "When {topic} is your entire personality.",
    "When you try to run away from {topic}, but it's faster.",
    "When {topic} is the plot of your life.",
    "When you realize {topic} is forever.",
]

def get_random_caption(topic):
    template = random.choice(caption_templates)
    return template.format(topic=topic)

def generate_meme(template_id, text0, text1):
    params = {
        "template_id": template_id,
        "username": USERNAME,
        "password": PASSWORD,
        "text0": text0,
        "text1": text1
    }
    response = requests.post("https://api.imgflip.com/caption_image", params=params)
    return response.json()

topic = st.text_input("Tu shabd de 💀 me meme deta 👻 ")

if topic:
    try:
        templates = requests.get("https://api.imgflip.com/get_memes").json()["data"]["memes"]
        random_templates = random.sample(templates, 5)

        st.subheader("Ab tu dekh ... ")
        cols = st.columns(5)
        for i, template in enumerate(random_templates):
            text0 = get_random_caption(topic)
            text1 = get_random_caption(topic)
            meme = generate_meme(template["id"], text0, text1)
            if meme["success"]:
                with cols[i]:
                    st.image(meme["data"]["url"], caption=template["name"])
                    st.write("Share this meme:")
                    st.code(meme["data"]["url"])
            else:
                with cols[i]:
                    st.warning(f"Could not generate meme for template: {template['name']}")
        st.info("Refresh or change the topic for a fresh batch of memes every time!")
    except Exception as e:
        st.error("Kuch toh gadbad hai, bhai! 😅\n\n" + str(e))
else:
    st.caption("Kuch bhi likh, mast meme milega! 🚀")

