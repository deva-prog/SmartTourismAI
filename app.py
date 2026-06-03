import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from chatbot import tourism_chatbot

# PAGE CONFIG
st.set_page_config(
    page_title="SmartTourismAI",
    page_icon="🌍",
    layout="wide"
)

# SIDEBAR
st.sidebar.header("🌟 Smart Tourism Menu")

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #00BFFF;
}

.stButton>button {
    background-color: #00BFFF;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

.stTextInput>div>div>input {
    border-radius: 10px;
}

.stSelectbox>div>div {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    """
    <h1 style='text-align: center; color: #00BFFF;'>
    🌍 SmartTourismAI
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>AI Powered Travel Planner ✈️</h3>",
    unsafe_allow_html=True
)

# HERO IMAGE
st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    use_container_width=True
)

st.success("✨ Discover India's Best Tourist Destinations with AI")

st.write("Plan your perfect trip with AI ✈️")

st.divider()

# INPUT SECTION
col1, col2 = st.columns(2)

with col1:

    city = st.text_input("📍 Enter Destination")

    budget = st.selectbox(
        "💰 Select Budget",
        ["Low", "Medium", "High"]
    )

with col2:

    days = st.slider("📅 Trip Days", 1, 15, 3)

    interests = st.multiselect(
        "🎯 Interests",
        ["Adventure", "Food", "Historical", "Nature", "Shopping"]
    )

# TRIP PLAN
if st.button("Generate AI Trip Plan"):

    st.success(f"Trip Plan Generated for {city}")

    st.subheader("🗺️ Your Travel Plan")

    st.write(f"📍 Destination: {city}")
    st.write(f"💰 Budget: {budget}")
    st.write(f"📅 Days: {days}")
    st.write(f"🎯 Interests: {', '.join(interests)}")

    # AI ITINERARY
    st.subheader("🗺️ Your AI Travel Itinerary")

for day in range(1, days + 1):

    if day == 1:
        activity = f"Explore famous places in {city}"

    elif day == 2:
        activity = "Enjoy local food and culture"

    elif day == 3:
        activity = "Shopping + photography + relaxation"

    else:
        activity = "Discover hidden tourist attractions"

    st.info(f"Day {day}: {activity}")

# LOAD DATA
data = pd.read_csv("places.csv")

# DATASET
st.subheader("📍 Tourist Places Dataset")

st.dataframe(data)

# RECOMMENDATION SYSTEM
st.divider()

st.header("🤖 Travel Recommendation System")

category = st.selectbox(
    "Select Category",
    data["Category"].unique()
)

filtered_data = data[data["Category"] == category]

st.subheader(f"Best {category} Places")

st.dataframe(filtered_data)

# CULTURAL CARDS
st.divider()

st.header("🏛️ Cultural Information Cards")

for index, row in data.iterrows():

    st.subheader(f"📍 {row['Place']}")

    st.write(f"🌎 State: {row['State']}")
    st.write(f"🎯 Category: {row['Category']}")
    st.write(f"💰 Budget: {row['Budget']}")
    st.write(f"⭐ Rating: {row['Rating']}")
    st.write(f"🕒 Timing: {row['Timing']}")
    st.write(f"📖 Description: {row['Description']}")

    st.divider()

# DASHBOARD
st.divider()

st.header("📊 Tourism Dashboard")

graph_option = st.selectbox(
    "Choose Graph Type",
    ["Category Distribution", "Ratings Graph"],
    key="graph_select"
)

# CATEGORY GRAPH
if graph_option == "Category Distribution":

    category_count = data["Category"].value_counts()

    st.bar_chart(category_count)

# RATINGS GRAPH
elif graph_option == "Ratings Graph":

    st.line_chart(data["Rating"])

# CHATBOT
tourism_chatbot()