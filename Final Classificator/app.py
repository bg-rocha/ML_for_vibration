import streamlit as st
import pandas as pd
from predict_class import *

st.title('Classificador de Desbalanceamento')
st.markdown('Modelo desenvolvido durante o trabalho de conclusão de curso da Engenharia Mecânica UFPR')
st.markdown("Alunos: Bruno Gonçalves Rocha e João Guilherme Cotta Machado de Souza")
info = st.checkbox('Mostrar instruções', value=True)
uploaded_file = st.sidebar.file_uploader('Choose a file', help='teste')
aq1, aq2 = st.sidebar.columns(2)
freq_s = aq1.number_input('Frequencia de aquisição dos dados:', min_value=0,step=100, value=1200,)
unidade = aq2.radio("Unidade:", ['Hz', 'RPM'])
motor1, motor2 = st.sidebar.columns(2)
rot = motor1.number_input('Rotação do motor:', min_value=0,step=100, value=1000)
unidade2 = motor2.radio("Unidade:", ['Hz', 'RPM'], key='unidade_motor')
_,meio,_ = st.sidebar.columns(3)
pred = meio.button('Predict')



if uploaded_file is not None:
    extensao = uploaded_file.name.split('.')[1]
    if extensao == 'csv':
        df = pd.read_csv(uploaded_file)
    elif extensao == 'xlsx':
        df = pd.read_excel(uploaded_file)
    else:
        st.sidebar.write('Arquivo Invalido')
    # st.dataframe(df)

fs = freq_s /60 if unidade == 'RPM' else freq_s
rot = rot /60 if unidade2 == 'RPM' else rot

def error_message(text, size=12):
    return f'<p style="font-family:Courier; color:red; font-size: {size}px;">{text}</p>'

if pred:
    if uploaded_file is None:
        st.sidebar.markdown(error_message('Nenhum arquivo foi adicionado'),unsafe_allow_html=True)
    else:
        try:
            prediction = predictUnbalance(df,fs,rot)
            st.markdown('# Prediction:')
            col1, col2 = st.columns(2)
            if prediction.predict()[0] == 0:
                col1.image('assets/positive.png', width=150)
                col2.markdown('## Normal')
            elif prediction.predict()[0] == 1:
                col1.image('assets/negative.png', width=150)
                col2.markdown('## Desbalanceado')
        except:
            st.sidebar.markdown(error_message('Verificar se os valores estão corretos'),unsafe_allow_html=True)
