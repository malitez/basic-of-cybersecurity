import hashlib
import optparse
def crack(password_hash,passFile):
	try:
		passwords = open(passFile,'r') #La variable password correspond au fichier choisi en mode Read
	except:
		print("no file found") #Erreur sur la présence du fichier txt
	for password in passwords:
		encoding = password.encode("utf-8") #Mise en forme des mots dans le fichier txt au norme utf-8
		digest = hashlib.md5(encoding.strip()).hexdigest() #Encodage des mots dans le fichier txt avec l'algorithme md5
		if digest == password_hash:
			print("[+] password Found : {} ".format(password))
			break
parser = optparse.OptionParser(usage = "passwordCraker [--hash][--file]") #Format de la commande pour l'utilisation du programme py
parser.add_option("--hash","--hash-value",
dest = "pass_hash", type = str,
	help = "le hash du mot de passe à cracker")
parser.add_option("--file","--pass_file",dest="passfile",
help = "fichier contenant des mots de passes")
(options,arguments) = parser.parse_args()
if not options.pass_hash or not options.passfile:
	print("user l'option help avoir plus d'information")
else:
	crack(options.pass_hash,options.passfile)
