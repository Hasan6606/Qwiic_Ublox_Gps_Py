"""Predefined message classes"""

from . import core

__all__ = ['ACK_CLS', 'NAV_CLS', ]

ACK_CLS = core.Cls(0x05, 'ACK', [
    core.Message(0x01, 'ACK', [
        core.Field('clsID', 'U1'),
        core.Field('msgID', 'U1'),
    ]),
    core.Message(0x00, 'NAK', [
        core.Field('clsID', 'U1'),
        core.Field('msgID', 'U1'),
    ])
])

CFG_CLS = core.Cls(0x06, 'CFG', [
    core.Message(0x41, 'OTP', [
    ]),
    core.Message(0x2C, 'PIO', [
        core.Field('version', 'U1'),
        core.Field('request', 'U1'),
        core.RepeatedBlock('RB', [ 
            core.Field('requiredPinState', 'U1'),
        ]) 
    ]),    
    core.Message(0x59, 'PT2', [
        core.Field('version', 'U1'),
        core.BitField('activate', 'X1', [
            core.Flag('enable', 0, 1),
            core.Flag('lnaMode', 6, 8),
        ]),
        core.Field('extint', 'U1'),
        core.Field('reAcqCno', 'U1'),
        core.Field('refFreq ', 'U4'),
        core.Field('refFreqAcc ', 'U4'),
        core.RepeatedBlock('RB', [ 
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.Field('sigId', 'U1'),
            core.Field('accsId', 'U1'),
        ]) 
    ]),
    core.Message(0x04, 'RST', [
        core.BitField('navBbrMask', 'X2', [
            core.Flag('eph', 0, 1),
            core.Flag('alm', 1, 2),
            core.Flag('health', 2, 3),
            core.Flag('klob', 3, 4),
            core.Flag('pos', 4, 5),
            core.Flag('clkd', 5, 6),
            core.Flag('osc', 6, 7),
            core.Flag('utc', 7, 8),
            core.Flag('rtc', 8, 9),
            core.Flag('sfdr', 11, 12),
            core.Flag('vmon', 12, 13),
            core.Flag('tct', 13, 14),
            core.Flag('aop', 15, 16),
        ]),
        core.Field('resetMode', 'U1'),
        core.PadByte(),
    ]),    
    core.Message(0x64, 'SPT', [
        core.Field('version', 'U1'),
        core.PadByte(),
        core.Field('sensorId', 'U2'),
        core.PadByte(repeat=8),
    ]),    
    core.Message(0x58, 'USBTEST', [
        core.Field('version', 'U1'),
        core.Field('usbPinState', 'U1'),
    ]),    
    core.Message(0x8c, 'VALDEL', [ # With transaction
        core.Field('version', 'U1'),
        core.Field('usbPinState', 'U1'),
        core.BitField('layers', 'X1', [
            core.Flag('bbr', 1, 2),
            core.Flag('flash', 2, 3),
        ]),
        core.PadByte(repeat=2),
        core.RepeatedBlock('RB', [
            core.Field('keys','U4'),
        ]),
    ]),    
    core.Message(0x8b, 'VALGET', [ # Get configuration items
        core.Field('version', 'U1'),
        core.Field('layer', 'U1'),
        core.Field('position', 'U2'),
        core.RepeatedBlock('RB', [
            core.Field('cfgData','U4'),
        ]),
    ]),    
    core.Message(0x8a, 'VALSET', [ # With Tranaction 
        core.Field('version', 'U1'),
        core.BitField('layers', 'X1', [
            core.Flag('ram', 0, 1),
            core.Flag('bbr', 1, 2),
            core.Flag('flash', 2, 3),
        ]),
        core.Field('transaction', 'U1'),
        core.Field('action', 'U1'),
        core.PadByte(),
        core.RepeatedBlock('RB', [
            core.Field('cfgData','U4'),
        ]),
    ]),    
])

