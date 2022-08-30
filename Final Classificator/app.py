import streamlit as st
import pandas as pd
from predict_class import *

st.title('Unbalance Classifier')
st.markdown('Model developed for our final project of Mechanical Engineer at UFPR')
st.markdown("Students: Bruno Gonçalves Rocha & João Guilherme Cotta Machado de Souza")


info = st.checkbox('Show info', value=False)
if info:
    st.markdown('### 1 - Select an excel or .csv file')
    st.markdown('The file must follow the example:')
    ex = pd.read_csv('assets/exemplo.csv')
    st.dataframe(ex)
    st.markdown('The columns correspond to the acceleration by time of the mechanical system.')
    st.markdown(" * The columns don't need to have the same name as the example, but must follow the same sequence (axial, tangential and radial directions)")
    st.image('assets/directions.png')

    st.markdown('### 2 - Acquisition sample rate')
    st.markdown("It's the rate that the data (acceleration) is acquired")
    st.latex(r'f_s = \frac{1}{(t_1 - t_0)} [Hz]')
    st.markdown("""
    * This model considers for the classification frequencies up to 2x the rotation frequency of the system. Therefore, based on Nyquist's theorem, the acquisition frequency should be at least 4x greater than the motor rotation frequency. 
    """)
    
    st.markdown('### 3 - Shaft rotation speed:')
    st.markdown("""It's the rotation frequency of the system shaft, ideally it should be obtained from a measurement with a tachometer.
    If this is not possible, the engine speed can be informed.
     """)

    st.markdown('### Exemple:')
    st.markdown("""Below are two files obtained from experiments carried out during this work,
    the acquisition frequency for both is 1200 Hz and the motor speed is informed in the file name.
    """)
    with open('assets/exemples/exemples.rar', 'rb') as f:
        st.download_button('Download Exemple', data=f, file_name='exemples.rar')






uploaded_file = st.sidebar.file_uploader('Select the file', 
                            help='Excel or csv file. Check info for more details',
                            type=['csv', 'xlsx'])
aq1, aq2 = st.sidebar.columns(2)
freq_s = aq1.number_input('Acquisition sample rate:', min_value=0,step=100, value=1200)
unidade = aq2.radio("Unity:", ['Hz', 'CPM'])
motor1, motor2 = st.sidebar.columns(2)
rot = motor1.number_input('Shaft rotation speed:', min_value=0,step=100, value=1000)
unidade2 = motor2.radio("Unity:", ['Hz', 'CPM'], key='unidade_motor')
_,meio,_ = st.sidebar.columns(3)
pred = meio.button('Predict')



if uploaded_file is not None:
    extensao = uploaded_file.name.split('.')[1]
    if extensao == 'csv':
        df = pd.read_csv(uploaded_file)
    elif extensao == 'xlsx':
        df = pd.read_excel(uploaded_file)
    else:
        st.sidebar.write('Invalid File')
    # st.dataframe(df)

fs = freq_s /60 if unidade == 'CPM' else freq_s
rot = rot /60 if unidade2 == 'CPM' else rot

def error_message(text, size=12):
    return f'<p style="font-family:Courier; color:red; font-size: {size}px;">{text}</p>'

if pred:
    info = False
    if uploaded_file is None:
        st.sidebar.markdown(error_message('No file'),unsafe_allow_html=True)
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
                col2.markdown('### Unbalance')
        except:
            st.sidebar.markdown(error_message('Invalid values, check info for more details'),unsafe_allow_html=True)
