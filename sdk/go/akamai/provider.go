// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package akamai

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The provider type for the akamai package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:akamai", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	Dns             []ProviderDn       `pulumi:"dns"`
	DnsSection      *string            `pulumi:"dnsSection"`
	Edgerc          *string            `pulumi:"edgerc"`
	GtmSection      *string            `pulumi:"gtmSection"`
	Gtms            []ProviderGtm      `pulumi:"gtms"`
	PapiSection     *string            `pulumi:"papiSection"`
	Properties      []ProviderProperty `pulumi:"properties"`
	PropertySection *string            `pulumi:"propertySection"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	Dns             ProviderDnArrayInput
	DnsSection      pulumi.StringPtrInput
	Edgerc          pulumi.StringPtrInput
	GtmSection      pulumi.StringPtrInput
	Gtms            ProviderGtmArrayInput
	PapiSection     pulumi.StringPtrInput
	Properties      ProviderPropertyArrayInput
	PropertySection pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}
