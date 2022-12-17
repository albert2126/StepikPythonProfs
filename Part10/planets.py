from typing import Generator


def txt_to_dict() -> Generator[dict, None, None]:
    with open("planets.txt") as fd:
        for planet in (planet.split('\n') for planet in fd.read().split('\n\n')):
            yield {k: v for k, v in (par.split(' = ') for par in planet)}


# Test:
planets = txt_to_dict()
print(next(planets))
