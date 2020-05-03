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
    public sealed class PropertyVariablesVariableVariable
    {
        /// <summary>
        /// — (Optional) A human-readable description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// — (Optional) Whether to hide the variable when debugging requests
        /// </summary>
        public readonly bool Hidden;
        /// <summary>
        /// — (Required) The name of the variable.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// — (Optional) Whether to obscure the value when debugging requests
        /// </summary>
        public readonly bool Sensitive;
        /// <summary>
        /// — (Required) The default value to assign to the variable
        /// </summary>
        public readonly string? Value;

        [OutputConstructor]
        private PropertyVariablesVariableVariable(
            string? description,

            bool hidden,

            string name,

            bool sensitive,

            string? value)
        {
            Description = description;
            Hidden = hidden;
            Name = name;
            Sensitive = sensitive;
            Value = value;
        }
    }
}