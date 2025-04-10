
import streamlit as st

# PAGE SETUP
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/dashboard.py",
    title="Big Dick Stock Dashboard",
    icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

project_3_page = st.Page(
    page="views/stock_comparison.py",
    title="Stock Performance Comparison",
    icon=":material/bar_chart:",
)
#MATERIAL ICONS WEBSITE https://fonts.google.com/icons

pepe_bird = st.Page(
    page="views/pepebird.py",
    title="PePe Bird",
    icon=":material/sports_esports:",
)

# ------- NAVIGATION SETUP [WITH SECTIONS]--------
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
        "Games": [pepe_bird],
    }
)

# ------- SHARED ON ALL PAGES --------
st.logo("assets/Pepe.png")
st.sidebar.text("Made by Shauny B")



# ------- RUN NAVIGATION ------
pg.run()


# TO RUN ----- Enter in Terminal Below: Streamlit run stonks.py
# TO End ----- in Terminal below: Control + C

