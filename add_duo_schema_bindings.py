import asyncio
from synapseclient.models import Project, File
import synapseclient
import json
import os

import yaml


def main():
    """Invoke adding DUO schema bindings"""
    syn = synapseclient.Synapse()
    syn.setEndpoints(**synapseclient.client.STAGING_ENDPOINTS)
    syn.login()
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)

    for configuration in config:
        syn.get_available_services()
        js = syn.service("json_schema")
        my_org = js.JsonSchemaOrganization("governance.schemas")
        my_org.create()
        with open(configuration['filepath'], 'r') as f:
            example_schema = json.load(f)
        # Create a new JSON schema version for an existing organization
        schema_name = os.path.basename(configuration['filepath']).replace(".json", '').replace("_", '.')
        # TODO: need to figure out only pushing new schemas
        print(example_schema)
        print(schema_name)
        new_version1 = my_org.create_json_schema(example_schema, schema_name)
        print(new_version1.uri)
        synapse_id = configuration['synapse_id']
        request_body = {
            "entityId": synapse_id,
            "schema$id": new_version1.uri,
            "enableDerivedAnnotations": True
        }
        syn.restPUT(
            f"/entity/{synapse_id}/schema/binding", body=json.dumps(request_body)
        )


if __name__ == "__main__":
    main()
