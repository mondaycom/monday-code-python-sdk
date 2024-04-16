# PublishMessageParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from monday_code.models.publish_message_params import PublishMessageParams

# TODO update the JSON string below
json = "{}"
# create an instance of PublishMessageParams from a JSON string
publish_message_params_instance = PublishMessageParams.from_json(json)
# print the JSON string representation of the object
print PublishMessageParams.to_json()

# convert the object into a dict
publish_message_params_dict = publish_message_params_instance.to_dict()
# create an instance of PublishMessageParams from a dict
publish_message_params_form_dict = publish_message_params.from_dict(publish_message_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


