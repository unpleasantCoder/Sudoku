f=open('sudoku.txt')
line=f.readlines()
a = [0] * 9
for i in range(9):
    a[i] = [0] * 9
for i in range(9):
    m=line[i]
    for j in range(9):
        a[i][j]=int(m[j])

def matrica():
    for i in range(9):
        if i==0:
            print('=====================') 
        print('|',a[i][0],a[i][1],a[i][2],a[i][3],a[i][4],a[i][5],a[i][6],a[i][7],a[i][8],'|')
        if i==8:
            print('=====================')      
         
def viucher(h,l):
    for n in range(len(nom)):
            h2=int(list(nom[n])[0])
            l2=int(list(nom[n])[1])
            if h2==h and l2!=l and (a[h][l] in a[h2][l2]) :
                a[h2][l2].remove(a[h][l])
            if l2==l and h2!=h and (a[h][l] in a[h2][l2]) :
                a[h2][l2].remove(a[h][l])

def paru(mass): #подпрограмма для поиска пар среди строк, столбцов и подквадратов
    # flgpar1=False
    # flgpar2=False
    for i in range(0,len(mass)-1):# проходим массив с номерами ячеек не до конца
        h=int(list(mass[i])[0])#
        l=int(list(mass[i])[1])#
        if len(a[h][l])==int(2):# если в ячейке может быть 2 числа, то
            for j in range(i+1,len(mass)):#в оставшейся части массива нахожим такой же вариант
                h2=int(list(mass[j])[0])
                l2=int(list(mass[j])[1])
                if a[h][l]==a[h2][l2]:# если вариант найден
                    # print('polupara',h,l,a[h][l],'dlina=',len(a[h][l]),h2,l2,a[h2][l2])
                    #flgpar1=True
                    for n in range(0,len(mass)):# проходим массив заного
                        h3=int(list(mass[n])[0])
                        l3=int(list(mass[n])[1])
                        if (h3!=h and l3!=l) or (h3!=h2 and l3!=l2):# если ячеейке не 2 предыдущих
                            if a[h][l][0] in a[h3][l3]:#
                                a[h3][l3].remove(a[h][l][0])#
                                # print(a[h3][l3])
                                # print(a[h][l][0])
                                # flgpar2=True
                                # print('para') 
                        if (h3!=h and l3!=l) or (h3!=h2 and l3!=l2):#
                            if a[h][l][1] in a[h3][l3]:#
                                a[h3][l3].remove(a[h][l][1])#
                                # print(a[h3][l3])
                                # print(a[h][l][0])
                                # flgpar2=True 
                                # print('para')    
matrica()   
k=0
ide=[1,2,3,4,5,6,7,8,9]
coord=[0,0,0,3,0,6,3,0,3,3,3,6,6,0,6,3,6,6]
nom=[]
for i in range(9):
    for j in range(9):
        if a[i][j]==0:
            a[i][j]=[]
            a[i][j].extend(ide)
            nom.append(str(i)+str(j))
for i in range(9):
    for j in range(9):
        viucher(i,j)
# matrica()
q=0
print(len(nom),'|nom|')
flg=True
#  while len(nom)!=0 or flg==True or q<3 :
while flg==True:
    isp=len(nom)
