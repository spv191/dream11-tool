import streamlit as st
import requests
import pandas as pd

# Free API for cricket player stats (Example API - Replace with actual free API if needed)
API_URL = "https://api.example.com/player-stats?name="

# Streamlit UI
st.title("Real-Time Player Analysis")
player_name = st.text_input("Enter Player Name:")

if st.button("Get Player Stats"):
    if player_name:
        try:
            response = requests.get(API_URL + player_name)
            data = response.json()
            
            if data:
                # Display Key Stats
                st.subheader(f"Stats for {player_name}")
                df = pd.DataFrame([data])  # Convert JSON to DataFrame
                st.dataframe(df)
                
                # Analytical Insights
                st.subheader("Analysis & Insights")
                st.write(f"**Recent Form:** {data.get('recent_form', 'N/A')}")
                st.write(f"**Strike Rate:** {data.get('strike_rate', 'N/A')}")
                st.write(f"**Batting Average:** {data.get('batting_avg', 'N/A')}")
                st.write(f"**Bowling Economy:** {data.get('bowling_economy', 'N/A')}")
                
            else:
                st.error("No data found for this player. Try another name.")
        except Exception as e:
            st.error(f"Error fetching data: {e}")
    else:
        st.warning("Please enter a player name.")
