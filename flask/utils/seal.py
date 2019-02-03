import bcrypt

from utils.token import random_token

IS_SEAL_FROM_IP = False

def get_footprint_from_request(request):

    if IS_SEAL_FROM_IP:
        remote_ip = request.remote_addr
        real_ip = request.environ.get('HTTP_X_REAL_IP', remote_ip)
        forwarded_for_ip = request.environ.get('HTTP_X_FORWARDED_FOR', real_ip)
        footprint = forwarded_for_ip
        return footprint

    footprint = request.args.get('footprint', 'NEW')
    return footprint

def get_sealprint_from_footprint(footprint):
    if IS_SEAL_FROM_IP:
        sealprint = footprint
    else:
        sealprint = random_token()
    return sealprint

def get_seal_from_sealprint(sealprint):
    seal = bcrypt.hashpw(
        sealprint.encode('utf-8'),
        bcrypt.gensalt()
    )

    return seal

def is_footprint_from_seal(footprint, seal):
    return bcrypt.hashpw(footprint.encode('utf-8'), seal) == seal
