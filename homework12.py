vibor_texta = input("text viberi: ")
gg = vibor_texta.split()
gg_new = ""


for pp in gg:
    if pp.count("a") == 2:
        print(pp.title(), end=" ")