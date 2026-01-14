#!/bin/bash

# https://extensionworkshop.com/documentation/publish/promoting-your-extension/
curl -sSLO https://blog.mozilla.org/addons/files/2020/04/get-the-addon-fx-apr-2020.svg
inkscape --export-type=png --export-width=172 --export-background-opacity=0 get-the-addon-fx-apr-2020.svg