# while len(nom)!=0:
    num=[]
    # print(q)
    q+=1
    for i in range(len(nom)):
        h=int(list(nom[i])[0])
        l=int(list(nom[i])[1])
        # print(h,l)
        if len(a[h][l])==1:
            num.append(nom[i])
    if len(num)!=0:
        k+=len(num)
        for i in range(len(num)):
            h=int(list(num[i])[0])
            l=int(list(num[i])[1])
            a[h][l]=int(str(a[h][l][0]))
            nom.remove(num[i])
        for i in range(len(num)):
            h=int(list(num[i])[0])
            l=int(list(num[i])[1])
            viucher(h,l)
    # matrica()   
    for i in range(9):
        stolb=[]
        stroka=[]
        stolbpr=['']*10
        strokapr=['']*10
        got=[]
        for j in range(len(nom)):
            h=int(list(nom[j])[0])
            l=int(list(nom[j])[1])
            if h==i:
                stolb.append(nom[j])
            if l==i:
                stroka.append(nom[j])
        # print(stolb,stroka)
        # paru(stolb)
        # paru(stroka)
        for j in range(len(stolb)):
            h=int(list(stolb[j])[0])
            l=int(list(stolb[j])[1])
            for n in range(len(a[h][l])):
                stolbpr[a[h][l][n]]+=stolb[j]
        for j in range(len(stroka)):
            h=int(list(stroka[j])[0])
            l=int(list(stroka[j])[1])
            for n in range(len(a[h][l])):
                strokapr[a[h][l][n]]+=stroka[j]
        for j in range(len(strokapr)):
            if len(strokapr[j])==2:
                h=int(list(strokapr[j])[0])
                l=int(list(strokapr[j])[1])
                a[h][l]=j
                got.append(strokapr[j])
        for j in range(len(stolbpr)):
            if len(stolbpr[j])==2:
                h=int(list(stolbpr[j])[0])
                l=int(list(stolbpr[j])[1])
                a[h][l]=j
                if stolbpr[j] not in got:
                    got.append(stolbpr[j])
        for j in range(len(got)):
            if got[j] in nom:
                nom.remove(got[j])
        # print(got,'got')
        for j in range(len(got)):
            h=int(list(got[j])[0])
            l=int(list(got[j])[1])
            viucher(h,l)

    for i in range(0,18,2):# в данном цикле делим на квадраты 3 на 3 и ведем с ними работу: сначала исключаем варианты из ячеек потом находим единственные значения
        kvcel=[] #сюда записываются все ячейки с челыми числами из одного под квадрата
        kvvar=[] # сюда записываются координаты вариативных ячеек из одного подквадрата
        kvprov=['']*10 # сюда будут добавляться номера ячеек в котрых может быть та или иная цифра
        kva=[] # список для последующего удаления из массива с координатами вариативных ячеек заполненных в процессе этого алгоритма
        for j in range(coord[i],coord[i]+3): # разбиваем строчку на 3 части 0-2 3-5 6-8
            for n in range(coord[i+1],coord[i+1]+3): # разбиваем столбец на 3 части 0-2 3-5 6-8
                if type(a[j][n])==int: # если клетка заполненная, то записываем ее номер
                    kvcel.append(str(j)+str(n)) # клетка заполенна
                if type(a[j][n])==list:#если клетка вариативна, то записываем ее номер
                    if (str(j)+str(n)) not in nom:
                        print('huita')
                    kvvar.append(str(j)+str(n))# записываем номер
        for j in range(len(kvcel)):# перебираем заполненные ячейки
            h=int(list(kvcel[j])[0])#выписываем координаты
            l=int(list(kvcel[j])[1])#
            for n in range(len(kvvar)):#перебираем вариативные ячейки
                h2=int(list(kvvar[n])[0])#выписываем координаты
                l2=int(list(kvvar[n])[1])#
                if a[h][l] in a[h2][l2]:# если число из заполненной есть в вариативной исключаем его оттуда
                    a[h2][l2].remove(a[h][l])# исключаем число
        paru(kvvar)
        for j in range(len(kvvar)):#перебираем вариативные ячейки
            h=int(list(kvvar[j])[0])#выписываем координаты
            l=int(list(kvvar[j])[1])#
            for n in range(len(a[h][l])):#проходимся по цифрам содержащимся в вариативной ячейке
                kvprov[a[h][l][n]]+=(str(h)+str(l))#добавляем в массив номер ячейке, число равно номеру дополняемой ячейке
        for j in range(10):#цикл от 0 до 10
            if len(kvprov[j])==2:#если у данного числа есть только 2 координаты, значит клетка одна
                h=int(list(kvprov[j])[0])# выписываем координаты
                l=int(list(kvprov[j])[1])#
                a[h][l]=j# присваиваем ячейке ее значение
                kva.append(str(h)+str(l))# дополняем массив ее номером. для последующего удаления этой ячейки из общего списка вариативных ячеек и вычеркивания варианта из строки и столбца
        for j in range(len(kva)):#перебираем массив свежехаполненных ячеек
            nom.remove(kva[j])#удаляем из общего масисива координат вариативных ячеек
        for j in range(len(kva)):#перебираем массив
            h=int(list(kva[j])[0])#выписываем координаты
            l=int(list(kva[j])[1])#
            viucher(h,l)# вычеркиваем по стровкам и столбцам свежую цифру
    if len(nom)==isp:
        q+=1
        if q>5:
            flg=False               
# print(k,'k')            
matrica()
print(len(nom),'|nom|')
jnjn=[]
for i in range(0,18,2):
    jnjn=[]
    print('podkvadratu')
    for j in range(coord[i],coord[i]+3): # разбиваем строчку на 3 части 0-2 3-5 6-8
            for n in range(coord[i+1],coord[i+1]+3):
                jnjn.append(a[j][n])
    print(jnjn[0:3])
    print(jnjn[3:6])
    print(jnjn[6:9])
 
for i in range(9):
    print(a[i],"stroka")
    print()
    # for j in range(9):
    #     print(a[j][i], end='')
    #     if j==8:
    #         print('stolb')
    # print()
for i in range(9):
    for j in range(9):
        print(a[j][i],'', end='')
        if j==8:
            print('stolb')
    print()
