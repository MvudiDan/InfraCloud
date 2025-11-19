netmask_prefixes = {
    '255.255.255,255': '/32'
    ,'255.240.0.0': '/12'
    ,'255.224.0.0': '/11'
    ,'255.192.0.0': '/10'
    ,'255.128.0.0': '/9'
    ,'255.0.0,0': '/8'
}

def get_net_prefix(p_subnet_mask):
    try:
        net_prefix = netmask_prefixes[p_subnet_mask]
        return net_prefix

    except:
        return "Wrong input: garbage in, garbage out"

netmask_prefix = get_net_prefix('255.255.255.192')
print(netmask_prefix)