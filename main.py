import plotly.express as px
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Dados de exemplo
data = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [30, 20, 40, 10]
}

df = pd.DataFrame(data)

# Título do Dashboard
#st.title('Meu Dashboard Básico')
st.markdown("""
    <h1 style='text-align: center;'>Meu Dashboard Básico</h1>
    """, unsafe_allow_html=True)

# Adicionando uma linha horizontal para dividir o conteúdo
st.markdown("---")

# Adicionando as métricas dentro da linha horizontal
#st.markdown("## Métricas")
col1, col2, col3, col4 = st.columns(4)

# Adicionando as métricas em cada coluna
with col1:
    st.metric(label="Métrica 1", value=100)

with col2:
    st.metric(label="Métrica 2", value=200)

with col3:
    st.metric(label="Métrica 3", value=300)

# Adicionando gráficos abaixo da linha horizontal

col1, col2, col3 = st.columns(3)

with col1:
    fig = px.pie(df, values='Valores', names='Categoria', title='Gráfico de Pizza')

    # Mostrando o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(df, x='Categoria', y='Valores', title='Gráfico de Barras')

    # Mostrando o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.header('Gráfico 3')
    # Adicione o código para o terceiro gráfico aqui
    # Expander sobre o dashboard
    with st.expander('Sobre o Dashboard'):
        st.write('Este é um dashboard simples criado com Streamlit para demonstração.')



