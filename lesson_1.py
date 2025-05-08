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

print("My name is %s." % "Tanaka")
print("%s is %d years old." % ("Tanaka", 28))
print("%(name)s is %(age)d years old." % {'name': "Tanaka", 'age': 28})

# ファイルを開いて、書き込みを行う場合は、「r」「w」をうまく使い分ける
f = open("test.txt", "w")
print("Hello World!I'm from Japan.Please talk to me friendly.", file=f)
f.close()
