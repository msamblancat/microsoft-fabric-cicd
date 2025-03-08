# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""
Example of leveraging default authentication flows
Refer to the authentication section in the README for details:
https://github.com/microsoft/fabric-cicd/tree/main?tab=readme-ov-file#authentication
"""
# START-EXAMPLE
import os
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items

# Sample values for FabricWorkspace parameters
workspace_id = os.environ.get('TARGET_WORKSPACE_ID')
environment = os.environ.get('TARGET_ENVIRONMENT_NAME')
repository_directory = "."#"your-repository-directory"
item_type_in_scope = ["DataPipeline"]

# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id=workspace_id,
    environment=environment,
    repository_directory=repository_directory,
    item_type_in_scope=item_type_in_scope,
)

# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)

# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)


