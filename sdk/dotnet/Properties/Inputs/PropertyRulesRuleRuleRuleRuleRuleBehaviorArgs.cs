// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Akamai.Properties.Inputs
{

    public sealed class PropertyRulesRuleRuleRuleRuleRuleBehaviorArgs : Pulumi.ResourceArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("options")]
        private InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleBehaviorOptionArgs>? _options;
        public InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleBehaviorOptionArgs> Options
        {
            get => _options ?? (_options = new InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleBehaviorOptionArgs>());
            set => _options = value;
        }

        public PropertyRulesRuleRuleRuleRuleRuleBehaviorArgs()
        {
        }
    }
}
