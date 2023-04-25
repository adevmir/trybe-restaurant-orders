from src.models.ingredient import (
    Ingredient,
    Restriction
)  # noqa: F401, E261, E501


INGREDIENTS = (
    Ingredient("queijo mussarela"),
    Ingredient("tomate"),
)


# Req 1
def test_ingredient():
    assert INGREDIENTS[0].restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
        }
    assert repr(INGREDIENTS[0]) == "Ingredient('queijo mussarela')"
    assert repr(INGREDIENTS[0]) != "Ingredient('tomate')"
    assert INGREDIENTS[0] == Ingredient("queijo mussarela")
    assert INGREDIENTS[1] == Ingredient("tomate")
    assert INGREDIENTS[0] != INGREDIENTS[1]
    assert hash(INGREDIENTS[0]) == hash(Ingredient("queijo mussarela"))
    assert hash(INGREDIENTS[1]) == hash(Ingredient("tomate"))
    assert INGREDIENTS[0].name == "queijo mussarela"
