# monday_code.EnvironmentVariablesApi

All URIs are relative to *http://localhost:59999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_environment_variable**](EnvironmentVariablesApi.md#get_environment_variable) | **GET** /environment-variables/{name} | 
[**get_environment_variable_keys**](EnvironmentVariablesApi.md#get_environment_variable_keys) | **GET** /environment-variables | 


# **get_environment_variable**
> object get_environment_variable(name)



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
    api_instance = monday_code.EnvironmentVariablesApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.get_environment_variable(name)
        print("The response of EnvironmentVariablesApi->get_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentVariablesApi->get_environment_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**object**

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

# **get_environment_variable_keys**
> List[str] get_environment_variable_keys()



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
    api_instance = monday_code.EnvironmentVariablesApi(api_client)

    try:
        api_response = api_instance.get_environment_variable_keys()
        print("The response of EnvironmentVariablesApi->get_environment_variable_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentVariablesApi->get_environment_variable_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

