dic = {
}
tup = ()
for key in dic:
  print(f"{key}: {dic[key]}")
  tup += ((key, dic[key]),)

   # fmt: skipprint(tuple(sorted(tup,reverse=True,key=lambda item: item[1]))[0])
print(len(dic))