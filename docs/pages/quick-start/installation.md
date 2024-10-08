---
layout: default
title: " - Installation"
nav_order: 3
---

# Installation

## Setup Configure Tool & Environments

<div style="margin-left: 20px;">
<br>If you have not previously installed the Configuration Tool, follow the instructions below to install it on the host.
</div>

### **NVIDIA Jetson Series**
### **MediaTek Genio Series**

#### **Requirements:**

* Ubuntu 22.04(LTS) Server 

Step 1. Use the following command to install the required packages
```
sudo apt-get install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev
mkdir -p ~/.bin
PATH="${HOME}/.bin:${PATH}"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+rx ~/.bin/repo
```
Step 2. Setup required software, USB device rules and install Genio Tools.
```
# Repo
$ mkdir -p ~/.bin
$ PATH="${HOME}/.bin:${PATH}"
$ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
$ chmod a+rx ~/.bin/repo

# Git
$ add-apt-repository ppa:git-core/ppa
$ apt update
$ apt-get install git

# Python3
$ sudo apt update
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```

Step 3. Install the Fastboot & USB Driver
```
$ sudo apt update
$ sudo apt-get install android-tools-adb android-tools-fastboot

$ echo -n 'SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="201c", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", ATTR{idProduct}=="0003", MODE="0660", TAG+="uaccess" SUBSYSTEM=="usb", ATTR{idVendor}=="0403", MODE="0660", TAG+="uaccess" SUBSYSTEM=="gpio", MODE="0660", TAG+="uaccess"' | sudo tee /etc/udev/rules.d/72-aiot.rules
$ sudo udevadm control --reload-rules
$ sudo udevadm trigger
```
Step 4. Install and verify the installation
```
$ pip3 install -U genio-tools
$ genio-config
fastboot: OK
udev rules: OK
```



### **ARM Raspberry Pi Series**


## Flash Image to Boards

### **NVIDIA Jetson Series**
### **MediaTek Genio Series**

  <details>
  <summary><strong>Genio 350 EVK</strong></summary>

  1. A
    <pre><code>
        <span>print('hello world')</span>
        <span>print('hello world')</span>
        <span>print('hello world')</span>
    </code></pre>
  2. B<br>
  3. C<br>

  </details>

### **ARM Raspberry Pi Series**