class universe():
	
	def matrix(firstw,secondw): #kelimelerdeki aynı harfleri atmanın bir yolunu bul setler yeterince seksi degil
#		f = set(firstw)
#		s = set(secondw)
#		f = sorted(f)
#		s = sorted(s)
#		firstwv = ''.join(f)
#		secondwv = ''.join(s)
		firstwv = str(firstw)
		secondwv = str(secondw)
		w = len(firstwv) 
		h = len(secondwv) 
		#Matrix = [[0 for x in range(w)] for y in range(h)]
		Endic = {}
		#Endiccoz = {}
		global Endiccoz
		# kelimexkelime buyuklugunde matris oluştur
		#print(Matrix)
		#print(Matrix[4][6],firstwv[4],secondwv[6])
		alfabelist = ["1","2","3","4","5","6","7","8","9","0","q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç","Q","W","E","R","T","Y","U","I","O","P","Ğ","Ü","A","S","D","F","G","H","J","K","L","Ş","İ","Z","X","C","V","B","N","M","Ö","Ç"," "]
		i = 0
		a = 0
		acounter = 0
		
		while(len(alfabelist) != w*h):
			alfabelist.append("**")

		# #harfleri sozluge ata
		while(a < h):
			#print(len(alfabelist))

			while(i < w):
				Endiccoz[str(firstwv[a]+secondwv[i])] = alfabelist[acounter] # please spirit of software spare me
				Endic[alfabelist[acounter]] = str(firstwv[a]+secondwv[i])
				acounter = acounter + 1

				i = i + 1
			#print("dalyarak" , a , i)
			i = 0
			a = a + 1
		  #aaaand it does not work! okay it works now
		print("table is complete")
		#print(Matrix.index("1"))
		return Endic
	def sifrele(matris,metin):
		sifrelist = [] #olusturulan sozlukte harflerin karsılıgını al
		for i in metin:
			sifrelist.append(matris[i])
		print(''.join(sifrelist))
		return ''.join(sifrelist)
	def coz(matris,sifreli):
		sif = str(sifreli)
		n = 2
		sonlist = []
		cozlist = [sif[i:i+n] for i in range(0, len(sif), n)] # thank you stack overflow
		for i in cozlist:
			sonlist.append(Endiccoz[i])
		sonlist = ''.join(sonlist)
		print(cozlist)
		print(sonlist)
		return sonlist
Endiccoz = {}
word1 = "dalyrkDALYRK"
word2 = "dalyrkDALYRK"
a = universe.matrix(word1,word2)
test = universe.sifrele(a,input("metin gir \n"))
universe.coz(a,test)