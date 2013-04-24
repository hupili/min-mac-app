# Minimalist's MAC App Creation

This is for fresh beginners of MAC to quickly package an application in the `.app` format.
People who eagerly want a try can jump to the "Usage" section.

## Motivation

   * You had some interesting executables: native binary, bash, jar arvhive, Python, Perl, ...
   * You had some good application but not so well packaged for MAC.
   * You don't want to invoke from CLI everytime. 
   * You don't want to tap into Object-C in order to write MACish applications or wrapper for them. 
   * You don't want to install XCode 
   (installing a 1.8G app for this simple goal feels like an elephant on your toe!)

After some Googling, 
you find the "hello world" examples are all telling you how to create an XCode project
or how to create a window with some elements using XCode. 
How come nobody tells you the minimalist's way to layout an `.app` folder?
What you want is simply

   * a properly layed-out `.app` folder with minimum stuffs.
   * an entrance script, probably a bash script, that will be executed 
   when you run this App with `open` or from Spotlight or ...

Awesome!
You can essentially do everything now with this setting! 
What you don't want is

   * A framework with binaries, which you don't know exactly what is happening.
   You OCD forces to use only those the internal works are transparent to you. 
   * Run additional "packager", "installer" ... 
   Why not give me the package directly so that I can modify it accordingly? 

OK. 
If you have the same feelings like me, here it is!

## Usage

   * Clone/ download this project. 
   * Put the `my.app` under your `/Applications/` dir. 
   Rename as you wish. 
   * Modify `Contents/MacOS/main.sh` accordingly so that it invokes your executables. 
   You may want to put other resources in the same folder to make it more like a package. 

Before any modification, you can try `open my.app` from CLI to test whether it works. 
It should open [this project repo](https://github.com/hupili/min-mac-app/) with your default browser.

## Case Study

JabRef is my current favourite reference manager. 
I started to use on Linux. 
Although there is an OSX package on the 
[download page of JabRef](http://sourceforge.net/projects/jabref/files/jabref/2.9.2),
MAC does not execute it
(prompt "damaged package" and the only option is to cancel or move to trash).
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
   * Put `my.app` under `/Applications/` dir an rename it to `JabRef.app`
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

## Surveyed Methods

   * My first trial is to use a command-line XCode project.
   It turns out there is no option to distribute it as `.app` bundle. 
   * Then I tried the Cocoa application. 
   From "product"-"archive"-"distribute", one can choose the `.app` bundle format. 
   That is pretty close to what I'm looking for. 
   I don't have time to dive into OC in order to figure out a good way to invoke other scripts. 
   I just find the `main.c` file and modify the `main()` function therein. 
   Luckily, OC is at least C.
   I can do it with out learning the "weird" grammar (to me) of OC.
   However, this way is not always portable to other platforms.
   If I share the X project instead of distributed `.app`, others need to compile it first. 
   It contradicts with the original intention. 
   * A [stackoverflow discussion](http://stackoverflow.com/questions/7404792/how-to-create-mac-application-bundle-for-python-script-via-python) 
   on how to package a python script into MAC's app structure. 
   The author had come up with Python script to implement this minimal framework. 
   The final layout of the minimalist's app bundle framework is adapted from this scripts. 
   We made a copy in `other/gen-app.py` for easy reference. 
   * [PyInstaller](http://www.pyinstaller.org), 
   which is pointed out in the above thread, 
   looks sophisticated but it's only for Python. 
   Later I may use it to package larger projects. 
   * [platypus](http://sveinbjorn.org/platypus) creates MAC apps from scripts. 
   
