from AES import AES

import os

def encrypt(key, filename):
	chunksize = 16
	outputFile = "(enc)"+filename
	filesize = str(os.path.getsize(filename)).zfill(16)

	encryptor = AES(key, 128)

	with open(filename, 'rb') as infile:#rb means read in binary
		with open(outputFile, 'wb') as outfile:#wb means write in the binary mode
			outfile.write(filesize.encode('utf-8'))

			while True:
				chunk = infile.read(chunksize)
				if len(chunk) == 0:
					break
				elif len(chunk)%16 != 0:
					chunk += b' '*(16-(len(chunk)%16))

				# print(type(chunk))
				outfile.write(encryptor.encrypt(chunk))
            



def decrypt(key, filename, newfilename):
	chunksize = 16
	outputFile = newfilename

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))

		decryptor= AES(key, 128)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(filesize)

def Main():
	choice = input("Would you like to (E)encrypt or (D)Decrypt ")

	if choice == 'E':
		filename = input("File to encrypt: ")
		password = input("Password: ")
		encrypt(password, filename)
		print('Done.')
	elif choice == 'D':
		filename = input("File to decrypt: ")
		password = input("Password: ")
		newfilename = input("Name new file: ")
		decrypt(password,filename, newfilename)
		print("Done.")

	else:
		print("No option selected, closing...")


Main()