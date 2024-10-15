import pandas as pd
import streamlit as st

@st.cache_data
def load_database():
    df = pd.read_excel('data/db_dados.xlsx') 
    df['Ano'] = df['Data'].dt.year
    df['Mes'] = df['Data'].dt.month
    df['Data'] = df['Data'].astype(str)  # Converte o campo 'Data' para string
    return df

st.set_page_config(page_title="Gestão do Conhecimento", layout="wide")
st.session_state['df'] = load_database()
st.session_state['dimensao'] = [
    'Loja', 'Data', 'Ano', 'Mes', 'Vendedor', 'SKU', 'Produto', 'Tipo pagamento', 'Forma Pagamento', 'Quantidade de parcelas'
]
st.session_state['dimensao_tempo'] = ['Data','Ano','Mes']
st.session_state['medida'] = ['Qtd Vendida', 'Preço Unitário', 'Descontos','Acréscimos','Valor Total', 'Valor Desconto', 'Valor Acréscimos', 'Valor Total Compra', 'Valor Parcela']
st.session_state['agregador'] = ['sum', 'mean', 'count', 'min', 'max']
st.title('Gestão do Conhecimento')

pg = st.navigation(
    {
        "Introdução": [
            st.Page(page='introduction/tabela.py', title='Tabela', icon=':material/house:'),
            st.Page(page='introduction/cubo.py', title='Cubo', icon=':material/help:'),
            st.Page(page='introduction/dashboard.py', title='Dashboard', icon=':material/help:'),
            st.Page(page='introduction/visualizacao.py', title='Visualização', icon=':material/help:'),
        ],
        "Visualização": [
            st.Page(page='visualizacao/descritiva.py', title='Análise Descritiva',
                    icon=':material/house:'),
            st.Page(page='visualizacao/diagnostica.py', title='Análise Diagnóstica',
                    icon=':material/house:'),
            st.Page(page='visualizacao/preditiva.py', title='Análise Preditiva',
                    icon=':material/house:'),
            st.Page(page='visualizacao/prescritiva.py', title='Análise Prescritiva',
                    icon=':material/house:'),
        ]
    }
)
pg.run()

