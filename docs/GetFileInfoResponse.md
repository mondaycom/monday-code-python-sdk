# GetFileInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 
**file_info** | [**FileInfo**](FileInfo.md) |  | [optional] 

## Example

```python
from monday_code.models.get_file_info_response import GetFileInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFileInfoResponse from a JSON string
get_file_info_response_instance = GetFileInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetFileInfoResponse.to_json())

# convert the object into a dict
get_file_info_response_dict = get_file_info_response_instance.to_dict()
# create an instance of GetFileInfoResponse from a dict
get_file_info_response_from_dict = GetFileInfoResponse.from_dict(get_file_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


