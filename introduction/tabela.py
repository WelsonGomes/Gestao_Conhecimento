import streamlit as st

st.title('Tabela')
st.dataframe(
    st.session_state['df'],
    hide_index=True,
    use_container_width=True,
    column_config={
        'Data': st.column_config.DateColumn(label='Data do Pedido'),
        'Preço Unitário': st.column_config.NumberColumn(label='Valor Unitário', format='R$ %.2f'),
        'Valor Total': st.column_config.NumberColumn(label='Valor Bruto', format='R$ %.2f'),
        'Valor Desconto': st.column_config.NumberColumn(label='Desconto', format='R$ %.2f'),
        'Valor Acréscimos': st.column_config.NumberColumn(label='Acréscimos', format='R$ %.2f'),
        'Valor Total Compra': st.column_config.NumberColumn(label='Valor Líquido', format='R$ %.2f'),
        'Valor Parcela': st.column_config.NumberColumn(label='Valor Parcela', format='R$ %.2f'),
        'Descontos': st.column_config.NumberColumn(label='Descontos (%)',format='10%%'),
        'Acréscimos': st.column_config.NumberColumn(label='Descontos (%)',format='%.2f%%')
    }
)
