#streamlit
import streamlit as st # type: ignore

st.set_page_config (page_title= "growth mindset project")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome To Your Growth Journey!")
st.write("Embrace Challenges,learn from mistakes,and unlock your full potential.This AI-powered helps you build a growth mindset with reflection,challenges,and achievements!")

#quote section
st.header("Todays Growth Mindset Quote")
st.write("'Success is not final,Failure is not fatal:it is the courage to continue that counts.' _Winston Churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing: ")

#condition
if user_input:
    st.success(f"You're facing: {user_input}.Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

    #reflexing
    st.header(" Reflect on your learning")
reflection = st.text_area("write your reflection here:")

if reflection:
      st.success(f"Great Insight! Your reflection: {reflection}")
else :
      st.info("Reflection on past experience help you grow!Share your difficulties")

#achievements
st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you have recently accomplished:")

if achievement:
     st.success(f"Amazing!You achieved: {achievement}")
else:
     st.info("Big or small , every achievement counts! Share one now")


#footer
st.write("- - - ")
st.write("Keep believing in your self.Growth is a journey,not a destination!")
st.write("**Created by Rabia Atif**")