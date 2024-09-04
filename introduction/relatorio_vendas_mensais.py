import pandas as pd
import streamlit as st

class RelatorioVendasMensais:
    def __init__(self, data):
        self.data = data

    def processar_dados(self):
    #    st.write("Colunas do DataFrame:", self.data.columns)

        monthly_sales = self.data.groupby(['Ano', 'Mes']) \
            .agg(total_vendas=('Valor Total', 'sum'),
                 numero_transacoes=('Valor Total', 'count')).reset_index()
        return monthly_sales

    def exibir_resultado(self):
        df = self.processar_dados()
        st.write("Relatório de Vendas Mensais")
        st.dataframe(df)
    #    st.write("Colunas do DataFrame para gráfico:", df.columns)
        df.set_index(['Ano', 'Mes'], inplace=True)
        st.line_chart(df['total_vendas'])

# Uso em Streamlit
df = st.session_state['df']
relatorio = RelatorioVendasMensais(df)
relatorio.exibir_resultado()
