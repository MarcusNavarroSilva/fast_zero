from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Este teste acontece em tres etapas, que podemos resumir em AAA:
     A: arrange - arranjo
     A: act - teste, executa (Sut)
     A: assert - verifica se o teste funcionou
    """
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get('/')
    # Assert
    assert response.json() == {'message: ': 'ola mundo'}
    assert response.status_code == HTTPStatus.OK
