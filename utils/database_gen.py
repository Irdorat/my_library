from faker import Faker
import random

fake=Faker("ru_RU")

def fake_generate_book():
    return {
        "category": random.choice(["Фантастика", "Роман", "Детектив", "Фэнтези"]),
        "title": fake.sentence(nb_words=3),
        "author": fake.name(),
        "year": random.randint(1900, 2024),
        "pages": random.randint(100, 1000),
        "is_read": random.random() < 0.01
    }

def fake_upd_book():
    pass
