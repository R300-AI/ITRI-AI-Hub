---
layout: default
title: " - ROCm"
nav_order: 8
---

# How to install AMD Radeon Driver on Ubuntu 22.04 LTS

<div align="center"><img src="../../assets/images/rocm.png" width="640"/></div>

**Step 1**: Download and convert the package signing key
```
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null
```

**Step 2**: Add the AMDGPU Repository and Install the Kernel-mode Driver
```
# setting a variable for the version of the AMDGPU repository we want to use
ver=5.7
# add the AMDGPU repository for Ubuntu 22.04
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/$ver/ubuntu jammy main" | sudo tee /etc/apt/sources.list.d/amdgpu.list
# update the package list to include the newly added repository
sudo apt update

# Create a preference file to prioritize packages from the AMDGPU repository over system packages.
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
sudo apt install amdgpu-dkms
sudo reboot
```
