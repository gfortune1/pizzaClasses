class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
    def calculate_cost(self):
        # Calculate the cost based on size and toppings
        cost = 5  # Base cost for a pizza
        if self.size == "medium":
            cost += 2
        elif self.size == "large":
            cost += 4
        cost += len(self.toppings) * 1.5  # $1.50 per topping
        return cost
    def prepare(self):
        # Simulate pizza preparation
        print(f"Preparing a {self.size} pizza with {', '.join(self.toppings)} toppings.")
class MargheritaPizza(Pizza):
    def __init__(self, size):
        super().__init__(size, ["cheese", "tomato sauce"])
    def prepare(self):
        # Custom preparation for Margherita pizza
        print(f"Preparing a delicious Margherita pizza ({self.size} size).")
class PepperoniPizza(Pizza):
    def __init__(self, size):
        super().__init__(size, ["cheese", "tomato sauce", "pepperoni"])
    def prepare(self):
        # Custom preparation for Pepperoni pizza
        print(f"Preparing a mouth-watering Pepperoni pizza ({self.size} size).")
class VeggiePizza(Pizza):
    def __init__(self, size):
        super().__init__(size, ["cheese", "tomato sauce", "bell peppers", "mushrooms", "onions"])
    def prepare(self):
        # Custom preparation for Veggie pizza
        print(f"Preparing a healthy Veggie pizza ({self.size} size).")
def test_pizza_ordering_system():
    margherita = MargheritaPizza("medium")
    pepperoni = PepperoniPizza("large")
    veggie = VeggiePizza("small")
    pizzas = [margherita, pepperoni, veggie]
    total_cost = sum(pizza.calculate_cost() for pizza in pizzas)
    print("Pizza Order Summary:")
    for pizza in pizzas:
        pizza.prepare()
    print(f"Total Cost: ${total_cost:.2f}")
if __name__ == "__main__":
    test_pizza_ordering_system()














