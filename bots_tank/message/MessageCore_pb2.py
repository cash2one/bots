# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageCore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MessageCore.proto',
  package='Message',
  serialized_pb=_b('\n\x11MessageCore.proto\x12\x07Message\"9\n\x0c\x44seNetAccept\x12\x0c\n\x04sock\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\r\n\x05\x65rror\x18\x03 \x01(\x05\":\n\rDseNetConnect\x12\x0c\n\x04sock\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\r\n\x05\x65rror\x18\x03 \x01(\x05\"8\n\x0b\x44seNetClose\x12\x0c\n\x04sock\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\r\n\x05\x65rror\x18\x03 \x01(\x05\"T\n\rDseServerInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0c\n\x04\x61\x64\x64r\x18\x04 \x01(\t\x12\r\n\x05world\x18\x07 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DSENETACCEPT = _descriptor.Descriptor(
  name='DseNetAccept',
  full_name='Message.DseNetAccept',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sock', full_name='Message.DseNetAccept.sock', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.DseNetAccept.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='Message.DseNetAccept.error', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=87,
)


_DSENETCONNECT = _descriptor.Descriptor(
  name='DseNetConnect',
  full_name='Message.DseNetConnect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sock', full_name='Message.DseNetConnect.sock', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.DseNetConnect.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='Message.DseNetConnect.error', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=147,
)


_DSENETCLOSE = _descriptor.Descriptor(
  name='DseNetClose',
  full_name='Message.DseNetClose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sock', full_name='Message.DseNetClose.sock', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.DseNetClose.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='Message.DseNetClose.error', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=205,
)


_DSESERVERINFO = _descriptor.Descriptor(
  name='DseServerInfo',
  full_name='Message.DseServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Message.DseServerInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Message.DseServerInfo.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='Message.DseServerInfo.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addr', full_name='Message.DseServerInfo.addr', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world', full_name='Message.DseServerInfo.world', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=291,
)

DESCRIPTOR.message_types_by_name['DseNetAccept'] = _DSENETACCEPT
DESCRIPTOR.message_types_by_name['DseNetConnect'] = _DSENETCONNECT
DESCRIPTOR.message_types_by_name['DseNetClose'] = _DSENETCLOSE
DESCRIPTOR.message_types_by_name['DseServerInfo'] = _DSESERVERINFO

DseNetAccept = _reflection.GeneratedProtocolMessageType('DseNetAccept', (_message.Message,), dict(
  DESCRIPTOR = _DSENETACCEPT,
  __module__ = 'MessageCore_pb2'
  # @@protoc_insertion_point(class_scope:Message.DseNetAccept)
  ))
_sym_db.RegisterMessage(DseNetAccept)

DseNetConnect = _reflection.GeneratedProtocolMessageType('DseNetConnect', (_message.Message,), dict(
  DESCRIPTOR = _DSENETCONNECT,
  __module__ = 'MessageCore_pb2'
  # @@protoc_insertion_point(class_scope:Message.DseNetConnect)
  ))
_sym_db.RegisterMessage(DseNetConnect)

DseNetClose = _reflection.GeneratedProtocolMessageType('DseNetClose', (_message.Message,), dict(
  DESCRIPTOR = _DSENETCLOSE,
  __module__ = 'MessageCore_pb2'
  # @@protoc_insertion_point(class_scope:Message.DseNetClose)
  ))
_sym_db.RegisterMessage(DseNetClose)

DseServerInfo = _reflection.GeneratedProtocolMessageType('DseServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _DSESERVERINFO,
  __module__ = 'MessageCore_pb2'
  # @@protoc_insertion_point(class_scope:Message.DseServerInfo)
  ))
_sym_db.RegisterMessage(DseServerInfo)


# @@protoc_insertion_point(module_scope)
