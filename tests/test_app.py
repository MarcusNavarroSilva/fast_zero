from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    Este teste acontece em tres etapas, que podemos resumir em AAA:
     A: arrange - arranjo
     A: act - teste, executa (Sut)
     A: assert - verifica se o teste funcionou
    """
    # Arrange
    # client = TestClient(app) -- não usamos mais para chamar teste
    # Act
    response = client.get('/')
    # Assert
    assert response.json() == {'message': 'ola mundo'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'password': 'secret',
            'email': 'alice@uno.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@uno.com',
        'id': 1,
    }


def test_return_users(client):

    response = client.get(
        '/users/',
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@uno.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'alice',
            'email': 'alice@uno.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@uno.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/user/1')

    assert response.status_code == HTTPStatus.NOT_FOUND

def test_get_user_should_return_not_found__exercicio(client):
    response = client.get('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user___exercicio(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }