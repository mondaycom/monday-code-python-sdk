import sys

# append the full absolute path of parent folder into path using pathlib
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))


import os

from flask import Flask

import monday_sdk
from monday_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:59999
# See configuration.py for a list of all supported configuration parameters.
configuration = monday_sdk.Configuration(host="http://localhost:59999")

app = Flask(__name__)


@app.route("/")
def hello_world():
    print(os.environ)
    name = os.environ.get("NAME", "World")
    return f"Hello from Python {name}!"


@app.route("/set-secure-storage-string")
def set_secure_storage_string():
    with monday_sdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = monday_sdk.SecureStorageApi(api_client)
        key = "string_key"  # str |
        storage_data_contract = (
            monday_sdk.StorageDataContract()
        )  # StorageDataContract |
        storage_data_contract["value"] = "some_secret"
        print(storage_data_contract)
        try:
            api_instance.put_secure_storage(key, storage_data_contract)
        except Exception as e:
            print(
                "Exception when calling SecureStorageApi->put_secure_storage: %s\n" % e
            )


@app.route("/get-secure-storage-string")
def get_secure_storage_string():
    with monday_sdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = monday_sdk.SecureStorageApi(api_client)
        key = "string_key"  # str |

        try:
            api_response = api_instance.get_secure_storage(key)
            print("The response of SecureStorageApi->get_secure_storage:\n")
            pprint(api_response)
        except Exception as e:
            print(
                "Exception when calling SecureStorageApi->get_secure_storage: %s\n" % e
            )


@app.route("/set-secure-storage-object")
def set_secure_storage_object():
    with monday_sdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = monday_sdk.SecureStorageApi(api_client)
        key = "object_key"  # str |
        storage_data_contract = monday_sdk.StorageDataContract(
            value={"some_secret_key": "some_secret_value"}
        )

        try:
            api_instance.put_secure_storage(key, storage_data_contract)
            # return suceess
            return "success"

        except Exception as e:
            print(
                "Exception when calling SecureStorageApi->put_secure_storage: %s\n" % e
            )


@app.route("/get-secure-storage-object")
def get_secure_storage_object():
    with monday_sdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = monday_sdk.SecureStorageApi(api_client)
        key = "object_key"  # str |

        try:
            api_response = api_instance.get_secure_storage(key)
            print("The response of SecureStorageApi->get_secure_storage:\n")
            pprint(api_response)
            return api_response.value
        except Exception as e:
            print(
                "Exception when calling SecureStorageApi->get_secure_storage: %s\n" % e
            )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
