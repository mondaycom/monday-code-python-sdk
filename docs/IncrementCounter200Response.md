# IncrementCounter200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_counter_value** | **float** |  | 
**message** | **str** |  | 
**success** | **bool** |  | 
**error** | **object** |  | 

## Example

```python
from monday_code.models.increment_counter200_response import IncrementCounter200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IncrementCounter200Response from a JSON string
increment_counter200_response_instance = IncrementCounter200Response.from_json(json)
# print the JSON string representation of the object
print(IncrementCounter200Response.to_json())

# convert the object into a dict
increment_counter200_response_dict = increment_counter200_response_instance.to_dict()
# create an instance of IncrementCounter200Response from a dict
increment_counter200_response_from_dict = IncrementCounter200Response.from_dict(increment_counter200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


