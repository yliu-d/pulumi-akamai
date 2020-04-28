// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Akamai.Properties.Inputs
{

    public sealed class PropertyRulesRuleRuleRuleRuleRuleGetArgs : Pulumi.ResourceArgs
    {
        [Input("behaviors")]
        private InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleBehaviorGetArgs>? _behaviors;
        public InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleBehaviorGetArgs> Behaviors
        {
            get => _behaviors ?? (_behaviors = new InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleBehaviorGetArgs>());
            set => _behaviors = value;
        }

        [Input("comment")]
        public Input<string>? Comment { get; set; }

        [Input("criteriaMatch")]
        public Input<string>? CriteriaMatch { get; set; }

        [Input("criterias")]
        private InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleCriteriaGetArgs>? _criterias;
        public InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleCriteriaGetArgs> Criterias
        {
            get => _criterias ?? (_criterias = new InputList<Inputs.PropertyRulesRuleRuleRuleRuleRuleCriteriaGetArgs>());
            set => _criterias = value;
        }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public PropertyRulesRuleRuleRuleRuleRuleGetArgs()
        {
        }
    }
}
