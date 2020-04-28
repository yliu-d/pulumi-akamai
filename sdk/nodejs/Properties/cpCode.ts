// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The `akamai.Properties.CpCode` resource allows you to create or re-use CP Codes.
 * 
 * If the CP Code already exists it will be used instead of creating a new one.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as akamai from "@pulumi/akamai";
 * 
 * const cpCode = new akamai.Properties.CpCode("cpCode", {
 *     contract: akamai_contract_contract.id,
 *     group: akamai_group_group.id,
 *     product: "prdXxx",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-akamai/blob/master/website/docs/r/cp_code.html.markdown.
 */
export class CpCode extends pulumi.CustomResource {
    /**
     * Get an existing CpCode resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CpCodeState, opts?: pulumi.CustomResourceOptions): CpCode {
        return new CpCode(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'akamai:Properties/cpCode:CpCode';

    /**
     * Returns true if the given object is an instance of CpCode.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CpCode {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CpCode.__pulumiType;
    }

    /**
     * — (Required) The Contract ID
     */
    public readonly contract!: pulumi.Output<string>;
    /**
     * — (Required) The Group ID
     */
    public readonly group!: pulumi.Output<string>;
    /**
     * — (Required) The CP Code name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * — (Required) The Product ID
     */
    public readonly product!: pulumi.Output<string>;

    /**
     * Create a CpCode resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CpCodeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CpCodeArgs | CpCodeState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as CpCodeState | undefined;
            inputs["contract"] = state ? state.contract : undefined;
            inputs["group"] = state ? state.group : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["product"] = state ? state.product : undefined;
        } else {
            const args = argsOrState as CpCodeArgs | undefined;
            if (!args || args.contract === undefined) {
                throw new Error("Missing required property 'contract'");
            }
            if (!args || args.group === undefined) {
                throw new Error("Missing required property 'group'");
            }
            if (!args || args.product === undefined) {
                throw new Error("Missing required property 'product'");
            }
            inputs["contract"] = args ? args.contract : undefined;
            inputs["group"] = args ? args.group : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["product"] = args ? args.product : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(CpCode.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CpCode resources.
 */
export interface CpCodeState {
    /**
     * — (Required) The Contract ID
     */
    readonly contract?: pulumi.Input<string>;
    /**
     * — (Required) The Group ID
     */
    readonly group?: pulumi.Input<string>;
    /**
     * — (Required) The CP Code name
     */
    readonly name?: pulumi.Input<string>;
    /**
     * — (Required) The Product ID
     */
    readonly product?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CpCode resource.
 */
export interface CpCodeArgs {
    /**
     * — (Required) The Contract ID
     */
    readonly contract: pulumi.Input<string>;
    /**
     * — (Required) The Group ID
     */
    readonly group: pulumi.Input<string>;
    /**
     * — (Required) The CP Code name
     */
    readonly name?: pulumi.Input<string>;
    /**
     * — (Required) The Product ID
     */
    readonly product: pulumi.Input<string>;
}
