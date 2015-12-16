{
  'variables': {
        'target_arch%': '<!(node -e \"var os = require(\'os\'); console.log(os.arch());\")>'},

        'targets': [
            {
                'conditions': [
                        ['OS == "win"', {
                              'msvs_settings': {
                                    'VCCLCompilerTool': {
                                    'RuntimeTypeInfo': 'false',
                                    'EnableFunctionLevelLinking': 'true',
                                    'ExceptionHandling': '2',
                                    'DisableSpecificWarnings': [ '4355', '4530' ,'4267', '4244', '4506' ]
                                    }
                              },
                        }]
                  ],
                  'target_name': 'sodium',
                  'sources': [
                        'sodium.cc',
                  ],
                  "dependencies": [
                        "<(module_root_dir)/deps/libsodium.gyp:libsodium"
                  ],
                  'include_dirs': [
                       './deps/libsodium/src/libsodium/include',
                       "<!(node -e \"require('nan')\")"
                  ],
                  'cflags!': [ '-fno-exceptions' ],
                  
            }
      ]
}
