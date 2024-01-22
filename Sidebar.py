def draw_sidebar(st):
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home", "Train", "Quiz"])
    st.sidebar.title("")

    return page