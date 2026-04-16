# 🎓 EduLogic - Assistente de Aprovação

---

## Sobre o Projeto
O **EduLogic** surgiu como uma solução prática para um desafio comum no ambiente acadêmico: a gestão precisa e rápida de notas e frequências. Desenvolvido como parte das atividades curriculares da **Uniasselvi**, este assistente automatiza o cálculo da situação final de alunos, eliminando erros manuais e oferecendo um feedback visual imediato.

### O Desafio Lógico
O core do sistema implementa uma máquina de estados simples para a situação do aluno:
1.  **Aprovação Plena**: Mérito acadêmico (Média ≥ 7.0) + Assiduidade (Frequência ≥ 75%).
2.  **Recuperação**: Oportunidade de melhoria para médias entre 5.0 e 6.9, desde que mantida a frequência mínima.
3.  **Reprovação Crítica**: Médias abaixo de 5.0 ou infrequência (abaixo de 75%).

## Stack Tecnológica
A escolha das tecnologias foi pautada em eficiência e manutenibilidade:
- **[Python](https://www.python.org/):** Core da lógica de processamento.
- **[Streamlit](https://streamlit.io/):** Utilizado para transformar o script em uma aplicação web interativa com baixíssima sobrecarga de código de front-end.
- **[Pandas](https://pandas.pydata.org/):** Engine para estruturação de dados e exportação de relatórios CSV.
- **[Pytest](https://docs.pytest.org/):** Framework de testes para garantir que nenhuma alteração futura quebre as regras de negócio estabelecidas.

## Como Rodar o Projeto

```bash
# 1. Clone o repositório
git clone https://github.com/bia024/edulogic-assistente-aprovacao.git

# 2. Instale as dependências necessárias
pip install streamlit pandas pytest pytest-cov

# 3. Inicie o assistente
streamlit run main.py
```

## Engenharia de Qualidade
Diferente de scripts acadêmicos simples, o EduLogic foi construído sob a ótica de **Test-Driven Development (TDD)** em mente. 

Para garantir que a lógica de aprovação seja infalível, implementamos testes parametrizados que cobrem:
- Casos de borda (notas mínimas e máximas).
- Reprovação por falta vs. Reprovação por nota.
- Entradas vazias ou inesperadas.

**Executar Testes:**
```bash
pytest
```

### Cobertura de Testes
```bash
pytest --cov=main --cov-report=term-missing
```

### Autora - Bianca Caetano 
- **[GitHub](https://github.com/bia024/edulogic-assistente-aprovacao)**
- **[LinkedIn](www.linkedin.com/in/bia-caetano)**

# EduLogic - Assistente de Aprovação 🎓

Sistema automatizado para cálculo de situação acadêmica, desenvolvido para o Desafio Profissional (UNIASSELVI).

## Links do Projeto
- **Deploy Online:** [Clique aqui para testar o sistema](https://edulogic-assistente-aprovacaogit-j8wwktpeyjmfdwc8s9gdqu.streamlit.app/)
- **Repositório:** [https://github.com/bia024/edulogic-assistente-aprovacao](https://github.com/bia024/edulogic-assistente-aprovacao)

## Fluxograma de Decisão
O gráfico abaixo representa a lógica de negócio implementada:

```mermaid
flowchart TD
    A["Início: Entrada de Dados"] --> B{"Frequência >= 75%?"}
    B -- "Não" --> C["Resultado: Reprovado por Frequência"]
    B -- "Sim" --> D{"Média >= 7.0?"}
    D -- "Sim" --> E(("✅ Resultado: Aprovado"))
    D -- "Não" --> F{"Média >= 5.0?"}
    F -- "Sim" --> G(("⚠️ Resultado: Recuperação"))
    F -- "Não" --> H["Resultado: Reprovado por Nota"]
    C --> I["Fim: Relatório CSV"]
    E --> I
    G --> I
    H --> I

    classDef aprovado stroke:#22c55e,stroke-width:4px,fill:#f0fdf4;
    classDef recuperacao stroke:#eab308,stroke-width:4px,fill:#fefce8,stroke-dasharray: 5 5;
    classDef reprovado stroke:#ef4444,fill:#fef2f2;
    classDef inicioFim stroke:#6366f1,fill:#eef2ff;
    class E aprovado;
    class G recuperacao;
    class C,H reprovado;
    class A,I inicioFim;
