# Sec-tools
A collection of custom tools to assist in various security challenges

![Capture the Flag](https://i.memecaptain.com/gend_images/KlaO_w.jpg)

# Installation
```
git clone git@github.com:CameronLonsdale/sec-tools.git
cd sec-tools
virtualenv -p /usr/bin/python3 letsjusthackshit
source ./letsjusthackshit/bin/activate
pip install -r requirements.txt
```

# Tools

Tool         | Description                                       | Python support
------------ | ------------------------------------------------- | --------------
hex_to_file  | Writes a given hex string as bytes to stdout      | 2 & 3
wtf_is_this  | Enumerates decodings for a strange looking string | 3
