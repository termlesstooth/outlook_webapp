import os

CLIENT_ID = "94d2f74f-fb08-4269-9673-7f1004be2c0f" # Application (client) ID of app registration

# TODO: Configure for production - secure client secret
CLIENT_SECRET = "AwK8Q~eTWQ1VeY~NcKGgGfzX~SDytigpgEA2rcCz" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

#AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
AUTHORITY = "https://login.microsoftonline.com/64cb88a7-417c-4661-bf4a-efcc191f26a5"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent
GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0' # will be used to access mail

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
