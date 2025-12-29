import azure.functions as func
import logging
import os
import json
from azure.cosmos import CosmosClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HTTP trigger received request")

    try:
        # --- Connect to Cosmos DB ---
        cosmos_uri = os.environ["COSMOS_URI"]
        cosmos_key = os.environ["COSMOS_KEY"]

        client = CosmosClient(cosmos_uri, cosmos_key)
        database = client.get_database_client("crcdb")
        container = database.get_container_client("counter")

        # --- Read item ---
        item = container.read_item(
            item="visits",
            partition_key="visits"
        )

        # --- Increment counter ---
        item["count"] += 1

        # --- Update item ---
        container.replace_item(item=item, body=item)

        logging.info(f"Visitor count updated to {item['count']}")

        return func.HttpResponse(
            json.dumps({"count": item["count"]}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.exception("Cosmos DB error")
        return func.HttpResponse(
            f"Internal Server Error: {str(e)}",
            status_code=500
        )
