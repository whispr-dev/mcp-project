from __future__ import annotations

try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("Missing dependency: pydantic. Install with: pip install pydantic")
    raise SystemExit(0)

class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=150)

if __name__ == "__main__":
    print(User(name="Ada", age=36).model_dump())
    try:
        User(name="Ben", age=-5)
    except ValidationError as e:
        print("Validation error:", e.errors()[0]["msg"])
