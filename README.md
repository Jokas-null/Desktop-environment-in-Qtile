# Qtile-Config
My qtile.

# Screenshots 🖥️

![pic2.png](https://github.com/Jokas-null/Qtile-Config/blob/main/screenshots/pic2.png)

![pic1.png](https://github.com/Jokas-null/Qtile-Config/blob/main/screenshots/pic1.png)

## Installation (Arch based)🐧

Install Qtile and dependencies:

```
sudo pacman -S qtile 
yay -S nerd-fonts-ubuntu-mono
pip install psutil
```
### For Debian, Ubuntu

For Debian, Ubuntu and derivates [here](http://docs.qtile.org/en/latest/manual/install/ubuntu.html) is the qtile installation guide.


## Cloning the config files 📁

Clone this repository and copy my configs:

```bash
git clone https://github.com/Jokas-null/Qtile-Config.git
cp -r Qtile-Config ~/.config/qtile
```
## Startup  🏁

One of the most important functions in the config is the startup function located at ```config.py```.

``` python
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
```

If you want to change *autostart* programs, open  ```./autostart.sh```.

```bash
#!/bin/sh

nitrogen --restore &

picom --experimental-backends &
```
