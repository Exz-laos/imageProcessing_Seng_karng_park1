import streamlit as st
from gtts import gTTS
import io
import base64
import random
import re
from data import flashcard_data, thai_translations, english_translations

# --- Configuration for English UI ---
# Status mapping
STATUS_MAP_JA_TO_EN = {
    "未確認": "Unchecked",
    "理解済み": "✅Understood",
    "復習が必要": "Needs Review"
}
# Initial status must be in Japanese, then mapped for display
INITIAL_STATUS_JA = "未確認" 
STATUS_UNDERSTOOD_JA = "理解済み"
STATUS_NEEDS_REVIEW_JA = "復習が必要"

# --- Functions ---

@st.cache_data
def generate_audio(text):
    """Generates audio and returns a Base64 encoded Data URI."""
    audio_bytes = io.BytesIO()
    try:
        # NOTE: Keeping lang='ja' to pronounce the Japanese terms/answers
        tts = gTTS(text=text, lang='ja', slow=False) 
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        b64 = base64.b64encode(audio_bytes.read()).decode('utf-8')
        audio_uri = f"data:audio/mp3;base64,{b64}"
        return audio_uri
    except Exception as e:
        print(f"Audio generation error: {e}")
        return None

def render_content_with_latex(content):
    """Renders text, splitting it to use st.latex for math formulas."""
    # Regex to find text enclosed by $...$ or $$...$$
    # It splits the string into text parts and LaTeX parts (keeping the delimiters)
    # The pure Japanese term keys don't contain $ so this mainly affects the answers.
    parts = re.split(r'(\$.+?\$|\$\$.+?\$\$)', content)

    for part in parts:
        if part.startswith('$'):
            # This is a LaTeX formula part (starts with $ or $$)
            latex_code = part.strip('$')
            if latex_code:
                # Use st.latex for correct rendering
                st.latex(latex_code)
        elif part:
            # This is a regular text part
            # Use st.markdown with the custom class for bigger font
            st.markdown(f'<div class="flashcard-text">{part}</div>', unsafe_allow_html=True)


def initialize_session_state():
    """Initializes the session state, incorporating master/active deck indices."""
    all_keys = list(flashcard_data.keys())
    
    if 'card_keys_master' not in st.session_state:
        # Master list of keys, based on the initial full deck or applied range
        st.session_state.card_keys_master = all_keys
    
    if 'card_keys_active' not in st.session_state:
        # Active list of keys currently being viewed
        st.session_state.card_keys_active = st.session_state.card_keys_master
    
    if 'total_cards' not in st.session_state:
        st.session_state.total_cards = len(st.session_state.card_keys_active)
    
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    
    if 'is_flipped' not in st.session_state:
        st.session_state.is_flipped = False
    
    if 'card_status' not in st.session_state:
        # Status is tracked by the original Japanese term key
        st.session_state.card_status = {key: INITIAL_STATUS_JA for key in all_keys}
    
    if 'shuffle_on' not in st.session_state:
        st.session_state.shuffle_on = False
    
    if 'audio_to_play' not in st.session_state:
        st.session_state.audio_to_play = None
    if 'show_thai_translation' not in st.session_state:
        st.session_state.show_thai_translation = None
    if 'show_english_translation' not in st.session_state:
        st.session_state.show_english_translation = None


def apply_range(start_num, end_num):
    """Applies the selected range of cards and sets it as the master list."""
    start_idx = start_num - 1
    end_idx = end_num
    
    all_keys = list(flashcard_data.keys())
    
    if 0 <= start_idx < end_idx <= len(all_keys):
        master_list = all_keys[start_idx:end_idx]
        
        if st.session_state.shuffle_on:
            random.shuffle(master_list)
        
        st.session_state.card_keys_master = master_list
        st.session_state.card_keys_active = master_list # The active deck is the new master deck
        
        st.session_state.total_cards = len(st.session_state.card_keys_active)
        st.session_state.current_index = 0
        st.session_state.is_flipped = False
    else:
        st.sidebar.error("Invalid range selected.")


def filter_deck_for_review():
    """Filters the active deck to only show unmastered cards from the master list."""
    # Filter based on the master list to respect the user's initial range
    review_keys = [
        key for key in st.session_state.card_keys_master 
        if st.session_state.card_status.get(key) != STATUS_UNDERSTOOD_JA
    ]

    if not review_keys:
        st.sidebar.success("Great job! No cards left to review in this range. 🎉")
        return

    st.session_state.card_keys_active = review_keys
    st.session_state.total_cards = len(review_keys)
    st.session_state.current_index = 0
    st.session_state.is_flipped = False

