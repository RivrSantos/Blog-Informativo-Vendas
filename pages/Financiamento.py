import streamlit as st
from selenium import webdriver


st.logo('images/icon_finan.png')
# @st.dialog("Cast your vote")
# def vote(item):
#     st.write(f"Why is {item} your favorite?")
#     reason = st.text_input("Because...")
#     if st.button("Submit"):
#         st.session_state.vote = {"item": item, "reason": reason}
#         st.rerun()
# st.table('tb1')
# navegador = webdriver.Chrome()
# navegador.get('')

# cont= st.container(border= True, height= 700)

# cont.text_area(label= 'Noe')
st.subheader('APOS PRRENCHER O FORMULARIO CLIQUE NO BOTAO "ENVIAR"')
with st.form(key='send', clear_on_submit= True):
    st.subheader('SIMULAÇAO')
    st.text_input(label= 'NOME')
    st.number_input(label='CPF', max_value= 100000000000)
    st.number_input(label='CONTATO', max_value= 100000000000)
    st.text_input(label='ENDEREÇO')
    st.number_input(label='IDADE', max_value= 100000000000)
    st.text_input(label='PROFISSAO')
    st.number_input(label='RENDA R$')
    st.text_input('INTERESSADO EM: (DIGITE NOME/MODELO DA MOTOCICLETA)')
    st.date_input('Data')
    st.checkbox('concordo e me responsabiliso pelos dados presentes neste formulario')
    submit = st.form_submit_button('ENVIAR')
    # st.rerun()


# st.form_submit_button('enviar')

# st.sidebar.video('C:/Users/user/Desktop/Art_Stream/Post_Eli_Atualizado.mp4', autoplay= True, loop= True)

# container1= st.container(border= True, height= 100)

# st.header('FAZER SIMULAÇAO ! 👍')
