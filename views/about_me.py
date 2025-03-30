import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# ---  HERO SECTION ----
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/pepe_suit.png", width = 500)
with col2:
    st.title("Pepe", anchor=False)
    st.write(
        "Senior Investment Banker at Goldman Sachs"
    )
    if st.button("Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS -----
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - I was around years before Bitcoin and am the king of crypto
    - Will overtake DOGE soon
    - Best meme of all time
    - I AM THE INTERNET
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Python
    - Apptio
    - Memes
    """
)


