import streamlit as st
import pandas as pd

# Initialize or load existing data
if 'scores_df' not in st.session_state:
    st.session_state['scores_df'] = pd.DataFrame(columns=['Test Name', 'Score', 'Total Score', 'Percentage', 'Grade'])

st.title("Test Scores Recorder")

# File uploader for previously saved scores
uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
if uploaded_file:
    uploaded_df = pd.read_csv(uploaded_file)
    st.session_state['scores_df'] = pd.concat([st.session_state['scores_df'], uploaded_df]).drop_duplicates().reset_index(drop=True)
    st.success("File uploaded successfully!")

# Input form for test scores
with st.form(key='score_form'):
    test_name = st.text_input("Test Name")
    score = st.number_input("Score", min_value=0, max_value=100)
    total_score = st.number_input("Total Score", min_value=0, max_value=100)
    grade = st.text_input("Grade")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if test_name and score is not None and total_score != 0:
            percentage = (score / total_score) * 100
            new_data = pd.DataFrame({
                'Test Name': [test_name],
                'Score': [score],
                'Total Score': [total_score],
                'Percentage': [percentage],
                'Grade': [grade]
            })
            st.session_state['scores_df'] = pd.concat([st.session_state['scores_df'], new_data], ignore_index=True)
            st.success("Score added successfully!")
        else:
            st.error("Please fill in all fields and ensure total score is not zero.")

# Display recorded scores
st.subheader("Recorded Scores")
st.table(st.session_state['scores_df'])

# Save to CSV
csv = st.session_state['scores_df'].to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='test_scores.csv',
    mime='text/csv'
)
