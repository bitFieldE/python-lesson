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