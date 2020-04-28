// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use `akamai.EdgeDNS.getAuthoritiesSet` datasource to retrieve a contracts authorities set for use when creating new zones.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as akamai from "@pulumi/akamai";
 * 
 * const example = pulumi.output(akamai.EdgeDNS.getAuthoritiesSet({
 *     contract: "ctr_#####",
 * }, { async: true }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-akamai/blob/master/website/docs/d/authorities_set.html.markdown.
 */
export function getAuthoritiesSet(args: GetAuthoritiesSetArgs, opts?: pulumi.InvokeOptions): Promise<GetAuthoritiesSetResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("akamai:EdgeDNS/getAuthoritiesSet:getAuthoritiesSet", {
        "contract": args.contract,
    }, opts);
}

/**
 * A collection of arguments for invoking getAuthoritiesSet.
 */
export interface GetAuthoritiesSetArgs {
    /**
     * — (Required) The contract ID.
     */
    readonly contract: string;
}

/**
 * A collection of values returned by getAuthoritiesSet.
 */
export interface GetAuthoritiesSetResult {
    readonly authorities: string[];
    readonly contract: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
