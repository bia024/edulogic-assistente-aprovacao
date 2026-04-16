import pytest
from main import calcular_situacao, MEDIA_APROVACAO, MEDIA_REPROVACAO, FREQUENCIA_MINIMA

@pytest.mark.parametrize("notas, frequencia, esperado", [
    # Casos de Aprovação
    ([7.0, 7.0], 75, "Aprovado"),
    ([10.0, 9.0, 8.0], 80, "Aprovado"),
    
    # Casos de Recuperação
    ([5.0, 5.0], 75, "Recuperação"),
    ([6.9, 6.9], 90, "Recuperação"),
    
    # Casos de Reprovação por Nota
    ([4.9, 4.9], 100, "Reprovado"),
    ([2.0, 3.0], 75, "Reprovado"),
    
    # Casos de Reprovação por Frequência
    ([10.0, 10.0], 74, "Reprovado"),
    ([7.0, 7.0], 0, "Reprovado"),
    
    # Casos de Borda e Lista Vazia
    ([], 100, "Reprovado"),
    ([0.0], 75, "Reprovado"),
])
def test_calculo_situacao(notas, frequencia, esperado):
    """
    Testa a função calcular_situacao contra diversos cenários de notas e frequências.
    """
    _, resultado = calcular_situacao(notas, frequencia)
    assert resultado == esperado