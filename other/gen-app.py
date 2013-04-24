#!/usr/bin/python

import sys
assert len(sys.argv) > 1

apppath = sys.argv[1]

import os, os.path
assert os.path.splitext(apppath)[1] == ".app"

os.mkdir(apppath)
os.mkdir(apppath + "/Contents")
os.mkdir(apppath + "/Contents/MacOS")

version = "1.0.0"
bundleName = "Test"
bundleIdentifier = "org.test.test"

f = open(apppath + "/Contents/Info.plist", "w")
f.write("""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>English</string>
    <key>CFBundleExecutable</key>
    <string>main.py</string>
    <key>CFBundleGetInfoString</key>
    <string>%s</string>
    <key>CFBundleIconFile</key>
    <string>app.icns</string>
    <key>CFBundleIdentifier</key>
    <string>%s</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleName</key>
    <string>%s</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>%s</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleVersion</key>
    <string>%s</string>
    <key>NSAppleScriptEnabled</key>
    <string>YES</string>
    <key>NSMainNibFile</key>
    <string>MainMenu</string>
    <key>NSPrincipalClass</key>
    <string>NSApplication</string>
</dict>
</plist>
""" % (bundleName + " " + version, bundleIdentifier, bundleName, bundleName + " " + version, version))
f.close()

f = open(apppath + "/Contents/PkgInfo", "w")
f.write("APPL????")
f.close()

f = open(apppath + "/Contents/MacOS/main.py", "w")
f.write("""#!/usr/bin/python
print "Hi there"
""")
f.close()

import stat
oldmode = os.stat(apppath + "/Contents/MacOS/main.py").st_mode
os.chmod(apppath + "/Contents/MacOS/main.py", oldmode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
