import streamlit as st
from selenium import webdriver

st.logo('images\icon-forms.png')
st.sidebar.image('images\eli.jpg', caption='Eliane Ferreira')
# st.image('images\carmo.png', width=200)
# st.image('images\mymoto.jpg')
# navegador = webdriver.Chrome()
# navegador.get('')
# navegador.get(
#     'https://www.motoo.com.br/yamaha-crosser-150-2025-lancamento-oficial-preco-fotos/')
# tabela = navegador.find_elements('//*[@id="wrap"]/table[2]')
st.markdown('''Como funciona o Consórcio Nacional Yamaha
        \nEscolha do plano: Ao aderir ao Consórcio Yamaha, você escolhe o valor da carta de crédito que deseja e a quantidade de parcelas que cabe no seu bolso.
        \nFormação do grupo: Você será inserido em um grupo de pessoas com objetivos semelhantes.
        \nPagamento das parcelas: Mensalmente, você paga uma parcela que será destinada ao fundo comum do grupo.
        \nContemplação: A contemplação pode ocorrer de duas formas: por sorteio ou lance.
        \nSorteio: Mensalmente, é realizado um sorteio para definir quem será contemplado.
        \nLance: Se você quiser adiantar a sua contemplação, pode oferecer um lance, que é um valor adicional pago para antecipar a sua carta de crédito.
        \nUtilização da carta de crédito: Após ser contemplado, você poderá utilizar a carta de crédito para adquirir a motocicleta Yamaha de sua preferência em qualquer concessionária da marca.
        \n. Quais são as vantagens do Consórcio Yamaha?\n

        \nSem juros: Você não paga juros sobre o valor financiado, apenas as parcelas do consórcio.\n
        \nPlanejamento financeiro: O consórcio te ajuda a planejar a compra da sua moto, dividindo o pagamento em parcelas que cabem no seu bolso.
        \nFlexibilidade: Você pode escolher o valor da carta de crédito e o prazo do consórcio que melhor se adaptam às suas necessidades.
        \nDiversidade de modelos: Você pode escolher qualquer modelo de motocicleta Yamaha disponível no mercado.
        \nSegurança: O consórcio é uma modalidade de compra segura e regulamentada pelo Banco Central.
        \n. Quais são os documentos necessários para aderir ao consórcio?\n
        \nDocumento de identidade\n
        \nCPF\n
        \nComprovante de renda\n
        \nComprovante de residência\n
        \nOnde posso encontrar mais informações?\n
        \n. Para obter mais informações sobre o Consórcio Yamaha, você pode acessar o site oficial da Yamaha ou entrar em contato com uma concessionária da marca.\n
        \nEm resumo:\n
        \nO Consórcio Yamaha é uma excelente opção para quem deseja adquirir uma motocicleta Yamaha de forma planejada e sem pagar juros. Com o consórcio, você realiza o sonho de ter sua moto nova, com segurança e flexibilidade.''')