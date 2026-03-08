from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


# aqui não testa se os dados foram validados,
#  mas se o python instancia a classe.
def test_create_user():
    user = User(
        username='teste', email='exemplo@exemplo.com', password='password'
    )

    assert user.username == 'teste'
    assert user.email == 'exemplo@exemplo.com'
    assert user.password == 'password'


def create_test_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='test', email='test@test', password='secret')
        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'test'))

        assert asdict(user) == {
            'id': 1,
            'username': 'test',
            'email': 'test@test',
            'password': 'secret',
            'created_at': time,
        }
