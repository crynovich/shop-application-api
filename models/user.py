from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    _internal_id: int = 123

    def greet(self) -> str:
        return f"Hello, my name is {self.name}"
