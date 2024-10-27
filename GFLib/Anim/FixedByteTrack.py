# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Anim

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FixedByteTrack(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FixedByteTrack()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFixedByteTrack(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FixedByteTrack
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FixedByteTrack
    def Byte(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def FixedByteTrackStart(builder):
    builder.StartObject(1)

def Start(builder):
    FixedByteTrackStart(builder)

def FixedByteTrackAddByte(builder, byte):
    builder.PrependUint8Slot(0, byte, 0)

def AddByte(builder, byte):
    FixedByteTrackAddByte(builder, byte)

def FixedByteTrackEnd(builder):
    return builder.EndObject()

def End(builder):
    return FixedByteTrackEnd(builder)


class FixedByteTrackT(object):

    # FixedByteTrackT
    def __init__(self):
        self.byte = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        fixedByteTrack = FixedByteTrack()
        fixedByteTrack.Init(buf, pos)
        return cls.InitFromObj(fixedByteTrack)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, fixedByteTrack):
        x = FixedByteTrackT()
        x._UnPack(fixedByteTrack)
        return x

    # FixedByteTrackT
    def _UnPack(self, fixedByteTrack):
        if fixedByteTrack is None:
            return
        self.byte = fixedByteTrack.Byte()

    # FixedByteTrackT
    def Pack(self, builder):
        FixedByteTrackStart(builder)
        FixedByteTrackAddByte(builder, self.byte)
        fixedByteTrack = FixedByteTrackEnd(builder)
        return fixedByteTrack