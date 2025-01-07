import streamlit as st
import pandas as pd
from selenium import webdriver
import time


st.logo('images/icon_menu.png')
# st.sidebar.image('eli.png', caption='Eliane Ferreira')
st.subheader('👈 Selecione uma das opções no menu lateral', divider=True)
# st.toggle('ATIVAR')

def moto():
    motos = st.sidebar.radio('Modelos disponiveis', ['CROSSER 150', 'FACTOR 150', 'FZ 15 CONNECTED', 'FZ 25 CONNECTED',
                                                   'LANDER CONNECTED', 'MT 07', 'MT 09', 'NMAX 160 CONNECTED', 'NEOS', 'R 3 ABS','R 15 ABS', 'TRACER 900 GT', 'XMAX 250'], index=None)
    if motos == 'CROSSER 150':
        DATA_URL = (
            'https://www.yamaha-motor.com.br/file/v6985822204182688206/products/lateral-carenagem-todoterreno-crosserz-150-abs-30131-fx01-img-01-v01-desk.png')
        st.image(DATA_URL)
        st.markdown('A Yamaha Crosser 150 2025 é uma das opções trail da marca, juntamente com a Lander 250 2025. Apesar de outros modelos da linha da empresa terem ganhado mais novidade neste temporada, a Crosser rebeceu apenas algumas alterações, incluindo adequação do motor às regras ambientais e nova paleta de cores. No coração da Crosser 150 2025, está o motor monocilíndrico flex de 149 cc, agora ajustado para 11,7 cavalos a 7.250 rpm, uma redução de 0,5 cv em relação ao modelo anterior, que alcançava até 12,4 cv a 7.500 rpm. O torque, porém, permanece o mesmo, com 1,3 kgfm a 6.000 rpm. Esses ajustes visam reduzir emissões, alinhando o modelo às novas exigências ambientais.')
    elif motos == 'FACTOR 150':
        DATA_URL = ('https://mobilidade.estadao.com.br/wp-content/uploads/2024/12/Yamaha_FACTOR150_2025.jpg.webp')
        st.image(DATA_URL)
        st.markdown('''Yamaha Factor 150 2025: Uma nova geração da moto mais vendida do Brasil
            A Yamaha Factor 150 2025 chegou com novidades que prometem consolidar ainda mais seu lugar como uma das motocicletas mais populares do Brasil. A principal mudança está no visual, com um design mais robusto e moderno, que inclui um novo conjunto óptico com faróis de LED, proporcionando maior visibilidade e um visual mais atraente.
            \nPrincipais novidades:\n
            \nDesign: Linhas mais modernas e esportivas, com um novo painel e um spoiler sob o motor.\n
            \nIluminação: Faróis de LED, que oferecem maior eficiência energética e melhor visibilidade.\n
            \nMotor: O motor monocilíndrico flex de 150 cc foi atualizado para atender às novas normas de emissões, mas teve uma pequena redução de potência.\n
            \nTanque: O tanque de combustível agora tem capacidade para 15,4 litros, garantindo maior autonomia.\n
            \nCores e versões: A Factor 150 2025 está disponível em diversas cores e versões, com opções para todos os gostos.\n
            \nO que mais mudou:\n
            \nPeso: A moto ficou levemente mais pesada em relação ao modelo anterior.\n
            \nSuspensão: A suspensão foi ajustada para oferecer maior conforto e estabilidade.\n
            \nFreios: Os freios continuam sendo a disco na dianteira e tambor na traseira, mas com ajustes para melhorar o desempenho.\n
            \nPor que a Factor 150 é tão popular?\n
            \nA Yamaha Factor 150 é conhecida por sua economia de combustível, baixo custo de manutenção, durabilidade e facilidade de pilotagem. Além disso, a moto é muito versátil, podendo ser utilizada tanto no dia a dia quanto em pequenas viagens.\n
            \nPara quem a Factor 150 é indicada?\n
            \nA Factor 150 é uma excelente opção para quem busca uma moto econômica, prática e confiável para o dia a dia. A moto também é uma boa escolha para iniciantes, graças à sua posição de pilotagem confortável e fácil manobrabilidade.\n
            \nEm resumo:\n
            \nA Yamaha Factor 150 2025 é uma excelente opção para quem busca uma motocicleta versátil, econômica e com um design moderno. Com suas diversas melhorias, a moto promete continuar sendo um sucesso de vendas no mercado brasileiro.''')
    elif motos == 'FZ 15 CONNECTED':
        DATA_URL = (
            'https://www.yamaha-motor.com.br/file/v267926292075367768/products/lateral-urbano-fazer-fz15-150-abs-30128-fx01-img-01-v02-desk.png')
        st.image(DATA_URL)
        st.markdown('''A Yamaha FZ15 2025 chegou ao mercado com um visual completamente repaginado, mantendo a essência esportiva que a caracteriza. A moto recebeu um novo conjunto óptico com faróis de LED, além de um design mais agressivo e moderno.\n
            \nPrincipais novidades:\n
            \nDesign: Linhas mais esportivas e aerodinâmicas, com um novo painel e um spoiler sob o motor.\n
            \nIluminação: Faróis de LED, que oferecem maior eficiência energética e melhor visibilidade.\n
            \nMotor: O motor monocilíndrico flex de 150 cc foi mantido, mas recebeu ajustes para atender às novas normas de emissões.\n
            \nSuspensão: A suspensão foi ajustada para oferecer maior conforto e esportividade.\n
            \nFreios: A FZ15 continua com freio a disco nas duas rodas, com ABS na dianteira, proporcionando maior segurança nas frenagens.\n
            \nCores e versões: A moto está disponível em diversas cores e versões, com opções para todos os gostos.\n
            \nO que mais mudou:\n
            \nPeso: A moto ficou levemente mais pesada em relação ao modelo anterior.\n
            \nErgonomia: A posição de pilotagem foi ligeiramente ajustada para oferecer maior conforto em longas distâncias.\n
            \nPor que escolher a FZ15?\n
            \nA Yamaha FZ15 é uma excelente opção para quem busca uma moto esportiva de entrada com um design moderno e um bom desempenho. A moto é ágil, divertida de pilotar e oferece um bom custo-benefício.\n
            \nPara quem a FZ15 é indicada?\n
            \nA FZ15 é indicada para pilotos iniciantes que buscam uma moto esportiva para o dia a dia ou para quem procura uma moto para curtir passeios mais esportivos nos finais de semana.\n
            \nEm resumo:\n
            \nA Yamaha FZ15 2025 é uma excelente opção para quem busca uma moto esportiva de entrada com um visual moderno e um bom desempenho. Com suas diversas melhorias, a moto promete continuar sendo um sucesso de vendas no mercado brasileiro.''')
    elif motos == 'FZ 25 CONNECTED':
        DATA_URL = ('https://www.yamaha-motor.com.br/ccstore/v1/images/?source=/file/v7556127250904524801/products/Banner%20Home%20-%20FZ25%20-%20Desktop%201.png&height=1080&width=1920&quality=1.0')
        st.image(DATA_URL)
        st.markdown('''A Yamaha FZ25 Connected 2025 chegou ao mercado trazendo uma série de novidades que a tornam ainda mais atraente para os motociclistas brasileiros. Com um design moderno e esportivo, a FZ25 Connected oferece um conjunto completo de recursos tecnológicos e um desempenho emocionante.
            \nDesign e Estilo\n
            \nA FZ25 Connected 2025 exibe um visual completamente renovado, com linhas mais agressivas e aerodinâmicas. O novo conjunto óptico com faróis de LED full-LED confere à moto um visual moderno e elegante.\n
            \nPainel Digital e Conectividade\n
            \nUma das principais novidades da FZ25 Connected é o painel de instrumentos LCD totalmente digital e com design "blackout", que oferece uma visualização clara e intuitiva das informações. Além disso, a moto conta com conectividade Bluetooth através do aplicativo Yamaha Motorcycle Connect (Y-Connect), permitindo que o piloto receba notificações de chamadas, mensagens e acompanhe dados da motocicleta, como consumo médio e distância percorrida.\n
            \nMotor e Performance\n
            \nA FZ25 Connected é equipada com um motor monocilíndrico de 249 cm³, refrigerado a ar, que oferece um bom equilíbrio entre desempenho e economia de combustível. O motor foi atualizado para atender às normas de emissões mais recentes, proporcionando uma pilotagem suave e agradável.\n
            \nCiclística e Suspensão\n
            \nA ciclística da FZ25 Connected foi projetada para oferecer um manuseio preciso e ágil, ideal para o uso urbano e em estradas. A suspensão dianteira conta com garfo telescópico convencional e a traseira com monoamortecedores, ambos ajustáveis na pré-carga.\n
            \nFreios\n
            \nA segurança é garantida pelos freios a disco nas duas rodas, com sistema ABS (Anti-lock Brake System) na roda dianteira, proporcionando maior controle e eficiência nas frenagens.\n
            \nCores e Versões\n
            \nA FZ25 Connected está disponível em diversas opções de cores, permitindo que cada piloto escolha a que mais combina com seu estilo.
            \nPrincipais Características:\n
            \nDesign moderno e esportivo\n
            \nPainel digital LCD com conectividade Bluetooth\n
            \nMotor monocilíndrico de 249 cm³\n
            \nFreios a disco com ABS na roda dianteira\n
            \nSuspensão ajustável\n
            \nDiversas opções de cores\n
            \nConclusão\n
            \nA Yamaha FZ25 Connected 2025 é uma excelente opção para quem busca uma motocicleta esportiva, versátil e com um bom custo-benefício. Com seu design moderno, tecnologia embarcada e desempenho confiável, a FZ25 Connected conquistará os corações dos motociclistas mais exigentes.''')
    elif motos == 'LANDER CONNECTED':
        DATA_URL = ('https://www.yamaha-motor.com.br/ccstore/v1/images/?source=/file/v4248815581081380366/products/LANDER%201920x1080%20-%20Banner%20Home%20-%20Desktop%20(2).png&height=1080&width=1920&quality=1.0')
        st.image(DATA_URL)
        st.markdown('''Yamaha Lander Connected 2025: Aventura Conectada
            \nA Yamaha Lander Connected 2025 representa um novo patamar para as motocicletas trail, combinando o espírito aventureiro com a mais recente tecnologia. Essa moto é perfeita para quem busca uma experiência de pilotagem emocionante tanto em ambientes urbanos quanto em trilhas off-road.
            \nDesign Robusto e Moderno\n
            \nA Lander Connected possui um design marcante, com linhas robustas e agressivas que transmitem a sensação de aventura. O farol dianteiro em LED confere um visual moderno e garante excelente iluminação, enquanto o painel de instrumentos digital oferece todas as informações necessárias para o piloto de forma clara e intuitiva.
            \nAbre uma nova janela\n
            \nMotor Potente e Econômico\n
            \nEquipada com um motor monocilíndrico de 250cc, a Lander Connected oferece um desempenho equilibrado, com boa potência para encarar as mais diversas situações e um consumo de combustível eficiente. O motor é robusto e confiável, garantindo longas jornadas com tranquilidade.
            \nConectividade Inteligente\n
            \nA grande novidade da Lander Connected é a conectividade com smartphones através de um aplicativo dedicado. Essa função permite que o piloto acesse diversas informações, como:
            \nNavegação: Utilize o GPS do seu celular para encontrar o caminho mais curto e seguro.
            \nInformações da moto: Monitore o consumo de combustível, autonomia, histórico de viagens e outras informações relevantes.
            \nNotificações: Receba notificações de chamadas, mensagens e redes sociais diretamente no painel da moto.
            \nLocalização: Em caso de roubo, você pode localizar sua moto através do aplicativo.
            \nSuspensão e Freios
            \nA suspensão da Lander Connected é projetada para oferecer conforto e segurança tanto em estradas asfaltadas quanto em trilhas off-road. A dianteira conta com garfo telescópico e a traseira com monoamortecedor, ambos com ajustes para diferentes tipos de terreno. Os freios a disco, com sistema ABS, garantem frenagens seguras e eficientes em qualquer situação.
            \nPneus e Rodas
            \nA Lander Connected vem equipada com pneus off-road de alta performance, que oferecem excelente tração em diversos tipos de terreno. As rodas raiadas contribuem para a robustez da moto e garantem maior durabilidade.
            \nConforto e Ergonomia
            \nA posição de pilotagem da Lander Connected é confortável e ergonômica, permitindo longas jornadas sem fadiga. O assento é largo e macio, proporcionando maior conforto ao piloto e ao garupa.
            \nEm resumo, a Yamaha Lander Connected 2025 é uma moto completa e versátil, ideal para quem busca aventura e tecnologia. Com seu design moderno, motor potente, conectividade inteligente e suspensões robustas, a Lander Connected é a companheira perfeita para suas expedições.''')
    elif motos == 'MT 03':
        DATA_URL = ('https://www.yamaha-motor.com.br/file/v8175103964778769023/products/lateral-mtseries-mt03-321-abs-30118-fx01-img-01-v02-desktop.jpg')
        st.image(DATA_URL)
        st.markdown('''O conceito “Touro de Aço” foi a inspiração da nova MT-03.
            \nA Líder da categoria possui freios ABS de série nas duas rodas em sua nova versão. Com seu motor bicilíndrico de 321 cc e potência de 42 cv, essa motocicleta é a melhor opção para quem deseja uma moto Leve e Ágil na cidade e um mix de Perfomance e Estabilidade que surpreendem nas estradas.
            \nSeu Desing é único, característico da Série MT. Sua luz de posição em LED mantém toda a sua agressividade e modernidade à noite. Além disso ela conta com 4 Anos de Garantia e Revisão Preço Fixo. Venha conhecer uma de perto!''')
    elif motos == 'MT 07':
        DATA_URL = (
            'https://www.yamaha-motor.com.br/file/v972548829457220531/products/lateral-mtseries-mt07-321-abs-30119-fx01-img-01-v02-desktop.jpg')
        st.image(DATA_URL)
        st.markdown('''A Yamaha MT 07 chegou se destacando primeiramente pelo seu design moderno e agressivo, mas também pela performance. A MT-07 exibe, desde sua primeira geração, ainda presente por aqui, a força e a harmonia com seus dois cilindros. Um motor compacto e potente, mas de alto desempenho. Seu motor de 689 cc tem duplo comando de válvulas no cabeçote (DOHC) e quatro válvulas por cilindro e virabrequim Crossplane. O suficiente para entregar 74,8 cv a 9.000 rpm e seu torque máximo é 6,9 kgf.m a 6.500 rpm - junto do câmbio de 6 velocidades. O conjunto tem ainda na suspensão dianteira garfo do tipo convencional, sem regulagem, com 130 mm de curso. Na traseira está o sistema Monocross com link, que melhora a progressividade e oferece os mesmos 130 mm de curso. O tanque é de 14 litros, feito de chapa de aço, mas com uma cobertura de plástico para efeitos de estética. No que se refere ao consumo, a moto faz médias de 21 km/litro. Já a velocidade estimada pela Yamaha para a MT é de 230 Km. Já o painel tinha display em LCD, iluminado por LEDs e totalmente digital. Enquanto a iluminação era toda em lâmpadas halógenas. O peso total em ordem de marcha ficava em 179 kg na versão standard e 182 kg na versão com ABS. Falando nisso, o sistema de freios da MT 07 - tanto na versão STD quando a ABS - conta com dois discos flutuantes de 282 mm e 4 pistões hidráulicos em cada pinça na roda dianteira e um disco de 245 mm na traseira com pinça de um pistão. Em 2018, a MT 07 ganhou um farol maior e mais largo, além de tanque de combustível redesenhado. Já a partir de 2019 a moto chegava apenas na versão ABS. Lembrando que em seu lançamento no mercado, em 2015, veio para rivalizar com as concorrentes Honda CB 500F, além das Kawasaki ER6-n, BMW F 800R e Triumph Street Triple.''')
    elif motos == 'MT 09':
        DATA_URL = (
            'https://www.yamaha-motor.com.br/file/v4092077966796018393/products/lateral-mtseries-mt09-321-abs-30120-fx01-img-01-v01-desktop.jpg')
        st.image(DATA_URL)
        st.markdown('A Yamaha MT-09 traz um conceito radical em design e performance. O motor de 3 cilindros é capaz de gerar um torque brutal de 8,92 kgf. m. Esse modelo é leve, com peso de apenas 193 quilos, que dividido pelos 115 cv do motor, gera ótima relação peso e potência de 1,67 quilo por cv.')
    elif motos == 'NMAX 160 CONNECTED':
        DATA_URL = ('https://www.yamaha-motor.com.br/file/v6562319903931981071/products/3-4-scooter-nmax-connected-160-abs-30076-fx01-img-01-v02-desktop.jpg')
        st.image(DATA_URL)
        st.markdown('''A NMAX Connected 160 ABS SE vem equipada com controle de tração, que associado aos freios ABS nas duas rodas, proporciona melhor controle da pilotagem em pisos de baixa aderência. Sua suspensão traseira traz dois níveis de ajuste manual para escolher a posição mais adequada, suave ou firme. Já os novos pneus Pirelli Diablo Scooter, têm longa durabilidade e excelente aderência. A moto de 160 cc e 15,4 cv de potência segue com tecnologias exclusivas na categoria, como o cilindro em DiASil, que melhora a eficiência do motor, e o comando de válvulas variável (VVA), que garante maior desempenho e menor consumo de combustível. Além do sistema Stop & Start, que desliga o motor, religando automaticamente ao acelerar, reduzindo o consumo de combustível e emissão de poluentes.''')
    elif motos == 'NEOS':
        with st.spinner('carregando!'):
            time.sleep(2)
        DATA_URL = ('https://www.yamaha-motor.com.br/ccstore/v1/images/?source=/file/v8478437528813682099/products/NEOS%20lateral-scooter-neos-eletrica-30130-fx01-img-01-v01-desk%201.png&height=1080&width=1920&quality=1.0')
        st.image(DATA_URL)
        st.markdown('''Yamaha Neo's 2025: A revolução elétrica sobre duas rodas
            \nA Yamaha Neo's 2025 marca um novo capítulo na história da mobilidade urbana, sendo a primeira motocicleta elétrica da marca japonesa a ser produzida no Brasil. Com design moderno e futurista, a Neo's oferece uma experiência de condução suave, silenciosa e ecologicamente correta.
            \nDesign e Estilo:
            \nA Neo's possui um design único e atraente, com linhas fluidas e detalhes que remetem ao futuro. Os faróis dianteiros em LED conferem à moto um visual moderno e marcante, enquanto a carenagem envolvente proporciona proteção contra o vento e a chuva.
            \nMotorização:
            \nEquipada com um motor elétrico, a Neo's oferece aceleração instantânea e suave, além de zero emissões de poluentes. A autonomia da bateria varia de acordo com o modo de condução e as condições do trânsito, podendo chegar até 80 km.
            \nTecnologia:\n
            \nA Neo's vem equipada com diversas tecnologias que facilitam a vida do piloto, como:
            \nPainel de instrumentos digital: Apresenta informações claras e intuitivas sobre a velocidade, autonomia, nível da bateria e outros dados importantes.
            \nYamaha Neo's 2025 digital dashboard
            \nConectividade: Permite conectar o smartphone ao veículo através de um aplicativo, proporcionando diversas funcionalidades, como navegação e controle de algumas funções da moto.
            \nModos de condução: A Neo's oferece diferentes modos de condução, permitindo ajustar a performance da moto de acordo com as suas necessidades.
            \nConforto e Segurança:
            \nA Neo's oferece um excelente conforto ao pilotar, com assento macio e posição de pilotagem relaxada. Além disso, a moto conta com freios a disco nas duas rodas, proporcionando maior segurança nas frenagens.
            \nPrática e versátil:
            \nA Neo's é perfeita para o dia a dia na cidade, sendo fácil de manobrar e estacionamento. Seu baú sob o assento oferece espaço suficiente para guardar um capacete e outros objetos pessoais.
            \nEm resumo:
            \nA Yamaha Neo's 2025 é uma excelente opção para quem busca um meio de transporte ecologicamente correto, prático e com design moderno. Com sua tecnologia avançada e baixo custo de manutenção, a Neo's é a escolha perfeita para quem deseja se locomover pela cidade de forma sustentável e divertida.
            \nPontos fortes da Neo's:
            \nDesign moderno e futurista
            \nMotor elétrico silencioso e eficiente
            \nTecnologia embarcada
            \nConforto e praticidade
            \nBaixo custo de manutenção
            \nPontos a considerar:
            \nAutonomia limitada em comparação com motos a combustão
            \nTempo de recarga da bateria
            \nDisponibilidade de pontos de recarga
            \nSe você está buscando uma moto elétrica para o dia a dia, a Yamaha Neo's 2025 é uma excelente opção a ser considerada.''')
    elif motos == 'R 3 ABS':
        DATA_URL = ('https://www.yamaha-motor.com.br/file/v8053955512855454416/general/premiacao-supersport-r3-321-abs-30109-fx08-img-01-v03.jpg')
        st.image(DATA_URL)
        st.markdown('''Dentro do mais puro conceito racing, a Yamaha YZF R3 ABS foi feita para quem gosta de esportividade. Muita coisa nela lembra as motos de corrida, como os semiguidões baixos, a carenagem integral e o banco bipartido separado do garupa.
            \nPelas suas características claramente esportivas, não é tão simples pilotá-la no uso urbano, principalmente pelo pouco esterçamento dos semiguidões, assim como pelos espelhos retrovisores colocados na carenagem.
            \nPor outro lado, ela é baixa (780 mm) e leve (170 kg), o que facilita a condução de quem tem menos de 1,70 m. ''')
    elif motos == 'R 15 ABS':
        DATA_URL = ('https://www.yamaha-motor.com.br/file/v8455595307359693098/products/lateral-supersport-r15-abs-30133-fx01-img-01-v02-desktop.jpg')
        st.image(DATA_URL)
        st.markdown('''A R15 ABS foi eleita a Melhor Moto do Brasil na categoria City, na premiação concedida em 2024 pela Revista Motociclismo.
            \nEsse reconhecimento é fruto da confiança e do voto de consumidores apaixonados, que inspiram a YAMAHA a superar desafios continuamente.
            \nSeu design foi inspirado nas superesportivas de maior cilindrada da Yamaha. Com faróis em LED, a carenagem dianteira traz uma entrada de ar em forma de M, semelhante à YZR-M1, moto da marca na MotoGP. Lanterna em LED e painel totalmente digital completam os diferenciais da mini esportiva japonesa.''')
    elif motos == 'TRACER 900 GT':
        DATA_URL = ('https://www.yamaha-motor.com.br/file/v7957540279432677006/products/carenagem-esquerda-sporttouring-tracer-900-30122-fx01-img-01-v01-desk.jpg')
        st.image(DATA_URL)
        st.markdown('''A Nova Tracer 900 GT veio totalmente reformulada: arrojada, imponente, sofisticada e esportiva.
            \nEquipada com itens de tecnologia como Piloto Automático, Controle de Tração, Sistema Quick Shift, D-Mode, Embreagem Assistida e Deslizante. Essa moto, que se destaca nas estradas e viagens a longa distância, agora conta com um Guidão mais estreito, um amplo Para-Brisa, Assentos mais confortáveis e Pedaleiras e Alças do Garupa reposicionadas, novas Suspensões Dianteira e Traseira e muito mais! Esse modelo é o mais leve e potente da categoria, e ainda conta com Farol Duplo e Lanterna Traseira em LED e seu Painel Completo em TFT.
            \nSe aventure com a Nova Tracer 900 GT!''')
    elif motos == 'XMAX 250':
        DATA_URL = (
            'https://www.yamaha-motor.com.br/file/v8034493036967814121/products/lateral-scooter-xmax-160-abs-30123-fx01-img-01-v01-desk.png')
        st.image(DATA_URL)
        st.markdown('''A nova XMAX ABS Connected traz ainda mais sofisticação para o dia a dia. O novo conjunto óptico full LED forma um elegante 'X' quando aceso tanto no farol quanto na lanterna, elevando o estilo e reforçando a presença da sua scooter. Traz conectividade Bluetooth com o aplicativo Yamaha Motorcycle Connect, o Y-Connect, com ele é possível gerenciar indicadores de utilização e performance e visualizar pelo painel mensagens e ligações recebidas. A XMAX ABS Connected combina inovação, economia e um visual marcante.''')

moto()
