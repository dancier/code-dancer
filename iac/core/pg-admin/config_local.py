# -*- coding: utf-8 -*-

##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2022, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
# config.py - Core application configuration settings
#
##########################################################################

import builtins
import logging
import os
import sys

# We need to include the root directory in sys.path to ensure that we can
# find everything we need when running in the standalone runtime.
root = os.path.dirname(os.path.realpath(__file__))
if sys.path[0] != root:
    sys.path.insert(0, root)

from pgadmin.utils import env, IS_WIN, fs_short_path

##########################################################################
# Application settings
##########################################################################

# Name of the application to display in the UI
APP_NAME = 'pgAdmin 4'
APP_ICON = 'pg-icon'

##########################################################################
# Application settings
##########################################################################


##########################################################################
# OAuth2 Configuration
##########################################################################

# Multiple OAUTH2 providers can be added in the list like [{...},{...}]
# All parameters are required

AUTHENTICATION_SOURCES = ['oauth2']

PGADMIN_CONFIG_ENHANCED_COOKIE_PROTECTION = False

OAUTH2_CONFIG = [
    {
        # The name of the of the oauth provider, ex: github, google
        'OAUTH2_NAME': 'Test-Dancier',
        # The display name, ex: Google
        'OAUTH2_DISPLAY_NAME': 'Dancier User',
        # Oauth client id
        'OAUTH2_CLIENT_ID': 'pgadmin',
        # Oauth secret
        'OAUTH2_CLIENT_SECRET': os.getenv('PG_ADMIN_OAUTH_SECRET'),
        # URL to generate a token,
        # Ex: https://github.com/login/oauth/access_token
        'OAUTH2_TOKEN_URL': os.getenv('PG_ADMIN_OAUTH2_TOKEN_URL'),
        # URL is used for authentication,
        # Ex: https://github.com/login/oauth/authorize
        'OAUTH2_AUTHORIZATION_URL': os.getenv('PG_ADMIN_OAUTH2_AUTHORIZATION_URL'),
        # Oauth base url, ex: https://api.github.com/
        'OAUTH2_API_BASE_URL': os.getenv('PG_ADMIN_OAUTH2_API_BASE_URL'),
        # Name of the Endpoint, ex: user
        'OAUTH2_USERINFO_ENDPOINT': os.getenv('PG_ADMIN_OAUTH2_USERINFO_ENDPOINT'),
        # Oauth scope, ex: 'openid email profile'
        # Note that an 'email' claim is required in the resulting profile
        'OAUTH2_SCOPE': 'openid email profile',
        # Font-awesome icon, ex: fa-github
        'OAUTH2_ICON': None,
        # UI button colour, ex: #0000ff
        'OAUTH2_BUTTON_COLOR': None,
    }
]

# After Oauth authentication, user will be added into the SQLite database
# automatically, if set to True.
# Set it to False, if user should not be added automatically,
# in this case Admin has to add the user manually in the SQLite database.

OAUTH2_AUTO_CREATE_USER = True


