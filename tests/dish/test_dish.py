from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish_1 = Dish("lasanha berinjela", 27.00)
    dish_2 = Dish("lasanha presunto", 25.90)
    dish_1.add_ingredient_dependency(Ingredient("massa de lasanha"), 100)

    assert dish_1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        }
    assert dish_1.get_ingredients() == {Ingredient("massa de lasanha")}
    assert repr(dish_1) == "Dish('lasanha berinjela', R$27.00)"
    assert repr(dish_1) != "Dish('lasanha presunto', R$25.90)"
    assert hash(dish_1) == hash(dish_1)
    assert hash(dish_1) != hash(dish_2)
    assert dish_1 == dish_1
    assert dish_1 != dish_2
    assert dish_1.name == "lasanha berinjela"
    assert dish_1.price == 27.0
    with pytest.raises(TypeError):
        Dish("lasanha berinjela", "27.00")
    with pytest.raises(ValueError):
        Dish("lasanha berinjela", -30.00)
