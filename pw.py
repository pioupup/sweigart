#! python3
# pw.py - Программа для незащищенного хранения паролей

PASSWORDS = {'email': 'sgdASGDasdfasg',
			 'blog': '@42435',
			 'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('''Используйте: python pw.py [имя учетной записи] 
		     - копирование пароля учетной записи''')
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Пароль для ' + account + ' скопирован в буфер.')
else:
	print('Учетная запись ' + account + ' отсутсвует в списке.')
