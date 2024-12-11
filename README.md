# IPL-win-probability-predictor
This project is a machine learning-based web application that predicts the win probability of a team during an IPL (Indian Premier League) match in real-time. It leverages past IPL data to provide insights into the likelihood of a team's victory based on match conditions such as runs, overs, wickets, and target scores.
Features
Interactive Web Interface: Built using Streamlit for a user-friendly experience.
Team and Venue Selection: Allows users to select batting and bowling teams as well as the match venue.
Live Match Inputs: Accepts real-time inputs like current score, overs completed, and wickets down.
Win Probability Calculation: Dynamically computes and displays the probability of the batting team winning or losing the match.
Data-driven Insights: Uses a machine learning model trained on historical IPL match data.

Technology Stack
Frontend: Streamlit for creating an interactive and responsive web application.
Backend: Python with a pre-trained machine learning model (stored in pipe.pkl).
Machine Learning: Predictive model trained on historical IPL data to analyze match probabilities.

Requirements
Python 3.8 or higher
Required libraries: Streamlit, Pandas, Pickle, Scikit-learn

Future Enhancements
Add support for other cricket leagues.
Enhance prediction model with additional features like player form and weather conditions.
Include a historical data visualization feature for IPL match statistics.
