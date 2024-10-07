import streamlit as st
import pandas as pd

# Initialize or load existing data
if 'climb_log_df' not in st.session_state:
    st.session_state['climb_log_df'] = pd.DataFrame(columns=['Date', 'Climb Name', 'Location', 'Grade', 'Type', 'Attempts', 'Send Type', 'Notes'])

st.title("Climbing Log Recorder")

# File uploader for previously saved logs
uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
if uploaded_file:
    uploaded_df = pd.read_csv(uploaded_file)
    st.session_state['climb_log_df'] = pd.concat([st.session_state['climb_log_df'], uploaded_df]).drop_duplicates().reset_index(drop=True)
    st.success("File uploaded successfully!")

# Input form for climb log
with st.form(key='climb_log_form'):
    date = st.date_input("Date")
    climb_name = st.text_input("Climb Name")
    location = st.text_input("Location")
    grade = st.text_input("Grade")
    climb_type = st.selectbox("Type of Climb", options=["Bouldering", "Sport", "Trad", "Top Rope", "Other"])
    attempts = st.number_input("Number of Attempts", min_value=1, step=1)
    send_type = st.selectbox("Send Type", options=["Flash", "Onsight", "Redpoint"])
    notes = st.text_area("Notes")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if climb_name and location:
            new_data = pd.DataFrame({
                'Date': [date],
                'Climb Name': [climb_name],
                'Location': [location],
                'Grade': [grade],
                'Type': [climb_type],
                'Attempts': [attempts],
                'Send Type': [send_type],
                'Notes': [notes]
            })
            st.session_state['climb_log_df'] = pd.concat([st.session_state['climb_log_df'], new_data], ignore_index=True)
            st.success("Climb log added successfully!")
        else:
            st.error("Please fill in all required fields.")

# Display recorded climb logs
st.subheader("Recorded Climb Logs")
st.table(st.session_state['climb_log_df'])

# Save to CSV
csv = st.session_state['climb_log_df'].to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='climb_log.csv',
    mime='text/csv'
)
