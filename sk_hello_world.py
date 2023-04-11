
import streamlit
import pandas as pd

streamlit.title('hello world')

streamlit.header('header')
streamlit.text('text')
streamlit.text('This is amn update')

uploaded_file_ = st.file_uploader('Upload File Here')

products_list = [['laptop',1300],['printer',150],['tablet',300],['desk',450],['chair',200]]

df = pd.DataFrame (products_list, columns = ['product_name', 'price'])
print (df)
