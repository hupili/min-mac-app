

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
   Our final layout of the minimalist's app bundle framework is adapted from this scripts. 
   We made a copy in `other/gen-app.py` for easy reference. 
   * [PyInstaller](http://www.pyinstaller.org), 
   which is pointed out in the above thread, 
   looks sophisticated but it's only for Python. 
   Later I may use it to package larger projects. 
   * [platypus](http://sveinbjorn.org/platypus) creates MAC apps from scripts. 
   * Actually, my first trial is not the first point...
   I really tried to go into other app's dir can modify a minimal layout. 
   However, even if after modifying `CFBundleExecutable` of `Info.plist`, the script does not execute. 
   There are too many entries in a normal `Info.plist`...
   I don't have time to learn it and turned to the Internet. 
   Hope someone who understands the detailed structure can make the "minimal" 
   `Info.plist` in this repo the real minimal. 
   
