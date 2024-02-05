from dataclasses import dataclass


@dataclass(frozen=True)
class Flat:
	price: float
	area: float
	description: str
	