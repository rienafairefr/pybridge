# pybridge.DefaultApi

All URIs are relative to *https://sync.bankin.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_user**](DefaultApi.md#authenticate_user) | **POST** /authenticate | Authenticate a User
[**create_user**](DefaultApi.md#create_user) | **POST** /users | Create a User
[**delete_all_users**](DefaultApi.md#delete_all_users) | **DELETE** /users | Delete all users


# **authenticate_user**
> InlineResponse200 authenticate_user(email, password)

Authenticate a User

### Example
```python
from __future__ import print_function
import time
import pybridge
from pybridge.rest import ApiException
from pprint import pprint

# Configure API key authorization: ClientId
configuration = pybridge.Configuration()
configuration.api_key['client_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['client_id'] = 'Bearer'
# Configure API key authorization: ClientSecret
configuration = pybridge.Configuration()
configuration.api_key['client_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['client_secret'] = 'Bearer'

# create an instance of the API class
api_instance = pybridge.DefaultApi(pybridge.ApiClient(configuration))
email = 'email_example' # str | User's email address.
password = 'password_example' # str | User's password. Must be at least 6 characters and less than 255 characters. 

try:
    # Authenticate a User
    api_response = api_instance.authenticate_user(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->authenticate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User&#39;s email address. | 
 **password** | **str**| User&#39;s password. Must be at least 6 characters and less than 255 characters.  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(email, password)

Create a User

### Example
```python
from __future__ import print_function
import time
import pybridge
from pybridge.rest import ApiException
from pprint import pprint

# Configure API key authorization: ClientId
configuration = pybridge.Configuration()
configuration.api_key['client_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['client_id'] = 'Bearer'
# Configure API key authorization: ClientSecret
configuration = pybridge.Configuration()
configuration.api_key['client_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['client_secret'] = 'Bearer'

# create an instance of the API class
api_instance = pybridge.DefaultApi(pybridge.ApiClient(configuration))
email = 'email_example' # str | User's email address.
password = 'password_example' # str | User's password. Must be at least 6 characters and less than 255 characters. 

try:
    # Create a User
    api_response = api_instance.create_user(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User&#39;s email address. | 
 **password** | **str**| User&#39;s password. Must be at least 6 characters and less than 255 characters.  | 

### Return type

[**User**](User.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_users**
> delete_all_users()

Delete all users

### Example
```python
from __future__ import print_function
import time
import pybridge
from pybridge.rest import ApiException
from pprint import pprint

# Configure API key authorization: ClientId
configuration = pybridge.Configuration()
configuration.api_key['client_id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['client_id'] = 'Bearer'
# Configure API key authorization: ClientSecret
configuration = pybridge.Configuration()
configuration.api_key['client_secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['client_secret'] = 'Bearer'

# create an instance of the API class
api_instance = pybridge.DefaultApi(pybridge.ApiClient(configuration))

try:
    # Delete all users
    api_instance.delete_all_users()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_all_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

