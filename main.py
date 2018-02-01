class universe():
    def matrix(firstw,secondw):
        firstwv = str(firstw)
        secondwv = str(secondw)
        w = len(firstwv)
        h = len(secondwv)
        Matrix = [[0 for x in range(w)] for y in range(h)]
        # kelimexkelime buyuklugunde matris oluştur
        print(Matrix)
        print(Matrix[4][6],firstwv[4],secondwv[6])
        alfabelist = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç","Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç"]
        i = 0
        a = 0
        abcounter = 0
        if(len(alfabelist) != w*h):
            alfabelist.append("**")

        # #harfleri matrise ata
        while(a <= h):
            while(i <= w):
                Matrix[a][i] = alfabelist[abcounter]
                abcounter = abcounter + 1
                i = i + 1
            i = 0
            a = a + 1
        #aaaand it does not work!
        print(Matrix)
word1 = "dalyrkDALYRK"
word2 = "dalyrkDALYRK"
universe.matrix(word1,word2)