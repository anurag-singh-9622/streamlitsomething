import streamlit as st
import numpy as np

# chatbox = st.chat_message("user")
# chatbox.write("Hello 👋")
# # chatbox.line_chart(np.random.randn(30, 3))

# prompt = st.chat_input("Say something")
# if prompt:
#     chatbox.write("\n")
#     chatbox.write(f"User has sent the following prompt: {prompt}")

# '''Session State'''
# input = st.text_input("Input", key = "input")

# if 'key' not in st.session_state:
#     st.session_state.key = 'value'

# st.session_state

# def form_callback():
#     st.write(st.session_state.my_slider)
#     st.write(st.session_state.my_checkbox)

# with st.form(key='my_form'):
#     slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
#     checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
#     submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

# slider_input
# st.session_state.my_slider
# st.session_state
# def showsomething():
#     st.write(500)


# slider = st.slider("slider", key = "s")
# if slider > 50:
#     "hooray!"
# else: "not"


### Thought Counter app
# st.title("Thought Counter")
# col1, col2, col3 = st.columns([2,1,2])
# if 'thought_counter' not in st.session_state:
#     st.session_state.thought_counter = 0
# if 'boolean' not in st.session_state:
#     st.session_state.boolean = False

# thought_button = col2.button(":red[Thought]", help="Unecessary Thought Counter")

# if thought_button:
#     st.session_state.thought_counter += 1
#     st.session_state.boolean = not st.session_state.boolean

# # st.session_state
# col2.write(f":blue[No of thoughts:] :red[{st.session_state.thought_counter}]")

##Convert the units

st.title("Convert Units")
st.session_state


col1, buff, col2 = st.columns([2,1,2])

def lbs_to_kgs():
    st.session_state.kgs = st.session_state.lbs*0.45359237

def kgs_to_lbs():
    st.session_state.lbs = st.session_state.kgs/0.45359237
units = ["Pound", "Kilogram", "Ounce"]

# left_units = col1.selectbox(label = "Units",options = units)

with col1:
    pounds = st.number_input('Pounds', key = "lbs", on_change = lbs_to_kgs)

with col2:
    kilograms = st.number_input('Kilograms', key = "kgs", on_change = kgs_to_lbs)


