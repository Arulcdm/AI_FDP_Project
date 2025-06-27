
import streamlit as st

st.set_page_config(page_title="My Personal Webpage", layout="wide")

# --- Sidebar form ---
with st.sidebar.form("profile_form"):
    st.title("👤 Personal Details")
    name = st.text_input("Full Name", "Dr. R. Arulraj")
    tagline = st.text_input("Tagline / Role", "AI Researcher | Educator | Developer")
    bio = st.text_area("Short Bio", "Passionate about developing AI-powered solutions for real-world problems.")
    email = st.text_input("Email", "arulrajkrce@gmail.com")
    phone = st.text_input("Phone", "+91-9894174820")
    linkedin = st.text_input("LinkedIn URL", "https://linkedin.com/in/arulraj")
    github = st.text_input("GitHub URL", "https://github.com/arulraj")
    submit = st.form_submit_button("Update Profile")

# --- Display profile ---
if submit:
    st.markdown(f"# {name}")
    st.markdown(f"### *{tagline}*")
    st.write(bio)

    st.markdown("📫 **Contact:**")
    st.markdown(f"- 📧 Email: {email}")
    st.markdown(f"- 📱 Phone: {phone}")
    st.markdown(f"- 🔗 [LinkedIn]({linkedin}) | [GitHub]({github})")

    st.divider()

    st.markdown("## 🛠️ Skills")
    skills = st.text_area("Enter skills separated by commas (in sidebar)", "Python, Machine Learning, Streamlit, Deep Learning")
    st.markdown(", ".join([f"`{s.strip()}`" for s in skills.split(",")]))

    st.markdown("## 📁 Projects")
    st.info("Add project details in the sidebar ➡️ (currently static)")
    st.markdown("""
    - **Book Recommender System**  
      A Streamlit app using LLMs and user preferences to suggest books. [GitHub](https://github.com/example/book-recommender)

    - **IoT Crop Protection System**  
      A smart animal detection system using ML and sensors. [Paper](https://example.com)
    """)

    st.markdown("## 🎓 Education")
    st.markdown("""
    - **Ph.D. in Power Systems**, Annamalai University, 2019  
    - **M.Tech in Power System Engineering**, Annamalai University, 2013
    """)

    st.markdown("## 📜 Certifications")
    st.markdown("""
    - Generative AI – FDP – 2025  
    - Electric Vehicles & Smart Grid – 2025
    """)

    st.success("✔️ Profile updated successfully!")
else:
    st.markdown("👈 Fill in your personal details in the **sidebar form** to create your profile page!")
