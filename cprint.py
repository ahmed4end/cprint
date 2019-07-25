import random, sys, time, os,subprocess
text = "Hello, Human!, this message should be printed in a cool way xD: "

class cprint():
	"""
	Some Color Codes to use: A: light blue, F:light white, D:light purple, C:light red, E:light yellow
			
	#i know it's crazy using oop this way, but i don't really care, this is the way i opertate xD
	"""
	def __init__(self,text , style='d', speed=1/99,cmd_color="A"):
		os.system("color "+cmd_color)
		self.letters = [chr(i) for  i in range(65, 123)] + ["@", "#", "$", "%", "^", "&", "*", "~"] #Editable! 
		if len(text) > 75: #Warning!
			self.dprint("WARNING: your text must be less than 75 letters! or shit happens.")
			print("\n")
			self.tprint("Press any key to continue...", speed=1/92)
			input()


		categories = { 
			"d": "self.dprint(text, speed)",     #Distortion printing
			"fo": "self.foprint(text, speed)",   #Fade out print
			"sd": "self.sdprint(text, speed)",   #Slow #Distortion printing
			"rsd": "self.rsdprint(text, speed)", #reverse #Slow #Distortion printing
			"t": "self.tprint(text, speed)",     #Train printing
			"rt": "self.rtprint(text, speed)",	 #Reverse #Train printing 
			"s": "self.sprint(text, speed)",	 #Slow printing   
			"rs": "self.rsprint(text, speed)",	 #Reverse #Slow printing
			"m": "self.mprint(text, speed)",     #Middle printing
			"rm": "self.rmprint(text, speed)",	 #reverse #Middle printing

		}
		try:
			eval(categories[style])
		except:
			print("invalid Choice")

	def dprint(self, text, speed=1/99): 
		#Full name: Distortion printing
		res = [text]
		text = list(text)
		for i in range(len(text)+5):
			for _ in range(random.randint(0, 6)):
				text[random.randint(0, len(text)-1)] = random.choice(self.letters)
			res.append("".join(text))
		self.Core(res[::-1], "i", speed, False)

	def foprint(self, text, speed=1/99):
		#Full name: fade out print
		res = [text]
		text = list(text)
		for i in range(len(text)+5):
			for _ in range(random.randint(0, 3)):
				text[random.randint(0, len(text)-1)] = " "
			res.append("".join(text))
		self.Core(res[::-1], "i", speed, False)

	def sdprint(self, text, speed=1/99):
		#Full name: Slow distortion printing
		res = [text]
		text = list(text)
		for i in range(len(text)):
			for _ in range(random.randint(0, 6)):
				text[random.randint(0, len(text)-1)] = random.choice(self.letters)
			res.append("".join(text)[:len(text)-i])
		self.Core(res[::-1], "i", speed, False)
	
	def rsdprint(self, text, speed=1/99):
		#Full name: Reverse slow distortion printing
		res = [(0, text)]
		text = list(text)
		for i in range(len(text)):
			for _ in range(random.randint(0, (len(text)-i)//10)):
				text[random.randint(0, len(text)-1)] = random.choice(self.letters)
			piece = "".join(text)[:len(text)-i]
			res.append( (len(text)-len(piece), piece) )
		
		self.Core(res[::-1], "' '*i+j", speed)

	def tprint(self, text, speed=1/99):
		#Full name: Train style print.
		seq = [text[i:] for i in range(len(text)+1,0,-1)] + [text]
		self.Core(seq, "i", speed, double=False)

	def rtprint(self, text, speed=1/99):
		#Full name: Reverse train style print.
		seq = [(len(text)-len(text[:i]), text[:i]) for i in range(0, len(text)+1)] + [(0, text)]
		self.Core(seq, "' '*i + j", speed)
	
	def sprint(self, text, speed=1/99): 
		#Full name: Slow printing.
		seq = [text[0:i] for i in range(1, len(text)+1)]
		self.Core(seq, "i", speed, double=False)

	def rsprint(self, text, speed=1/99): 
		#Full name: Reverse slow printing.
		re_seq = [(len(text)-i, text[-i:]) for i in range(1, len(text)+1)]
		pattern = "' '*i + j"
		self.Core(re_seq, pattern, speed)

	def mprint(self, text, speed=1/99): 
		##Full name: Middle slow printing.
		seq = [(len(text)-i, text[-i:i]) for i in range(1, len(text)+1) if text[-i:i] != ""]
		pattern = "' '*i + j + ' '*i"
		self.Core(seq, pattern, speed)

	def rmprint(self, text, speed=1/99): 
		#Full name: Reverse middle slow printing.
		if len(text)<6:
			print("ERROR: text must be at least 6 letters.")
			return None
		seq, re_seq = [text[0:i] for i in range(1, len(text)//2+1)], [text[-i:] for i in range(1, len(text)//2+1)]
		seq, pattern = zip(seq, re_seq), "i + ' '*(" + str(len(text)) + "-len(i)*2) + j"
		self.Core(seq, pattern, speed)

	def Core(self, seq, pattern, speed, double=True):
		if double:
			for i, j in seq:
				sys.stdout.write("\r" + eval(pattern))
				sys.stdout.flush()
				time.sleep(speed)
		else:
			for i in seq:
				sys.stdout.write("\r" + eval(pattern))
				sys.stdout.flush()
				time.sleep(speed)


########### Simple example of only one style #################

cprint(text)                              #Default style = 'd' 
print("\n") #Do work here instead
cprint(text, style="d")

##############################################################

########### Simple example of trying all styles ##############

for  i in ["d", "fo", "sd", "rsd", "t", "rt", "s", "rs", "m", "rm"]:
	cprint(text, style=i)
	print("\n") #Do work here instead
##############################################################





time.sleep(5)  # DO SOME WORK HERE INSTEAD XD