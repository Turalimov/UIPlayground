from dataclasses import dataclass


@dataclass
class Person:
    login_name: str = None
    gen_password: str = None

