# coding: utf-8

"""
    Bridge API

    bridgeapi.io  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pybridge.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authenticate_user(self, email, password, **kwargs):  # noqa: E501
        """Authenticate a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate_user(email, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: User's email address. (required)
        :param str password: User's password. Must be at least 6 characters and less than 255 characters.  (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authenticate_user_with_http_info(email, password, **kwargs)  # noqa: E501
        else:
            (data) = self.authenticate_user_with_http_info(email, password, **kwargs)  # noqa: E501
            return data

    def authenticate_user_with_http_info(self, email, password, **kwargs):  # noqa: E501
        """Authenticate a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authenticate_user_with_http_info(email, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: User's email address. (required)
        :param str password: User's password. Must be at least 6 characters and less than 255 characters.  (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['email', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method authenticate_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in local_var_params or
                local_var_params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `authenticate_user`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in local_var_params or
                local_var_params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `authenticate_user`")  # noqa: E501

        if ('password' in local_var_params and
                len(local_var_params['password']) > 255):
            raise ValueError("Invalid value for parameter `password` when calling `authenticate_user`, length must be less than or equal to `255`")  # noqa: E501
        if ('password' in local_var_params and
                len(local_var_params['password']) < 6):
            raise ValueError("Invalid value for parameter `password` when calling `authenticate_user`, length must be greater than or equal to `6`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email' in local_var_params:
            query_params.append(('email', local_var_params['email']))  # noqa: E501
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/authenticate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def check_email_validation(self, **kwargs):  # noqa: E501
        """check Email Validation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_email_validation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_email_validation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.check_email_validation_with_http_info(**kwargs)  # noqa: E501
            return data

    def check_email_validation_with_http_info(self, **kwargs):  # noqa: E501
        """check Email Validation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_email_validation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_email_validation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/users/me/email/confirmation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_user(self, email, password, **kwargs):  # noqa: E501
        """Create a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user(email, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: User's email address. (required)
        :param str password: User's password. Must be at least 6 characters and less than 255 characters.  (required)
        :param EmptyBody empty_body:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_user_with_http_info(email, password, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_with_http_info(email, password, **kwargs)  # noqa: E501
            return data

    def create_user_with_http_info(self, email, password, **kwargs):  # noqa: E501
        """Create a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_user_with_http_info(email, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: User's email address. (required)
        :param str password: User's password. Must be at least 6 characters and less than 255 characters.  (required)
        :param EmptyBody empty_body:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['email', 'password', 'empty_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in local_var_params or
                local_var_params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `create_user`")  # noqa: E501
        # verify the required parameter 'password' is set
        if ('password' not in local_var_params or
                local_var_params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `create_user`")  # noqa: E501

        if ('password' in local_var_params and
                len(local_var_params['password']) > 255):
            raise ValueError("Invalid value for parameter `password` when calling `create_user`, length must be less than or equal to `255`")  # noqa: E501
        if ('password' in local_var_params and
                len(local_var_params['password']) < 6):
            raise ValueError("Invalid value for parameter `password` when calling `create_user`, length must be greater than or equal to `6`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email' in local_var_params:
            query_params.append(('email', local_var_params['email']))  # noqa: E501
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'empty_body' in local_var_params:
            body_params = local_var_params['empty_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_all_users(self, **kwargs):  # noqa: E501
        """Delete all users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_all_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_all_users_with_http_info(self, **kwargs):  # noqa: E501
        """Delete all users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_users" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user(self, password, **kwargs):  # noqa: E501
        """delete a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user(password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str password: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_with_http_info(password, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_with_http_info(password, **kwargs)  # noqa: E501
            return data

    def delete_user_with_http_info(self, password, **kwargs):  # noqa: E501
        """delete a User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_with_http_info(password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str password: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'password' is set
        if ('password' not in local_var_params or
                local_var_params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `delete_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'password' in local_var_params:
            query_params.append(('password', local_var_params['password']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/users/{uuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_user(self, current_password, new_password, **kwargs):  # noqa: E501
        """edit User credentials  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_user(current_password, new_password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str current_password: (required)
        :param str new_password: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_user_with_http_info(current_password, new_password, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_user_with_http_info(current_password, new_password, **kwargs)  # noqa: E501
            return data

    def edit_user_with_http_info(self, current_password, new_password, **kwargs):  # noqa: E501
        """edit User credentials  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_user_with_http_info(current_password, new_password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str current_password: (required)
        :param str new_password: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['current_password', 'new_password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'current_password' is set
        if ('current_password' not in local_var_params or
                local_var_params['current_password'] is None):
            raise ValueError("Missing the required parameter `current_password` when calling `edit_user`")  # noqa: E501
        # verify the required parameter 'new_password' is set
        if ('new_password' not in local_var_params or
                local_var_params['new_password'] is None):
            raise ValueError("Missing the required parameter `new_password` when calling `edit_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'current_password' in local_var_params:
            query_params.append(('current_password', local_var_params['current_password']))  # noqa: E501
        if 'new_password' in local_var_params:
            query_params.append(('new_password', local_var_params['new_password']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/users/{uuid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_banks(self, **kwargs):  # noqa: E501
        """get All banks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_banks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_banks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_banks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_banks_with_http_info(self, **kwargs):  # noqa: E501
        """get All banks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_banks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_banks" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/banks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_email_validation_url(self, **kwargs):  # noqa: E501
        """get the URL for email validation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_validation_url(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_email_validation_url_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_email_validation_url_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_email_validation_url_with_http_info(self, **kwargs):  # noqa: E501
        """get the URL for email validation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_email_validation_url_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_email_validation_url" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/connect/users/email/confirmation/url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_users(self, **kwargs):  # noqa: E501
        """List users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_users_with_http_info(self, **kwargs):  # noqa: E501
        """List users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_users" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ClientId', 'ClientSecret']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)