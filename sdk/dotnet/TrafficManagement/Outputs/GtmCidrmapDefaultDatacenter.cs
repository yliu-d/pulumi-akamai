// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Akamai.TrafficManagement.Outputs
{

    [OutputType]
    public sealed class GtmCidrmapDefaultDatacenter
    {
        public readonly int DatacenterId;
        public readonly string? Nickname;

        [OutputConstructor]
        private GtmCidrmapDefaultDatacenter(
            int datacenterId,

            string? nickname)
        {
            DatacenterId = datacenterId;
            Nickname = nickname;
        }
    }
}
