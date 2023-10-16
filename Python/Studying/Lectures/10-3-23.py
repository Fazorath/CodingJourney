## Defining 2 Functions

## Functioning calling another function
def makepizza():
    sauce = getIngredient()
    dough = getIngredient()
    topping = getIngredient()
    topping2 = getIngredient()
    print("\n",sauce)
    print("\n",dough)
    print("\n",topping)
    print("\n",topping2)

def getIngredient():
    ingredient = input("\nWhat is the Ingredient: ")
    return ingredient

makepizza()
