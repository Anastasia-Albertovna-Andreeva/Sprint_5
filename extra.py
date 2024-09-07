import random
import string

# Функция для создания случайного email
def generate_login_email():
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
    email = f"user_{letters}_{random.randint(100, 999)}@example.com"
    return email

# Функция для создания случайного пароля
def generate_secure_password():
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(3))
    password = f"pass_{letters}_{random.randint(10, 99)}"
    return password

# Функция для создания основы email для негативных тестов
def generate_email_prefix():
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    email_prefix = f"test_{letters}_{random.randint(100, 999)}"
    return email_prefix

# Подключение генераторов логинов и паролей к тестам
def test_registration():
    email = generate_login_email()
    password = generate_secure_password()
    print(f"Регистрация с логином: {email} и паролем: {password}")

