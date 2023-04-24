import streamlit as st
import time


st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latesut_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latesut_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expandar = st.expander('問合せ')
expandar.write('問合せ内容を書く')