// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Akamai.Properties.Inputs
{

    public sealed class PropertyVariablesVariableVariableArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// — (Optional) A human-readable description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// — (Optional) Whether to hide the variable when debugging requests
        /// </summary>
        [Input("hidden", required: true)]
        public Input<bool> Hidden { get; set; } = null!;

        /// <summary>
        /// — (Required) The name of the variable.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// — (Optional) Whether to obscure the value when debugging requests
        /// </summary>
        [Input("sensitive", required: true)]
        public Input<bool> Sensitive { get; set; } = null!;

        /// <summary>
        /// — (Required) The default value to assign to the variable
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public PropertyVariablesVariableVariableArgs()
        {
        }
    }
}