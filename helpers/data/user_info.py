import random

from dataclasses import dataclass
from faker import Faker

fake = Faker('ru_RU')


@dataclass
class User:
    first_name: str
    last_name: str

    def __hash__(self):
        return hash((self.first_name, self.last_name))


@dataclass
class UserForTextBox(User):
    user_email: str
    current_address: str
    permanent_address: str

    def __hash__(self):
        return hash((super().__hash__(), self.user_email, self.current_address, self.permanent_address))


class TextBoxUserGenerator:
    @classmethod
    def generate_user(cls) -> UserForTextBox:
        return UserForTextBox(first_name=fake.first_name(),
                              last_name=fake.last_name(),
                              user_email=fake.unique.email(),
                              current_address=fake.address(),
                              permanent_address=fake.address())

    @classmethod
    def generate_users(cls, count: int = 10) -> list[UserForTextBox]:
        return [cls.generate_user() for _ in range(count)]

    @classmethod
    def get_random_user(cls) -> UserForTextBox:
        return cls.generate_user()


@dataclass
class UsersForPracticeForm(User):
    user_email: str
    gender: str
    user_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: list[str]
    hobbies: list[str]
    current_address: str
    state: str
    city: str

    def __hash__(self):
        return hash((
            super().__hash__(),
            self.user_email,
            self.gender,
            self.user_number,
            self.birth_day,
            self.birth_month,
            self.birth_year,
            self.subjects,
            self.hobbies,
            self.current_address,
            self.state,
            self.city))


class PracticeFormUserGenerator:
    @classmethod
    def generate_user(cls) -> UsersForPracticeForm:
        return UsersForPracticeForm(first_name=fake.first_name(),
                                    last_name=fake.last_name(),
                                    user_email=fake.unique.email(),
                                    gender=fake.random_elements(elements=('Male', 'Female', 'Other'), length=1)[0],
                                    user_number="8" + "".join([str(random.randint(0, 9)) for _ in range(9)]),
                                    birth_day=str(random.randint(a=12, b=27)),
                                    birth_month=fake.random_elements(elements=(
                                        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                        'September', 'October', 'November', 'December'),
                                        length=1)[0],
                                    birth_year=str(fake.year()),
                                    subjects=list(set(fake.random_elements(elements=(
                                        'Maths', 'English', 'Computer Science', 'Chemistry', 'Physics', 'Biology',
                                        'Accounting', 'Arts', 'Commerce', 'Economics', 'History'),
                                        length=random.randint(a=2, b=4), unique=True))),
                                    hobbies=list(set(fake.random_elements(elements=(
                                        'Sports', 'Music', 'Reading'),
                                        length=random.randint(a=1, b=3), unique=True))),
                                    current_address=fake.address(),
                                    # state=fake.random_elements(elements=('NCR', 'Uttar Pradesh',
                                    # 'Haryana', 'Rajasthan'), length=1)[0], TODO!!! fix it
                                    state='Uttar Pradesh',
                                    city=fake.random_elements(elements=('Agra', 'Lucknow', 'Merrut'), length=1)[0])

    @classmethod
    def generate_users(cls, count: int = 10) -> list[UsersForPracticeForm]:
        return [cls.generate_user() for _ in range(count)]

    @classmethod
    def get_random_user(cls) -> UsersForPracticeForm:
        return cls.generate_user()
