# IncrementCounterParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**renewal_date** | **datetime** |  | 
**kind** | **str** |  | 
**increment_by** | **float** |  | 
**period** | [**Period**](Period.md) |  | 

## Example

```python
from monday_code.models.increment_counter_params import IncrementCounterParams

# TODO update the JSON string below
json = "{}"
# create an instance of IncrementCounterParams from a JSON string
increment_counter_params_instance = IncrementCounterParams.from_json(json)
# print the JSON string representation of the object
print IncrementCounterParams.to_json()

# convert the object into a dict
increment_counter_params_dict = increment_counter_params_instance.to_dict()
# create an instance of IncrementCounterParams from a dict
increment_counter_params_form_dict = increment_counter_params.from_dict(increment_counter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


