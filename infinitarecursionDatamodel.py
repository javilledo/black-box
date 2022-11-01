from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast

T = TypeVar("T")

def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x

def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x

def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()

@dataclass
class ValueData:
    nombre: str
    edad: int

    @staticmethod
    def from_dict(obj: Any) -> 'ValueData':
        assert isinstance(obj, dict)
        nombre = from_str(obj.get("nombre"))
        edad = from_int(obj.get("edad"))
        return ValueData(nombre, edad)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nombre"] = from_str(self.nombre)
        result["edad"] = from_int(self.edad)
        return result

@dataclass
class InfinitaRecursionData:
    id: int
    value: ValueData
    version: int

    @staticmethod
    def from_dict(obj: Any) -> 'InfinitaRecursionData':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        value = ValueData.from_dict(obj.get("value"))
        version = from_int(obj.get("version"))
        return InfinitaRecursionData(id, value, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["value"] = to_class(ValueData, self.value)
        result["version"] = from_int(self.version)
        return result

def infinita_recursion_data_from_dict(s: Any) -> InfinitaRecursionData:
    return InfinitaRecursionData.from_dict(s)

def infinita_recursion_data_to_dict(x: InfinitaRecursionData) -> Any:
    return to_class(InfinitaRecursionData, x)