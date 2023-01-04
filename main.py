import streamlit as st
import pandas as pd

input = st.file_uploader("Choose a CSV input")

colName= ['query id', 'q. start', 'q. end', 'query length', 'subject id', 's. start', 's. end', 'subject length','% identity','alignment length', 'evalue', 'bit score', 'subject strand']

st.write('CSV Input Format:')
st.write(pd.DataFrame(columns=colName))

if input is None:
    st.stop()

data = input.getvalue().decode('utf-8').splitlines()
file = [i for i, line in enumerate(data) if line.startswith('#')]
df = pd.read_csv(input, delimiter='\t', header=None, skiprows=file, names=colName)

st.write('Input')
st.write(df)

st.write('Output')
df = df.loc[df['% identity'] == 100]
df = df.loc[(df['q. end'] == df['query length']) & (df['s. start'] == 1)]
df = df.loc[df['query id'] != df['subject id']]
st.write(df)