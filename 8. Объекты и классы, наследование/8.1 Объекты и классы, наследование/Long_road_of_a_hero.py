
class Hero:

  def go_right(self, number):
    print(f"Я иду {number} метров направо")

  def go_left(self, number):
    print(f"Я иду {number} метров налево")

  def observe(self):
    print("Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()