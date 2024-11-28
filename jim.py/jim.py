import streamlit as st
import datetime

st.set_page_config(page_title="Jimryx's Biography", layout="wide")

# Initialize session state if not already initialized
if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False
if 'name' not in st.session_state:
    st.session_state.name = "Jimry E. Cajefe"
if 'about_me' not in st.session_state:
    st.session_state.about_me = ("Hi I'm Jimryx who loves playing online games and finds joy in the simple things, like cooking and keeping things tidy. "
                                  "When I'm not in the kitchen whipping up something delicious like my favorite, chicken curry, you might find me watching anime or spending time in our sari-sari store.")
if 'mybirthday' not in st.session_state:
    st.session_state.mybirthday = datetime.date(2006, 7, 18)  # Default birthdate (can be updated)

def toggle_button():
    st.session_state.toggle_state = not st.session_state.toggle_state

# App Header with Image on Top Right
header = st.columns([3, 1])
with header[0]:
    st.markdown(
        """
        <div style="text-align: left; font-size: 40px; font-weight: bold;">
            Jimryx's Biography
        </div>
        """, unsafe_allow_html=True,
    )
with header[1]:
    st.image(
        "https://scontent.fcgy2-2.fna.fbcdn.net/v/t39.30808-6/468482331_1624844638453560_5679958443007815294_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeFvUpxAYFihycI0Hz_KR0a7-zAgtKplgBj7MCC0qmWAGMj6PPon-WAAeCXZwMfJy5jM2s6uq-xnVFGQ5DZDcyA3&_nc_ohc=IWreYOxo0-AQ7kNvgEcVZde&_nc_zt=23&_nc_ht=scontent.fcgy2-2.fna&_nc_gid=AiqAJsuzwOFMqCqo7PyysrC&oh=00_AYD0fqy4xLzRuq5CN9EpqCHXkoTLMEmt27Qeukp-Ox15KA&oe=674AE75C",
        width=120,
        caption="Jimryx Cajefe"
    )

# Main Content in Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Personal Info", "Hobbies & Achievements", "Social Media", "Education & Family"])

with tab1:
    st.subheader("Personal Information")
    st.text_input("Full Name", st.session_state.name, key="name")
    st.date_input("Date of Birth", st.session_state.mybirthday, key="mybirthday")
    st.write(f"Age: {(datetime.date.today() - st.session_state.mybirthday).days // 365} years old")
    st.text_input("Place of Birth", st.session_state.get("birthplace", "Sta.Cruz Manila"), key="birthplace")
    st.text_input("Current Address", st.session_state.get("current_address", "Bad-as, Placer, Surigao del Norte"), key="current_address")
    st.radio("Gender", ["Male", "Female"], index=0 if st.session_state.get("gender", "Male") == "Male" else 1, key="gender")
    st.text_area("About Me", st.session_state.about_me, key="about_me", height=150)

with tab2:
    st.subheader("Hobbies & Achievements")
    st.text_area("Hobbies", st.session_state.get("hobbies", "- I Play online games\n- Cooking"), key="hobbies", height=100)
    if st.button("Toggle Achievements"):
        toggle_button()
    if st.session_state.toggle_state:
        st.text_area("Achievements", "- With Honor", height=100)
        st.text_area("Game Achievements",
                     "- Reach Mythical Immortal in Mobile Legends\n"
                     "- Champion in MSL tournament\n"
                     "- Obtain Blade of Kibuo\n"
                     "- Top 48 Surigao del Norte using Brody\n"
                     "- Top 8 Surigao del Norte Chou",
                     height=150)

with tab3:
    st.subheader("Social Media")
    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://www.facebook.com/jimryx.espanto" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" width="40" height="40" />
            
        </div>
        """, unsafe_allow_html=True,
    )

with tab4:
    st.subheader("Education & Family")
    st.text_input("High School", st.session_state.get("high_school", "Amando A. Fabio Memorial National Highschool"), key="high_school")
    st.text_input("Senior High School", st.session_state.get("senior_high_school", "Amando A. Fabio Memorial National Highschool"), key="senior_high_school")
    st.text_input("College", st.session_state.get("college", "Surigao del Norte State University"), key="college")
    st.text_input("Mother's Name", st.session_state.get("mother_name", "Emmylou E. Cajefe"), key="mother_name")
    st.date_input("Mother's Birthday", st.session_state.get("mother_bday", datetime.date(1972, 9, 8)), key="mother_bday")
    st.text_input("Father's Name", st.session_state.get("father_name", "Ermie P. Cajefe"), key="father_name")
    st.date_input("Father's Birthday", st.session_state.get("father_bday", datetime.date(1969, 8, 13)), key="father_bday")
