from pymacaroons import Macaroon

class JsonSerializer:
    def serialize(self, m: Macaroon) -> str: ...
    def deserialize(self, serialized: str | bytes) -> Macaroon: ...
