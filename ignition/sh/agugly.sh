#!/bin/bash
# This script is meant to do a system update and upgrade and fix-missing for apt-get.
# agug - Apt-Get UpGrade

sudo apt-get update --fix-missing
sudo apt-get autoremove
sudo apt-get upgrade -y
sudo apt-get update --fix-missing