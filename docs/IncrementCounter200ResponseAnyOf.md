# IncrementCounter200ResponseAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_counter_value** | **object** |  | [optional] 
**message** | **object** |  | [optional] 
**success** | **bool** |  | 
**error** | **str** |  | 

## Example

```python
from monday_code.models.increment_counter200_response_any_of import IncrementCounter200ResponseAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of IncrementCounter200ResponseAnyOf from a JSON string
increment_counter200_response_any_of_instance = IncrementCounter200ResponseAnyOf.from_json(json)
# print the JSON string representation of the object
print(IncrementCounter200ResponseAnyOf.to_json())

# convert the object into a dict
increment_counter200_response_any_of_dict = increment_counter200_response_any_of_instance.to_dict()
# create an instance of IncrementCounter200ResponseAnyOf from a dict
increment_counter200_response_any_of_from_dict = IncrementCounter200ResponseAnyOf.from_dict(increment_counter200_response_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


