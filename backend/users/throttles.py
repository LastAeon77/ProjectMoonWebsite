from rest_framework.throttling import SimpleRateThrottle


class _PerIPThrottle(SimpleRateThrottle):
    """Limits requests per client IP, whether or not the request is authenticated."""

    def get_cache_key(self, request, view):
        return self.cache_format % {"scope": self.scope, "ident": self.get_ident(request)}


class AuthBurstThrottle(_PerIPThrottle):
    scope = "auth_burst"


class AuthSustainedThrottle(_PerIPThrottle):
    scope = "auth_sustained"


# Applied to the login (token obtain) and signup endpoints to slow down password guessing.
AUTH_THROTTLES = (AuthBurstThrottle, AuthSustainedThrottle)
