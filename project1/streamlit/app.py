import streamlit as st  # Import Streamlit for web app creation
import pandas as pd  # Import pandas for data manipulation
import numpy as np  # Import numpy for numerical operations

# Set the title of the Streamlit app
st.title("My first app")

# Write a text to the Streamlit app
st.write("Here's our first attempt at using data to create a table:")

# Create a simple DataFrame and display it in the Streamlit app
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Create another DataFrame with specific data
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Generate a DataFrame with random numbers and specific column names
df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20))
)

# Display the DataFrame with random numbers in the Streamlit app
st.write(df)

# Create a DataFrame with random numbers for a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Display a line chart in the Streamlit app using the random data
st.line_chart(chart_data)