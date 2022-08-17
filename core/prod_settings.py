import os
import dj_database_url
from core.settings import *
from stdlib import get_env_var


DEBUG = False;
TEMPLATE_DEBUG = False;

# To force HTTPs communication to server
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https');
SECURE_SSL_REDIRECT     = True;

# Heroku database configuration
DATABASES['default'].update(dj_database_url.config());

# HOST list allowed by this server
ALLOWED_HOSTS = ['heroku-dj.herokuapp.com'];

# Statics directories creation
STATIC_TMP = os.path.join(BASE_DIR, 'static');
os.makedirs(STATIC_TMP, exist_ok=True);
os.makedirs(STATIC_ROOT, exist_ok=True);

# CONFIGURATION DE WHITENOISE
# ================================================================
# WhiteNoise permet à votre application Web de servir ses
# propres fichiers statiques, ce qui en fait une unité autonome
# qui peut être déployée n'importe où sans dépendre de nginx,
# d'Amazon S3 ou de tout autre service externe. (Particulièrement
# utile sur Heroku, OpenShift et autres fournisseurs PaaS.).
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware'];
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage';
