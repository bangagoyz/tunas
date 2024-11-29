a = int(input("N :"))
b = int (input("M :"))
ai = []
bi = []
skill = 0

for i in range (a):
    c = int(input("masukkan ai"))
    d = int(input("masukkan bi"))
    ai.append(c)
    bi.append(d)


for j in range (len(ai)):
    if ai[j] > a:
        skill=a
    else:
        skill += bi[j]
        
print(b, a)
print(ai)
print(bi)
print(skill)


    
    
    
