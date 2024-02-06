from dataclasses import dataclass


@dataclass(frozen=True)
class Flat:
	href: str
	price: float
	area: float
	description: str
	