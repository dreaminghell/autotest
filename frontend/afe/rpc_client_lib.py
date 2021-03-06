"""
This module provides utility functions useful when writing clients for the RPC
server.
"""

__author__ = 'showard@google.com (Steve Howard)'

import getpass
import os

from autotest.client.shared import utils

from json_rpc import proxy


class AuthError(Exception):
    pass


def get_proxy(*args, **kwargs):
    """Use this to access the AFE or TKO RPC interfaces."""
    return proxy.ServiceProxy(*args, **kwargs)


def _base_authorization_headers(username, server):
    """
    Don't call this directly, call authorization_headers().
    This implementation may be overridden by site code.

    :return: A dictionary of authorization headers to pass in to get_proxy().
    """
    if not username:
        if 'AUTOTEST_USER' in os.environ:
            username = os.environ['AUTOTEST_USER']
        else:
            username = getpass.getuser()
    return {'AUTHORIZATION': username}


authorization_headers = utils.import_site_function(
    __file__, 'autotest.frontend.afe.site_rpc_client_lib',
    'authorization_headers', _base_authorization_headers)
