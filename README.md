# FYI
You do not really need this tool, all you need to do to save the qtdesigner's ui as .jui is locate your **JAVA_HOME** on your *\*rc file*
to do so:
```
export JAVA_HOME=path_to_java_home
```

## ui2jui
Small tool to convert qt designer ui files to jui(Java user interface definition file) which is required for
JUIC(Java User Interface Compiler) to generate java source files.
## Usage
**convert one specific ui file**
```
python ui2jui.py -f somedesignfile.ui
```

**convert all ui files from current directory**
```
python ui2jui.py -d
```

**convert all ui files recursively from current directory**
```
python ui2jui.py -r
```

****
***NOTE: if you want to remove original file after converted just add -rm flag***

####Tips
add ui2jui.py to your local binary directory so that you can call the ui2jui from any directory you want

```
sudo ln -s abs_path_to_ui2jui.py /usr/local/bin/ui2jui
sudo chmod +x /usr/local/bin/ui2jui
```

now you can call the script from any **working directory** you want with
```
ui2jui options
```
