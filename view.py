import streamlit as st

def main():
    from dao import ItemDAO
    from controller import ItemController

    dao = ItemDAO()
    controller = ItemController(dao)

    st.title('Cadastro de Itens')

    with st.form('form_item'):
        descricao = st.text_input('Nome do Item')
        quantidade = st.number_input('Quantidade', min_value=1, step=1)
        submitted = st.form_submit_button('Adicionar Item')

        if submitted:
            if descricao:
                controller.criarItem(descricao, quantidade)
                st.success('Item adicionado com sucesso!')
            else:
                st.error('A descrição é obrigatória!')

    st.subheader('Itens Cadastrados')
    itens = controller.obterTodosOsItens()
    for item in itens:
        st.write(f'ID: {item.id} | Nome do Item: {item.descricao} | Quantidade: {item.quantidade}')

if __name__ == '__main__':
    main()
