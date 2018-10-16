# pybridge.DefaultApi

All URIs are relative to *https://sync.bankin.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_user**](DefaultApi.md#authenticate_user) | **POST** /authenticate | Authenticate a User
[**check_email_validation**](DefaultApi.md#check_email_validation) | **GET** /users/me/email/confirmation | check Email Validation
[**create_user**](DefaultApi.md#create_user) | **POST** /users | Create a User
[**delete_all_users**](DefaultApi.md#delete_all_users) | **DELETE** /users | Delete all users
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /users/{uuid} | delete a User
[**edit_user**](DefaultApi.md#edit_user) | **PUT** /users/{uuid} | edit User credentials
[**get_all_banks**](DefaultApi.md#get_all_banks) | **GET** /banks | get All banks
[**get_email_validation_url**](DefaultApi.md#get_email_validation_url) | **GET** /connect/users/email/confirmation/url | get the URL for email validation
[**list_users**](DefaultApi.md#list_users) | **GET** /users | List users


# **authenticate_user**
> InlineResponse2005 authenticate_user(email, password)

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

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_email_validation**
> InlineResponse2002 check_email_validation()

check Email Validation

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
    # check Email Validation
    api_response = api_instance.check_email_validation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->check_email_validation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(email, password, empty_body=empty_body)

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
empty_body = pybridge.EmptyBody() # EmptyBody |  (optional)

try:
    # Create a User
    api_response = api_instance.create_user(email, password, empty_body=empty_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User&#39;s email address. | 
 **password** | **str**| User&#39;s password. Must be at least 6 characters and less than 255 characters.  | 
 **empty_body** | [**EmptyBody**](EmptyBody.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_user**
> delete_user(password)

delete a User

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
password = 'password_example' # str | 

try:
    # delete a User
    api_instance.delete_user(password)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user**
> InlineResponse2001 edit_user(current_password, new_password)

edit User credentials

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
current_password = 'current_password_example' # str | 
new_password = 'new_password_example' # str | 

try:
    # edit User credentials
    api_response = api_instance.edit_user(current_password, new_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->edit_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current_password** | **str**|  | 
 **new_password** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_banks**
> InlineResponse2004 get_all_banks()

get All banks

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
    # get All banks
    api_response = api_instance.get_all_banks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_banks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_validation_url**
> InlineResponse2003 get_email_validation_url()

get the URL for email validation

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
    # get the URL for email validation
    api_response = api_instance.get_email_validation_url()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_email_validation_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> InlineResponse200 list_users()

List users

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
    # List users
    api_response = api_instance.list_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ClientId](../README.md#ClientId), [ClientSecret](../README.md#ClientSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

