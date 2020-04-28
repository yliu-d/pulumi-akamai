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
    public sealed class GetPropertyRulesRuleBehaviorResult
    {
        /// <summary>
        /// — (Required) The name of the behavior.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// — (Optional) One or more options for the behavior.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPropertyRulesRuleBehaviorOptionResult> Options;

        [OutputConstructor]
        private GetPropertyRulesRuleBehaviorResult(
            string name,

            ImmutableArray<Outputs.GetPropertyRulesRuleBehaviorOptionResult> options)
        {
            Name = name;
            Options = options;
        }
    }
}
