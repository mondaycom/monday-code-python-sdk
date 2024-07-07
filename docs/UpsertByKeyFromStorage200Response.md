# UpsertByKeyFromStorage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**success** | **bool** |  | 
**version** | **object** |  | 

## Example

```python
from monday_code.models.upsert_by_key_from_storage200_response import UpsertByKeyFromStorage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertByKeyFromStorage200Response from a JSON string
upsert_by_key_from_storage200_response_instance = UpsertByKeyFromStorage200Response.from_json(json)
# print the JSON string representation of the object
print(UpsertByKeyFromStorage200Response.to_json())

# convert the object into a dict
upsert_by_key_from_storage200_response_dict = upsert_by_key_from_storage200_response_instance.to_dict()
# create an instance of UpsertByKeyFromStorage200Response from a dict
upsert_by_key_from_storage200_response_from_dict = UpsertByKeyFromStorage200Response.from_dict(upsert_by_key_from_storage200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


