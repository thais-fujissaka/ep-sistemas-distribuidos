# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpctests.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgrpctests.proto\x12\tgrpctests\x1a\x1bgoogle/protobuf/empty.proto\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"1\n\nparameters\x12\x0e\n\x06number\x18\x01 \x01(\x03\x12\x13\n\x0blong_values\x18\x02 \x03(\x03\"\x1f\n\rLong_Response\x12\x0e\n\x06result\x18\x01 \x01(\x03\"\x18\n\x07MyClass\x12\r\n\x05value\x18\x01 \x01(\x05\";\n\x13ProcessClassRequest\x12$\n\x08instance\x18\x01 \x01(\x0b\x32\x12.grpctests.MyClass\"&\n\x14ProcessClassResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\xdb\x02\n\x08TestsRPC\x12\x43\n\x11GetServerResponse\x12\x12.grpctests.Message\x1a\x1a.grpctests.MessageResponse\x12\x39\n\x08GetsVoid\x12\x15.grpctests.parameters\x1a\x16.google.protobuf.Empty\x12;\n\x08GetsLong\x12\x15.grpctests.parameters\x1a\x18.grpctests.Long_Response\x12\x41\n\x0eGetsEightLongs\x12\x15.grpctests.parameters\x1a\x18.grpctests.Long_Response\x12O\n\x0cProcessClass\x12\x1e.grpctests.ProcessClassRequest\x1a\x1f.grpctests.ProcessClassResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpctests_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGE']._serialized_start=59
  _globals['_MESSAGE']._serialized_end=85
  _globals['_MESSAGERESPONSE']._serialized_start=87
  _globals['_MESSAGERESPONSE']._serialized_end=121
  _globals['_PARAMETERS']._serialized_start=123
  _globals['_PARAMETERS']._serialized_end=172
  _globals['_LONG_RESPONSE']._serialized_start=174
  _globals['_LONG_RESPONSE']._serialized_end=205
  _globals['_MYCLASS']._serialized_start=207
  _globals['_MYCLASS']._serialized_end=231
  _globals['_PROCESSCLASSREQUEST']._serialized_start=233
  _globals['_PROCESSCLASSREQUEST']._serialized_end=292
  _globals['_PROCESSCLASSRESPONSE']._serialized_start=294
  _globals['_PROCESSCLASSRESPONSE']._serialized_end=332
  _globals['_TESTSRPC']._serialized_start=335
  _globals['_TESTSRPC']._serialized_end=682
# @@protoc_insertion_point(module_scope)