import streamlit as st
from pathlib import Path
import webbrowser

curSub=1
levelsCompleted=0

st.title("CIRCUIT QUEST")

#def read_markdown_file(markdown_file):
#    return Path(markdown_file).read_text()

def displayPrompt(level):
     listOfPrompts = ["BLINK: Create a circuit that powers an LED light on and off every second. You’ll need two wires, a resistor, and an LED.",
                      "Create a circuit that requires a button press to power a light.",
                      "Use a potentiometer to control the amount of light that the LED gives off.",
                      "Power any two of the three color pins and have a third one controlled by a potentiometer to change the color. If your circuit does not work",
                      "For Challenge 5, have the readings of an ultrasonic sensor control an RGB light, with red corresponding to a long distance, green for a medium distance, and blue for a short distance. Use pin 2 for red, 3 for green, 4 for blue. If distance is greater than 50, display red, if less than 50 but greater than 20 display green, otherwise display blue."]
     st.header(listOfPrompts[level-1])

def giveHint(level):
     listOfHints=["Remember to position the cathode and anode correctly as well as line up the pins correctly.",
                  "Remember to orient the button correctly and make sure that all of your wires line up so that the circuit flows continuously.",
                  "Remember to make sure to use the correct pins, as each corresponds to a specific purpose. The left one is for ground, the center is for signal (output), and the right is for input",
                  "Remember to orient the RGB lights. If it doesn't work, consider rotating the light 180 degrees",
                  "Make sure that the trig and echo pins are connected correctly. Check the serial to see if distance is working as intended. If you cannot see anything else, double check your if-statements."
                  ]
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
          #st.markdown("![lesson2image](https://lh7-us.googleusercontent.com/6p7tP_1HyXoNyM65Sxsb2OWF-PQqqgXWTJH55BTO0WaETV3NpaIxrzDdC9bcOy5ClmVyTl-d8SsHxw9pitL02fmrfDiMzsvNsZFMgs5ST_gDdxmKJ48lu9QwxeZUnw13qK9y5I519NnyQ2zaea50x3I)")
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

c1,c2,c3,c4,c5=st.colums(5)
with c1:
     if st.button("Level 1"):
          levelsCompleted = 0
          bar.progress(0, text=f"Progress: 0%")
          webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson1.md")
          lesson(1)
with c2:
     if st.button("Level 2"):
     levelsCompleted = 1
     bar.progress(0, text=f"Progress: 20%")
     webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson2.md")
     lesson(1)
with c3:
     if st.button("Level 3"):
     levelsCompleted = 2
     bar.progress(0, text=f"Progress: 40%")
     webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson3.md")
     lesson(1)
with c4:
     if st.button("Level 4"):
     levelsCompleted = 3
     bar.progress(0, text=f"Progress: 60%")
     webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson4.md")
     lesson(1)
with c5:
     if st.button("Level 5"):
     levelsCompleted = 4
     bar.progress(0, text=f"Progress: 80%")
     webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson5.md")
     lesson(1)
#if curSub==1 and levelsCompleted==0:
     #lesson(1)
#if curSub==2:
#     col1, col2, col3 = st.columns(3)
#     with col1:
#          if st.button("Hint"):
#               giveHint(levelsCompleted)
#     with col2:
#          if st.button("Give Up"):
#               giveSolution(levelsCompleted)
#     
#     with col3:
#          if st.button("Level 1"):
#               levelsCompleted = 0
#               bar.progress(0, text=f"Progress: 0%")
#               webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson1.md")
          #      lesson(1)
          # if st.button("Level 2"):
          #      bar.progress(20,text=f"Progress: 14%")
          #      webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson2.md")
          #      lesson(2)
          # if st.button("Level 3"):
          #      bar.progress(40, text=f"Progress: 28%")
          #      webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson3.md")
          # if st.button("Level 4"):
          #      bar.progress(60, text=f"Progress: 42%")
          #      webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson4.md")
          # if st.button("Level 5"):
          #      bar.progress(80, text=f"Progress: 56%")
          #      webbrowser.open_new_tab("https://github.com/Shiven121S/MakeSPP/blob/main/lesson5.md")