NAV_CLS = core.Cls(0x10, 'ESF', [
    core.Message(0x14, 'ALG', [
        core.Field('iTOW','U4'),    
        core.Field('version','U1'),    
        core.BitField('flags', 'X1', [
            core.Flag('autoMntAlgOn', 0, 1),
            core.Flag('status', 1, 4),

        ]),
        core.BitField('error', 'X1', [
            core.Flag('tiltAlgError', 0, 1),
            core.Flag('yawAlgoError', 1, 2),
            core.Flag('angleError', 2, 3),
        ]),
        core.PadByte(),
        core.Field('yaw','U4'), 
        core.Field('pitch','I2'), 
        core.Field('roll','I2'), 
    ]),
    core.Message(0x15, 'INS', [
        core.BitField('biltfield0', 'X4', [
            core.Flag('version', 0, 8),
            core.Flag('xAngRateValid', 8, 9),
            core.Flag('yAngRateValid', 9, 10),
            core.Flag('zAngRateValid', 10, 11),
            core.Flag('xAccelValid', 11, 12),
            core.Flag('yAccelValid', 12, 13),
            core.Flag('zAccelValid', 13, 14),
        ]),
        core.PadByte(repeat=4),
        core.Field('iTOW','U4'),
        core.Field('xAngRate','I4'),
        core.Field('yAngRate','I4'),
        core.Field('zAngRate','I4'),
        core.Field('xAccel','I4'),
        core.Field('yAccel','I4'),
        core.Field('zAccel','I4'),
    ]),
    core.Message(0x02, 'MEAS', [
        core.Field('timeTag','U4'),
        core.BitField('flags', 'X2', [
            core.Flag('timeMarkSent', 0, 2),
            core.Flag('timeMarkEdge', 2, 3),
            core.Flag('calibTtagValid', 3, 4),
            core.Flag('numMeas', 11, 16),
        ]),
        core.Field('id','U2'),
        core.RepeatedBlock('RB', [
            core.BitField('data','X4', [
                core.Flag('dataField', 0, 24),
                core.Flag('dataType', 24, 30),
            ]),
            core.Field('calibTtag','U4'),
        ]),
    ]),
    core.Message(0x03, 'RAW', [
        core.PadByte(repeat=4),
        core.RepeatedBlock('RB', [
            core.BitField('data','X4', [
                core.Flag('dataField', 0, 24),
                core.Flag('dataType', 24, 30),
            ]),
            core.Field('sTag','U4'),
        ]),
    ]),
    core.Message(0x13, 'RESETALG', [
    ]),
    core.Message(0x10, 'STATUS', [
        core.Field('iTOW','U4'),
        core.Field('version','U1'),
        core.BitField('initStatus1', 'X1', [
            core.Flag('wtInitStatus', 0, 2),
            core.Flag('mntAlgStatus', 2, 5),
            core.Flag('insInitStatus', 5, 7),
        ]),
        core.BitField('initStatus2', 'X1', [
            core.Flag('imuInitStatus', 0, 2),
        ]),
        core.PadByte(repeat=5),
        core.Field('fusionMode','U1'),
        core.PadByte(repeat=2),
        core.Field('numSens','U1'),
        core.BitField('senStatus1', 'X1', [
            core.Flag('type', 0, 6),
            core.Flag('used', 6, 7),
            core.Flag('ready', 7, 8),
        ]),
        core.BitField('senStatus2', 'X1', [
            core.Flag('calibStatus', 0, 2),
            core.Flag('timeStatus', 2, 4),
        ]),
        core.Field('freq', 'U1'),
        core.BitField('faults', 'X1', [
            core.Flag('badMeas', 0, 1),
            core.Flag('badTTag', 1, 2),
            core.Flag('missingMeas', 2, 3),
            core.Flag('noisyMeas', 3, 4),
        ]),
    ]),
    
])

NAV_CLS = core.Cls(0x04, 'INF', [
    core.Message(0x04, 'DEBUG', [
        core.RepeatedBlock('RB', [
            core.Field('str','CH'),
        ]),
    ]),
    core.Message(0x00, 'ERROR', [
        core.RepeatedBlock('RB', [
            core.Field('str','CH'),
        ]),
    ]),
    core.Message(0x02, 'NOTICE', [
        core.RepeatedBlock('RB', [
            core.Field('str','CH'),
        ]),
    ]),
    core.Message(0x03, 'TEST', [
        core.RepeatedBlock('RB', [
            core.Field('str','CH'),
        ]),
    ]),
    core.Message(0x01, 'WARNING', [
        core.RepeatedBlock('RB', [
            core.Field('str','CH'),
        ]),
    ]),
])

