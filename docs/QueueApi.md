# monday_code.QueueApi

All URIs are relative to *http://localhost:59999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publish_message**](QueueApi.md#publish_message) | **POST** /queue | 
[**validate_secret**](QueueApi.md#validate_secret) | **POST** /queue/validate-secret | 


# **publish_message**
> PublishMessageResponse publish_message(publish_message_params)



### Example


```python
import monday_code
from monday_code.models.publish_message_params import PublishMessageParams
from monday_code.models.publish_message_response import PublishMessageResponse
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
    except Exception as e:
        print("Exception when calling QueueApi->publish_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_message_params** | [**PublishMessageParams**](PublishMessageParams.md)|  | 

### Return type

[**PublishMessageResponse**](PublishMessageResponse.md)

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

# **validate_secret**
> ValidateSecretResponse validate_secret(validate_secret_params)



### Example


```python
import monday_code
from monday_code.models.validate_secret_params import ValidateSecretParams
from monday_code.models.validate_secret_response import ValidateSecretResponse
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
    validate_secret_params = monday_code.ValidateSecretParams() # ValidateSecretParams | 

    try:
        api_response = api_instance.validate_secret(validate_secret_params)
        print("The response of QueueApi->validate_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueueApi->validate_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_secret_params** | [**ValidateSecretParams**](ValidateSecretParams.md)|  | 

### Return type

[**ValidateSecretResponse**](ValidateSecretResponse.md)

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

