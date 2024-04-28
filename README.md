# monday-code

## Installation & Usage
```sh
pip install monday-code
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import monday_code
from monday_code.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:59999
# See configuration.py for a list of all supported configuration parameters.
configuration = monday_code.Configuration(
    host = "http://localhost:59999"
)



# Enter a context with an instance of the API client
with monday_code.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monday_code.QueueApi(api_client)
    publish_message_params = monday_code.PublishMessageParams() # PublishMessageParams | 

    try:
        api_response = api_instance.publish_message(publish_message_params)
        print("The response of QueueApi->publish_message:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueueApi->publish_message: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:59999*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*QueueApi* | [**publish_message**](docs/QueueApi.md#publish_message) | **POST** /queue | 
*QueueApi* | [**validate_secret**](docs/QueueApi.md#validate_secret) | **POST** /queue/validate-secret | 
*SecretApi* | [**get_secret**](docs/SecretApi.md#get_secret) | **GET** /secrets/{name} | 
*SecureStorageApi* | [**delete_secure_storage**](docs/SecureStorageApi.md#delete_secure_storage) | **DELETE** /secure-storage/{key} | 
*SecureStorageApi* | [**get_secure_storage**](docs/SecureStorageApi.md#get_secure_storage) | **GET** /secure-storage/{key} | 
*SecureStorageApi* | [**put_secure_storage**](docs/SecureStorageApi.md#put_secure_storage) | **PUT** /secure-storage/{key} | 
*StorageApi* | [**delete_by_key_from_storage**](docs/StorageApi.md#delete_by_key_from_storage) | **DELETE** /storage/{key} | 
*StorageApi* | [**get_by_key_from_storage**](docs/StorageApi.md#get_by_key_from_storage) | **GET** /storage/{key} | 
*StorageApi* | [**increment_counter**](docs/StorageApi.md#increment_counter) | **POST** /storage/counter/increment | 
*StorageApi* | [**upsert_by_key_from_storage**](docs/StorageApi.md#upsert_by_key_from_storage) | **PUT** /storage/{key} | 


## Documentation For Models

 - [GetByKeyFromStorage404Response](docs/GetByKeyFromStorage404Response.md)
 - [GetByKeyFromStorage500Response](docs/GetByKeyFromStorage500Response.md)
 - [IncrementCounterParams](docs/IncrementCounterParams.md)
 - [JsonValue](docs/JsonValue.md)
 - [Period](docs/Period.md)
 - [PublishMessageParams](docs/PublishMessageParams.md)
 - [PublishMessageResponse](docs/PublishMessageResponse.md)
 - [SecureStorageDataContract](docs/SecureStorageDataContract.md)
 - [StorageDataContract](docs/StorageDataContract.md)
 - [ValidateSecretParams](docs/ValidateSecretParams.md)
 - [ValidateSecretResponse](docs/ValidateSecretResponse.md)

