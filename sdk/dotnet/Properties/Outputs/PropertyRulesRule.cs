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
    public sealed class PropertyRulesRule
    {
        public readonly ImmutableArray<Outputs.PropertyRulesRuleBehavior> Behaviors;
        public readonly string? CriteriaMatch;
        public readonly bool? IsSecure;
        public readonly ImmutableArray<Outputs.PropertyRulesRuleRule> Rules;
        public readonly ImmutableArray<Outputs.PropertyRulesRuleVariable> Variables;

        [OutputConstructor]
        private PropertyRulesRule(
            ImmutableArray<Outputs.PropertyRulesRuleBehavior> behaviors,

            string? criteriaMatch,

            bool? isSecure,

            ImmutableArray<Outputs.PropertyRulesRuleRule> rules,

            ImmutableArray<Outputs.PropertyRulesRuleVariable> variables)
        {
            Behaviors = behaviors;
            CriteriaMatch = criteriaMatch;
            IsSecure = isSecure;
            Rules = rules;
            Variables = variables;
        }
    }
}
