# monday_code.LogsApi

All URIs are relative to *http://localhost:59999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**write_log**](LogsApi.md#write_log) | **POST** /logs | 


# **write_log**
> write_log(write_log_request_body)

### Example


```python
import monday_code
from monday_code.models.write_log_request_body import WriteLogRequestBody
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
    api_instance = monday_code.LogsApi(api_client)
    write_log_request_body = monday_code.WriteLogRequestBody() # WriteLogRequestBody | 

    try:
        api_instance.write_log(write_log_request_body)
    except Exception as e:
        print("Exception when calling LogsApi->write_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **write_log_request_body** | [**WriteLogRequestBody**](WriteLogRequestBody.md)|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

