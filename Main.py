import streamlit as st
from Content import ActivationFunctions, NetworkArchitecture, Dataset
import Sidebar
from Pages import Train, Quiz

def main():
    page = Sidebar.draw_sidebar(st)

    if(page=="Home"):
        st.title("Introduction to Neural Networks")
        st.write("This Streamlit app is designed to be an educational and hands-on tool for individuals interested in Neural Networks. It provides an intuitive interface to experiment with mathematical functions, generate datasets, and observe how neural networks learn from and predict on different data patterns.")
        st.divider()

        ActivationFunctions.draw(st)
        st.divider()
        

        NetworkArchitecture.draw(st)
        st.divider()

        Dataset.draw(st)
        st.divider()
    elif(page=="Train"):
        Train.main()
    elif(page=="Quiz"):
        Quiz.main()

if __name__ == "__main__":
    main()