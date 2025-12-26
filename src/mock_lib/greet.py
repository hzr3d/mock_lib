def greet(name: str) -> str:
    name = (name or "").strip()
    return f"Hello, {name or 'world'}!"
