import binascii
from math import gcd


pubkeys = {
    "key1": 0x7292f12b97f2bb6810ab6de8c12b114015248a38fd516bf51a58e6a3443a4b705806253d709e70de0b567ae3b1dc012239ee518afb9b3623140055a8bd3a30254ea4998743bbb0edf1129c40e098ce28107f36d31776b2f153142caf79e325e47808f6f5cfdddf56247a2ac289a5bfc20ba723ba8b5ad26df7a9658f824e8509c325362fc8cd304f723f33ebf0b065c6d60b2b9b9d33ef0b39ce41b1c7e3af547f6d0f65ca7fb41228271bb7dcaf8b707f941751eb85a7d2c58578e11215d301cd72c0d1917f12e151595ee3fe408a7549d9e986e58254951410e4edd1d88f3776df3293c8355b3cdbf37b26db838d2046aa18628851dfc6883e1736c0efaba3,
    "key2": 0x00914f6b95335685ba37f4f95bf9893ed7c02bb131d6d7a4a37ced72c31f5283a65774ea67d38c7029d1e751a82564b2c189bf6c76c75e07f8738e973636856f3461d59211fe96f818a4193a0ad4532cc1e595ff187dc8ce1490ad19ae9e4b2ea63a070ee7e92d436c6452fa07007e3a9662eeeb432ae90354a0749c3fca8fa5e25ea73d640c352e165a857cefa1628afa17e024b73e78246e12402e71ab65abbedced8306629d31194ad88bf07b085abe723500fd02e44e7042079cfb8158c6ed88b7dfd25266e4199f68ed1c582fd959f87a572f7ab8c7b54ef327205f710c7f270b229dd7a37315582e5921865adc7b74ac73816be21b42e0bdd9117e2fb133,
    "key3": 0x69e5e5db6a80a32c59ec1ec63710f4886407ee0007a1050b22178d5ae88865d861b66371a93120d581ba701bc1221cf2b4a0e3f3ff15f79dfe66d0f7a795e9b083650f382fa5f7e5b4d8fd7a85423deb8263f595701b9e863e3b698d3ed1629b9394580ab50c511c9a9c059f9b7c3f02bdec1fbe4fa9b13a376f04245493727a19d32e820ba4aa31535cee42cc4ec2603ffce5d77255376a5bbd693f275618d8c0900eb4f4f263bedaa524bd0fb650d59c7deba3de4bfa4fb3ca50312fc585860e89c01bd90675f321cc7edc83912e9e3a9590ff08b145851b1cf847bd2baf1a4a6d409e8bbb8ecd374743c65fceaf052c33a430670770abf24daeea2f276f67
}

q = 0
e = 3 
cyphertext = 4522827319495133992180681297469132393090864882907734433792485591515487678316653190385712678072377419115291918844825910187405830252000250630794128768175509500175722681252259065645121664124102118609133000959307902964132117526575091336372330412274759536808500083138400040526445476933659309071594237016007983559466411644234655789758508607982884717875864305554594254277210539612940978371460389860098821834289907662354612012313188685915852705277220725621370680631005616548237038578956187747135229995137050892471079696577563496115023198511735672164367020373784482829942657366126399823845155446354953052034645278225359074399


def multiples(a, b):
    if a == 0:
        return (0, 1)
    else:
        y, x = multiples(b % a, a)
        return (x - (b // a) * y, y)

def modinv(n, mod):
    if False == True :
        print("ERROR: inputs are not relativly prime")
        return 0
    else:
        x, y = multiples(n, mod)
        return x % mod

def root3rd(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    return y

def normal(q, cyphertext, modulus):
    if q == 0:
        for i in range(2, 1000000):
            if modulus % i == 0:
                q = i

    if q != 0:
        p = modulus//q
        phi = (p-1) * (q-1)
        privkey = modinv( e, phi )
        rawMessage = pow( cyphertext, privkey, modulus )

        

### Start Execution
if len(pubkeys) > 1 and q == 0:
    print("More than one key given. Trying to find GCD")

    for pubkey1 in pubkeys:
        for pubkey2 in pubkeys:
            if pubkey1 != pubkey2:
                cd = gcd(pubkeys[pubkey1], pubkeys[pubkey2])
                print("GCD for {} and {}: {}".format(pubkey1, pubkey2, cd))

for pubkey in pubkeys:
    pubkey = pubkeys[pubkey]

    rawMessage = 0
    if e == 3 and q == 0:
        if root3rd(cyphertext) < root3rd(pubkey):
            normal(q, cyphertext, pubkey)
        else:
            normal(q, cyphertext, pubkey)
    else:
        normal(q, cyphertext, pubkey)

    if rawMessage != 0:
        test = str(hex(rawMessage))[2:].strip()
        if len(test) % 2 == 1:
            test = test + "0"

        print(binascii.unhexlify(test))
    else:
        print("Encryption failed")