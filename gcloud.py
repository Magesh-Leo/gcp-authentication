import urllib

import google.auth.transport.requests
import google.oauth2.id_token


def make_authorized_get_request(service_url, audience):
    """
    make_authorized_get_request makes a GET request to the specified HTTP endpoint
    by authenticating with the ID token obtained from the google-auth client library
    using the specified audience value.
    """

    # Cloud Run uses your service's hostname as the `audience` value
    audience = 'https://helloworld-dev-zlzujd3glq-el.a.run.app/'

    req = urllib.request.Request(service_url)

    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    req.add_header("Authorization", f"Bearer {id_token}")
    request=req
    response = urllib.request.urlopen(req)

    return response.read(),id_token,request

print(make_authorized_get_request(service_url="https://helloworld-dev-zlzujd3glq-el.a.run.app/",audience="https://helloworld-dev-zlzujd3glq-el.a.run.app/"))
