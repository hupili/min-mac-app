# Minimalist's MAC App Creation

This is for fresh beginners of MAC to quickly package an application in the `.app` format.
(Read [more](https://github.com/hupili/min-mac-app/blob/master/more.md) about the motivation and reference)

## Usage

   * Clone / 
   [download](https://github.com/hupili/min-mac-app/archive/master.zip)
   this project. 
   * Put `my.app` dir under your `/Applications/` dir. 
   Rename as you wish. 
   * Modify `Contents/MacOS/main.sh` accordingly so that it invokes your executables. 
   You may want to put other resources in the same folder to make it more like a package. 

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
