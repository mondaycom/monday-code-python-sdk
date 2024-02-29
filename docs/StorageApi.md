# monday_sdk.StorageApi

All URIs are relative to *http://localhost:59999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_storage**](StorageApi.md#delete_storage) | **DELETE** /storage/{key} | 
[**get_storage**](StorageApi.md#get_storage) | **GET** /storage/{key} | 
[**put_storage**](StorageApi.md#put_storage) | **PUT** /storage/{key} | 
[**storage_increment_counter**](StorageApi.md#storage_increment_counter) | **PUT** /storage/{key}/counter/increment | 


# **delete_storage**
> delete_storage(key, x_monday_access_token)



### Example


```python
import monday_sdk
from monday_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:59999
# See configuration.py for a list of all supported configuration parameters.
configuration = monday_sdk.Configuration(
    host = "http://localhost:59999"
)


# Enter a context with an instance of the API client
with monday_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monday_sdk.StorageApi(api_client)
    key = 'key_example' # str | 
    x_monday_access_token = 'x_monday_access_token_example' # str | 

    try:
        api_instance.delete_storage(key, x_monday_access_token)
    except Exception as e:
        print("Exception when calling StorageApi->delete_storage: %s\n" % e)
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

# **get_storage**
> StorageDataContract get_storage(key, shared, x_monday_access_token)



### Example


```python
import monday_sdk
from monday_sdk.models.storage_data_contract import StorageDataContract
from monday_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:59999
# See configuration.py for a list of all supported configuration parameters.
configuration = monday_sdk.Configuration(
    host = "http://localhost:59999"
)


# Enter a context with an instance of the API client
with monday_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monday_sdk.StorageApi(api_client)
    key = 'key_example' # str | 
    shared = True # bool | 
    x_monday_access_token = 'x_monday_access_token_example' # str | 

    try:
        api_response = api_instance.get_storage(key, shared, x_monday_access_token)
        print("The response of StorageApi->get_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_storage: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_storage**
> put_storage(key, x_monday_access_token, shared, previous_version, storage_data_contract)



### Example


```python
import monday_sdk
from monday_sdk.models.storage_data_contract import StorageDataContract
from monday_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:59999
# See configuration.py for a list of all supported configuration parameters.
configuration = monday_sdk.Configuration(
    host = "http://localhost:59999"
)


# Enter a context with an instance of the API client
with monday_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monday_sdk.StorageApi(api_client)
    key = 'key_example' # str | 
    x_monday_access_token = 'x_monday_access_token_example' # str | 
    shared = True # bool | 
    previous_version = 'previous_version_example' # str | 
    storage_data_contract = monday_sdk.StorageDataContract() # StorageDataContract | 

    try:
        api_instance.put_storage(key, x_monday_access_token, shared, previous_version, storage_data_contract)
    except Exception as e:
        print("Exception when calling StorageApi->put_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **x_monday_access_token** | **str**|  | 
 **shared** | **bool**|  | 
 **previous_version** | **str**|  | 
 **storage_data_contract** | [**StorageDataContract**](StorageDataContract.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_increment_counter**
> storage_increment_counter(x_monday_access_token, key, increment_counter_params)



### Example


```python
import monday_sdk
from monday_sdk.models.increment_counter_params import IncrementCounterParams
from monday_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:59999
# See configuration.py for a list of all supported configuration parameters.
configuration = monday_sdk.Configuration(
    host = "http://localhost:59999"
)


# Enter a context with an instance of the API client
with monday_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monday_sdk.StorageApi(api_client)
    x_monday_access_token = 'x_monday_access_token_example' # str | 
    key = 'key_example' # str | 
    increment_counter_params = monday_sdk.IncrementCounterParams() # IncrementCounterParams | 

    try:
        api_instance.storage_increment_counter(x_monday_access_token, key, increment_counter_params)
    except Exception as e:
        print("Exception when calling StorageApi->storage_increment_counter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_monday_access_token** | **str**|  | 
 **key** | **str**|  | 
 **increment_counter_params** | [**IncrementCounterParams**](IncrementCounterParams.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

