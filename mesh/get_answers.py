import requests
from data import config


def get_answers(link):
	headers = {
		'token': f'{config.mdz_token}',
		'link': f'{link}'
	}

	answer = requests.post('http://mdzbot.ru/cdz/', headers=headers)

	return answer.text