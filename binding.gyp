{
	'targets': [{
		'target_name': 'protobuf',
		'sources': [ './src/init.cpp', './src/native.cpp', './src/parse.cpp', './src/serialize.cpp' ],
		'include_dirs': [
			'<!(node -e "require(\'nan\')")',
			'<(module_root_dir)/deps/protobuf/src'
		],
		"dependencies": [
	    	"<(module_root_dir)/deps/protobuf.gyp:libprotobuf"
	     ],
		'cflags' : [ '-Ofast', '-ffast-math', '-funroll-loops', '-fomit-frame-pointer', '-std=c++11', '-pthread', '-static', '-I../../' ],
		'cflags_cc' : [ '-Ofast', '-ffast-math', '-funroll-loops', '-fomit-frame-pointer', '-std=c++11', '-pthread', '-static', '-I../../' ],
		'conditions': [
			['OS == "win"', {
				'msvs_settings': {
					'VCLinkerTool': {
						
					}
				}
			}],
			['OS == "mac"', {
				'xcode_settings': {
					'MACOSX_DEPLOYMENT_TARGET': '10.7',
					'OTHER_CPLUSPLUSFLAGS': [
						'-stdlib=libc++',
					],
					'GCC_ENABLE_CPP_RTTI': 'YES'
				}
			}],
			['OS == "linux"', {
				'cflags_cc!': [ '-fno-rtti' ],
			}]
		]
	}]
}
