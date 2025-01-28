import streamlit as st

st.logo('carmo.png')
# st.header('Especialista em Motos Yamaha', divider= True)
st.image('elip.png')
st.subheader("Seja bem vindo(a) ao mundo Yamaha.", divider= True)
st.info('Acesse o menu lateral clicando na setinha no canto superior esquerdo da sua tela')
st.markdown('''Com mais de 15 anos de experiência, Eliane se destaca no mercado como uma especialista em atendimento, além de se destacar pela empatia, simpatia, entusiasmo, persistência e atenção com foco no cliente. Sua paixão por motos e sua habilidade em construir relacionamentos duradouros a tornam a profissional ideal para te auxiliar na escolha da sua próxima aventura sobre duas rodas.''')
st.subheader('Aqui ofereço:')
st.markdown('''Conhecimento profundo: Eliane domina as características técnicas de toda a linha Yamaha, desde as motos mais populares até os modelos mais sofisticados.\n
        \nAtendimento personalizado: Ela compreende que cada cliente possui necessidades e expectativas únicas, por isso oferece soluções sob medida, facilitando a negociação e garantindo a sua satisfação.\n
        \nPós-venda completo: O compromisso de Eliane vai além da venda. Ela oferece um acompanhamento completo após a aquisição da moto, estando sempre à disposição para tirar dúvidas e oferecer suporte.\n
        \nProdutos náuticos: Além de motocicletas, Eliane também é especialista em produtos náuticos Yamaha, oferecendo um portfólio completo para os amantes de atividades aquáticas.\n''')
st.subheader('Por que me escolher?')
st.markdown('''Experiência: Mais de 15 anos de experiência no mercado de vendas.\n
        \nConhecimento: Domínio técnico da linha Yamaha e de outras marcas.\n
        \nAtendimento personalizado: Soluções sob medida para cada cliente.\n
        \nPós-venda completo: Suporte completo após a venda.\n''')
st.info('🚨. Entre em contato com Eliane e descubra a moto perfeita para você! 🚨')
st.link_button(label= 'Fale comigo!', url='https://wa.me/message/P2RUEPY7L3C4B1', type='primary')
st.markdown('#CarmoMotosYamaha #Yamaha #Motocicletas #Náutica #AtendimentoPersonalizado #SuaAventuraComeçaAqui')
st.divider()
st.markdown('AVALIE MEU ATENDIMENTO')
avaliar = st.feedback('thumbs')
if avaliar == True:
        st.info('Fico muito feliz com o seu feedback positivo. Obrigado pela confiança!')
elif avaliar == False:
        st.info('Agradecemos sua visita, foi um prazer atende-lo!')
st.sidebar.subheader('NOVIDADE', divider= True)
bt= st.sidebar.button('LIBERACRED')
if bt == True:
        st.sidebar.video('vdlib.mp4', autoplay= True)
        
