# Python Script For Banner Grabbing

### This Script Is Created For http://bitforestinfo.blogspot.com


With This Python Script We Can Easily Find Open Ports Of Any Website And Then We Can Grab Different Banners of Services Available On Different Ports.

# Features

- Easy To Use

- Easy To Maintain

# Usages

```
Usage: bannergrab.py [options] 

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -t TARGET, --target=TARGET
                        Specify Target For Scan
  -i INPUT, --input=INPUT
                        Specify Input Txt File Of Data
  -p PORT, --port=PORT  Specify Target Ports Seperated by commas or Provide
                        Range of Ports. eg. 80-1200
  -n THREAD, --thread=THREAD
                        Specify Number of Thread For Scanning
  -o OUTPUT, --output=OUTPUT
                        Specify Path For Saving Output in Txt.
  -c CHECK, --check=CHECK
                        Specify False Or 0 If Provided Open Ports Are Already
                        TESTED. Or if open ports are not verified then, don't
                        use this argument.
  -T TIMEOUT, --timeout=TIMEOUT
                        Specify Port Time Out Seconds
```
# Examples

#### Example 1:
```
    python bannergrab.py -t www.site.in -p 0-22,24,80 
```

#### Example 2:
```
    python bannergrab.py -t www.site.in -p 22,80,60,65,453 -o results.txt

```
#### Example 3:
```
    python bannergrab.py -t www.site.in -p 0-22000 -o results.txt --thread 800
```


# Author.

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/

    Note: We Feel Proud To Be Indian
######################################################



# Development.


Want to Contribute? Great!


There Are 2 Methods.

1. Pull Request ( Github Account Required ).

2. Through Email.


### 1. Pull Request ( Github A/c Required ). 

1. Fork it!

2. Create your feature branch: `git checkout -b my-new-feature`

3. Commit your changes: `git commit -am 'Add some feature'`

4. Push to the branch: `git push origin my-new-feature`

5. Submit a pull request :D



### 2. Through Email.

1. Send Your Updated Version On My Email.

- surajsinghbisht054@gmail.com


----

## License

Apache License


