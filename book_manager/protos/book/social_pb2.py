# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/book/social.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18protos/book/social.proto\x12\x0b\x62ook_social\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\":\n\x0fLikeBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0c\n\x04like\x18\x02 \x01(\x08\x12\x0b\n\x03uid\x18\x03 \x01(\t\"#\n\x13GetBookLikesRequest\x12\x0c\n\x04isbn\x18\x01 \x03(\t\"5\n\x12GetBookLikesResult\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x11\n\tbook_like\x18\x02 \x01(\x05\"I\n\x16GetBookLikesListResult\x12/\n\x06result\x18\x01 \x03(\x0b\x32\x1f.book_social.GetBookLikesResult\"@\n\x12\x43ommentBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\t\"\x93\x01\n\x15GetBookCommentRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x39\n\x10next_create_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x03 \x01(\x05H\x01\x88\x01\x01\x42\x13\n\x11_next_create_timeB\x08\n\x06_limit\"s\n\x14GetBookCommentResult\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"M\n\x18GetBookCommentListResult\x12\x31\n\x06result\x18\x01 \x03(\x0b\x32!.book_social.GetBookCommentResult2\xcf\x02\n\nBookSocial\x12\x41\n\tlike_book\x12\x1c.book_social.LikeBookRequest\x1a\x16.google.protobuf.Empty\x12V\n\rget_book_like\x12 .book_social.GetBookLikesRequest\x1a#.book_social.GetBookLikesListResult\x12G\n\x0c\x63omment_book\x12\x1f.book_social.CommentBookRequest\x1a\x16.google.protobuf.Empty\x12]\n\x10get_book_comment\x12\".book_social.GetBookCommentRequest\x1a%.book_social.GetBookCommentListResultb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.book.social_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIKEBOOKREQUEST._serialized_start=103
  _LIKEBOOKREQUEST._serialized_end=161
  _GETBOOKLIKESREQUEST._serialized_start=163
  _GETBOOKLIKESREQUEST._serialized_end=198
  _GETBOOKLIKESRESULT._serialized_start=200
  _GETBOOKLIKESRESULT._serialized_end=253
  _GETBOOKLIKESLISTRESULT._serialized_start=255
  _GETBOOKLIKESLISTRESULT._serialized_end=328
  _COMMENTBOOKREQUEST._serialized_start=330
  _COMMENTBOOKREQUEST._serialized_end=394
  _GETBOOKCOMMENTREQUEST._serialized_start=397
  _GETBOOKCOMMENTREQUEST._serialized_end=544
  _GETBOOKCOMMENTRESULT._serialized_start=546
  _GETBOOKCOMMENTRESULT._serialized_end=661
  _GETBOOKCOMMENTLISTRESULT._serialized_start=663
  _GETBOOKCOMMENTLISTRESULT._serialized_end=740
  _BOOKSOCIAL._serialized_start=743
  _BOOKSOCIAL._serialized_end=1078
# @@protoc_insertion_point(module_scope)
