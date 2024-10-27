# automatically generated by the FlatBuffers compiler, do not modify
from GFLib.Anim.DynamicBooleanTrack import DynamicBooleanTrackT
from GFLib.Anim.FixedBooleanTrack import FixedBooleanTrackT
from GFLib.Anim.Framed16BooleanTrack import Framed16BooleanTrackT
from GFLib.Anim.Framed8BooleanTrack import Framed8BooleanTrackT


# namespace: Anim

class BooleanTrack(object):
    NONE = 0
    FixedBooleanTrack = 1
    DynamicBooleanTrack = 2
    Framed16BooleanTrack = 3
    Framed8BooleanTrack = 4

def BooleanTrackCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == BooleanTrack().FixedBooleanTrack:
        return FixedBooleanTrackT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == BooleanTrack().DynamicBooleanTrack:
        return DynamicBooleanTrackT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == BooleanTrack().Framed16BooleanTrack:
        return Framed16BooleanTrackT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == BooleanTrack().Framed8BooleanTrack:
        return Framed8BooleanTrackT.InitFromBuf(table.Bytes, table.Pos)
    return None