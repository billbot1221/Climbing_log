import streamlit as st
import random 


st.set_page_config(
    page_title="Play Your Cards Right",
    page_icon="🃏",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={'About': "I Made This Game When I Was 13 Years Old"}
)

def game():
    st.title("Play Your Cards Right!")

    st.write("Welcome! Guess whether the next card will be higher or lower than the current card.")
    cards = st.session_state.get('cards', ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"])
    score = st.session_state.get('score', 0)
    option = st.session_state.get('option', list(range(0, 13)))  # Adjusted the range
    first_card = st.session_state.get('first_card', None)
    end = st.session_state.get('end', False)
    
    if score < 5:
        if first_card is None:
            first_card = random.choice(option)

        second_card = random.choice(option)

        with st.form("my_form"):
            st.write(f"Your First Card: {cards[first_card]}")

            human_input = st.selectbox("Higher Or Lower", options=["Lower", "Higher"])

            submitted = st.form_submit_button("Submit")

            if submitted:
                if (human_input == "Lower" and first_card >= second_card) or \
                   (human_input == "Higher" and first_card <= second_card):
                    st.write(f"Correct! The Second Card Was a: {cards[second_card]}")  # Adjusted here
                    score += 1
                    st.write(f"Score: {score}")
                else:
                    st.write(f"Wrong! The Second Card Was a: {cards[second_card]}")  # Adjusted here
                    st.write(f"Score: {score}")
                    end = True

                first_card = second_card
                
        st.session_state['score'] = score
        st.session_state['first_card'] = first_card
        st.session_state['end'] = end
        
        if end:
            st.error('You Lost', icon="❌")
            st.session_state.clear()  # Reset session state after winning
        if score >= 5:
            st.success("Congratulations! You won!", icon="✅")
            st.balloons()
            st.session_state.clear()  # Reset session state after winning

if __name__ == "__main__":
    game()
