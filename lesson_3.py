# 関数定義（def）
def add(x, y):
  ans = x + y
  return ans

# 戻り値（return）
n = add(3, 5)
print("result of function add:", n)

count = 0 # グローバル変数

def func1():
  print(count)

def func2():
  global count
  count += 1

# キーワード引数
def repeat_msg(msg, repeat=3):
  for i in range(repeat):
    print(msg)

repeat_msg('Hello')
repeat_msg('Yahoo', repeat=5)

def func(a, b, *, c): # 「*」以降は「c=xx」のようにキーワードを指定する必要がある。
  print("a=%s, b=%s, c=%s" %(a, b, c))

func("A", "B", c="C")
# func("A", "B", "C")

# ノンローカル変数（nonlocal）
count = 999

def counter():
  count = 0        # count_up()から見るとローカルではない変数
  def count_up():
    nonlocal count # グローバルでもローカルでもない親関数の変数を参照
    count += 1
    return count
  return count_up

cnt = counter()
print(cnt())
print(cnt())
print(cnt())

# ラムダ式（lambda）
# 名前のない小さな関数の定義をする役割
myfunc = lambda x, y: x + y
print("result of myfunc:", myfunc(3, 5))

# イテレータ（iterator）
class MyRange:
  def __init__(self, max):
    self._max = max

  def __iter__(self):
    self._count = 0
    return self
  def __next__(self):
    result = self._count
    if result >= self._max:
      raise StopIteration
    self._count += 1
    return result
  
for n in MyRange(5):
  print(n)

# ジェネレータ（yield）
def funcA(list):
  ret = []
  for n in list:
    ret.append(n * 2)
  return ret

for n in funcA([1, 2, 3, 4, 5]):
  print(n)

def readfileA(f):
  lines = []
  for line in f:
    lines.append(line.rstrip())
  return lines

f = open("test.txt")
for line in readfileA(f):
  if (line == "__END__"):
    break
  print(line)
f.close

# デコレータ（@）
def mydecolater(func):  # デコレータを定義
  def wrapper():
    print("start")      # 前処理を実行する
    func()              # デコレート対象の関数を実行する
    print("end")        # 後処理を実行する
  return wrapper

@mydecolater
def hello():
  print("hello")

hello()

def mydecolater(func):
  import functools
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("Funcname:", func.__name__)
    print("Arguments:", args)
    print("Keywords:", args)
    ret = func(*args, **kwargs)
    print("Return:", ret)
    return ret
  return wrapper

@mydecolater
def func(msg1, msg2, flag=1, mode=2):
  """A sample function"""
  print("----", msg1, msg2, "----")
  return 1234

n = func("Hello", "Hello2", flag=1)
print(n)
print(repr(func))
print(func.__doc__)
