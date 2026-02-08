# DeleteFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from monday_code.models.delete_file_response import DeleteFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFileResponse from a JSON string
delete_file_response_instance = DeleteFileResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteFileResponse.to_json())

# convert the object into a dict
delete_file_response_dict = delete_file_response_instance.to_dict()
# create an instance of DeleteFileResponse from a dict
delete_file_response_from_dict = DeleteFileResponse.from_dict(delete_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


