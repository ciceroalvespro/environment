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

# Dados fictícios de exemplo (latitude e longitude)
data2 = {
    'Aeroporto': ['GRU', 'GIG', 'CGH', 'BSB', 'CNF', 'VCP'],  # Incluímos 'VCP' para Viracopos
    'Latitude': [-23.4253, -22.8126, -23.6261, -15.8697, -19.6336, -23.0074],  # Latitude de Viracopos
    'Longitude': [-46.4692, -43.2505, -46.6555, -47.9207, -43.9686, -47.1345]  # Longitude de Viracopos
}

df2 = pd.DataFrame(data2)

# Título do Dashboard
st.markdown("""
    <h1 style='text-align: center;'>Dashboard Básico</h1>
    """, unsafe_allow_html=True)

# Adicionando uma linha horizontal para dividir o conteúdo
st.markdown("---")

# Adicionando as métricas dentro da linha horizontal
#st.markdown("## Métricas")
col1, col2, col3, col4= st.columns(4)

# Adicionando as métricas em cada coluna
with col1:
    st.metric(label="Faturamento Bruto", value="R$ 100.450,45")

with col2:
    st.metric(label="Margem Líquida", value="16.3%")

with col3:
    st.metric(label="Margem Ebitda", value="18.30%")

with col4:
    st.metric(label="ROE", value="12.20%")

# Adicionando uma linha horizontal para dividir o conteúdo
st.markdown("---")

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
    # Criando o mapa com os aeroportos
    fig = px.scatter_geo(df2, lat='Latitude', lon='Longitude', hover_name='Aeroporto', scope='south america')

    # Configurações adicionais do layout do mapa
    fig.update_geos(projection_type="natural earth")
    fig.update_layout(title='Principais Aeroportos no Brasil')

    # Mostrando o mapa no Streamlit
    st.plotly_chart(fig, use_container_width=True)
   
    # Expander sobre o dashboard
    with st.expander('Sobre o Dashboard'):
        st.write('Este é um dashboard simples criado com Streamlit para demonstração.')