def reset_to_master_deck():
    """Resets the active deck to the master list selected by the user."""
    st.session_state.card_keys_active = st.session_state.card_keys_master
    st.session_state.total_cards = len(st.session_state.card_keys_master)
    st.session_state.current_index = 0
    st.session_state.is_flipped = False

def next_card():
    if st.session_state.current_index < st.session_state.total_cards - 1:
        st.session_state.current_index += 1
        st.session_state.is_flipped = False


def prev_card():
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        st.session_state.is_flipped = False


def mark_status(status_ja):
    """Marks the status using the Japanese key."""
    # Get the key from the active deck
    current_key = st.session_state.card_keys_active[st.session_state.current_index]
    st.session_state.card_status[current_key] = status_ja


# --- UI Layout ---
st.set_page_config(page_title="Digital image processing Flashcards", layout="wide", page_icon="🗂️")

# --- Custom Dark Theme & Font Size CSS ---
st.markdown("""
    <style>
        /* General Theme */
        body, .stApp { background-color: #121212; color: #E0E0E0; }
        .stMarkdown, .stText, .stSubheader, .stHeader, .stTitle { color: #E0E0E0 !important; }
        div.stButton > button { background-color: #2E2E2E; color: #E0E0E0; border: 1px solid #444; border-radius: 10px; padding: 0.6em 1.2em; font-size: 16px; font-weight: 500; }
        div.stButton > button:hover { background-color: #444; border: 1px solid #666; color: #FFFFFF; }
        section[data-testid="stSidebar"] { background-color: #1A1A1A; border-right: 1px solid #333; }

        /* 🌟 Custom Font Size for Regular Text (150% of base font) 🌟 */
        .flashcard-text {
            font-size: 1.5em; /* Increased by 50% */
            line-height: 1.6; /* Maintain line spacing for readability */
        }
    </style>
""", unsafe_allow_html=True)

initialize_session_state()

# --- Sidebar Controls (English Translation) ---
with st.sidebar:
    st.header("⚙️ Settings")
    st.subheader("Card Range")
    total_cards_overall = len(flashcard_data)
    start_num = st.number_input("Start Card #", min_value=1, max_value=total_cards_overall, value=1, step=1)
    end_num = st.number_input("End Card #", min_value=1, max_value=total_cards_overall, value=min(10, total_cards_overall), step=1)

    st.toggle("Shuffle", key="shuffle_on", help="Shuffle the selected range.")
    if st.button("Apply Range", use_container_width=True):
        apply_range(start_num, end_num)
        st.rerun()

    st.header("📊 Progress")
    
    # Progress is calculated across the entire master deck of the current term keys
    remembered_count = list(st.session_state.card_status.values()).count(STATUS_UNDERSTOOD_JA)
    repeat_count = list(st.session_state.card_status.values()).count(STATUS_NEEDS_REVIEW_JA)
    
    st.metric(label="✅ Understood", value=f"{remembered_count} / {total_cards_overall}")
    st.metric(label="🔄 Needs Review", value=f"{repeat_count} / {total_cards_overall}")
    
    if st.button("Reset Progress", use_container_width=True):
        st.session_state.card_status = {key: INITIAL_STATUS_JA for key in list(flashcard_data.keys())}
        st.rerun()
    
    st.divider()
    
    # --- Review Mode Features ---
    st.header("🔄 Review Mode")
    st.button("Show Unmastered Only", on_click=filter_deck_for_review, use_container_width=True, help="Filters to show only 'Unchecked' and 'Needs Review' cards from your active range.")
    st.button("Show All Cards in Range", on_click=reset_to_master_deck, use_container_width=True, help="Resets the deck to show all cards in the range you last applied.")


# --- Main Flashcard Area ---
st.title("Digital image processing")

if not st.session_state.card_keys_active:
    st.warning("No cards loaded or the filtered deck is empty. Please set a range or choose a deck view.")
    # Show status for the overall range if no active cards
    if len(st.session_state.card_keys_master) > 0 and len(st.session_state.card_keys_active) == 0:
         st.info("The current filtered deck is empty. All cards in your selected range might be marked as 'Understood'. Try 'Show All Cards in Range'.")
