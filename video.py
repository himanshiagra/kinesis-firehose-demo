import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

st.set_page_config(page_title="Video Streaming Analytics", layout="wide")

st.title("Video Streaming Analytics Dashboard")

video_titles = [
    "Cloud Computing Basics",
    "AWS Tutorial",
    "Python Full Course",
    "Data Structures",
    "AI Introduction"
]

countries = ["India", "USA", "UAE", "Qatar", "UK"]

data = []


viewer_metric = st.empty()
watch_metric = st.empty()


chart = st.line_chart()


table_placeholder = st.empty()

total_viewers = 0
total_watch_time = 0

for i in range(30):

    viewers = random.randint(100, 1000)

    watch_time = random.randint(1, 60)

    new_data = {
        "video": random.choice(video_titles),
        "country": random.choice(countries),
        "viewers": viewers,
        "watch_time_minutes": watch_time,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }

    data.append(new_data)

    df = pd.DataFrame(data)

    total_viewers += viewers
    total_watch_time += watch_time

   
    viewer_metric.metric("Total Viewers", total_viewers)

    watch_metric.metric("Total Watch Time", f"{total_watch_time} mins")

    
    table_placeholder.dataframe(df)

    
    chart.add_rows(
        pd.DataFrame(
            {
                "Viewers": [viewers],
                "Watch Time": [watch_time]
            }
        )
    )

   
    if viewers > 900:
        st.warning("High Video Traffic Detected!")

    time.sleep(1)


csv = df.to_csv(index=False)

st.download_button(
    label="Download Streaming Report",
    data=csv,
    file_name="video_streaming_report.csv",
    mime="text/csv"
)
