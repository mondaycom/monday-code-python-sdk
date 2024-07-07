# IncrementCounter200ResponseAnyOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **object** |  | [optional] 
**success** | **bool** |  | 
**new_counter_value** | **float** |  | 
**message** | **str** |  | 

## Example

```python
from monday_code.models.increment_counter200_response_any_of1 import IncrementCounter200ResponseAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of IncrementCounter200ResponseAnyOf1 from a JSON string
increment_counter200_response_any_of1_instance = IncrementCounter200ResponseAnyOf1.from_json(json)
# print the JSON string representation of the object
print(IncrementCounter200ResponseAnyOf1.to_json())

# convert the object into a dict
increment_counter200_response_any_of1_dict = increment_counter200_response_any_of1_instance.to_dict()
# create an instance of IncrementCounter200ResponseAnyOf1 from a dict
increment_counter200_response_any_of1_from_dict = IncrementCounter200ResponseAnyOf1.from_dict(increment_counter200_response_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


