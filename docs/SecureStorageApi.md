# monday_code.SecureStorageApi

All URIs are relative to *http://localhost:59999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_secure_storage**](SecureStorageApi.md#delete_secure_storage) | **DELETE** /secure-storage/{key} | 
[**get_secure_storage**](SecureStorageApi.md#get_secure_storage) | **GET** /secure-storage/{key} | 
[**put_secure_storage**](SecureStorageApi.md#put_secure_storage) | **PUT** /secure-storage/{key} | 


# **delete_secure_storage**
> delete_secure_storage(key)



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
    api_instance = monday_code.SecureStorageApi(api_client)
    key = 'key_example' # str | 

    try:
        api_instance.delete_secure_storage(key)
    except Exception as e:
        print("Exception when calling SecureStorageApi->delete_secure_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secure_storage**
> SecureStorageDataContract get_secure_storage(key)



### Example


```python
import monday_code
from monday_code.models.secure_storage_data_contract import SecureStorageDataContract
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
    api_instance = monday_code.SecureStorageApi(api_client)
    key = 'key_example' # str | 

    try:
        api_response = api_instance.get_secure_storage(key)
        print("The response of SecureStorageApi->get_secure_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureStorageApi->get_secure_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**SecureStorageDataContract**](SecureStorageDataContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_secure_storage**
> object put_secure_storage(key, secure_storage_data_contract)



### Example


```python
import monday_code
from monday_code.models.secure_storage_data_contract import SecureStorageDataContract
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
    api_instance = monday_code.SecureStorageApi(api_client)
    key = 'key_example' # str | 
    secure_storage_data_contract = monday_code.SecureStorageDataContract() # SecureStorageDataContract | 

    try:
        api_response = api_instance.put_secure_storage(key, secure_storage_data_contract)
        print("The response of SecureStorageApi->put_secure_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecureStorageApi->put_secure_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **secure_storage_data_contract** | [**SecureStorageDataContract**](SecureStorageDataContract.md)|  | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

