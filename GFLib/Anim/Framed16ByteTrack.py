# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Anim

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Framed16ByteTrack(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Framed16ByteTrack()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFramed16ByteTrack(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Framed16ByteTrack
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Framed16ByteTrack
    def Frames(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 2))
        return 0

    # Framed16ByteTrack
    def FramesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint16Flags, o)
        return 0

    # Framed16ByteTrack
    def FramesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Framed16ByteTrack
    def FramesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Framed16ByteTrack
    def Byte(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Framed16ByteTrack
    def ByteAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Framed16ByteTrack
    def ByteLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Framed16ByteTrack
    def ByteIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Framed16ByteTrackStart(builder):
    builder.StartObject(2)

def Start(builder):
    Framed16ByteTrackStart(builder)

def Framed16ByteTrackAddFrames(builder, frames):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(frames), 0)

def AddFrames(builder, frames):
    Framed16ByteTrackAddFrames(builder, frames)

def Framed16ByteTrackStartFramesVector(builder, numElems):
    return builder.StartVector(2, numElems, 2)

def StartFramesVector(builder, numElems):
    return Framed16ByteTrackStartFramesVector(builder, numElems)

def Framed16ByteTrackAddByte(builder, byte):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(byte), 0)

def AddByte(builder, byte):
    Framed16ByteTrackAddByte(builder, byte)

def Framed16ByteTrackStartByteVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartByteVector(builder, numElems):
    return Framed16ByteTrackStartByteVector(builder, numElems)

def Framed16ByteTrackEnd(builder):
    return builder.EndObject()

def End(builder):
    return Framed16ByteTrackEnd(builder)

try:
    from typing import List
except:
    pass

class Framed16ByteTrackT(object):

    # Framed16ByteTrackT
    def __init__(self):
        self.frames = None  # type: List[int]
        self.byte = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        framed16ByteTrack = Framed16ByteTrack()
        framed16ByteTrack.Init(buf, pos)
        return cls.InitFromObj(framed16ByteTrack)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, framed16ByteTrack):
        x = Framed16ByteTrackT()
        x._UnPack(framed16ByteTrack)
        return x

    # Framed16ByteTrackT
    def _UnPack(self, framed16ByteTrack):
        if framed16ByteTrack is None:
            return
        if not framed16ByteTrack.FramesIsNone():
            if np is None:
                self.frames = []
                for i in range(framed16ByteTrack.FramesLength()):
                    self.frames.append(framed16ByteTrack.Frames(i))
            else:
                self.frames = framed16ByteTrack.FramesAsNumpy()
        if not framed16ByteTrack.ByteIsNone():
            if np is None:
                self.byte = []
                for i in range(framed16ByteTrack.ByteLength()):
                    self.byte.append(framed16ByteTrack.Byte(i))
            else:
                self.byte = framed16ByteTrack.ByteAsNumpy()

    # Framed16ByteTrackT
    def Pack(self, builder):
        if self.frames is not None:
            if np is not None and type(self.frames) is np.ndarray:
                frames = builder.CreateNumpyVector(self.frames)
            else:
                Framed16ByteTrackStartFramesVector(builder, len(self.frames))
                for i in reversed(range(len(self.frames))):
                    builder.PrependUint16(self.frames[i])
                frames = builder.EndVector()
        if self.byte is not None:
            if np is not None and type(self.byte) is np.ndarray:
                byte = builder.CreateNumpyVector(self.byte)
            else:
                Framed16ByteTrackStartByteVector(builder, len(self.byte))
                for i in reversed(range(len(self.byte))):
                    builder.PrependUint8(self.byte[i])
                byte = builder.EndVector()
        Framed16ByteTrackStart(builder)
        if self.frames is not None:
            Framed16ByteTrackAddFrames(builder, frames)
        if self.byte is not None:
            Framed16ByteTrackAddByte(builder, byte)
        framed16ByteTrack = Framed16ByteTrackEnd(builder)
        return framed16ByteTrack