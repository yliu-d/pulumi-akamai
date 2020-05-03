// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The `akamai.EdgeDNS.DnsZone` provides the resource for configuring a dns zone to integrate easily with your existing DNS infrastructure to provide a secure, high performance, highly available and scalable solution for DNS hosting.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as akamai from "@pulumi/akamai";
 * 
 * const demozone = new akamai.EdgeDNS.DnsZone("demozone", {
 *     comment: "some comment",
 *     contract: "ctr_XXX",
 *     group: "100",
 *     masters: [
 *         "1.2.3.4",
 *         "1.2.3.5",
 *     ],
 *     signandserve: true,
 *     type: "primary",
 *     zone: "example.com",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-akamai/blob/master/website/docs/r/dns_zone.html.markdown.
 */
export class DnsZone extends pulumi.CustomResource {
    /**
     * Get an existing DnsZone resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DnsZoneState, opts?: pulumi.CustomResourceOptions): DnsZone {
        return new DnsZone(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'akamai:EdgeDNS/dnsZone:DnsZone';

    /**
     * Returns true if the given object is an instance of DnsZone.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DnsZone {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DnsZone.__pulumiType;
    }

    /**
     * — (Required) A descriptive comment.  
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * — (Required) The contract ID. 
     */
    public readonly contract!: pulumi.Output<string>;
    /**
     * — (Required) The currently selected group ID.   
     */
    public readonly group!: pulumi.Output<string>;
    /**
     * — (Required) The names or addresses of the customer’s nameservers from which the zone data should be retrieved.  
     */
    public readonly masters!: pulumi.Output<string[] | undefined>;
    /**
     * — (Required) Whether DNSSEC Sign&Serve is enabled.  
     */
    public readonly signAndServe!: pulumi.Output<boolean>;
    /**
     * — (Required) Whether the zone is primary or secondary.  
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * — (Required) Domain zone, encapsulating any nested subdomains.  
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a DnsZone resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DnsZoneArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DnsZoneArgs | DnsZoneState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DnsZoneState | undefined;
            inputs["comment"] = state ? state.comment : undefined;
            inputs["contract"] = state ? state.contract : undefined;
            inputs["group"] = state ? state.group : undefined;
            inputs["masters"] = state ? state.masters : undefined;
            inputs["signAndServe"] = state ? state.signAndServe : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as DnsZoneArgs | undefined;
            if (!args || args.contract === undefined) {
                throw new Error("Missing required property 'contract'");
            }
            if (!args || args.group === undefined) {
                throw new Error("Missing required property 'group'");
            }
            if (!args || args.signAndServe === undefined) {
                throw new Error("Missing required property 'signAndServe'");
            }
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            if (!args || args.zone === undefined) {
                throw new Error("Missing required property 'zone'");
            }
            inputs["comment"] = args ? args.comment : undefined;
            inputs["contract"] = args ? args.contract : undefined;
            inputs["group"] = args ? args.group : undefined;
            inputs["masters"] = args ? args.masters : undefined;
            inputs["signAndServe"] = args ? args.signAndServe : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["zone"] = args ? args.zone : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DnsZone.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DnsZone resources.
 */
export interface DnsZoneState {
    /**
     * — (Required) A descriptive comment.  
     */
    readonly comment?: pulumi.Input<string>;
    /**
     * — (Required) The contract ID. 
     */
    readonly contract?: pulumi.Input<string>;
    /**
     * — (Required) The currently selected group ID.   
     */
    readonly group?: pulumi.Input<string>;
    /**
     * — (Required) The names or addresses of the customer’s nameservers from which the zone data should be retrieved.  
     */
    readonly masters?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * — (Required) Whether DNSSEC Sign&Serve is enabled.  
     */
    readonly signAndServe?: pulumi.Input<boolean>;
    /**
     * — (Required) Whether the zone is primary or secondary.  
     */
    readonly type?: pulumi.Input<string>;
    /**
     * — (Required) Domain zone, encapsulating any nested subdomains.  
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DnsZone resource.
 */
export interface DnsZoneArgs {
    /**
     * — (Required) A descriptive comment.  
     */
    readonly comment?: pulumi.Input<string>;
    /**
     * — (Required) The contract ID. 
     */
    readonly contract: pulumi.Input<string>;
    /**
     * — (Required) The currently selected group ID.   
     */
    readonly group: pulumi.Input<string>;
    /**
     * — (Required) The names or addresses of the customer’s nameservers from which the zone data should be retrieved.  
     */
    readonly masters?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * — (Required) Whether DNSSEC Sign&Serve is enabled.  
     */
    readonly signAndServe: pulumi.Input<boolean>;
    /**
     * — (Required) Whether the zone is primary or secondary.  
     */
    readonly type: pulumi.Input<string>;
    /**
     * — (Required) Domain zone, encapsulating any nested subdomains.  
     */
    readonly zone: pulumi.Input<string>;
}