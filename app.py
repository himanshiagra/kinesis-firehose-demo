import streamlit as st
import streamlink

st.set_page_config(layout="wide")

st.title("Live YouTube Multi Stream Dashboard")

youtube_urls = [
    "https://www.youtube.com/watch?v=NphMcnU8ymU&pp=ygUQZGF0YSB3YXJlaG91c2luZw%3D%3D",
    "https://www.youtube.com/watch?v=s0LLVQeMmtU&pp=ygUJbGl2ZSBuZXdz0gcJCQQLAYcqIYzv",
    "http://youtube.com/watch?v=J326LIUrZM8&list=PL9ooVrP1hQOEDSc5QEbI8WYVV_EbWKJwX",
    "https://www.youtube.com/watch?v=UiTvqSd52ak&list=PLTsNSGeIpGnGP8A74Ie1PgqHhewsqD3fv"
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


with col1:
    st.subheader("Live Stream 1")
    stream_url = get_stream_url(youtube_urls[0])

    if stream_url:
        st.video(stream_url)


with col2:
    st.subheader("Live Stream 2")
    stream_url = get_stream_url(youtube_urls[1])

    if stream_url:
        st.video(stream_url)


col3, col4 = st.columns(2)


with col3:
    st.subheader("Live Stream 3")
    stream_url = get_stream_url(youtube_urls[2])

    if stream_url:
        st.video(stream_url)


with col4:
    st.subheader("Live Stream 4")
    stream_url = get_stream_url(youtube_urls[3])

    if stream_url:
        st.video(stream_url)
