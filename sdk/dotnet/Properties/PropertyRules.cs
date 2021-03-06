// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Akamai.Properties
{
    public partial class PropertyRules : Pulumi.CustomResource
    {
        /// <summary>
        /// JSON Rule representation
        /// </summary>
        [Output("json")]
        public Output<string> Json { get; private set; } = null!;

        [Output("rules")]
        public Output<ImmutableArray<Outputs.PropertyRulesRule>> Rules { get; private set; } = null!;

        [Output("variables")]
        public Output<string?> Variables { get; private set; } = null!;


        /// <summary>
        /// Create a PropertyRules resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PropertyRules(string name, PropertyRulesArgs? args = null, CustomResourceOptions? options = null)
            : base("akamai:Properties/propertyRules:PropertyRules", name, args ?? new PropertyRulesArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PropertyRules(string name, Input<string> id, PropertyRulesState? state = null, CustomResourceOptions? options = null)
            : base("akamai:Properties/propertyRules:PropertyRules", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PropertyRules resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PropertyRules Get(string name, Input<string> id, PropertyRulesState? state = null, CustomResourceOptions? options = null)
        {
            return new PropertyRules(name, id, state, options);
        }
    }

    public sealed class PropertyRulesArgs : Pulumi.ResourceArgs
    {
        [Input("rules")]
        private InputList<Inputs.PropertyRulesRuleArgs>? _rules;
        public InputList<Inputs.PropertyRulesRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.PropertyRulesRuleArgs>());
            set => _rules = value;
        }

        [Input("variables")]
        public Input<string>? Variables { get; set; }

        public PropertyRulesArgs()
        {
        }
    }

    public sealed class PropertyRulesState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// JSON Rule representation
        /// </summary>
        [Input("json")]
        public Input<string>? Json { get; set; }

        [Input("rules")]
        private InputList<Inputs.PropertyRulesRuleGetArgs>? _rules;
        public InputList<Inputs.PropertyRulesRuleGetArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.PropertyRulesRuleGetArgs>());
            set => _rules = value;
        }

        [Input("variables")]
        public Input<string>? Variables { get; set; }

        public PropertyRulesState()
        {
        }
    }
}
