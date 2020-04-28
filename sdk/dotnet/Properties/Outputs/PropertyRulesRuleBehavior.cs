// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Akamai.Properties.Outputs
{

    [OutputType]
    public sealed class PropertyRulesRuleBehavior
    {
        public readonly string Name;
        public readonly ImmutableArray<Outputs.PropertyRulesRuleBehaviorOption> Options;

        [OutputConstructor]
        private PropertyRulesRuleBehavior(
            string name,

            ImmutableArray<Outputs.PropertyRulesRuleBehaviorOption> options)
        {
            Name = name;
            Options = options;
        }
    }
}
