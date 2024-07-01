# JsonDataContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | 

## Example

```python
from monday_code.models.json_data_contract import JsonDataContract

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataContract from a JSON string
json_data_contract_instance = JsonDataContract.from_json(json)
# print the JSON string representation of the object
print(JsonDataContract.to_json())

# convert the object into a dict
json_data_contract_dict = json_data_contract_instance.to_dict()
# create an instance of JsonDataContract from a dict
json_data_contract_from_dict = JsonDataContract.from_dict(json_data_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


