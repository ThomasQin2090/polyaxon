#!/usr/bin/python
#
# Copyright 2019 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/run.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from v1 import base_pb2 as v1_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/run.proto',
  package='v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cv1/run.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\rv1/base.proto\"\\\n\x0bRunMetaInfo\x12\x0f\n\x07service\x18\x01 \x01(\x08\x12\x13\n\x0b\x63oncurrency\x18\x02 \x01(\x05\x12\x15\n\rparallel_kind\x18\x03 \x01(\t\x12\x10\n\x08run_kind\x18\x04 \x01(\t\"\x9a\x06\n\x03Run\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x04 \x03(\t\x12\x0f\n\x07\x64\x65leted\x18\x05 \x01(\x08\x12\x0c\n\x04user\x18\x06 \x01(\t\x12\r\n\x05owner\x18\x07 \x01(\t\x12\x0f\n\x07project\x18\x08 \x01(\t\x12.\n\ncreated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_managed\x18\r \x01(\t\x12\x0f\n\x07\x63ontent\x18\x0e \x01(\t\x12\x0e\n\x06status\x18\x0f \x01(\t\x12\x0e\n\x06readme\x18\x10 \x01(\t\x12\x12\n\nbookmarked\x18\x11 \x01(\x08\x12\"\n\tmeta_info\x18\x12 \x01(\x0b\x32\x0f.v1.RunMetaInfo\x12\x19\n\x04kind\x18\x13 \x01(\x0e\x32\x0b.v1.RunKind\x12\x0b\n\x03hub\x18\x14 \x01(\t\x12\'\n\x06inputs\x18\x15 \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x07outputs\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x07run_env\x18\x17 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tis_resume\x18\x18 \x01(\x08\x12\x10\n\x08is_clone\x18\x19 \x01(\x08\x12\x18\n\x10\x63loning_strategy\x18\x1a \x01(\t\x12\x10\n\x08pipeline\x18\x1b \x01(\t\x12\x10\n\x08original\x18\x1c \x01(\t\x12\x15\n\rpipeline_name\x18\x1d \x01(\t\x12\x15\n\roriginal_name\x18\x1e \x01(\t\x12!\n\x08settings\x18\x1f \x01(\x0b\x32\x0f.v1.RunSettings\"F\n\x0eRunBodyRequest\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x14\n\x03run\x18\x03 \x01(\x0b\x32\x07.v1.Run\"^\n\x14\x45ntityRunBodyRequest\x12\x30\n\x06\x65ntity\x18\x01 \x01(\x0b\x32 .v1.ProjectEntityResourceRequest\x12\x14\n\x03run\x18\x02 \x01(\x0b\x32\x07.v1.Run\"[\n\x10ListRunsResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x18\n\x07results\x18\x02 \x03(\x0b\x32\x07.v1.Run\x12\x10\n\x08previous\x18\x03 \x01(\t\x12\x0c\n\x04next\x18\x04 \x01(\t\"0\n\x12RunSettingsCatalog\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xb9\x03\n\x0bRunSettings\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12%\n\x05\x61gent\x18\x02 \x01(\x0b\x32\x16.v1.RunSettingsCatalog\x12%\n\x05queue\x18\x03 \x01(\x0b\x32\x16.v1.RunSettingsCatalog\x12*\n\nlogs_store\x18\x04 \x01(\x0b\x32\x16.v1.RunSettingsCatalog\x12-\n\routputs_store\x18\x05 \x01(\x0b\x32\x16.v1.RunSettingsCatalog\x12\x30\n\x10init_connections\x18\x06 \x03(\x0b\x32\x16.v1.RunSettingsCatalog\x12+\n\x0b\x63onnections\x18\x07 \x03(\x0b\x32\x16.v1.RunSettingsCatalog\x12,\n\x0cgit_accesses\x18\x08 \x03(\x0b\x32\x16.v1.RunSettingsCatalog\x12/\n\x0fregistry_access\x18\t \x01(\x0b\x32\x16.v1.RunSettingsCatalog\x12\x30\n\x10\x63onfig_resources\x18\n \x03(\x0b\x32\x16.v1.RunSettingsCatalog*6\n\x07RunKind\x12\x07\n\x03job\x10\x00\x12\x0b\n\x07service\x10\x01\x12\x07\n\x03\x64\x61g\x10\x02\x12\x0c\n\x08parallel\x10\x03\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,v1_dot_base__pb2.DESCRIPTOR,])

