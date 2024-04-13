import streamlit as st
from pathlib import Path
import webbrowser

curSub=1
levelsCompleted=0

st.title("CIRCUIT QUEST")

#def read_markdown_file(markdown_file):
#    return Path(markdown_file).read_text()

def displayPrompt(level):
     listOfPrompts = ["BLINK: Create a circuit that powers an LED light on and off every second. You’ll need two wires, a resistor, and an LED."]
     st.header(listOfPrompts[level-1])

def giveHint(level):
     listOfHints=["Remember to position the cathode and anode correctly as well as line up the pins correctly."]
     st.write(listOfHints[level])

def giveSolution(level):
     if level+1==1:
          st.image("code1.png")
          st.image("solution1a.png")

#placeholder1 = st.empty()
#placeholder2 = st.empty()     
#def parseMarkdown(file, levelNumber):
#     placeholder=read_markdown_file(file)
#     placeholder=st.markdown(placeholder, unsafe_allow_html=True)
#     if st.button(f"Finished Reading Level {levelNumber}?"):
#          placeholder.empty()

def lesson(level):
     if level == 1:
          #parseMarkdown("lesson1.md", level)
          st.markdown("")
          moveOn()
     elif level == 2:
          st.markdown("![lesson2image](https://lh7-us.googleusercontent.com/6p7tP_1HyXoNyM65Sxsb2OWF-PQqqgXWTJH55BTO0WaETV3NpaIxrzDdC9bcOy5ClmVyTl-d8SsHxw9pitL02fmrfDiMzsvNsZFMgs5ST_gDdxmKJ48lu9QwxeZUnw13qK9y5I519NnyQ2zaea50x3I)")
          #parseMarkdown("lesson2.md", level)
          moveOn()
     elif level == 3:
          pass
          moveOn()
     elif level == 4:
          pass
          moveOn()
     elif level == 5:
          pass
          moveOn()
     elif level == 6:
          pass
          moveOn()
     elif level == 7:
          pass


playerProgress=1
if curSub == 1:
     playerProgress=(levelsCompleted+0.5)/7
if curSub == 2:
     playerProgress=(levelsCompleted+1)/7
if curSub==1 and levelsCompleted==0:
     playerProgress=0

bar = st.progress(playerProgress, text=f"Progress: {round(playerProgress*100)}%" )

def moveOn():
     global curSub
     global levelsCompleted
     if curSub==1:
          curSub=2
          bar.progress(playerProgress+0.07, text=f"Progress: {round((playerProgress+0.07)*100)}%")
     elif curSub==2:
          curSub=1
          levelsCompleted+=1
          playerProgress
          bar.progress(playerProgress+0.07, text=f"Progress: {round((playerProgress+0.07)*100)}%")

if curSub==1 and levelsCompleted==0:
     lesson(1)
if curSub==2:
     col1, col2, col3 = st.columns(3)
     with col1:
          if st.button("Hint"):
               giveHint(levelsCompleted)
     with col2:
          if st.button("Give Up"):
               giveSolution(levelsCompleted)
     
     with col3:
          if st.button("Level 1"):
               levelsCompleted = 0
               bar.progress(0, text=f"Progress: 0%")
               lesson(1)
          if st.button("Level 2"):
               bar.progress(14, text=f"Progress: 14%")
               lesson(2)
          if st.button("Level 3"):
               bar.progress(28, text=f"Progress: 28%")
          if st.button("Level 4"):
               bar.progress(42, text=f"Progress: 42%")
          if st.button("Level 5"):
               bar.progress(56, text=f"Progress: 56%")
          if st.button("Level 6"):
               bar.progress(70, text=f"Progress: 70%")
          if st.button("Level 7"):
               bar.progress(84, text=f"Progress: 84%")