else:
    current_key = st.session_state.card_keys_active[st.session_state.current_index]
    current_answer = flashcard_data[current_key]
    
    # Get status in Japanese, then map to English for display
    current_status_ja = st.session_state.card_status.get(current_key, INITIAL_STATUS_JA)
    current_status_en = STATUS_MAP_JA_TO_EN.get(current_status_ja, "Unchecked")
    
    # Get translation dictionaries
    thai_translation = thai_translations.get(current_key, {})
    english_translation = english_translations.get(current_key, {})

    progress_value = (st.session_state.current_index + 1) / st.session_state.total_cards
    st.progress(progress_value, text=f"Card {st.session_state.current_index + 1} / {st.session_state.total_cards}")

    card_placeholder = st.empty()

    if not st.session_state.is_flipped:
        with card_placeholder.container():
            st.markdown(f"**Status:** {current_status_en}")
            with st.container(height=300, border=True):
                st.subheader("Question (Japanese Term):")
                # Render the key using the custom function (important for terms like "6角錐モデル - HSV")
                render_content_with_latex(current_key) 

            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                if st.button("Show Answer ↩️", use_container_width=True):
                    st.session_state.is_flipped = True
                    st.rerun()
            with col2:
                if st.button("▶️", use_container_width=True, help="Play Question Audio"):
                    with st.spinner("Generating audio..."):
                        audio_uri = generate_audio(current_key)
                    st.session_state.audio_to_play = audio_uri
            with col3:
                if st.button("🇹🇭", use_container_width=True, help="Show Thai Translation"):
                    if st.session_state.show_thai_translation == "question":
                        st.session_state.show_thai_translation = None
                    else:
                        st.session_state.show_thai_translation = "question"
                    st.rerun()
            with col4:
                if st.button("🇬🇧", use_container_width=True, help="Show English Translation"):
                    if st.session_state.show_english_translation == "question":
                        st.session_state.show_english_translation = None
                    else:
                        st.session_state.show_english_translation = "question"
                    st.rerun()

            if st.session_state.audio_to_play:
                st.audio(st.session_state.audio_to_play)

            if st.session_state.show_english_translation == "question" and "question" in english_translation:
                with st.container(border=True):
                    st.subheader("🇬🇧 English Translation (Question)")
                    st.info(english_translation["question"])

            if st.session_state.show_thai_translation == "question" and "question" in thai_translation:
                with st.container(border=True):
                    st.subheader("🇹🇭 Thai Translation (Question)")
                    st.info(thai_translation["question"])

    else: # Card is flipped (Answer side)
        with card_placeholder.container():
            st.markdown(f"**Status:** {current_status_en}")
            with st.container(height=300, border=True):
                st.subheader("Answer (Japanese Explanation):")
                # Render the answer using the custom function, separating LaTeX
                render_content_with_latex(current_answer)

            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                if st.button("Hide Answer ↪️", use_container_width=True):
                    st.session_state.is_flipped = False
                    st.rerun()
            with col2:
                if st.button("▶️", use_container_width=True, help="Play Answer Audio"):
                    with st.spinner("Generating audio..."):
                        audio_uri = generate_audio(current_answer)
                    st.session_state.audio_to_play = audio_uri
            with col3:
                if st.button("🇹🇭", use_container_width=True, help="Show Thai Translation"):
                    if st.session_state.show_thai_translation == "answer":
                        st.session_state.show_thai_translation = None
                    else:
                        st.session_state.show_thai_translation = "answer"
                    st.rerun()
            with col4:
                if st.button("🇬🇧", use_container_width=True, help="Show English Translation"):
                    if st.session_state.show_english_translation == "answer":
                        st.session_state.show_english_translation = None
                    else:
                        st.session_state.show_english_translation = "answer"
                    st.rerun()

            if st.session_state.audio_to_play:
                st.audio(st.session_state.audio_to_play)
                
            if st.session_state.show_english_translation == "answer" and "answer" in english_translation:
                with st.container(border=True):
                    st.subheader("🇬🇧 English Translation (Answer)")
                    st.info(english_translation["answer"])

            if st.session_state.show_thai_translation == "answer" and "answer" in thai_translation:
                with st.container(border=True):
                    st.subheader("🇹🇭 Thai Translation (Answer)")
                    st.info(thai_translation["answer"])

    st.divider()

    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        st.button("⬅️ Previous", on_click=prev_card, use_container_width=True,
                  disabled=(st.session_state.current_index == 0))
    with nav_col2:
        st.button("Next ➡️", on_click=next_card, use_container_width=True,
                  disabled=(st.session_state.current_index == st.session_state.total_cards - 1))

    status_col1, status_col2 = st.columns(2)
    # Using Japanese status keys for the function arguments
    with status_col1:
        st.button("✅ Understood", on_click=mark_status, args=(STATUS_UNDERSTOOD_JA,), use_container_width=True)
    with status_col2:
        st.button("🔄 Needs Review", on_click=mark_status, args=(STATUS_NEEDS_REVIEW_JA,), use_container_width=True)