_RUNKIND = _descriptor.EnumDescriptor(
  name='RunKind',
  full_name='v1.RunKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='job', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='service', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='dag', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='parallel', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1820,
  serialized_end=1874,
)
_sym_db.RegisterEnumDescriptor(_RUNKIND)

RunKind = enum_type_wrapper.EnumTypeWrapper(_RUNKIND)
job = 0
service = 1
dag = 2
parallel = 3



_RUNMETAINFO = _descriptor.Descriptor(
  name='RunMetaInfo',
  full_name='v1.RunMetaInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='v1.RunMetaInfo.service', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concurrency', full_name='v1.RunMetaInfo.concurrency', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parallel_kind', full_name='v1.RunMetaInfo.parallel_kind', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_kind', full_name='v1.RunMetaInfo.run_kind', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=266,
)


_RUN = _descriptor.Descriptor(
  name='Run',
  full_name='v1.Run',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='v1.Run.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.Run.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='v1.Run.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.Run.tags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='v1.Run.deleted', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='v1.Run.user', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='v1.Run.owner', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project', full_name='v1.Run.project', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='v1.Run.created_at', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='v1.Run.updated_at', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='v1.Run.started_at', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished_at', full_name='v1.Run.finished_at', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_managed', full_name='v1.Run.is_managed', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='v1.Run.content', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='v1.Run.status', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readme', full_name='v1.Run.readme', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bookmarked', full_name='v1.Run.bookmarked', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta_info', full_name='v1.Run.meta_info', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='v1.Run.kind', index=18,
      number=19, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hub', full_name='v1.Run.hub', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='v1.Run.inputs', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='v1.Run.outputs', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_env', full_name='v1.Run.run_env', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_resume', full_name='v1.Run.is_resume', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_clone', full_name='v1.Run.is_clone', index=24,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloning_strategy', full_name='v1.Run.cloning_strategy', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='v1.Run.pipeline', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original', full_name='v1.Run.original', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_name', full_name='v1.Run.pipeline_name', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_name', full_name='v1.Run.original_name', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='v1.Run.settings', index=30,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=1063,
)


_RUNBODYREQUEST = _descriptor.Descriptor(
  name='RunBodyRequest',
  full_name='v1.RunBodyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='v1.RunBodyRequest.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project', full_name='v1.RunBodyRequest.project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run', full_name='v1.RunBodyRequest.run', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1065,
  serialized_end=1135,
)


_ENTITYRUNBODYREQUEST = _descriptor.Descriptor(
  name='EntityRunBodyRequest',
  full_name='v1.EntityRunBodyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='v1.EntityRunBodyRequest.entity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run', full_name='v1.EntityRunBodyRequest.run', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1137,
  serialized_end=1231,
)


_LISTRUNSRESPONSE = _descriptor.Descriptor(
  name='ListRunsResponse',
  full_name='v1.ListRunsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='v1.ListRunsResponse.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='v1.ListRunsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous', full_name='v1.ListRunsResponse.previous', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='v1.ListRunsResponse.next', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1233,
  serialized_end=1324,
)


_RUNSETTINGSCATALOG = _descriptor.Descriptor(
  name='RunSettingsCatalog',
  full_name='v1.RunSettingsCatalog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='v1.RunSettingsCatalog.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.RunSettingsCatalog.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1326,
  serialized_end=1374,
)


_RUNSETTINGS = _descriptor.Descriptor(
  name='RunSettings',
  full_name='v1.RunSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='v1.RunSettings.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent', full_name='v1.RunSettings.agent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queue', full_name='v1.RunSettings.queue', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs_store', full_name='v1.RunSettings.logs_store', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs_store', full_name='v1.RunSettings.outputs_store', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_connections', full_name='v1.RunSettings.init_connections', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connections', full_name='v1.RunSettings.connections', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_accesses', full_name='v1.RunSettings.git_accesses', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_access', full_name='v1.RunSettings.registry_access', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config_resources', full_name='v1.RunSettings.config_resources', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1377,
  serialized_end=1818,
)

