from src.models.ingredient import (
    Ingredient,
    Restriction
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    queijo = Ingredient("queijo mussarela")
    tomate = Ingredient("tomate")
    assert queijo.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        }
    assert repr(queijo) == "Ingredient('queijo mussarela')"
    assert repr(queijo) != "Ingredient('tomate')"
    assert queijo == Ingredient("queijo mussarela")
    assert tomate == Ingredient("tomate")
    assert queijo != tomate
    assert hash(queijo) == hash(Ingredient("queijo mussarela"))
    assert hash(queijo) != hash(Ingredient("tomate"))
    assert tomate.name == "tomate"
