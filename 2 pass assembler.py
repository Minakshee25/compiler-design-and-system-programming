lclst = []
LC = 0
BaseTable = {}
LiteralTable = {}
SymbolTable = {}
MOTdct = {}
pass1 = ''
with open("input.txt", "r") as file: 
    data = file.readlines() 
    
    for line in data:
        word = line.split()
        if ('START' in word):
            if(len(word)>2):
                LC = int(word[2])
                SymbolTable[word[0]] = [word[2],'R']
            else:
                SymbolTable[word[0]] = [0,'R']
            lclst.append(0)
            pass1 = pass1 + line
            
        elif ('USING' in word):
            Base = word[2]
            BaseTable[word[2]] = 0
            lclst.append(LC)
            pass1 = pass1 + line
            
        elif('DC' in word):
            if('C' in word):
                lclst.append(LC)
                LC = LC + 1
            elif('H' in word):
                lclst.append(LC)
                LC = LC +2
            elif('F' in word):
                lclst.append(LC)
                LC = LC +4
            elif('D' in word):
                lclst.append(LC)
                LC = LC +8
            SymbolTable[word[0]] = [lclst[-1],'R']
            if ("'" in word[-1]):
                s = word[-2] + word[-1]
                LiteralTable[s] = [lclst[-1],'R']
            l = bin(int(word[-1][1:-1]))[2:]
            pass1 = pass1 + l + "\n"
        
        elif('DS' in word):
            if('C' in word):
                lclst.append(LC)
                LC = LC + int(word[2])*1
            elif('H' in word):
                lclst.append(LC)
                LC = LC + int(word[2])*2
            elif('F' in word):
                lclst.append(LC)
                LC = LC + int(word[2])*4
            elif('D' in word):
                lclst.append(LC)
                LC = LC + int(word[2])*8
            SymbolTable[word[0]] = [lclst[-1],'R']
            l = word[-2] + word[-1]
            pass1 = pass1 + l + "\n"
        
        elif('EQU' in word):
            lclst.append(LC)
            SymbolTable[word[0]] = [lclst[-1],'A']
            pass1 = pass1 + line
            
        elif('END' in word):
            lclst.append(LC)
            pass1 = pass1 + "END"
        
        else:
            try:
                int(word[-1])
                pass1 = pass1 + line
                lclst.append(LC)
                LC = LC + 2
            except:
                lclst.append(LC)
                LC = LC + 4
                pass1 = pass1 + word[-3] + " " + word[-2] + ", " + word[-1] + " (0," +  Base + ")\n"
            if(len(word)==4):
                SymbolTable[word[0]] = [lclst[-1],'R']
            if ("'" in word[-1]):
                LiteralTable[word[-1]] = [lclst[-1],'R']
with open('Pass1.txt',"w") as f:
    f.write(pass1)

ST = 'Symbol\tValue\tR/A\n'
for i in SymbolTable:
    ST = ST + i + "\t" + str(SymbolTable[i][0]) + "\t" + SymbolTable[i][1] + "\n"

with open('Symbol Table.txt',"w") as f:
    f.write(ST)

LT = 'Literal\tValue\tR/A\n'
for i in LiteralTable:
    LT = LT + i + "\t" + str(LiteralTable[i][0]) + "\t\t" + LiteralTable[i][1] + "\n"

with open('Literal Table.txt',"w") as f:
    f.write(LT)

s = 'RegesterNumber' + '\tContent\n'
for i in BaseTable:
    s = s + str(i) + '\t\t\t\t' +str(BaseTable[i])

with open('Base Table.txt','w') as f:
    f.write(s)
    
# PASS 2
for i in SymbolTable:
    if i in pass1:
        pass1 = pass1.replace(i,str(SymbolTable[i][0]))
for i in LiteralTable:
    if i in pass1:
        pass1 = pass1.replace(i,str(LiteralTable[i][0]))
pass2 = pass1
with open("MOT.txt", "r") as file: 
    data = file.readlines()
    for line in data:
        word = line.split()
        MOTdct[word[0]] = word[1]
for i in pass2.split('\n'):
    if (i.split(' ')[0]) in MOTdct:
        pass2 = pass2.replace(i.split(' ')[0],MOTdct[i.split(' ')[0]])
with open('Pass2.txt',"w") as f:
    f.write(pass2)
