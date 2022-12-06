IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.1."
IPv6_STRING = "2001:0db8:85a3:0000:0000:FFFF:9FF9:9999"
IPv6_INVALID_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"
INVALID_IP_STRING = "Some arbitrary string"


def is_valid_IPv4_octet(octet: str):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    for e in octet.split("."):
        digit = int(e)
        if 0 <= digit <= 255:
            p = True
        else:
            return False
    return p


def is_valid_IPv4(ip: str):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    if is_valid_IPv4_octet(ip) == True:
        amount = 0
        for p in ip.split("."):
            amount += 1
        if amount == 4:
            return True
        else:
            return False
    else:
        return False


def is_valid_IPv6_hextet(hextet: str):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    for e in hextet.split(":"):
        if len(e) == 4:
            g = int(e, 16)
            if 0 <= g <= 65535:
                return True
            else:
                return False
        else:
            return False


def is_valid_IPv6(ip: str):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    if is_valid_IPv6_hextet(ip) == True:
        amount = 0
        for p in ip.split(":"):
            amount += 1
        if amount == 8:
            return True
        else:
            return False
    else:
        return False


def is_valid_IP(ip: str):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if ip.__contains__("."):
        return is_valid_IPv4(ip)
    elif ip.__contains__(":"):
        return is_valid_IPv6(ip)
    else:
        return False


print(
    f"{IPv4_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_STRING))
print(
    f"{IPv4_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_INVALID_STRING),
 )
print(
    f"{IPv6_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_STRING))
print(
    f"{IPv6_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_INVALID_STRING),
 )
print(
    f"{INVALID_IP_STRING} is a valid IP Address:",
    is_valid_IP(INVALID_IP_STRING),
 )
