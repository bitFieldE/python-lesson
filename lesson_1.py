# とほほのPython入門 - 構文
# https://www.tohoho-web.com/python/syntax.html#hello_world

# Hello Worldの書き方
print('Hello World!')

# コロンを使うことで変数宣言も続けて行うことが可能
a =1 ; b = 2; c = 3

# バックスラッシュを使って後続で書くことができる
# ただし、バックスラッシュの後に続いてコメントを書くことはできない
total = 123 \
      + 456 \
      + 789
print("total result:", total)

month = ['Jan', 'Feb', 'Mar', 'Apr', # ここにはコメントの記述が可能
         'Jun', 'Jul', 'Aug', 'Sep', # ここにはコメントの記述が可能
         'Oct', 'Nov', 'Dec']
print("months:", month)

a = 3
if a == 5:
  print("aの値は5です")
elif a == 3:
  print("aの値は3です")

print("My name is %s." % "Tanaka")
print("%s is %d years old." % ("Tanaka", 28))
print("%(name)s is %(age)d years old." % {'name': "Tanaka", 'age': 28})

# ファイルを開いて、書き込みを行う場合は、「r」「w」をうまく使い分ける
f = open("test.txt", "w")
print("Hello World!I'm from Japan.Please talk to me friendly.", file=f)
f.close()
