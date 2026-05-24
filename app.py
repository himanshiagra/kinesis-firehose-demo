import streamlit as st
import streamlink


st.set_page_config(layout="wide")


st.title("Live YouTube Multi Stream Dashboard")


youtube_urls = [
    "https://www.hotstar.com/in/clips/dhurandhar-trailer/1271644240/watch?search_query=trailer",
    "https://www.youtube.com/watch?v=s0LLVQeMmtU",
    "https://www.youtube.com/watch?v=J326LIUrZM8",
    "https://www.youtube.com/watch?v=UiTvqSd52ak",
    "https://www.netflix.com/watch/81556385?trackId=258067290"
]


def get_stream_url(youtube_url):

    try:
        streams = streamlink.streams(youtube_url)

        if "best" in streams:
            return streams["best"].url

        return None

    except Exception as e:
        st.error(f"Error loading stream: {e}")
        return None


col1, col2 = st.columns(2)

# Stream 1
with col1:

    st.subheader("Live Stream 1")

    stream_url = get_stream_url(youtube_urls[0])

    if stream_url:
        st.video(stream_url)

    else:
        st.warning("Unable to load stream")


# Stream 2
with col2:

    st.subheader("Live Stream 2")

    stream_url = get_stream_url(youtube_urls[1])

    if stream_url:
        st.video(stream_url)

    else:
        st.warning("Unable to load stream")



col3, col4 = st.columns(2)

# Stream 3
with col3:

    st.subheader("Live Stream 3")

    stream_url = get_stream_url(youtube_urls[2])

    if stream_url:
        st.video(stream_url)

    else:
        st.warning("Unable to load stream")


# Stream 4
with col4:

    st.subheader("Live Stream 4")

    stream_url = get_stream_url(youtube_urls[3])

    if stream_url:
        st.video(stream_url)

    else:
        st.warning("Unable to load stream")




# Stream 5
col5_container = st.container()

# Stream 5
with col5_container:

    st.subheader("Live Stream 5")

    stream_url = get_stream_url(youtube_urls[4])

    if stream_url:
        st.video(stream_url)

    else:
        st.warning("Unable to load stream")
