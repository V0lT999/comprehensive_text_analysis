from faker import Faker

fake = Faker()


def generate_text():
    return fake.text()


if __name__ == '__main__':
    print(generate_text())
