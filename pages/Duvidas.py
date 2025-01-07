import pandas as pd
import streamlit as st
import pydeck as pdk
import time

# st.sidebar.video('C:/Users/user/Desktop/Art_Stream/Post_Eli_Atualizado.mp4', autoplay= True, loop= True)

# container1= st.container(border= True, height= 100)
st.logo('images/icon_question.png')
st.sidebar.image('eli.png', caption='Eliane Ferreira')
st.header('Ajudarei voçe a esclarecer todas as suas duvidas! 👍')

st.header('Perguntas frequentes', divider=True)
with st.popover("Como funciona o financiamento?"):
    st.markdown("Em outras palavras, no financiamento, a instituição financeira empresta um valor que você usa para adquirir o bem ou serviço desejado. Em troca, você se compromete a devolver esse valor ao longo do tempo, em parcelas mensais, que incluem juros e outras taxas.")
with st.popover("O que um financiamento exige?"):
    st.markdown("Ser brasileiro ou, se estrangeiro, possuir visto permanente no País. Possuir capacidade civil e de pagamento. O seu nome não pode estar em cadastros de devedores, como SERASA. A prestação não pode ser maior que 30% da sua renda familiar mensal bruta.")
with st.popover("Quais são as vantagens do consórcio?"):
    st.markdown("Não tem juros. É para vários objetivos. Ajuda a ter um planejamento financeiro. Tem como acelerar a conquista. Parcelamento de 100% do valor.")
with st.popover("Libera Cred"):
    st.markdown('Financiar um produto Yamaha agora ficou muito mais simples, com o LIBERACRED você faz uma compra planejada, que garante a aprovação de um financiamento junto ao Banco Yamaha.\nPara garantir a aprovação do financiamento, ao final do seu plano, é preciso ter cumprido os requisitos: Ter pago no mínimo 08 recargas pontuais no período de 12 meses; Não ter realizado movimentações dos valores acumulados durante os 12 meses; Não possuir apontamentos no nome ao final do plano. Quer saber mais sobre o LIBERA CRED, clique no botao e assista o video que preparamos para voçe!')
with st.popover("Qual a localizaçao da concessionaria"):
    st.markdown(
        "Estamos localizado em regiao de facil acesso.\nNosso endereço Av Dulce Sarmento, 864, Alto Sao Joao")
    with st.spinner('carregando!'):
            time.sleep(2)
    df = pd.DataFrame({
        'lat': [-16.69641120149624],
        'lon': [-43.81215144729478]
    })
    container_map = st.container(border=True, height=600)
    container_map.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=-16.69641120149624,
            longitude=-43.81215144729478,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
        ],
    ))

    st.info('🌎 Montes Claros - Minas Gerais - Brasil')




























# option = st.sidebar.selectbox(
#     "",
#     ("🛠", "🏍", "✔", "🗓"),
#     index=None,
#     placeholder=" Buscar tabelas...")

# if option == "🏍":
#     st.sidebar.dataframe(motos_rev, hide_index= True, use_container_width= True)
# elif option == "🛠":
#     st.sidebar.dataframe(servico, hide_index= True)
# elif option == '✔':
#     st.sidebar.dataframe(anos, hide_index= True)
# elif option == '🗓':
#     st.subheader('DADOS BRUTOS', divider= True)
#     st.dataframe(regi, hide_index= True, width= 800, height= 700)
#     st.info('Os serviços podem variar de acordo com a demanda')
