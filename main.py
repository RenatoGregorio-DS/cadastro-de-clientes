import streamlit as st
from banco import banco

def main():
    st.title("Cadastro de Clientes")
    st.write("Bem-vindo ao sistema de cadastro de clientes!")

    # cadastro de clientes
    nome = st.text_input("Nome do Cliente")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")

    # Adicionar clientes 
    if st.button("Novo cliente"):
        try:
            if nome and email and telefone: # Verifica se não estão vazios
                banco.adicionar_cliente(nome, email, telefone)
                st.success(f"Cliente {nome} cadastrado com sucesso!")
            else:
                st.error("Por favor, preencha todos os campos antes de salvar.")
        except Exception as e:
            st.error(f"Erro ao cadastrar cliente: {e}")

    st.divider()

    # 3. Listar clientes pega dados presente no banco
    if st.button("Listar Clientes"):
        dados = banco.listar_clientes()
        if dados:
            st.table(dados) 
        else:
            st.info("O banco de dados está vazio.")
    st.divider()
   # Removido o 'if' antes do 'with'
    with st.expander("🗑️ Excluir Cliente"):
        cliente_id = st.number_input("ID do Cliente a Excluir", min_value=1, step=1)

        if st.button("Confirmar Exclusão definitiva"):
            try:
                # Mudado de 'db' para 'banco' (conforme sua importação na linha 2)
                banco.excluir_cliente(cliente_id) 
                st.success(f"✅ Cliente com ID {cliente_id} excluído com sucesso!")
                
                # Opcional: st.rerun() para atualizar a tabela na hora
            except Exception as e:
                st.error(f"❌ Erro ao excluir cliente: {e}")

if __name__ == "__main__":
    main()
