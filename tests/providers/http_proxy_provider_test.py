from scylla.providers import HttpProxyProvider
from .helpers import assert_provider


def test_http_proxy_provider():
    assert_provider(HttpProxyProvider())
