#import json, requests, hashlib
import requests
import hashlib

# config
rocketsms_login = '996890331'
rocketsms_password = 'cJ8hjuBH'
rocketsms_passhash = hashlib.md5(rocketsms_password.encode('utf-8')).hexdigest()
rocketsms_url = 'http://api.rocketsms.by/simple/send'

def sendsms(phone, message):
	data = {'username': rocketsms_login, 'password': rocketsms_passhash, 'phone': phone, 'text': message, 'priority': 'true'}
	try:
		request = requests.post(rocketsms_url, data = data)
		print(request)
		result = request.json()
		print(result)
		status = result['status']
	except Exception as e:
		print('Cannot send SMS: bad or no response from RocketSMS.')
		print(e)
	else:
		if (status == 'SENT') | (status == 'QUEUED'):
			print('SMS accepted, status: {}'.format(status))
		else:
			print('SMS rejected, status: {}'.format(status))

# testing
if __name__ == '__main__':
	sendsms(375445548131, 'Hello kitty:)')