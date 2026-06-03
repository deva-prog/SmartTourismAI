import streamlit as st
import random

def tourism_chatbot():

    st.divider()

    st.header("🤖 Smart Tourism Chatbot")

    user_question = st.text_input("Ask Your Travel Question")

    if user_question:

        question = user_question.lower()

        food_responses = [
            "🍴 Mumbai is amazing for street food lovers!",
            "😋 Amritsar is famous for Punjabi food.",
            "🌮 Jaipur offers royal Rajasthani cuisine."
        ]

        beach_responses = [
            "🏖️ Goa is the best beach destination in India.",
            "🌊 Goa offers nightlife and water sports.",
            "☀️ Beach lovers should definitely visit Goa."
        ]

        adventure_responses = [
            "⛰️ Rishikesh is great for rafting and adventure.",
            "🧗 Manali is perfect for trekking lovers.",
            "🚵 Adventure lovers should explore Uttarakhand."
        ]

        nature_responses = [
            "🌿 Kerala is famous for beautiful greenery.",
            "🏔️ Manali has amazing mountain views.",
            "🍃 Nature lovers will enjoy Darjeeling."
        ]

        if "food" in question:
            st.success(random.choice(food_responses))

        elif "beach" in question:
            st.success(random.choice(beach_responses))

        elif "adventure" in question:
            st.success(random.choice(adventure_responses))

        elif "nature" in question:
            st.success(random.choice(nature_responses))

        else:
            st.info("🤖 That's interesting! I am still learning more travel knowledge.")