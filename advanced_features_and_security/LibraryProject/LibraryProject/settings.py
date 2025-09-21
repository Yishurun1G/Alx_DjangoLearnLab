# -----------------------
# SECURITY SETTINGS
# -----------------------

# Disable debug in production
DEBUG = False

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
# Tells browsers to always use HTTPS for the specified period
SECURE_HSTS_SECONDS = 31536000            # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True     # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True                # Allow site to be preloaded in browsers

# Secure cookies
SESSION_COOKIE_SECURE = True              # Only send session cookies over HTTPS
CSRF_COOKIE_SECURE = True                 # Only send CSRF cookies over HTTPS

# Security headers
SECURE_BROWSER_XSS_FILTER = True          # Enable browser XSS filtering
SECURE_CONTENT_TYPE_NOSNIFF = True        # Prevent MIME type sniffing
X_FRAME_OPTIONS = 'DENY'                  # Prevent clickjacking

# Content Security Policy (CSP) via middleware (optional but recommended)
# Install django-csp: pip install django-csp
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # <-- Add CSP middleware
]

# Basic CSP settings
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
