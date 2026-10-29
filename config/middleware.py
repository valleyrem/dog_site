"""Project middleware."""


class ContentSecurityPolicyMiddleware:
    """Add a Content-Security-Policy header.

    Deliberately permissive where the site depends on it: Google Tag Manager
    (injected only after analytics consent) pulls code and beacons from
    Google's hosts, and photos live on S3/OCI, so scheme-wide sources are
    allowed for scripts, images and connections. What the policy really adds
    is the hardening directives: no <base> hijacking, no plugins, and the
    page can never be framed.
    """

    CSP = "; ".join(
        (
            "default-src 'self'",
            "base-uri 'self'",
            "object-src 'none'",
            "frame-ancestors 'none'",
            "form-action 'self'",
            "script-src 'self' 'unsafe-inline' https:",
            "style-src 'self' 'unsafe-inline'",
            "img-src 'self' data: https:",
            "font-src 'self' data:",
            "connect-src 'self' https:",
            "frame-src https:",
        )
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.headers.setdefault("Content-Security-Policy", self.CSP)
        return response
