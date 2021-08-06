import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Proactive Managemant of Material Obsolescence')
st.write("Equipment Lifecycle")
"""
# Markdown Heading 1
## Markdown Heading 2
### Markdown Heading 3
##### Markdown Heading 4
###### Markdown Heading 5

How do I make a Cartesian graph?

---
"""
st.write("Creating a chart with the write function")
st.write(pd.DataFrame({
    'first column': [5, 6, 7, 8],
    'second column':[50, 60, 70, 80]
}))

st.write("Creating a chart without the write function")
df = pd.DataFrame({
    'first column': [1, 2, 3,4],
    'second column':[10, 20, 30, 40]
})

df

"""
---
## Drawing a line chart
"""
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a','b', 'c'])
st.line_chart(chart_data)

"""
---
## Plot a Map
"""
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [36.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


"""
---
## Interactivity w/ widgets
"""

"""
### Use checkboxes to show/hide data
"""
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(30, 5),
        columns=['d', 'e','f', 'g', 'h'])

    chart_data


"""
### Use a selectbox for options
"""
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

"""
---
## Lay out your app
"""
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

"""
---
## Show progress in real time!
"""
"""
#### Starting a long computation
"""
#add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # update progress bar with each iteration
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

"""
#### and now we\'re done!
"""