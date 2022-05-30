# compile_conf
Simple builder configuration files from environment, encrypted values or user input

Complete syntax is:

```
compile_conf [{-k|--aes-key} aes_key_file] [{-K|--rsa-key} rsa_key_file] [{-d|--diff} diff_file] [{-D|--def} comment key value] {support|production|testing|internal|devel} sample_file config_file
```

but typical usage is very easier:

```
compile_conf production config.sample config.cfg
```

where
- **production** defines environment where be config.cfg used
- **config.sample** is source of configuration - contain definitions for all enviromnents
- **config.cfg** is output file

Tool is available by composer:

```
composer require travelport-czech/compile_conf '*'
```

Depends on package [PyCrypto](https://pypi.org/project/pycrypto/)(deprecated) or [PyCryptodome](https://pypi.org/project/pycryptodome/)(recommended)
