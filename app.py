import streamlit as st
import time

# Set up the romantic, warm birthday page config
st.set_page_config(page_title="Happy Birthday My Love", page_icon="💝", layout="centered")

# Custom Styling for the Golden/Warm Aesthetic
st.markdown("""
    <style>
    .main { background-color: #FFFDF9; }
    h1, h2, h3 { color: #D4AF37; text-align: center; font-family: 'Georgia', serif; }
    .gold-text { color: #C5A059; font-weight: bold; text-align: center; }
    .stButton>button { background-color: #D4AF37; color: white; border-radius: 20px; border: none; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #AA7C11; color: white; }
    .box { border: 1px solid #E6D7B8; padding: 20px; border-radius: 10px; background-color: #FFFDF3; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>✨ Happy Birthday My Love ✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='gold-text'><i>Every love story is beautiful, but ours is my favorite.</i></p>", unsafe_allow_html=True)
st.divider()

# Track the steps using Streamlit's session memory
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- STEP 1: ENTER WEDDING DATE ---
if st.session_state.step == 1:
    st.markdown("### 🔒 1. Enter Our Wedding Date")
    with st.container():
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        
        wedding_date = st.date_input("When did we promise forever?", value=None, key="wedding_key")
        submit_btn = st.button("Unlock 💛")
        
        if submit_btn and wedding_date:
            # Your wedding date successfully updated here!
            if str(wedding_date) == "2023-12-08": 
                st.success("Correct! The envelope is unlocking... 🎉")
                time.sleep(1) 
                st.session_state.step = 2
                st.rerun()
            else:
                st.error("Oops! Hmm... that's not quite right. Try our special day.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- STEP 2 & 3: OPEN THE ENVELOPE / A LETTER FOR YOU ---
if st.session_state.step >= 2:
    st.markdown("### ✉️ 2 & 3. A Letter For You")
    with st.expander("💌 Open the Envelope", expanded=True):
        st.markdown("""
        <div class='box' style='font-family: "Georgia", serif; font-size: 16px; line-height: 1.6;'>
        <strong>My love,</strong><br><br>
        Some feelings are too special to put into words, but I tried...<br>
        This letter is a small reminder of how much you mean to me.<br><br>
        Forever and always,<br>
        Yours ❤️
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.step == 2:
            if st.button("Continue to Memories ✨"):
                st.session_state.step = 3
                st.rerun()

# --- STEP 4: OUR MEMORIES ---
if st.session_state.step >= 3:
    st.divider()
    st.markdown("### 📸 4. Our Memories")
    
    images = [
        {"url": "https://picsum.photos/600/400?random=1", "caption": "One of my favorite memories"},
        {"url": "https://picsum.photos/600/400?random=2", "caption": "Another beautiful day together"},
        {"url": "https://picsum.photos/600/400?random=3", "caption": "Laughing with you is my favorite thing"}
    ]
    
    if 'img_idx' not in st.session_state:
        st.session_state.img_idx = 0
        
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if st.button("◀", key="prev"):
            st.session_state.img_idx = (st.session_state.img_idx - 1) % len(images)
    with col2:
        st.image(images[st.session_state.img_idx]["url"], caption=images[st.session_state.img_idx]["caption"])
    with col3:
        if st.button("▶", key="next"):
            st.session_state.img_idx = (st.session_state.img_idx + 1) % len(images)

    if st.session_state.step == 3:
        if st.button("See Reasons I Love You 👇"):
            st.session_state.step = 4
            st.rerun()

# --- STEP 5: 5 REASONS I LOVE YOU ---
if st.session_state.step >= 4:
    st.divider()
    st.markdown("### 💖 5. Reasons I Love You")
    reasons = [
        "💝 You always got my back.",
        "🧸 You always keep your inner child alive.",
        "🏖️ You also now love beaches.",
        "🌟 You care for me no matter which phase we are in.",
        "🧘 You handle every situation very calmly."
    ]
    
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    for reason in reasons:
        st.markdown(f"<div style='padding: 8px 0; font-size:16px; font-weight:500;'>{reason}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.session_state.step == 4:
        if st.button("Time to Celebrate! 🎉"):
            st.session_state.step = 5
            st.rerun()

# --- STEP 6 & 7: SPECIAL SURPRISE & BLOW CANDLES ---
if st.session_state.step >= 5:
    st.divider()
    st.markdown("### 🎁 6 & 7. Birthday Celebration")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='box' style='text-align:center; height:100%;'><strong>A SPECIAL SURPRISE</strong><br><br>The greatest gift I could ever have is you.</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='box' style='text-align:center;'><strong>Blow the candles and make a wish!</strong><br><br>🎂🎂🎂</div>", unsafe_allow_html=True)
        if st.button("Blow out the candles! 💨"):
            st.balloons()
            st.session_state.step = 6
            st.rerun()

# --- STEP 8: JUST FOR YOU ---
if st.session_state.step >= 6:
    st.divider()
    st.markdown("<h2>🎶 Happy Birthday to the love of my life 🎶</h2>", unsafe_allow_html=True)
    st.markdown("<p class='gold-text' style='font-size: 18px;'>Thank you for every smile, every adventure, and every moment. I love you. Always. Forever. 💛</p>", unsafe_allow_html=True)
