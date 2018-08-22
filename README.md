[conky](http://conky.sourceforge.net/) is a free, light-weight system monitor for X, that displays any information on your desktop & **conky-colors** is an easier way to configure **conky**.

This project (*pithy conky colors*) is based on [https://github.com/aikunzhe/conky_colors], I added *GPU name*, *HD temp*, *CPU temp*, and fixed *lunar*. I tried to add *CPU fan*, but abandoned it due to no fan-sensors. 

*conky* has a wealth of functions, you can reference to ```utils/conky_colors_params``` of this proj, and enjoy it. 

PS: I want to add a *weather module*, but I did not find a good way, if you have some ways, please share it to me, thanks!  

# Usage

## Prerequisites:

```
sudo apt-get install aptitude python-statgrab python-keyring ttf-ubuntu-font-family hddtemp curl lm-sensors conky-all
```
==============

***Attention***: if get failure in installing **statgrab**, go to ```utils```of this proj, and install statgrab manually,
1. ```sudo dpkg -i libstatgrab6_0.17-0ubuntu1_amd64.deb```
2. ```sudo dpkg -i python-support_1.0.15_all.deb```
3. ```sudo apkg -i python-statgrab_0.5-4_amd64.deb```

==============

## Sensors

1. ``` sudo chmod u+s /usr/sbin/hddtemp```
2. ```sudo sensors-detect```

***Attention***: answering ***Yes*** to all the questions. And restart your session(***log out*** or ***restart***).

## Install
Download this proj ```git clone https://github.com/CarryJzzZ/pithy-conky-colors.git```and enter it.

1. run: ```make```
2. run: ```sudo make install```
3. cp ```utils/lunar``` to ```~/.conkycolors/bin/```

## Run

1. run: ```conky-colors --theme=noble --lang=en --cpu=4 --network --hd=default --hdtemp1=sda --hdtemp2=sdb --cputemp --unit=C```(just an example)
2. Update font cache for displaying CN-font. ```sudo fc-cache -v -f```
3. replace the contents of ```~/.conkycolors/conkyrc``` with ```utils/conkyrc-bak``` of this proj.
4. run ```conky -c ~/.conkycolors/conkyrc```

***Attention***: evevry time you run ```conky-colors --<options>```, you should replace the contents of ```~/.conkycolors/conkyrc```.

## Results

***Attention***To run conky at startup, *go to System > Preferences > Startup Applications*, click *Add* and add the path to the conkyStart file (```/usr/local/share/conkycolors/bin/conkyStart```), and the widget will run 25s later the time you start the PC.

![utils/results.png]


## Issues

1. in ```conkyrc```, use ```WenQuanYi Micro Hei``` as CN font.
2. if there is wrong in displaying CN, please check whether the ```wqy/``` exists in  ```/usr/share/fonts/turetype/```
3. you can change the ```voffset, go to, alignment, gap_x, gap_y, minimum_size, maximum_width```and so on to customize the layout.

