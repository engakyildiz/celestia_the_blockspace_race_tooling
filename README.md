## celestia_the_blockspace_race_tooling
Create Toolings for the Celestia Network

# In this study, a simple tool was designed with Python Programming language to display the Celestia the Blockspace Race Light Node server CPU Usage, Memory Usage, Disk Usage, size of the /data folder and remaining disk space.

## Prerequisites

- Python3
- Python3 psutil Library

Make sure you have python3 on your server. To check python3 version, use the following command:

`python3 -V`

`which python3`

If you don't have python, please follow these step:

`sudo apt install python3 python3-pip`

Install the psutil library using pip:

`pip3 install psutil`

Clone the repository:

`git clone https://github.com/engakyildiz/celestia_the_blockspace_race_tooling.git`

## Install and Usage

Change to the path:

`cd celestia_the_blockspace_race_tooling/`

Run the bellow command:

`python3 celestia_the_blockspace_race_tooling.py`

After running the above command, you can see the statistics of CPU usage, Memory usage, Disk usage, Remaining Disk Space and the size of the /data folder every 60 seconds.



