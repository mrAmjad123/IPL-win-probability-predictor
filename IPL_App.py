import pickle

import streamlit as st
import pickle
import pandas as pd

teams = ['Royal Challengers Bengaluru',
 'Kolkata Knight Riders',
 'Gujarat Titans',
 'Lucknow Super Giants',
 'Delhi Capitals',
 'Mumbai Indians',
 'Rajasthan Royals',
 'Punjab Kings',
 'Chennai Super Kings',
 'Sunrisers Hyderabad']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']

pipe = pickle.load(open('pipe.pkl','rb'))

st.title('IPL Win Probability')
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting team..', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select Bowling team..', sorted(teams))

city = st.selectbox('Select host city..', sorted(cities))
target_runs = st.number_input('Enter target..')

col3,col4,col5 = st.columns(3)
with col3:
    score = st.number_input('Enter Current Score..')
with col4:
    overs = st.number_input('Enter overs completed..')
with col5:
    wickets = st.number_input('Enter Wickets Down..')

if st.button('Predict Probability'):
    runs_left = target_runs-score
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team], 'bowling_team':[bowling_team], 'city':[city],'runs_left':[runs_left], 'balls_left':[balls_left],
                  'wickets_left':[wickets_left], 'target_runs':[target_runs], 'crr':[crr], 'rrr':[rrr]})
    # st.table(input_df)

    result = pipe.predict_proba(input_df)
    # st.text(result)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100))+ "%")
    st.header(bowling_team + "- " + str(round(loss*100))+ "%")