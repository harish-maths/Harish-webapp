import streamlit as st

tab1,tab2,tab3 = st.tabs(["About","Hobbies","Contact"])

with tab1:
    
    col1,col2 = st.columns([0.3,0.7])
    
    with col1:
        st.image("my_picture/harish.jpg",width=200)
        st.subheader("Harish Ravi :sunglasses:")
    
    with col2:
        st.write("Hello, I am Harish Ravi, a Junior Developer :computer: . My parents find it challenging to manage and track their expenses. So, I created a website  to help them in tracking and managing their expenses. You can use this website to manage and track your expenses as well. I hope you all :blue_heart: it.")

with tab2:
     st.write("I love solving math :triangular_ruler: problems and watching documentaries 	:performing_arts: to learn about different things. Also, I'm into MMA fights :boxing_glove: , enjoying the intensity and skills of the fighters.")

with tab3:
    st.write("Email : harishmaths.ai@gmail.com")
    st.write("Website : https://harishmaths.home.blog/")