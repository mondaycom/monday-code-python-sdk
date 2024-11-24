# WriteLogRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**error** | [**WriteLogRequestBodyError**](WriteLogRequestBodyError.md) |  | [optional] 
**message** | **str** |  | 
**method** | [**LogMethods**](LogMethods.md) |  | 

## Example

```python
from monday_code.models.write_log_request_body import WriteLogRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of WriteLogRequestBody from a JSON string
write_log_request_body_instance = WriteLogRequestBody.from_json(json)
# print the JSON string representation of the object
print(WriteLogRequestBody.to_json())

# convert the object into a dict
write_log_request_body_dict = write_log_request_body_instance.to_dict()
# create an instance of WriteLogRequestBody from a dict
write_log_request_body_from_dict = WriteLogRequestBody.from_dict(write_log_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


