# monday_code.ObjectStorageApi

All URIs are relative to *http://localhost:59999*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](ObjectStorageApi.md#delete_file) | **DELETE** /object-storage/files/{filename} | 
[**download_file**](ObjectStorageApi.md#download_file) | **GET** /object-storage/files/{filename} | 
[**get_file_info**](ObjectStorageApi.md#get_file_info) | **GET** /object-storage/files/{filename}/info | 
[**list_files**](ObjectStorageApi.md#list_files) | **GET** /object-storage/files | 
[**upload_file**](ObjectStorageApi.md#upload_file) | **POST** /object-storage/files | 


# **delete_file**
> DeleteFileResponse delete_file(filename)

### Example


```python
import monday_code
from monday_code.models.delete_file_response import DeleteFileResponse
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
    api_instance = monday_code.ObjectStorageApi(api_client)
    filename = 'filename_example' # str | 

    try:
        api_response = api_instance.delete_file(filename)
        print("The response of ObjectStorageApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 

### Return type

[**DeleteFileResponse**](DeleteFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> DownloadFileResponse download_file(filename)

### Example


```python
import monday_code
from monday_code.models.download_file_response import DownloadFileResponse
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
    api_instance = monday_code.ObjectStorageApi(api_client)
    filename = 'filename_example' # str | 

    try:
        api_response = api_instance.download_file(filename)
        print("The response of ObjectStorageApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 

### Return type

[**DownloadFileResponse**](DownloadFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_info**
> GetFileInfoResponse get_file_info(filename)

### Example


```python
import monday_code
from monday_code.models.get_file_info_response import GetFileInfoResponse
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
    api_instance = monday_code.ObjectStorageApi(api_client)
    filename = 'filename_example' # str | 

    try:
        api_response = api_instance.get_file_info(filename)
        print("The response of ObjectStorageApi->get_file_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->get_file_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 

### Return type

[**GetFileInfoResponse**](GetFileInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> ListFilesResponse list_files(prefix=prefix, max_results=max_results, page_token=page_token)

### Example


```python
import monday_code
from monday_code.models.list_files_response import ListFilesResponse
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
    api_instance = monday_code.ObjectStorageApi(api_client)
    prefix = 'prefix_example' # str |  (optional)
    max_results = 3.4 # float |  (optional)
    page_token = 'page_token_example' # str |  (optional)

    try:
        api_response = api_instance.list_files(prefix=prefix, max_results=max_results, page_token=page_token)
        print("The response of ObjectStorageApi->list_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->list_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**|  | [optional] 
 **max_results** | **float**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**ListFilesResponse**](ListFilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> UploadFileResponse upload_file(content=content, filename=filename, content_type=content_type, metadata=metadata)

Upload file with unified content parameter
This endpoint accepts all content types through a single 'content' parameter
String content should be encoded as bytes and sent as file upload

### Example


```python
import monday_code
from monday_code.models.upload_file_response import UploadFileResponse
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
    api_instance = monday_code.ObjectStorageApi(api_client)
    content = None # bytearray |  (optional)
    filename = 'filename_example' # str |  (optional)
    content_type = 'content_type_example' # str |  (optional)
    metadata = 'metadata_example' # str |  (optional)

    try:
        api_response = api_instance.upload_file(content=content, filename=filename, content_type=content_type, metadata=metadata)
        print("The response of ObjectStorageApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectStorageApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content** | **bytearray**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **metadata** | **str**|  | [optional] 

### Return type

[**UploadFileResponse**](UploadFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

