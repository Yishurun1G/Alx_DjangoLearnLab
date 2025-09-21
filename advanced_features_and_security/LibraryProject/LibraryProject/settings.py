# DEBUG should be False in production
DEBUG = False

# Security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Cookies over HTTPS only
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Optional: Content Security Policy (CSP) via middleware
# Install django-csp: pip install django-csp
MIDDLEWARE = [
    ...
    'csp.middleware.CSPMiddleware',  # add CSP middleware
    ...
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