_RUN.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUN.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUN.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUN.fields_by_name['finished_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUN.fields_by_name['meta_info'].message_type = _RUNMETAINFO
_RUN.fields_by_name['kind'].enum_type = _RUNKIND
_RUN.fields_by_name['inputs'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RUN.fields_by_name['outputs'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RUN.fields_by_name['run_env'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RUN.fields_by_name['settings'].message_type = _RUNSETTINGS
_RUNBODYREQUEST.fields_by_name['run'].message_type = _RUN
_ENTITYRUNBODYREQUEST.fields_by_name['entity'].message_type = v1_dot_base__pb2._PROJECTENTITYRESOURCEREQUEST
_ENTITYRUNBODYREQUEST.fields_by_name['run'].message_type = _RUN
_LISTRUNSRESPONSE.fields_by_name['results'].message_type = _RUN
_RUNSETTINGS.fields_by_name['agent'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['queue'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['logs_store'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['outputs_store'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['init_connections'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['connections'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['git_accesses'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['registry_access'].message_type = _RUNSETTINGSCATALOG
_RUNSETTINGS.fields_by_name['config_resources'].message_type = _RUNSETTINGSCATALOG
DESCRIPTOR.message_types_by_name['RunMetaInfo'] = _RUNMETAINFO
DESCRIPTOR.message_types_by_name['Run'] = _RUN
DESCRIPTOR.message_types_by_name['RunBodyRequest'] = _RUNBODYREQUEST
DESCRIPTOR.message_types_by_name['EntityRunBodyRequest'] = _ENTITYRUNBODYREQUEST
DESCRIPTOR.message_types_by_name['ListRunsResponse'] = _LISTRUNSRESPONSE
DESCRIPTOR.message_types_by_name['RunSettingsCatalog'] = _RUNSETTINGSCATALOG
DESCRIPTOR.message_types_by_name['RunSettings'] = _RUNSETTINGS
DESCRIPTOR.enum_types_by_name['RunKind'] = _RUNKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunMetaInfo = _reflection.GeneratedProtocolMessageType('RunMetaInfo', (_message.Message,), {
  'DESCRIPTOR' : _RUNMETAINFO,
  '__module__' : 'v1.run_pb2'
  # @@protoc_insertion_point(class_scope:v1.RunMetaInfo)
  })
_sym_db.RegisterMessage(RunMetaInfo)

Run = _reflection.GeneratedProtocolMessageType('Run', (_message.Message,), {
  'DESCRIPTOR' : _RUN,
  '__module__' : 'v1.run_pb2'
  # @@protoc_insertion_point(class_scope:v1.Run)
  })
_sym_db.RegisterMessage(Run)

RunBodyRequest = _reflection.GeneratedProtocolMessageType('RunBodyRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNBODYREQUEST,
  '__module__' : 'v1.run_pb2'
  # @@protoc_insertion_point(class_scope:v1.RunBodyRequest)
  })
_sym_db.RegisterMessage(RunBodyRequest)

EntityRunBodyRequest = _reflection.GeneratedProtocolMessageType('EntityRunBodyRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYRUNBODYREQUEST,
  '__module__' : 'v1.run_pb2'
  # @@protoc_insertion_point(class_scope:v1.EntityRunBodyRequest)
  })
_sym_db.RegisterMessage(EntityRunBodyRequest)

ListRunsResponse = _reflection.GeneratedProtocolMessageType('ListRunsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRUNSRESPONSE,
  '__module__' : 'v1.run_pb2'
  # @@protoc_insertion_point(class_scope:v1.ListRunsResponse)
  })
_sym_db.RegisterMessage(ListRunsResponse)

RunSettingsCatalog = _reflection.GeneratedProtocolMessageType('RunSettingsCatalog', (_message.Message,), {
  'DESCRIPTOR' : _RUNSETTINGSCATALOG,
  '__module__' : 'v1.run_pb2'
  # @@protoc_insertion_point(class_scope:v1.RunSettingsCatalog)
  })
_sym_db.RegisterMessage(RunSettingsCatalog)

RunSettings = _reflection.GeneratedProtocolMessageType('RunSettings', (_message.Message,), {
  'DESCRIPTOR' : _RUNSETTINGS,
  '__module__' : 'v1.run_pb2'
  # @@protoc_insertion_point(class_scope:v1.RunSettings)
  })
_sym_db.RegisterMessage(RunSettings)


# @@protoc_insertion_point(module_scope)
