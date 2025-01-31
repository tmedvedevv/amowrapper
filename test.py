from amowrapper.services import OAuthClient



client = OAuthClient(
    client_id='78c859ba-0490-4b75-b18b-97d096f520f8',
    client_secret='D4ChhD9TEslSHMXin6T64xGvX6S7YD5qvffvtIipcXfVpFYT6XCF61p95QgVSrXp',
    redirect_uri='https://webhook.site/9616615b-a422-4f08-8175-7b5d105739f6',
).request(url='https://clearnacc.amocrm.ru/api/v4/contacts', method='GET', data=[], access_token='')

print(client)

