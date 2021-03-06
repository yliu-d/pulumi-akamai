# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class DnsRecord(pulumi.CustomResource):
    active: pulumi.Output[bool]
    """
    — (Required,Boolean) Whether the record is active.  
    """
    algorithm: pulumi.Output[float]
    digest: pulumi.Output[str]
    digest_type: pulumi.Output[float]
    expiration: pulumi.Output[str]
    fingerprint: pulumi.Output[str]
    fingerprint_type: pulumi.Output[float]
    flags: pulumi.Output[float]
    flagsnaptr: pulumi.Output[str]
    hardware: pulumi.Output[str]
    inception: pulumi.Output[str]
    iterations: pulumi.Output[float]
    key: pulumi.Output[str]
    keytag: pulumi.Output[float]
    labels: pulumi.Output[float]
    mailbox: pulumi.Output[str]
    name: pulumi.Output[str]
    """
    — (Required) The name of the record. The name is an owner name, that is, the name of the node to which this resource record pertains.  
    """
    next_hashed_owner_name: pulumi.Output[str]
    order: pulumi.Output[float]
    original_ttl: pulumi.Output[float]
    port: pulumi.Output[float]
    preference: pulumi.Output[float]
    priority: pulumi.Output[float]
    priority_increment: pulumi.Output[float]
    protocol: pulumi.Output[float]
    recordtype: pulumi.Output[str]
    regexp: pulumi.Output[str]
    replacement: pulumi.Output[str]
    salt: pulumi.Output[str]
    service: pulumi.Output[str]
    signature: pulumi.Output[str]
    signer: pulumi.Output[str]
    software: pulumi.Output[str]
    subtype: pulumi.Output[float]
    targets: pulumi.Output[list]
    """
    — (Required) A domain name that specifies the canonical or primary name for the owner. The owner name is an alias.  
    """
    ttl: pulumi.Output[float]
    """
    — (Required,Boolean) The TTL is a 32-bit signed integer that specifies the time interval that the resource record may be cached before the source of the information should be consulted again. Zero values are interpreted to mean that the RR can only be used for the transaction in progress, and should not be cached. Zero values can also be used for extremely volatile data.  
    """
    txt: pulumi.Output[str]
    type_bitmaps: pulumi.Output[str]
    type_covered: pulumi.Output[str]
    weight: pulumi.Output[float]
    zone: pulumi.Output[str]
    """
    — (Required) Domain zone, encapsulating any nested subdomains.  
    """
    def __init__(__self__, resource_name, opts=None, active=None, algorithm=None, digest=None, digest_type=None, expiration=None, fingerprint=None, fingerprint_type=None, flags=None, flagsnaptr=None, hardware=None, inception=None, iterations=None, key=None, keytag=None, labels=None, mailbox=None, name=None, next_hashed_owner_name=None, order=None, original_ttl=None, port=None, preference=None, priority=None, priority_increment=None, protocol=None, recordtype=None, regexp=None, replacement=None, salt=None, service=None, signature=None, signer=None, software=None, subtype=None, targets=None, ttl=None, txt=None, type_bitmaps=None, type_covered=None, weight=None, zone=None, __props__=None, __name__=None, __opts__=None):
        """
        The `EdgeDNS.DnsRecord` provides the resource for configuring a dns record to integrate easily with your existing DNS infrastructure to provide a secure, high performance, highly available and scalable solution for DNS hosting.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: — (Required,Boolean) Whether the record is active.  
        :param pulumi.Input[str] name: — (Required) The name of the record. The name is an owner name, that is, the name of the node to which this resource record pertains.  
        :param pulumi.Input[list] targets: — (Required) A domain name that specifies the canonical or primary name for the owner. The owner name is an alias.  
        :param pulumi.Input[float] ttl: — (Required,Boolean) The TTL is a 32-bit signed integer that specifies the time interval that the resource record may be cached before the source of the information should be consulted again. Zero values are interpreted to mean that the RR can only be used for the transaction in progress, and should not be cached. Zero values can also be used for extremely volatile data.  
        :param pulumi.Input[str] zone: — (Required) Domain zone, encapsulating any nested subdomains.  
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

            if active is None:
                raise TypeError("Missing required property 'active'")
            __props__['active'] = active
            __props__['algorithm'] = algorithm
            __props__['digest'] = digest
            __props__['digest_type'] = digest_type
            __props__['expiration'] = expiration
            __props__['fingerprint'] = fingerprint
            __props__['fingerprint_type'] = fingerprint_type
            __props__['flags'] = flags
            __props__['flagsnaptr'] = flagsnaptr
            __props__['hardware'] = hardware
            __props__['inception'] = inception
            __props__['iterations'] = iterations
            __props__['key'] = key
            __props__['keytag'] = keytag
            __props__['labels'] = labels
            __props__['mailbox'] = mailbox
            __props__['name'] = name
            __props__['next_hashed_owner_name'] = next_hashed_owner_name
            __props__['order'] = order
            __props__['original_ttl'] = original_ttl
            __props__['port'] = port
            __props__['preference'] = preference
            __props__['priority'] = priority
            __props__['priority_increment'] = priority_increment
            __props__['protocol'] = protocol
            if recordtype is None:
                raise TypeError("Missing required property 'recordtype'")
            __props__['recordtype'] = recordtype
            __props__['regexp'] = regexp
            __props__['replacement'] = replacement
            __props__['salt'] = salt
            __props__['service'] = service
            __props__['signature'] = signature
            __props__['signer'] = signer
            __props__['software'] = software
            __props__['subtype'] = subtype
            __props__['targets'] = targets
            if ttl is None:
                raise TypeError("Missing required property 'ttl'")
            __props__['ttl'] = ttl
            __props__['txt'] = txt
            __props__['type_bitmaps'] = type_bitmaps
            __props__['type_covered'] = type_covered
            __props__['weight'] = weight
            if zone is None:
                raise TypeError("Missing required property 'zone'")
            __props__['zone'] = zone
        super(DnsRecord, __self__).__init__(
            'akamai:EdgeDNS/dnsRecord:DnsRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, active=None, algorithm=None, digest=None, digest_type=None, expiration=None, fingerprint=None, fingerprint_type=None, flags=None, flagsnaptr=None, hardware=None, inception=None, iterations=None, key=None, keytag=None, labels=None, mailbox=None, name=None, next_hashed_owner_name=None, order=None, original_ttl=None, port=None, preference=None, priority=None, priority_increment=None, protocol=None, recordtype=None, regexp=None, replacement=None, salt=None, service=None, signature=None, signer=None, software=None, subtype=None, targets=None, ttl=None, txt=None, type_bitmaps=None, type_covered=None, weight=None, zone=None):
        """
        Get an existing DnsRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: — (Required,Boolean) Whether the record is active.  
        :param pulumi.Input[str] name: — (Required) The name of the record. The name is an owner name, that is, the name of the node to which this resource record pertains.  
        :param pulumi.Input[list] targets: — (Required) A domain name that specifies the canonical or primary name for the owner. The owner name is an alias.  
        :param pulumi.Input[float] ttl: — (Required,Boolean) The TTL is a 32-bit signed integer that specifies the time interval that the resource record may be cached before the source of the information should be consulted again. Zero values are interpreted to mean that the RR can only be used for the transaction in progress, and should not be cached. Zero values can also be used for extremely volatile data.  
        :param pulumi.Input[str] zone: — (Required) Domain zone, encapsulating any nested subdomains.  
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["active"] = active
        __props__["algorithm"] = algorithm
        __props__["digest"] = digest
        __props__["digest_type"] = digest_type
        __props__["expiration"] = expiration
        __props__["fingerprint"] = fingerprint
        __props__["fingerprint_type"] = fingerprint_type
        __props__["flags"] = flags
        __props__["flagsnaptr"] = flagsnaptr
        __props__["hardware"] = hardware
        __props__["inception"] = inception
        __props__["iterations"] = iterations
        __props__["key"] = key
        __props__["keytag"] = keytag
        __props__["labels"] = labels
        __props__["mailbox"] = mailbox
        __props__["name"] = name
        __props__["next_hashed_owner_name"] = next_hashed_owner_name
        __props__["order"] = order
        __props__["original_ttl"] = original_ttl
        __props__["port"] = port
        __props__["preference"] = preference
        __props__["priority"] = priority
        __props__["priority_increment"] = priority_increment
        __props__["protocol"] = protocol
        __props__["recordtype"] = recordtype
        __props__["regexp"] = regexp
        __props__["replacement"] = replacement
        __props__["salt"] = salt
        __props__["service"] = service
        __props__["signature"] = signature
        __props__["signer"] = signer
        __props__["software"] = software
        __props__["subtype"] = subtype
        __props__["targets"] = targets
        __props__["ttl"] = ttl
        __props__["txt"] = txt
        __props__["type_bitmaps"] = type_bitmaps
        __props__["type_covered"] = type_covered
        __props__["weight"] = weight
        __props__["zone"] = zone
        return DnsRecord(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

