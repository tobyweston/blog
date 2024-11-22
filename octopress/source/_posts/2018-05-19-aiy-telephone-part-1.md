---
layout: post
title: "AIY Telephone Part 1"
date: 2018-05-19 20:16
comments: true
categories: 
sidebar: false
published: false
keywords: ""
description: ""
---

# Setup AIY Kit 

I didn't want to use the Raspbian image supplied by Google as I prefer the more lightweight headless option.

1. Install Raspbian (Scratch) Lite
1. Setup basic Pi (see other posts)
1. Install AIY Kit via [the Github instructions](https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/HACKING.md)


## Setup the AIY Kit

1. Checkout the code

    ```
    cd
    git clone https://github.com/google/aiyprojects-raspbian.git AIY-projects-python    
    ```
    
1. Install `pip3`

    sudo apt-get install python3-pip

1. Install the related services `ntpdate` and `alsa-init`.

    ```
    cd ~/AIY-projects-python
    sudo scripts/install-services.sh
    
    ```
    
1. Setup audio

    ```
    cd ~/AIY-projects-python
    sudo scripts/configure-driver.sh  -- maybe 
    sudo scripts/install-alsa-config.sh
    sudo reboot
    ```

1. Install Google Assistant library

    There's some problems with the Github instructions (or were, see the [issue](https://github.com/google/aiyprojects-raspbian/issues/378)), so you will need to do the following.

    ```    
    sudo apt-get install python3-pip
    pip3 install google-assistant-library==0.1.0
    ```

1. Check your audio

    ```
    cd ~/AIY-projects-python
    checkpoints/check_audio.py
    ```

## Setup Google Cloud

You'll need an account on the Google Cloud Platform.

1. Goto https://console.cloud.google.com/

1. Create a project (`Select a Project` > `Create a Project`)

1. Assign the `Voice Kit` to the project (`API & Services` > `Library` > select `Google Assistant API`).

1. Create the credentials for Google Assistant API.

    Assign them to the project.

