import streamlit as st

# Adicionando CSS para estilização
st.markdown("""
<style>
    .title {
        color: #333333;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    .css-14xro0k {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# Função para alterar o tema com base na seleção do usuário
def set_theme(theme):
    if theme == 'Claro':
        theme_bg = 'light'
        theme_text = '#333333'
    elif theme == 'Escuro':
        theme_bg = 'dark'
        theme_text = '#ffffff'
    else:
        theme_bg = 'light'
        theme_text = '#333333'
    return theme_bg, theme_text

# Título da página
st.title('Dashboard')

# Opções de tema
theme_options = ['Claro', 'Escuro', 'Padrão']
selected_theme = st.sidebar.selectbox('Escolha o Tema', theme_options)

# Setando o tema
theme_bg, theme_text = set_theme(selected_theme)
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {theme_bg} !important;
            color: {theme_text};
        }}
    </style>
""", unsafe_allow_html=True)

# Sidebar com filtros
st.sidebar.title('Filtros')

# Selectbox para os projetos
projeto = st.sidebar.selectbox('Projetos', ['Projeto A', 'Projeto B', 'Projeto C'])

# Selectbox para os anos
ano = st.sidebar.selectbox('Ano', ['2022', '2023', '2024'])

# Layout com 3 colunas
col1, col2, col3 = st.columns(3)

# KPIs
with col1:
    st.metric(label='KPI 1', value=100)

with col2:
    st.metric(label='KPI 2', value=200)

with col3:
    st.metric(label='KPI 3', value=300)

# Gráfico de barras na horizontal
with col1:
    st.write('## Gráfico de Barras')
    st.bar_chart({'Projeto A': [10, 20, 30],
                  'Projeto B': [15, 25, 35],
                  'Projeto C': [20, 30, 40]})

# Mapa de calor
with col2:
    st.write('## Mapa de Calor')
    st.write('Aqui vai o mapa de calor...')

# Cartão com valor total
with col3:
    st.write('## Valor Total')
    st.write('O valor total é 600')

    # Expander sobre o dashboard
    with st.expander('Sobre o Dashboard'):
        st.write('Este é um dashboard simples criado com Streamlit para demonstração.')

