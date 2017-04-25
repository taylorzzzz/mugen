from enum import Enum
from typing import TypeVar, Union, Tuple

VERSION = "0.1.0"

"""
SEC.MIL or 'SEC.MIL'
(MIN, SEC.MIL) or 'MIN:SEC.MIL'
(HRS, MIN, SEC.MIL) or 'HRS:MIN:SEC.MIL'
"""
TIME_FORMAT = TypeVar(Union[float, Tuple[int, float], Tuple[int, int, float], str])


class FileType(str, Enum):
    AUDIO = 'audio'
    VIDEO = 'video'
    SPEC = 'spec'


class Track(str, Enum):
    pass

