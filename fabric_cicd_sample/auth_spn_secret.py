# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
Example of authenticating with SPN + Secret
Can be expanded to retrieve values from Key Vault or other sources
"""
import os
# START-EXAMPLE
from azure.identity import ClientSecretCredential

from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
tenant_id = os.environ.get('TENANT_ID')
token_credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

# Sample values for FabricWorkspace parameters
workspace_id = os.environ.get('TARGET_WORKSPACE_ID')
environment = os.environ.get('TARGET_ENVIRONMENT_NAME')
repository_directory = "."
item_type_in_scope = ["Lakehouse", "Notebook", "Environment"]

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    environment=environment,
    repository_directory=repository_directory,
    item_type_in_scope=item_type_in_scope,
    token_credential=token_credential,
)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)

# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)
