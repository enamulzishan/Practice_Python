class student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def study(self):
    print(f"{self.name} is studying.")
  def sleep(self):
    print(f"{self.name} is sleeping.")

s1 = student("Enamul", 20)

s1.study()