import requests
from bs4 import BeautifulSoup

def login():
    headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

    login_data={
        'jazoest': '2708',
        'lsd': 'AVqVRUtK',
        'email': 'doing.art.man',
        'pass': 'namra370h55v!',
        'timezone': '-480',
        'lgndim': 'eyJ3IjoxMjgwLCJoIjo4MDAsImF3IjoxMjgwLCJhaCI6NzMwLCJjIjoyNH0=',
        'lgnrnd': '234121_0LWL',
        'lgnjs': '1583221283',
        'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB',
        'locale': 'en_US',
        'next': 'https://www.facebook.com/',
        'login_source': 'login_bluebar',
        'guid': 'f1763b4afd7150c',
        'prefill_contact_point': 'doing.art.man',
        'prefill_source': 'browser_dropdown',
        'prefill_type': 'password',
        'skstamp': 'eyJoYXNoIjoiYWNjZDFhOTM5ZDBlNTJmNTg3ZDZiZmRkZWRmOWJlNDEiLCJoYXNoMiI6IjU4OGZlZGFlYTMwODRiZmU0ZWFlMDJhMmRjNWEzMDYxIiwicm91bmRzIjo1LCJzZWVkIjoiNzQwMjE3MjU1NGI4NDE5ODc0ODMwNDU1ODg3NjI2ODgiLCJzZWVkMiI6ImQ2ZDRjYmM1N2ZmNDVjOTJhOTc0MDgwYjFiZTBlMDQyIiwidGltZV90YWtlbiI6NDQyOTA0LCJzdXJmYWNlIjoibG9naW4ifQ=='
    }

    with requests.Session() as s:
        url="https://www.facebook.com"
        r=s.get(url,headers=headers)
        soup=BeautifulSoup(r.content,'html.parser')
        login_data['jazoest']=soup.find('input',attrs={'name':'jazoest'})['value']
        login_data['lsd']=soup.find('input',attrs={'name':'lsd'})['value']
        login_data['lgndim']=soup.find('input',attrs={'name':'lgndim'})['value']
        login_data['lgnrnd']=soup.find('input',attrs={'name':'lgnrnd'})['value']
        login_data['lgnjs']=soup.find('input',attrs={'name':'lgnjs'})['value']
        login_data['ab_test_data']=soup.find('input',attrs={'name':'ab_test_data'})['value']
        login_data['guid']=soup.find('input',attrs={'name':'guid'})['value']
        #login_data['skstamp']=soup.find('input',attrs={'name':'lsd'})['value']

        r=s.post(url,data=login_data,headers=headers)
        print(r.content)
    