from amowrapper.services import OAuthClient


def test_oauth_client():

    client = OAuthClient(
        client_id='78c859ba-0490-4b75-b18b-97d096f520f8',
        client_secret='D4ChhD9TEslSHMXin6T64xGvX6S7YD5qvffvtIipcXfVpFYT6XCF61p95QgVSrXp',
        redirect_uri='https://webhook.site/9616615b-a422-4f08-8175-7b5d105739f6',
    ).request(url='https://clearnacc.amocrm.ru/api/v4/leads/custom_fields', method='POST', data=[{'nasfasfme': 'afasfew', 'asfsafsafsafaefa214123512352135': 1}], access_token='')

    print(client)