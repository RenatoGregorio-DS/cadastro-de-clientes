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
    # .strip() garante que " " não seja aceito como dado
        if nome.strip() and email.strip() and telefone.strip():
        
        # Chamando as funções que você colocou no banco
            if not banco.validar_email(email):
                st.error("❌ E-mail inválido! Use o formato: nome@email.com")
            elif not banco.validar_telefone(telefone):
                st.error("❌ Telefone inválido! Use o formato: (11) 99999-9999")
        else:
            try:
                banco.adicionar_cliente(nome, email, telefone)
                st.success(f"✅ {nome} cadastrado com sucesso!")
                # Isso "reseta" a interface para o próximo paciente
                st.rerun() 
            except:
                st.error("⚠️ Este e-mail já está cadastrado!")
    else:
        st.warning("⚠️ Atenção: Todos os campos são obrigatórios.")

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
