# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dbData.proto

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
  name='dbData.proto',
  package='DBData',
  serialized_pb=_b('\n\x0c\x64\x62\x44\x61ta.proto\x12\x06\x44\x42\x44\x61ta\"\x19\n\x07\x44\x42_Prop\x12\x0e\n\x06propid\x18\x01 \x01(\x03\"\xa2\x01\n\rDB_PlayerAttr\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x02 \x01(\x03\x12\x0e\n\x06silver\x18\x03 \x01(\x05\x12\x0c\n\x04gold\x18\x04 \x01(\x05\x12\x10\n\x08viplevel\x18\x05 \x01(\x05\x12\x12\n\ncreatetime\x18\x06 \x01(\x03\x12\x11\n\tlogintime\x18\x07 \x01(\x03\x12\x10\n\x08ossystem\x18\x08 \x01(\x05\x12\x0c\n\x04plat\x18\t \x01(\x05\"\xbe\x01\n\tDB_Player\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0e\n\x06openid\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\ncreatetime\x18\x04 \x01(\x03\x12\x11\n\tlogintime\x18\x05 \x01(\x03\x12\x12\n\nlogouttime\x18\x06 \x01(\x03\x12(\n\tattribute\x18\x07 \x01(\x0b\x32\x15.DBData.DB_PlayerAttr\x12!\n\x08proplist\x18\x08 \x03(\x0b\x32\x0f.DBData.DB_Prop\"\x1f\n\rDB_GlobalData\x12\x0e\n\x06maxuid\x18\x01 \x01(\x03\"\xa7\x01\n\x0b\x44\x42_EventLog\x12\x0c\n\x04\x65vid\x18\x01 \x01(\x05\x12\x0b\n\x03uid\x18\x02 \x01(\x03\x12\r\n\x05stime\x18\x03 \x01(\t\x12\x0e\n\x06param1\x18\x04 \x01(\x03\x12\x0e\n\x06param2\x18\x05 \x01(\x03\x12\x0e\n\x06param3\x18\x06 \x01(\x03\x12\x0e\n\x06param4\x18\x07 \x01(\x03\x12\x0e\n\x06param5\x18\x08 \x01(\x03\x12\x0e\n\x06param6\x18\t \x01(\x03\x12\x0e\n\x06param7\x18\n \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DB_PROP = _descriptor.Descriptor(
  name='DB_Prop',
  full_name='DBData.DB_Prop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='propid', full_name='DBData.DB_Prop.propid', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=24,
  serialized_end=49,
)


_DB_PLAYERATTR = _descriptor.Descriptor(
  name='DB_PlayerAttr',
  full_name='DBData.DB_PlayerAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='DBData.DB_PlayerAttr.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='DBData.DB_PlayerAttr.exp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='silver', full_name='DBData.DB_PlayerAttr.silver', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='DBData.DB_PlayerAttr.gold', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='viplevel', full_name='DBData.DB_PlayerAttr.viplevel', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createtime', full_name='DBData.DB_PlayerAttr.createtime', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logintime', full_name='DBData.DB_PlayerAttr.logintime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ossystem', full_name='DBData.DB_PlayerAttr.ossystem', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plat', full_name='DBData.DB_PlayerAttr.plat', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=52,
  serialized_end=214,
)


_DB_PLAYER = _descriptor.Descriptor(
  name='DB_Player',
  full_name='DBData.DB_Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='DBData.DB_Player.uid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='openid', full_name='DBData.DB_Player.openid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='DBData.DB_Player.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createtime', full_name='DBData.DB_Player.createtime', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logintime', full_name='DBData.DB_Player.logintime', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logouttime', full_name='DBData.DB_Player.logouttime', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='DBData.DB_Player.attribute', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proplist', full_name='DBData.DB_Player.proplist', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=217,
  serialized_end=407,
)


_DB_GLOBALDATA = _descriptor.Descriptor(
  name='DB_GlobalData',
  full_name='DBData.DB_GlobalData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='maxuid', full_name='DBData.DB_GlobalData.maxuid', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=409,
  serialized_end=440,
)


_DB_EVENTLOG = _descriptor.Descriptor(
  name='DB_EventLog',
  full_name='DBData.DB_EventLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='evid', full_name='DBData.DB_EventLog.evid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='DBData.DB_EventLog.uid', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stime', full_name='DBData.DB_EventLog.stime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param1', full_name='DBData.DB_EventLog.param1', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param2', full_name='DBData.DB_EventLog.param2', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param3', full_name='DBData.DB_EventLog.param3', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param4', full_name='DBData.DB_EventLog.param4', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param5', full_name='DBData.DB_EventLog.param5', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param6', full_name='DBData.DB_EventLog.param6', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param7', full_name='DBData.DB_EventLog.param7', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=443,
  serialized_end=610,
)

_DB_PLAYER.fields_by_name['attribute'].message_type = _DB_PLAYERATTR
_DB_PLAYER.fields_by_name['proplist'].message_type = _DB_PROP
DESCRIPTOR.message_types_by_name['DB_Prop'] = _DB_PROP
DESCRIPTOR.message_types_by_name['DB_PlayerAttr'] = _DB_PLAYERATTR
DESCRIPTOR.message_types_by_name['DB_Player'] = _DB_PLAYER
DESCRIPTOR.message_types_by_name['DB_GlobalData'] = _DB_GLOBALDATA
DESCRIPTOR.message_types_by_name['DB_EventLog'] = _DB_EVENTLOG

DB_Prop = _reflection.GeneratedProtocolMessageType('DB_Prop', (_message.Message,), dict(
  DESCRIPTOR = _DB_PROP,
  __module__ = 'dbData_pb2'
  # @@protoc_insertion_point(class_scope:DBData.DB_Prop)
  ))
_sym_db.RegisterMessage(DB_Prop)

DB_PlayerAttr = _reflection.GeneratedProtocolMessageType('DB_PlayerAttr', (_message.Message,), dict(
  DESCRIPTOR = _DB_PLAYERATTR,
  __module__ = 'dbData_pb2'
  # @@protoc_insertion_point(class_scope:DBData.DB_PlayerAttr)
  ))
_sym_db.RegisterMessage(DB_PlayerAttr)

DB_Player = _reflection.GeneratedProtocolMessageType('DB_Player', (_message.Message,), dict(
  DESCRIPTOR = _DB_PLAYER,
  __module__ = 'dbData_pb2'
  # @@protoc_insertion_point(class_scope:DBData.DB_Player)
  ))
_sym_db.RegisterMessage(DB_Player)

DB_GlobalData = _reflection.GeneratedProtocolMessageType('DB_GlobalData', (_message.Message,), dict(
  DESCRIPTOR = _DB_GLOBALDATA,
  __module__ = 'dbData_pb2'
  # @@protoc_insertion_point(class_scope:DBData.DB_GlobalData)
  ))
_sym_db.RegisterMessage(DB_GlobalData)

DB_EventLog = _reflection.GeneratedProtocolMessageType('DB_EventLog', (_message.Message,), dict(
  DESCRIPTOR = _DB_EVENTLOG,
  __module__ = 'dbData_pb2'
  # @@protoc_insertion_point(class_scope:DBData.DB_EventLog)
  ))
_sym_db.RegisterMessage(DB_EventLog)


# @@protoc_insertion_point(module_scope)
