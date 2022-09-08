## Primeiro, preciso importar as bibliotecas que irão me ajudar no desenvolvimento.
## O pandas, irá me auxiliar na tabela que irá ler e estruturar os dados e o streamlit irá montar a aplicação web.
    ##importando a bibliteca panda e nomeando com pd.
import pandas as pd
    ##importando a biblioteca streamlit
import streamlit as st


    ## Atribuindo a variável df e pedindo para o pandas ler os dados.

    
df = pd.read_csv('covid-variants.csv')

##Agora preciso apresentar os dados para as variaveis que irei apresentar na aplicação, no caso PAIS e VARIANTES, o usuário poderá escolher entre elas, exemplo: Variante "A" no pais "B".
    ## Para apresentar os dados, transformo o aglomerado em uma lista e solicito apenas dados unicos, pois a muitos dados replicados.
paises = list(df['location'].unique())
variants = list(df['variant'].unique())

tipo = 'Casos diários'
titulo = tipo + ' para ' 

##Por se tratar de dados que se trata de número de infectados por data, preciso tratar o dado para que fique de forma correta na hora de expo-los.
    ## Para tratar a data devo orientar a biblioteca pandas a formatar a data em y-m-d.
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
##Feito isso, posso começar a estruturar o aplicação web, o streamlit.
    ##Começo com o os selects que irão alternar entre pais e variante, preciso testar para ver se só de adicionar mais um item na list ele irá somar. Não ele não soma.
pais = st.sidebar.selectbox('Escolha o país:', ['Todos os países'] + paises)
variante = st.sidebar.selectbox('Selecione a variante', ['Todas as variantes'] + variants )
    ##Precisa fazer uma somatória de todos os dados.
if(pais != 'Todos os países'):
    st.text('Resultados de ' + pais) ##Dando a direção do pais.
    df = df[df['location']== pais] ##mostrando só os resultados do pais escolhido, selecionando o grupo de linha na qual o pais escolhido esta inserido
    titulo = titulo + pais
else:
    st.header('Resultados de todos os paises' ) ##verificar a necessidade do else

if(variante !=  'Todas as variantes'):
    st.text('Mostrando dados para a variante ' + variante) ##Dando a direção do pais.
    df = df[df['variant'] == variante] ##mostrando só os resultados do pais escolhido, selecionando o grupo de linha na qual a variante escolhido esta inserida.
    titulo = titulo + ' (variante : ' + variante + ')' 
else:
    st.text('Resultados de todas as variantes' ) ##verificar a necessidade do else
    titulo = titulo + '(todas as variantes)'
    
    ##Agora preciso somar todas os valores da linha de datas para apresentar, exemplo somar todos os casos para o dia xx-xx-xx
dfSomaPorData = df.groupby(by = ['date']).sum()

##Fiz todo o tratamento dos datos e condicionamentos acima, agora preciso importar a biblioteca de gráficos plotly para apresentar o grafico na aplicação.
    ##importando a bibliteca plotly e nomeando com px.
import plotly.express as px

fig = px.line(dfSomaPorData, x=dfSomaPorData.index, y='num_sequences')
fig.update_layout(title='Dados de infecções do covid-19' )
st.plotly_chart(fig, use_container_width=True)
