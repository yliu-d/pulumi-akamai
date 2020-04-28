# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GtmDomain(pulumi.CustomResource):
    cname_coalescing_enabled: pulumi.Output[bool]
    """
    — (Boolean)
    """
    comment: pulumi.Output[str]
    """
    — A descriptive comment
    """
    contract: pulumi.Output[str]
    """
    — The contract ID (if creating domain) 
    """
    default_error_penalty: pulumi.Output[float]
    """
    — (Default: 75)
    """
    default_health_max: pulumi.Output[float]
    default_health_multiplier: pulumi.Output[float]
    default_health_threshold: pulumi.Output[float]
    default_max_unreachable_penalty: pulumi.Output[float]
    default_ssl_client_certificate: pulumi.Output[str]
    default_ssl_client_private_key: pulumi.Output[str]
    default_timeout_penalty: pulumi.Output[float]
    """
    — (Default: 25)
    * `load_imbalance_percentage`
    * `default_ssl_client_private_key`
    """
    default_unreachable_threshold: pulumi.Output[float]
    """

    * `min_pingable_region_fraction`
    * `servermonitor_liveness_count`
    * `round_robin_prefix`
    * `servermonitor_load_count`
    * `ping_interval`
    * `max_ttl`
    * `default_health_max`
    * `map_update_interval`
    * `max_properties`
    * `max_resources`
    * `default_error_penalty`
    * `max_test_timeout`
    * `default_health_multiplier`
    * `servermonitor_pool`
    * `min_ttl`
    * `default_max_unreachable_penalty`
    * `default_health_threshold`
    * `min_test_interval`
    * `ping_packet_size`
    """
    email_notification_lists: pulumi.Output[list]
    """
    — (List)
    """
    end_user_mapping_enabled: pulumi.Output[bool]
    """
    — (Boolean)
    """
    group: pulumi.Output[str]
    """
    — The currently selected group ID (if creating domain)   
    """
    load_feedback: pulumi.Output[bool]
    """
    — (Boolean)
    * `default_ssl_client_certificate`
    """
    load_imbalance_percentage: pulumi.Output[float]
    map_update_interval: pulumi.Output[float]
    max_properties: pulumi.Output[float]
    max_resources: pulumi.Output[float]
    max_test_timeout: pulumi.Output[float]
    max_ttl: pulumi.Output[float]
    min_pingable_region_fraction: pulumi.Output[float]
    min_test_interval: pulumi.Output[float]
    min_ttl: pulumi.Output[float]
    name: pulumi.Output[str]
    """
    — Domain name  
    """
    ping_interval: pulumi.Output[float]
    ping_packet_size: pulumi.Output[float]
    round_robin_prefix: pulumi.Output[str]
    servermonitor_liveness_count: pulumi.Output[float]
    servermonitor_load_count: pulumi.Output[float]
    servermonitor_pool: pulumi.Output[str]
    type: pulumi.Output[str]
    """
    — Domain type  
    """
    wait_on_complete: pulumi.Output[bool]
    """
    — (Boolean, Default: true) Wait for transaction to complete
    """
    def __init__(__self__, resource_name, opts=None, cname_coalescing_enabled=None, comment=None, contract=None, default_error_penalty=None, default_ssl_client_certificate=None, default_ssl_client_private_key=None, default_timeout_penalty=None, email_notification_lists=None, end_user_mapping_enabled=None, group=None, load_feedback=None, load_imbalance_percentage=None, name=None, type=None, wait_on_complete=None, __props__=None, __name__=None, __opts__=None):
        """
        `TrafficManagement.GtmDomain` provides the resource for creating, configuring and importing a gtm domain to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: `existing_domain_name`



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cname_coalescing_enabled: — (Boolean)
        :param pulumi.Input[str] comment: — A descriptive comment
        :param pulumi.Input[str] contract: — The contract ID (if creating domain) 
        :param pulumi.Input[float] default_error_penalty: — (Default: 75)
        :param pulumi.Input[float] default_timeout_penalty: — (Default: 25)
               * `load_imbalance_percentage`
               * `default_ssl_client_private_key`
        :param pulumi.Input[list] email_notification_lists: — (List)
        :param pulumi.Input[bool] end_user_mapping_enabled: — (Boolean)
        :param pulumi.Input[str] group: — The currently selected group ID (if creating domain)   
        :param pulumi.Input[bool] load_feedback: — (Boolean)
               * `default_ssl_client_certificate`
        :param pulumi.Input[str] name: — Domain name  
        :param pulumi.Input[str] type: — Domain type  
        :param pulumi.Input[bool] wait_on_complete: — (Boolean, Default: true) Wait for transaction to complete
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['cname_coalescing_enabled'] = cname_coalescing_enabled
            __props__['comment'] = comment
            __props__['contract'] = contract
            __props__['default_error_penalty'] = default_error_penalty
            __props__['default_ssl_client_certificate'] = default_ssl_client_certificate
            __props__['default_ssl_client_private_key'] = default_ssl_client_private_key
            __props__['default_timeout_penalty'] = default_timeout_penalty
            __props__['email_notification_lists'] = email_notification_lists
            __props__['end_user_mapping_enabled'] = end_user_mapping_enabled
            __props__['group'] = group
            __props__['load_feedback'] = load_feedback
            __props__['load_imbalance_percentage'] = load_imbalance_percentage
            __props__['name'] = name
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['wait_on_complete'] = wait_on_complete
            __props__['default_health_max'] = None
            __props__['default_health_multiplier'] = None
            __props__['default_health_threshold'] = None
            __props__['default_max_unreachable_penalty'] = None
            __props__['default_unreachable_threshold'] = None
            __props__['map_update_interval'] = None
            __props__['max_properties'] = None
            __props__['max_resources'] = None
            __props__['max_test_timeout'] = None
            __props__['max_ttl'] = None
            __props__['min_pingable_region_fraction'] = None
            __props__['min_test_interval'] = None
            __props__['min_ttl'] = None
            __props__['ping_interval'] = None
            __props__['ping_packet_size'] = None
            __props__['round_robin_prefix'] = None
            __props__['servermonitor_liveness_count'] = None
            __props__['servermonitor_load_count'] = None
            __props__['servermonitor_pool'] = None
        super(GtmDomain, __self__).__init__(
            'akamai:TrafficManagement/gtmDomain:GtmDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cname_coalescing_enabled=None, comment=None, contract=None, default_error_penalty=None, default_health_max=None, default_health_multiplier=None, default_health_threshold=None, default_max_unreachable_penalty=None, default_ssl_client_certificate=None, default_ssl_client_private_key=None, default_timeout_penalty=None, default_unreachable_threshold=None, email_notification_lists=None, end_user_mapping_enabled=None, group=None, load_feedback=None, load_imbalance_percentage=None, map_update_interval=None, max_properties=None, max_resources=None, max_test_timeout=None, max_ttl=None, min_pingable_region_fraction=None, min_test_interval=None, min_ttl=None, name=None, ping_interval=None, ping_packet_size=None, round_robin_prefix=None, servermonitor_liveness_count=None, servermonitor_load_count=None, servermonitor_pool=None, type=None, wait_on_complete=None):
        """
        Get an existing GtmDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cname_coalescing_enabled: — (Boolean)
        :param pulumi.Input[str] comment: — A descriptive comment
        :param pulumi.Input[str] contract: — The contract ID (if creating domain) 
        :param pulumi.Input[float] default_error_penalty: — (Default: 75)
        :param pulumi.Input[float] default_timeout_penalty: — (Default: 25)
               * `load_imbalance_percentage`
               * `default_ssl_client_private_key`
        :param pulumi.Input[float] default_unreachable_threshold: 
               * `min_pingable_region_fraction`
               * `servermonitor_liveness_count`
               * `round_robin_prefix`
               * `servermonitor_load_count`
               * `ping_interval`
               * `max_ttl`
               * `default_health_max`
               * `map_update_interval`
               * `max_properties`
               * `max_resources`
               * `default_error_penalty`
               * `max_test_timeout`
               * `default_health_multiplier`
               * `servermonitor_pool`
               * `min_ttl`
               * `default_max_unreachable_penalty`
               * `default_health_threshold`
               * `min_test_interval`
               * `ping_packet_size`
        :param pulumi.Input[list] email_notification_lists: — (List)
        :param pulumi.Input[bool] end_user_mapping_enabled: — (Boolean)
        :param pulumi.Input[str] group: — The currently selected group ID (if creating domain)   
        :param pulumi.Input[bool] load_feedback: — (Boolean)
               * `default_ssl_client_certificate`
        :param pulumi.Input[str] name: — Domain name  
        :param pulumi.Input[str] type: — Domain type  
        :param pulumi.Input[bool] wait_on_complete: — (Boolean, Default: true) Wait for transaction to complete
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cname_coalescing_enabled"] = cname_coalescing_enabled
        __props__["comment"] = comment
        __props__["contract"] = contract
        __props__["default_error_penalty"] = default_error_penalty
        __props__["default_health_max"] = default_health_max
        __props__["default_health_multiplier"] = default_health_multiplier
        __props__["default_health_threshold"] = default_health_threshold
        __props__["default_max_unreachable_penalty"] = default_max_unreachable_penalty
        __props__["default_ssl_client_certificate"] = default_ssl_client_certificate
        __props__["default_ssl_client_private_key"] = default_ssl_client_private_key
        __props__["default_timeout_penalty"] = default_timeout_penalty
        __props__["default_unreachable_threshold"] = default_unreachable_threshold
        __props__["email_notification_lists"] = email_notification_lists
        __props__["end_user_mapping_enabled"] = end_user_mapping_enabled
        __props__["group"] = group
        __props__["load_feedback"] = load_feedback
        __props__["load_imbalance_percentage"] = load_imbalance_percentage
        __props__["map_update_interval"] = map_update_interval
        __props__["max_properties"] = max_properties
        __props__["max_resources"] = max_resources
        __props__["max_test_timeout"] = max_test_timeout
        __props__["max_ttl"] = max_ttl
        __props__["min_pingable_region_fraction"] = min_pingable_region_fraction
        __props__["min_test_interval"] = min_test_interval
        __props__["min_ttl"] = min_ttl
        __props__["name"] = name
        __props__["ping_interval"] = ping_interval
        __props__["ping_packet_size"] = ping_packet_size
        __props__["round_robin_prefix"] = round_robin_prefix
        __props__["servermonitor_liveness_count"] = servermonitor_liveness_count
        __props__["servermonitor_load_count"] = servermonitor_load_count
        __props__["servermonitor_pool"] = servermonitor_pool
        __props__["type"] = type
        __props__["wait_on_complete"] = wait_on_complete
        return GtmDomain(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

