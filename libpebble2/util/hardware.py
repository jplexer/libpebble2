__author__ = 'katharine'


class PebbleHardware(object):
    UNKNOWN = 0
    TINTIN_EV1 = 1
    TINTIN_EV2 = 2
    TINTIN_EV2_3 = 3
    TINTIN_EV2_4 = 4
    TINTIN_V1_5 = 5
    BIANCA = 6
    SNOWY_EVT2 = 7
    SNOWY_DVT = 8
    SPALDING_EVT = 9
    BOBBY_SMILES = 10
    SPALDING = 11
    SILK_EVT = 12
    ROBERT_EVT = 13
    SILK = 14
    ASTERIX = 15
    OBELIX = 16

    TINTIN_BB = 0xFF
    TINTIN_BB2 = 0xFE
    SNOWY_BB = 0xFD
    SNOWY_BB2 = 0xFC
    SPALDING_BB2 = 0xFB
    SILK_BB = 0xFA
    ROBERT_BB = 0xF9
    SILK_BB2 = 0xF8
    ROBERT_BB2 = 0xF7
    SILK_FLINT = 0xF6
    SNOWY_ROBERT = 0xF5

    PLATFORMS = {
        UNKNOWN: 'unknown',
        TINTIN_EV1: 'aplite',
        TINTIN_EV2: 'aplite',
        TINTIN_EV2_3: 'aplite',
        TINTIN_EV2_4: 'aplite',
        TINTIN_V1_5: 'aplite',
        BIANCA: 'aplite',
        SNOWY_EVT2: 'basalt',
        SNOWY_DVT: 'basalt',
        BOBBY_SMILES: 'basalt',
        SPALDING_EVT: 'chalk',
        SPALDING: 'chalk',
        SILK_EVT: 'diorite',
        ROBERT_EVT: 'emery',
        SILK: 'diorite',
        ASTERIX: 'flint',
        OBELIX: 'emery',
        TINTIN_BB: 'aplite',
        TINTIN_BB2: 'aplite',
        SNOWY_BB: 'basalt',
        SNOWY_BB2: 'basalt',
        SPALDING_BB2: 'chalk',
        SILK_BB: 'diorite',
        ROBERT_BB: 'emery',
        SILK_BB2: 'diorite',
        ROBERT_BB2: 'emery',
        SILK_FLINT: 'flint',
        SNOWY_ROBERT: 'emery',
    }

    @classmethod
    def hardware_platform(cls, hardware):
        return cls.PLATFORMS.get(hardware, 'unknown')
