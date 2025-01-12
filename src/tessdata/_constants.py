# coding=utf-8
# See main file for licence
# pylint: disable=W0401,W0403
#
# by Mazoea s.r.o.
#

"""
    Tesseract constants.
"""

size_of_int32 = 4

NUM_CP_BUCKETS = 24
CLASSES_PER_CP = 32
NUM_BITS_PER_CLASS = 2
BITS_PER_WERD = int(8 * size_of_int32)
BITS_PER_CP_VECTOR = int(CLASSES_PER_CP * NUM_BITS_PER_CLASS)
WERDS_PER_CP_VECTOR = int(BITS_PER_CP_VECTOR / BITS_PER_WERD)
CLASS_PRUNER_STRUCT_SIZE = int(NUM_CP_BUCKETS * \
    NUM_CP_BUCKETS * NUM_CP_BUCKETS * WERDS_PER_CP_VECTOR)

PROTOS_PER_PROTO_SET = 64
NUM_PP_PARAMS = 3
WERDS_PER_PP_VECTOR = int(
    (PROTOS_PER_PROTO_SET + BITS_PER_WERD - 1) / BITS_PER_WERD)
MAX_NUM_CONFIGS = 64
WERDS_PER_CONFIG_VEC = int((MAX_NUM_CONFIGS + BITS_PER_WERD - 1) / BITS_PER_WERD)
NUM_PP_BUCKETS = 64
PROTO_PRUNER_SIZE = int(NUM_PP_PARAMS * NUM_PP_BUCKETS * WERDS_PER_PP_VECTOR)

# dawg
FORWARD_EDGE = 0
BACKWARD_EDGE = 1
MARKER_FLAG = 1
DIRECTION_FLAG = 2
WERD_END_FLAG = 4
LETTER_START_BIT = 0
NUM_FLAG_BITS = 3

#
PICO_FEATURE_LENGTH = 0.05
PROTO_PRUNER_SCALE = 4.0
INT_CHAR_NORM_RANGE = 256

PROTOS_PER_PP_WERD = int(BITS_PER_WERD)

PRUNER_X = 0
PRUNER_Y = 1
