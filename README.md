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
add ui2jui.py to your local binary directory just so you can call the ui2jui from any directory you want

```
sudo ln -s abs_path_to_ui2jui.py /usr/local/bin/ui2jui
sudo chmod +x /usr/local/bin/ui2jui
```
