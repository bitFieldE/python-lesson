# クラス（class）
# 引数に入るselfは、レシーバのようなもの
class Myclass:
  """
  A simple example class
  """

  def __init__(self):
    self.name = ""

  def getName(self):
    return self.name
  
  def setName(self, name):
    self.name = name

a = Myclass()
a.setName("Tanaka")
print(a.getName())

# クラス変数・インスタンス変数（attribute）
class MyClass:
  def __init__(self):
    self.name = ""

a1 = MyClass()
a1.name = "Tanaka"

a2 = MyClass()
a2.name = "Suzuki"

print(a1.name)
print(a2.name)

class MyClass:
  def __init__(self):
    self.name = ""

a1 = MyClass()
a1.name = "Tanaka"

a2 = MyClass()
a2.name = "Suzuki"

print(a1.name)
print(a2.name)

class MyClass:
  PI = 3.14

print(MyClass.PI)

class MyClass:
  count = 0

  def __init__(self):
    MyClass.count += 1

a1 = MyClass()
a2 = MyClass()
print(MyClass.count)

class MyClass:
  pass

a1 = MyClass()
a1.name2 = "Tanaka"
MyClass.PI2 = 3.141593

class MyClass:
  PI = 3.14

a1 = MyClass()
a2 = MyClass()
print(a1.PI)
a1.PI = 3.141593
print(a1.PI)
print(a2.PI)

class MyClass:
  name = ""
  def setName(self, name):
    self.name = name

a = MyClass()
a.setName("Tanaka")