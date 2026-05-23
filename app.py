import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

st.title("Kinesis Firehose Streaming Demo")

data = []

placeholder = st.empty()

for i in range(20):

    new_data = {
        "device_id": random.randint(1000, 9999),
        "temperature": random.randint(20, 40),
        "humidity": random.randint(40, 90),
        "time": datetime.now().strftime("%H:%M:%S")
    }

    data.append(new_data)

    df = pd.DataFrame(data)

    placeholder.dataframe(df)
    time.sleep(1)

    chart.add_rows(
        pd.DataFrame(
            {
                "temperature": [new_data["temperature"]],
                "humidity": [new_data["humidity"]]
            }
        )
    )
    time.sleep(1)
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Report",
        data=csv,
        file_name="streaming_report.csv",
        mime="text/csv"
    )


