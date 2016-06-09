{
  'targets': [
    {
      "target_name": "libprotobuf",
      "type": "static_library",
      'defines': [],
      "include_dirs": [
        "protobuf/src",
        "protobuf"
      ],
      'cflags_cc!': [
          '-fno-rtti',
      ],
      'cflags_cc': [
        '-Wno-return-type',
        '-Wno-unused-local-typedefs',
        '-Wno-sign-compare',
        '-Wno-ignored-qualifiers',
        '-Wno-maybe-uninitialized'
      ],
      "conditions": [
        [
          'OS=="mac"',
          {
            'xcode_settings': {
              'OTHER_CFLAGS' : [
                '-Wno-return-type',
                '-Wno-unused-local-typedefs',
                '-Wno-sign-compare',
                '-Wno-ignored-qualifiers',
                '-Wno-maybe-uninitialized'
                '-ObjC',
              ],
              'OTHER_LDFLAGS': [],
              'MACOSX_DEPLOYMENT_TARGET': '10.11',
            }
          }
        ],
        [
          'OS=="win"',
          {
            'msvs_settings': {
              'VCLinkerTool': {
                 'SetChecksum': 'true'
              }
            },
          }
        ]
      ],
      'sources': [
        "protobuf/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc",
        "protobuf/src/google/protobuf/stubs/atomicops_internals_x86_msvc.cc",
        "protobuf/src/google/protobuf/stubs/common.cc",
        "protobuf/src/google/protobuf/stubs/hash.h",
        "protobuf/src/google/protobuf/stubs/once.cc",
        "protobuf/src/google/protobuf/stubs/map_util.h",
        "protobuf/src/google/protobuf/stubs/shared_ptr.h",
        "protobuf/src/google/protobuf/stubs/stringprintf.cc",
        "protobuf/src/google/protobuf/stubs/stringprintf.h",
        "protobuf/src/google/protobuf/extension_set.cc",
        "protobuf/src/google/protobuf/generated_message_util.cc",
        "protobuf/src/google/protobuf/message_lite.cc",
        "protobuf/src/google/protobuf/repeated_field.cc",
        "protobuf/src/google/protobuf/wire_format_lite.cc",
        "protobuf/src/google/protobuf/io/coded_stream.cc",
        "protobuf/src/google/protobuf/io/coded_stream_inl.h",
        "protobuf/src/google/protobuf/io/zero_copy_stream.cc",
        "protobuf/src/google/protobuf/io/zero_copy_stream_impl_lite.cc",
        "protobuf/src/google/protobuf/stubs/strutil.cc",
        "protobuf/src/google/protobuf/stubs/strutil.h",
        "protobuf/src/google/protobuf/stubs/substitute.cc",
        "protobuf/src/google/protobuf/stubs/substitute.h",
        "protobuf/src/google/protobuf/stubs/structurally_valid.cc",
        "protobuf/src/google/protobuf/descriptor.cc",
        "protobuf/src/google/protobuf/descriptor.pb.cc",
        "protobuf/src/google/protobuf/descriptor_database.cc",
        "protobuf/src/google/protobuf/dynamic_message.cc",
        "protobuf/src/google/protobuf/extension_set_heavy.cc",
        "protobuf/src/google/protobuf/generated_message_reflection.cc",
        "protobuf/src/google/protobuf/message.cc",
        "protobuf/src/google/protobuf/reflection_ops.cc",
        "protobuf/src/google/protobuf/service.cc",
        "protobuf/src/google/protobuf/text_format.cc",
        "protobuf/src/google/protobuf/unknown_field_set.cc",
        "protobuf/src/google/protobuf/wire_format.cc",
        "protobuf/src/google/protobuf/io/gzip_stream.cc",
        "protobuf/src/google/protobuf/io/printer.cc",
        "protobuf/src/google/protobuf/io/strtod.cc",
        "protobuf/src/google/protobuf/io/tokenizer.cc",
        "protobuf/src/google/protobuf/io/zero_copy_stream_impl.cc",
        "protobuf/src/google/protobuf/compiler/importer.cc",
        "protobuf/src/google/protobuf/compiler/parser.cc"
      ]
    }
  ]
}
