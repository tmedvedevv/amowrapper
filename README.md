
# example 1. Create class integration

```python
from amowrapper.oauth.config import OAuthConfig
import os
from dotenv import load_dotenv
from amowrapper.oauth.exceptions import OAuthError

# Загрузка переменных окружения из файла .env
load_dotenv()

# Использование переменных окружения
integration = OAuthConfig(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    redirect_uri=os.environ['redirect_uri']
)
```

# example 2. Create client

```python
from amowrapper.oauth.factory import OAuthFactory

client: OAuthFactory = OAuthFactory(OAuthConfig=integration)
```


# Example 3. Add client to middleware and make simple requests from api reference

```python
from amowrapper.oauth.middleware import OAuthMiddleware
from amowrapper.oauth.exceptions import OAuthLongTermTokenExpired, OAuthAccessTokenExpired

middleware_client = OAuthMiddleware(oauth_client=client)

try:

    response = middleware_client.make_authenticated_request(endpoint='api/v4/leads')

except (OAuthAccessTokenExpired, OAuthLongTermTokenExpired) as e:
    # refresh tokens

    pass
```