from factories import UserFactory


def test_user_is_active():
    user = UserFactory.create()
    assert user.is_active is True
