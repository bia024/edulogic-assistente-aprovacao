import streamlit as st
import pandas as pd

# 1. CONSTANTES DE REGRA DE NEGÓCIO
MEDIA_APROVACAO = 7.0
MEDIA_REPROVACAO = 5.0
FREQUENCIA_MINIMA = 75

# 2. LÓGICA DO MOTOR DE DECISÃO
def calcular_situacao(notas, frequencia):
    """
    Processa a lógica de aprovação baseada nas regras de negócio da EduLogic.
    """
    if not notas:
        return 0.0, "Reprovado"
    
    media = sum(notas) / len(notas)
    
    # Validação de Frequência primeiro (Critério eliminatório)
    if frequencia < FREQUENCIA_MINIMA:
        return media, "Reprovado (Frequência)"
    
    # Validação de Nota
    if media >= MEDIA_APROVACAO:
        return media, "Aprovado"
    elif media >= MEDIA_REPROVACAO:
        return media, "Recuperação"
    else:
        return media, "Reprovado (Nota)"

# 3. INTERFACE STREAMLIT
def main():
    st.set_page_config(page_title="EduLogic Assistente", page_icon="🎓")
    
    st.title("🎓 EduLogic - Assistente de Aprovação")
    st.subheader("Cálculo Automatizado de Situação Acadêmica")
    st.markdown("---")

    # Entrada do Nome do Aluno (fora do form para persistência visual rápida)
    nome_aluno = st.text_input("Nome Completo do Estudante", placeholder="Ex: Bianca Caetano")

    # Formulário de Entrada de Dados
    with st.form("form_notas"):
        col1, col2 = st.columns(2)
        
        with col1:
            n1 = st.number_input("Nota Avaliação 1", min_value=0.0, max_value=10.0, step=0.1)
            n2 = st.number_input("Nota Avaliação 2", min_value=0.0, max_value=10.0, step=0.1)
            
        with col2:
            frequencia = st.slider("Frequência do Aluno (%)", 0, 100, 100)
            
        submit = st.form_submit_button("Gerar Resultado Final")

    # 4. PROCESSAMENTO E EXIBIÇÃO DO RESULTADO
    if submit:
        if nome_aluno.strip() == "":
            st.warning("⚠️ Por favor, insira o nome do aluno antes de calcular.")
        else:
            media_final, resultado = calcular_situacao([n1, n2], frequencia)
            
            st.divider()
            st.subheader(f"Relatório de Desempenho: {nome_aluno}")
            
            # Métricas em Colunas
            c1, c2 = st.columns(2)
            c1.metric("Média Final", f"{media_final:.1f}")
            c2.metric("Frequência", f"{frequencia}%")
            
            # Alertas de Situação
            if "Aprovado" in resultado:
                st.success(f"O(A) estudante **{nome_aluno}** está **{resultado}**.")
            elif "Recuperação" in resultado:
                st.warning(f"O(A) estudante **{nome_aluno}** está em **{resultado}**.")
            else:
                st.error(f"O(A) estudante **{nome_aluno}** está **{resultado}**.")

            # 5. FUNCIONALIDADE DE EXPORTAÇÃO (CSV)
            dados_exportacao = {
                "Estudante": [nome_aluno],
                "N1": [n1],
                "N2": [n2],
                "Média Final": [round(media_final, 2)],
                "Frequência (%)": [frequencia],
                "Situação": [resultado]
            }
            
            df = pd.DataFrame(dados_exportacao)
            csv = df.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="📥 Baixar Relatório (CSV)",
                data=csv,
                file_name=f"resultado_{nome_aluno.replace(' ', '_').lower()}.csv",
                mime="text/csv",
            )

if __name__ == "__main__":
    main()