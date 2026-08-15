from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="HTP Document Viewer", 
    page_icon="📖", 
    layout="wide"
)

# Determine absolute path to the directory containing app.py
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "page_images"

# -----------------------------------------------------------------------------
# AUTHENTICATION MODULE
# -----------------------------------------------------------------------------
def check_password():
    def password_entered():
        if st.session_state["password_input"] == st.secrets["auth"]["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password_input"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Enter Access Password:", type="password", on_change=password_entered, key="password_input")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Enter Access Password:", type="password", on_change=password_entered, key="password_input")
        st.error("🔒 Incorrect password.")
        return False
    return True

if not check_password():
    st.stop()

# -----------------------------------------------------------------------------
# LEFT SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.title("🤝 HTP PORTAL")
st.sidebar.markdown("---")

# Navigation Mapping with Bold Text & Emojis
page_map = {
    "📌 **UNDERSTANDING HONORING THE PARTNERSHIP**": 1,
    "📋 **HTP REQUIREMENTS**": 2,
    "✅ **PHASE A CHECKLIST**": 3,
    "💡 **COMMON CHALLENGES AND SOLUTIONS**": 4,
    "⚡ **PHASE B CHECKLIST**": 5,
    "🎯 **PHASE B - HONORING THE PARTNERSHIP**": 6,
    "👥 **DEVELOPING YOUR LIST**": 7,
    "🚀 **A & B LIST TO 3 LEG TEAM**": 8
}

selected_label = st.sidebar.radio(
    "**SELECT A SECTION TO VIEW:**",
    list(page_map.keys())
)

# -----------------------------------------------------------------------------
# RIGHT SIDE DISPLAY AREA
# -----------------------------------------------------------------------------
page_num = page_map[selected_label]
image_path = IMAGE_DIR / f"page_{page_num}.jpg"

if image_path.exists():
    st.image(str(image_path), use_column_width=True)
else:
    st.warning(f"Image for Page {page_num} not found at expected path:\n`{image_path}`")