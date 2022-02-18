import requests


def test_trainee_register():
    data = {
        'user_name': 'test',
        'first_name': 'first',
        'last_name': 'last',
        'email': 'test@test.com',
        'height': 6.2,
        'weight': 155,
        'goal_setting': 'PowerLifting'
    }
    response = requests.post("http://127.0.0.1:8000/api/auth/users/", data)
    print(response)


if __name__ == '__main__':
    test_trainee_register()