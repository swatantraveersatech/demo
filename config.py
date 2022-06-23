# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '0f45d668-a827-4734-8593-95f89ca9577f'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '0ff38eaa-ceb2-4a38-821e-80d150874f21'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = ''
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '314c1fbd-4e0b-42a4-9ef9-7227edf0f869'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = ''
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'swatantra@veersalabs.com'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'guhu@guhu00'