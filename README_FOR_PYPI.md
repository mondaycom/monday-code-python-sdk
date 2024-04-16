# monday-code


## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install monday-code
```

Then import the package:
```python
import monday_code
```

## Getting Started

```python

import monday_code
from monday_code.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:59999
# See configuration.py for a list of all supported configuration parameters.
configuration = monday_code.Configuration()

# Enter a context with an instance of the API client
with monday_code.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monday_code.QueueApi(api_client)
    publish_message_params = monday_code.PublishMessageParams() # PublishMessageParams | 

    try:
        api_response = api_instance.publish_message(publish_message_params)
        print("The response of QueueApi->publish_message:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueueApi->publish_message: %s\n" % e)

```

## Documentation 
Further documentation could be found at [GitHub](https://github.com/mondaycom/monday-code-python-sdk)