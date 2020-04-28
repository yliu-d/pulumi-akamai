// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Akamai.Inputs
{

    public sealed class ProviderPropertyArgs : Pulumi.ResourceArgs
    {
        [Input("accessToken")]
        public Input<string>? AccessToken { get; set; }

        [Input("clientSecret")]
        public Input<string>? ClientSecret { get; set; }

        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("maxBody")]
        public Input<int>? MaxBody { get; set; }

        public ProviderPropertyArgs()
        {
        }
    }
}
