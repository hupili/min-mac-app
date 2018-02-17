# Minimalist's MAC App Creation

This is for fresh beginners of MAC to quickly package an application in the `.app` format.

## Usage

   * Clone / 
   [download](https://github.com/hupili/min-mac-app/archive/master.zip)
   this project. 
   * Put `my.app` dir under your `/Applications/` dir. 
   Rename as you wish. 
   * Modify `Contents/MacOS/main.sh` accordingly so that it invokes your executables. 

Before any modification, you can try `open my.app` from CLI to test whether it works. 
It should open [this project repo](https://github.com/hupili/min-mac-app/) with your default browser.

## Case Study

JabRef is my current favourite reference manager. 
I started to use it on Linux. 
Although there is an OSX package on the 
[download page of JabRef](http://sourceforge.net/projects/jabref/files/jabref/2.9.2),
MAC does not execute it
(prompt "damaged package" and the only option is to cancel or move it to trash).
Nevertheless, it's written in Java and they have `jar` archive for download. 
So I use that `jar` and execute it with 
`open JabRef-2.9.2.jar`
or
`java -jar JabRef-2.9.2.jar`
from CLI.
After two months' use in this way, I think having an app package is better. 
Then I can start it from Spotlight or other app launchers. 
It's simple:

   * Download this project. 
   * Put `my.app` under `/Applications/` dir and rename it to `JabRef.app`
   * Download the 
   [.jar file](http://sourceforge.net/projects/jabref/files/jabref/2.9.2/)
   and put it under `Contents/MacOS/`.
   * Modify `Contents/MacOS/main.sh`:

```
#!/bin/bash

_dir=`dirname $0`
_fn=`basename $0`
cd $_dir

open JabRef-2.9.2.jar
```

Your minimal layout of the app looks like this:

![](https://raw.github.com/hupili/min-mac-app/master/screenshots/minimal-layout-app.png)

You can now launch it from spotlight: 

![](https://raw.github.com/hupili/min-mac-app/master/screenshots/spotlight.png)

OK, it's running now:

![](https://raw.github.com/hupili/min-mac-app/master/screenshots/jabref-launch.png)

## Extensions

### Icon

You can add a custom icon to the app

   * Put the icon under `Contents/Resources`
   * In your `info.plist` change/add

```
<key>CFBundleIconFile</key>
<string>iconfile</string>
```

The [diff](https://github.com/hupili/min-mac-app/commit/9545018fd1717021141441f93472af1fd89a3177)
shows you more intuitively how 
[an icon](http://findicons.com/icon/58561/mac?id=58719) is added.

## Further 

   * Read 
   [more](https://github.com/hupili/min-mac-app/blob/master/more.md)
   about the motivation and reference.
   * Go to the 
   [blog post](http://blog.hupili.net/p--20130424-min-mac-app/)
   for a discussion. 

## List of minimal Apps created with this repo

* https://github.com/hupili/mma-hkbu-vpn

## License

MIT
