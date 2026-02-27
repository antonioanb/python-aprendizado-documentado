
#uma generator function é como uma fabrica, cada yield entrega um valor e tudo depois dele até encontrar outro yield
def geradora():
    yield 2
    print("continuando ...")
    yield 3
    print("continuando....")
    yield 4
    print("vou termiminar")
    return "acabou"#return gera uma exeção StopIteration

#gen vai segurar o ponteiro, o estado onde o ultimo yield parou
gen = geradora()

#next() chama o ultimo estado que está guardado no gen
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

#usando for, o for sabe lidar com a  exeção StopIteration
for item in gen:
    print(item)