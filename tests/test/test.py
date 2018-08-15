def foo(a, b):
  c = 1
  for i in range(a, b):
      c += 1
  bar()

def bar():
    c = 40
    c += 1
    print "hola"

foo(1,4)
