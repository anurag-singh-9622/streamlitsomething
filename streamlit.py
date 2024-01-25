import streamlit as st
import numpy as np
import pandas as pd
import time


# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# st.dataframe(dataframe.style.highlight_max(axis=0))

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# st.table(dataframe)

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.session_state.name

# print(st.session_state.name)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data
# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# left_column, middle_column,right_column = st.columns(3)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# with middle_column:
#     'kbhbbk'

# 'Starting a long computation...'

# Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     # Update the progress bar with each iteration.
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)

# '... and now we\'re done!'
a = ['215', '315', '351', '265']
ans = st.radio("What is 25% of 1260?", a, None)
# latest_iteration = st.empty()
# bar = st.progress(0)


if ans == a[1]:
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Loading {i+1}%')
        bar.progress(i+1)
        time.sleep(0.05)
    'Sahi hai benchod'
if ans == a[0] or ans == a[2] or ans == a[3]:
    time.sleep(2)
    'Tere se na ho payega Benchod'
    time.sleep(3)
    'Ja Rajeev Barwe se Puch kar aaa, Betichod'