NAV_CLS = core.Cls(0x01, 'NAV', [
    core.Message(0x05, 'ATT', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.PadByte(repeat=3),
        core.Field('roll', 'I4'),
        core.Field('pitch', 'I4'),
        core.Field('heading', 'I4'),
        core.Field('accRoll', 'U4'),
        core.Field('accPitch', 'U4'),
        core.Field('accHeading', 'U4'),
    ]),
    core.Message(0x22, 'CLOCK', [
        core.Field('iTOW', 'U4'),
        core.Field('clkB', 'I4'),
        core.Field('clkD', 'I4'),
        core.Field('tAcc', 'U4'),
        core.Field('fAcc', 'U4'),
    ]),
    core.Message(0x36, 'COV', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('posCovValid', 'U1'),
        core.Field('velCovValid', 'U1'),
        core.PadByte(repeat=9),
        core.Field('posCovNN', 'R4'),
        core.Field('posCovNE', 'R4'),
        core.Field('posCovND', 'R4'),
        core.Field('posCovEE', 'R4'),
        core.Field('posCovED', 'R4'),
        core.Field('posCovDD', 'R4'),
        core.Field('velCovNN', 'R4'),
        core.Field('velCovNE', 'R4'),
        core.Field('velCovND', 'R4'),
        core.Field('velCovEE', 'R4'),
        core.Field('velCovED', 'R4'),
        core.Field('velCovDD', 'R4'),
    ]),
    core.Message(0x04, 'DOP', [
        core.Field('iTOW', 'U4'),
        core.Field('gDOP', 'U2'),
        core.Field('pDOP', 'U2'),
        core.Field('tDOP', 'U2'),
        core.Field('vDOP', 'U2'),
        core.Field('hDOP', 'U2'),
        core.Field('nDOP', 'U2'),
        core.Field('eDOP', 'U2'),
    ]),
    core.Message(0x3d, 'EELL', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('reserved', 'U1'),
        core.Field('errEllipseOrient', 'U2'),
        core.Field('errEllipseMajor', 'U4'),
        core.Field('errEllipseMinor', 'U4'),
    ]),
    core.Message(0x61, 'EOE', [
        core.Field('iTOW', 'U4'),
    ]),
    core.Message(0x39, 'GEOFENCE', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('status', 'U1'),
        core.Field('numFences', 'U1'),
        core.Field('combState', 'U1'),
        core.RepeatedBlock('RB', [
            core.Field('state', 'U1'),
            core.Field('id', 'U1'),
        ]),
    ]),
    core.Message(0x13, 'HPPOSECEF', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=3),
        core.Field('iTOW', 'U4'),
        core.Field('ecefX', 'I4'),
        core.Field('ecefY', 'I4'),
        core.Field('ecefZ', 'I4'),
        core.Field('ecefXHp', 'I1'),
        core.Field('ecefYHp', 'I1'),
        core.Field('ecefZHp', 'I1'),
        core.BitField('flags', 'X1', [
            core.Flag('invalidEcef', 0 ,1),
        ]),
        core.Field('pAcc', 'U4'),

    ]),
    core.Message(0x14, 'HPPOSLLH', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.BitField('flags', 'X1', [
            core.Flag('invalidLh', 0 ,1),
        ]),
        core.Field('iTOW', 'U4'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('lonHp', 'I1'),
        core.Field('latHp', 'I1'),
        core.Field('heightHp', 'I1'),
        core.Field('hMSLHp', 'I1'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
    ]),
    core.Message(0x34, 'ORB', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('numSv', 'U1'),
        core.PadByte(repeat=2),
        core.RepeatedBlock('RB', [
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.BitField('svFlag', 'X1', [
                core.Flag('health', 0, 2),
                core.Flag('visibility', 2, 4),
            ]),
            core.BitField('eph', 'X1', [
                core.Flag('ephUsability', 0, 5),
                core.Flag('ephSource', 5, 8),
            ]),
            core.BitField('alm', 'X1', [
                core.Flag('almUsability', 0, 5),
                core.Flag('almSource', 5, 8),
            ]),
            core.BitField('otherOrb', 'X1', [
                core.Flag('anoAopUsability', 0, 5),
                core.Flag('type', 5, 8),
            ]),
        ]),
    ]),
    core.Message(0x01, 'POSECEF', [
        core.Field('iTOW', 'U4'),
        core.Field('ecefX', 'I4'),
        core.Field('ecefY', 'I4'),
        core.Field('ecefZ', 'I4'),
        core.Field('pAcc', 'U4'),
    ]),
    core.Message(0x02, 'POSLLH', [
        core.Field('iTOW', 'U4'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
    ]),
    core.Message(0x07, 'PVT', [
        core.Field('iTOW', 'U4'),
        core.Field('year', 'U2'),
        core.Field('month', 'U1'),
        core.Field('day', 'U1'),
        core.Field('hour', 'U1'),
        core.Field('min', 'U1'),
        core.Field('sec', 'U1'),
        core.BitField('valid', 'X1', [
            core.Flag('validDate', 0, 1),
            core.Flag('validTime', 1, 2),
            core.Flag('fullyResolved', 2, 3),
            core.Flag('validMag', 3, 4),
        ]),
        core.Field('tAcc', 'U4'),
        core.Field('nano', 'I4'),
        core.Field('fixType', 'U1'),
        core.BitField('flags', 'X1', [
            core.Flag('gnssFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('psmState', 2, 5),
            core.Flag('headVehValid', 5, 6),
            core.Flag('carrSoln', 6, 8),
        ]),
        core.BitField('flags2', 'X1', [
            core.Flag('confirmedAvai', 5, 6),
            core.Flag('confirmedDate', 6, 7),
            core.Flag('confirmedTime', 7, 8),
        ]),
        core.Field('numSV', 'U1'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
        core.Field('velN', 'I4'),
        core.Field('velE', 'I4'),
        core.Field('velD', 'I4'),
        core.Field('gSpeed', 'I4'),
        core.Field('headMot', 'I4'),
        core.Field('sAcc', 'U4'),
        core.Field('headAcc', 'U4'),
        core.Field('pDOP', 'U2'),
        core.BitField('flags3', 'U2', [
            core.Flag('invalidL1h', 0, 1),
        ]),
        core.PadByte(repeat=5),
        core.Field('headVeh', 'I4'),
        core.Field('magDec', 'I2'),
        core.Field('magAcc', 'U2'),
    ]),
    core.Message(0x3C, 'RELPOSNED', [
        core.Field('version', 'U1'),
        core.PadByte(),
        core.Field('refStationId', 'U2'),
        core.Field('iTOW', 'U4'),
        core.Field('relPosN', 'I4'),
        core.Field('relPosE', 'I4'),
        core.Field('relPosD', 'I4'),
        core.Field('relPosLength', 'I4'),
        core.Field('relPosHeading', 'I4'),
        core.PadByte(),
        core.Field('relPosHPN', 'I1'),
        core.Field('relPosHPE', 'I1'),
        core.Field('relPosHPD', 'I1'),
        core.Field('relPosHPLength', 'I1'),
        core.Field('accN', 'U4'),
        core.Field('accE', 'U4'),
        core.Field('accD', 'U4'),
        core.Field('accLength', 'U4'),
        core.Field('accHeading', 'U4'),
        core.PadByte(repeat=4),
        core.BitField('flags', 'X4', [
            core.Flag('gnssFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('relPosValid', 2, 3),
            core.Flag('carrSoln', 3, 5),
            core.Flag('isMoving', 5, 6),
            core.Flag('refPosMiss', 6, 7),
            core.Flag('refObsMiss', 7, 8),
            core.Flag('relPosHeadingValid', 8, 9),
            core.Flag('relPosNormalized', 9, 10),
        ]),
    ]),
    core.Message(0x35, 'SAT', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('numSvs', 'U1'),
        core.PadByte(repeat=2),
        core.RepeatedBlock('RB', [
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.Field('cno', 'U1'),
            core.Field('elev', 'I1'),
            core.Field('azim', 'I2'),
            core.Field('prRes', 'I2'),
            core.BitField('flags', 'X4', [
                core.Flag('qualityInd', 0, 3),
                core.Flag('svUsed', 3, 4),
                core.Flag('health', 4, 6),
                core.Flag('diffCorr', 6, 7),
                core.Flag('smoothed', 7, 8),
                core.Flag('orbitSource', 8, 11),
                core.Flag('ephAvail', 11, 12),
                core.Flag('almAvail', 12, 13),
                core.Flag('anoAvail', 13, 14),
                core.Flag('aopAvail', 14, 15),
                core.Flag('sbasCorrUsed', 16, 17),
                core.Flag('rtcmCorrUsed', 17, 18),
                core.Flag('slasCorrUsed', 18, 19),
                core.Flag('prCorrUsed', 20, 21),
                core.Flag('crCorrUsed', 21, 22),
                core.Flag('doCorrUsed', 22, 23),
            ]),
        ]),
    ]),
    core.Message(0x32, 'SBAS', [
        core.Field('iTOW', 'U4'),
        core.Field('geo', 'U1'),
        core.Field('mode', 'U1'),
        core.Field('sys', 'I1'),
        core.BitField('service', 'X1', [
            core.Flag('Ranging', 0, 1),
            core.Flag('Corrections', 1, 2),
            core.Flag('Integrity', 2, 3),
            core.Flag('TestMode', 3, 4),
            core.Flag('Bad', 4, 5),
        ]),
        core.Field('cnt', 'U1'),
        core.PadByte(repeat=3),
        core.RepeatedBlock('RB', [
            core.Field('svid', 'U1'),
            core.Field('flags', 'U1'),
            core.Field('udre', 'U1'),
            core.Field('svSys', 'U1'),
            core.Field('svService', 'U1'),
            core.PadByte(),
            core.Field('prc', 'I2'),
            core.PadByte(repeat=2),
            core.Field('ic', 'I2'),
        ]),
    ]),
    core.Message(0x43, 'SIG', [ #here
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('numSigs', 'U1'),
        core.PadByte(repeat=2),
        core.RepeatedBlock('RB', [
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.Field('sigId', 'U1'),
            core.Field('freqId', 'U1'),
            core.Field('prRes', 'I2'),
            core.Field('cno', 'U1'),
            core.Field('qualityInd', 'U1'),
            core.Field('corrSource', 'U1'),
            core.Field('ionoModel', 'U1'),
            core.Field('sigFlags', 'X2', [
                core.Flag('health', 0, 2),
                core.Flag('prSmoothed', 2, 3),
                core.Flag('prUsed', 3, 4),
                core.Flag('crUsed', 4, 5),
                core.Flag('doUsed', 5, 6),
                core.Flag('prCorrUsed', 6, 7),
                core.Flag('crCorrUsed', 7, 8),
                core.Flag('doCorrUsed', 8, 9),
            ]),
        ]),
            core.PadByte(repeate=4)
    ]),
    core.Message(0x03, 'STATUS', [
        core.Field('iTOW', 'U4'),
        core.Field('gpsFix', 'U1'),
        core.BitField('flags', 'X1', [
            core.Flag('gpsFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('wknSet', 2, 3),
            core.Flag('towSet', 3, 4),
        ]),
        core.BitField('fixStat', 'X1', [
            core.Flag('diffCorr', 0, 1),
            core.Flag('caarSolnValid', 1, 2),
            core.Flag('mapMatching', 6, 8),
        ]),
        core.BitField('flags2', 'X1', [
            core.Flag('psmState', 0, 2),
            core.Flag('spoofDetState', 3, 5),
            core.Flag('carSoln', 6, 8),
        ]),
        core.Field('ttff', 'U4'),
        core.Field('msss', 'U4'),
    ]),
    core.Message(0x24, 'TIMEBDS', [
        core.Field('iTOW', 'U4'),
        core.Field('SOW', 'U4'),
        core.Field('fSOW', 'I4'),
        core.Field('week', 'I2'),
        core.Field('leapS', 'I1'),
        core.BitField('valid', 'X1', [
            core.Flag('sowValid', 0, 1),
            core.Flag('weekValid', 1, 2),
            core.Flag('leapSValid', 2, 3),
        ]),
        core.Field('tAcc','U4'), 
    ]),
    core.Message(0x25, 'TIMEGAL', [
        core.Field('iTOW', 'U4'),
        core.Field('galTow', 'U4'),
        core.Field('fGalTow', 'I4'),
        core.Field('galWno', 'I2'),
        core.Field('leapS', 'I1'),
        core.BitField('valid', 'X1', [
            core.Flag('galValid', 0, 1),
            core.Flag('galWnoValid', 1, 2),
            core.Flag('leapSValid', 2, 3),
        ]),
        core.Field('tAcc','U4'), 
    ]),
    core.Message(0x23, 'TIMEGLO', [
        core.Field('iTOW', 'U4'),
        core.Field('TOD', 'U4'),
        core.Field('fTOD', 'I4'),
        core.Field('Nt', 'U2'),
        core.Field('N4', 'U1'),
        core.BitField('valid', 'X1', [
            core.Flag('todValid', 0, 1),
            core.Flag('dateValid', 1, 2),
        ]),
        core.Field('tAcc','U4'), 
    ]),
    core.Message(0x20, 'TIMEGPS', [
        core.Field('iTOW', 'U4'),
        core.Field('fTOW', 'I4'),
        core.Field('week', 'I2'),
        core.Field('leapS', 'I1'),
        core.BitField('valid', 'X1', [
            core.Flag('towValid', 0, 1),
            core.Flag('weekValid', 1, 2),
            core.Flag('leapSValid', 2, 3),
        ]),
        core.Field('tAcc','U4'), 
    ]),
    core.Message(0x25, 'TIMELS', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.PadByte(repeat=3),
        core.Field('srcOfCurrLs', 'U1'),
        core.Field('currLs', 'I1'),
        core.Field('srcOfLsChange', 'U1'),
        core.Field('lsChange', 'I1'),
        core.Field('timeToLsEvent', 'I4'),
        core.Field('dateOfLsGpsWn', 'U2'),
        core.PadByte(repeat=3),
        core.BitField('valid', 'X1', [
            core.Flag('validCurrLs', 0, 1),
            core.Flag('validTimeToLsEvent', 1, 2),
        ]),
    ]),
    core.Message(0x27, 'TIMEQZSS', [
        core.Field('iTOW', 'U4'),
        core.Field('qzssTow', 'U4'),
        core.Field('fQzssTow', 'I4'),
        core.Field('qzssWno', 'I2'),
        core.Field('leapS', 'I1'),
        core.BitField('valid', 'X1', [
            core.Flag('qzssTowValid', 0, 1),
            core.Flag('qzssWnoValid', 1, 2),
            core.Flag('leapSValid', 2, 3),
        ]),
        core.Field('tAcc','U4'), 
    ]),
    core.Message(0x21, 'TIMEUTC', [
        core.Field('iTOW', 'U4'),
        core.Field('tAcc', 'U4'),
        core.Field('nano', 'I4'),
        core.Field('year', 'U2'),
        core.Field('month', 'U1'),
        core.Field('day', 'U1'),
        core.Field('hour', 'U1'),
        core.Field('min', 'U1'),
        core.Field('sec', 'U1'),
        core.BitField('valid', 'X1', [
            core.Flag('validTOW', 0, 1),
            core.Flag('validWKN', 1, 2),
            core.Flag('validUTC', 2, 3),
            core.Flag('utcStandard', 4, 8),
        ]),
    ]),
    core.Message(0x11, 'VELECEF', [
        core.Field('iTOW', 'U4'),
        core.Field('ecefVX', 'I4'),
        core.Field('ecefVY', 'I4'),
        core.Field('ecefVZ', 'I4'),
        core.Field('sAcc', 'U4'),
    ]),
    core.Message(0x12, 'VELNED', [
        core.Field('iTOW', 'U4'),
        core.Field('velN', 'I4'),
        core.Field('velE', 'I4'),
        core.Field('velD', 'I4'),
        core.Field('speed', 'U4'),
        core.Field('gSpeed', 'U4'),
        core.Field('heading', 'I4'),
        core.Field('sAcc', 'U4'),
        core.Field('cAcc', 'U4'),
    ]),
])

TIM_CLS = core.Cls(0x0D, 'TIM', [
    core.Message(0x03, 'TM2', [
        core.Field('ch', 'U1'),
        core.BitField('flags', 'X1', [
            core.Flag('mode', 0, 1),
            core.Flag('run', 1, 2),
            core.Flag('newFallingEdge', 2, 3),
            core.Flag('timeBase', 3, 5),
            core.Flag('utc', 5, 6),
            core.Flag('time', 6, 7),
            core.Flag('newRisingEdge', 7, 8),
        ]),
        core.Field('count', 'U2'),
        core.Field('wnR', 'U2'),
        core.Field('wnF', 'U2'),
        core.Field('towMsR', 'U4'),
        core.Field('towSubMsR', 'U4'),
        core.Field('towMsF', 'U4'),
        core.Field('towSubMsF', 'U4'),
        core.Field('accEst', 'U4'),
    ]),
    core.Message(0x01, 'TP', [
        core.Field('towMS', 'U4'),
        core.Field('towSubMS', 'U4'),
        core.Field('qErr', 'I4'),
        core.Field('week', 'I4'),
        core.BitField('flags', 'X1', [
            core.Flag('timeBase', 0, 1),
            core.Flag('utc', 1, 2),
            core.Flag('raim', 2, 4),
            core.Flag('qErrInvalid', 4, 5),
        ]),
        core.BitField('refInfo', 'X1', [
            core.Flag('timeRefGnss', 0, 4),
            core.Flag('utcStandard', 4, 8),
        ]),
    ]),
    core.Message(0x06, 'VRFY', [
        core.Field('itow', 'I4'),
        core.Field('frac', 'I4'),
        core.Field('deltaMs', 'I4'),
        core.Field('deltaNs', 'I4'),
        core.Field('wno', 'U2'),
        core.BitField('flags', 'X1', [
            core.Flag('src', 0, 3)
        ]),
    ]),
])
