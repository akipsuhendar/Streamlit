import streamlit as st

# Title and header
st.title("Hello, World!")
st.header("Welcome to your first Streamlit app!")

# Text and Markdown formatting
st.text("This is some simple text.")
st.markdown("And this is some formatted text with **bold** and _italics_.")

# Numbers and data structures
st.write([1, 2, 3])
st.dataframe({"fruit": ["apple", "banana", "cherry"], "price": [1.5, 2.0, 3.5]})

# Interactive elements
st.button("Click me!")
st.checkbox("Check me if you're happy.")
st.radio("Choose your favorite color:", ("red", "green", "blue"))

# Widgets and plots
st.slider("Pick a number:", min_value=0, max_value=10)
st.line_chart([1, 2, 3, 4])

# Customize layout with columns and rows
col1, col2 = st.columns(2)
col1.write("This is in the first column!")
col2.write("And this is in the second!")

# And much more!

# Bonus tip: Add a cool image to spice things up!
st.image("https://raw.githubusercontent.com/streamlit/streamlit/master/static/images/brand/streamlit-logo-medium.png")
