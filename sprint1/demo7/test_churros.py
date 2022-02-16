from main import soma


def test_se_soma_esta_somando():
    result = soma(1, 2)
    expected = 3

    assert result == expected, 'Verique se a funcao `soma` está retornando corretamente'
