---
layout: default
title: "　-　NeuronPilot"
nav_order: 31
---

# Install NeuronPilot for Genios-Ubuntu
##### update : 2024/10 by Markov Chen

### Step 1: Install Gstreamer and NeuronPilot Library
Clone the repository and run the setup script for your specific Genio device:

```
git clone https://github.com/R300-AI/ITRI-AI-Hub.git

# Genio 350
bash ITRI-AI-Hub/tools/setup_genio350.sh
# Genio 510
bash ITRI-AI-Hub/tools/setup_genio510.sh
# Genio 700
bash ITRI-AI-Hub/tools/setup_genio700.sh
# Genio 1200
bash ITRI-AI-Hub/tools/setup_genio1200.sh
```

### Step 2: Reboot and Verify the Installation
Reboot your system and verify the installation by running the following command:

```
sudo python3 /usr/share/neuropilot/benchmark_dla/benchmark.py --auto
```
