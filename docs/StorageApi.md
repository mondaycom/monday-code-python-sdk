# monday_code.StorageApi

All URIs are relative to *http://localhost:59999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_by_key_from_storage**](StorageApi.md#delete_by_key_from_storage) | **DELETE** /storage/{key} | 
[**get_by_key_from_storage**](StorageApi.md#get_by_key_from_storage) | **GET** /storage/{key} | 
[**increment_counter**](StorageApi.md#increment_counter) | **POST** /storage/counter/increment | 
[**upsert_by_key_from_storage**](StorageApi.md#upsert_by_key_from_storage) | **PUT** /storage/{key} | 


# **delete_by_key_from_storage**
> delete_by_key_from_storage(key, x_monday_access_token)



### Example


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
    api_instance = monday_code.StorageApi(api_client)
    key = 'key_example' # str | 
    x_monday_access_token = 'x_monday_access_token_example' # str | 

    try:
        api_instance.delete_by_key_from_storage(key, x_monday_access_token)
    except Exception as e:
        print("Exception when calling StorageApi->delete_by_key_from_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **x_monday_access_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_key_from_storage**
> StorageDataContract get_by_key_from_storage(key, shared, x_monday_access_token)



### Example


```python
import monday_code
from monday_code.models.storage_data_contract import StorageDataContract
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
    api_instance = monday_code.StorageApi(api_client)
    key = 'key_example' # str | 
    shared = True # bool | 
    x_monday_access_token = 'x_monday_access_token_example' # str | 

    try:
        api_response = api_instance.get_by_key_from_storage(key, shared, x_monday_access_token)
        print("The response of StorageApi->get_by_key_from_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_by_key_from_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **shared** | **bool**|  | 
 **x_monday_access_token** | **str**|  | 

### Return type

[**StorageDataContract**](StorageDataContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increment_counter**
> object increment_counter(x_monday_access_token, increment_counter_params)



### Example


```python
import monday_code
from monday_code.models.increment_counter_params import IncrementCounterParams
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
    api_instance = monday_code.StorageApi(api_client)
    x_monday_access_token = 'x_monday_access_token_example' # str | 
    increment_counter_params = monday_code.IncrementCounterParams() # IncrementCounterParams | 

    try:
        api_response = api_instance.increment_counter(x_monday_access_token, increment_counter_params)
        print("The response of StorageApi->increment_counter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->increment_counter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_monday_access_token** | **str**|  | 
 **increment_counter_params** | [**IncrementCounterParams**](IncrementCounterParams.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_by_key_from_storage**
> object upsert_by_key_from_storage(key, x_monday_access_token, storage_data_contract, shared=shared, previous_version=previous_version)



### Example


```python
import monday_code
from monday_code.models.storage_data_contract import StorageDataContract
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
    api_instance = monday_code.StorageApi(api_client)
    key = 'key_example' # str | 
    x_monday_access_token = 'x_monday_access_token_example' # str | 
    storage_data_contract = monday_code.StorageDataContract() # StorageDataContract | 
    shared = True # bool |  (optional)
    previous_version = 'previous_version_example' # str |  (optional)

    try:
        api_response = api_instance.upsert_by_key_from_storage(key, x_monday_access_token, storage_data_contract, shared=shared, previous_version=previous_version)
        print("The response of StorageApi->upsert_by_key_from_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->upsert_by_key_from_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **x_monday_access_token** | **str**|  | 
 **storage_data_contract** | [**StorageDataContract**](StorageDataContract.md)|  | 
 **shared** | **bool**|  | [optional] 
 **previous_version** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

