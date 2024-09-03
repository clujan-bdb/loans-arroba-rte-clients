class IdentificationType(str):
    DNI = 'dni'
    IDENTITY_CARD = 'ti'
    PASSPORT = 'ps'
    FOREIGN_ID = 'ce'
    NIT = 'nit'

    all = [DNI, IDENTITY_CARD, PASSPORT, FOREIGN_ID, NIT]


class Segment(str):
    PERSONAL = 'personal'
    BUSINESS = 'business'
    VIP = 'vip'

    all = [PERSONAL, BUSINESS, VIP]
