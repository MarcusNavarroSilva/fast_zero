from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


# aqui não testa se os dados foram validados,
#  mas se o python instancia a classe.
# com o session, fixture criada no conftest.py passamos a usar banco de dados
#  em memória e conseguimos criar um usuário
def test_create_user(session, mock_db_time):

    with mock_db_time(model=User) as time:
        new_user = User(
            username='teste', email='exemplo@exemplo.com', password='password'
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'teste'))

    assert asdict(user) == {
        'id': 1,
        'username': 'teste',
        'email': 'exemplo@exemplo.com',
        'password': 'password',
        'created_at': time,
    }
