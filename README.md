# Musical Instrument Project
This project manages and displays musical instruments within a database.

Users have the ability 

## Prerequisites
Access to a operating system capable of installing Vagrant.

## Installing
* Install [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Install [Vagrant](https://www.vagrantup.com/downloads.html)
* In a terminal navigate to the root directory of vagrant.
* Enter the command `vagrant up`, to boot the Vagrant environment
* Enter the command `vagrant ssh`, to login
* Download the Musical Instruments Project from git address.

* Navigate to the folder containing the `musical_instruments_project.py` file




Don't need this::::
* Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) that will be used in the ananlysis
* Unzip the downloaded file and place the `newsdata.sql` file in the working Vagrant directory.
* Enter the command `psql -d news -f newsdata.sql` to connect the database server and execute the necessary SQL commands to create tables and corresponding data.
Don't need this::::

#### Running the web application
* Enter the command `python musical_instruments_project.py`, to run the main driver.
* Once the vagrant application is running within the Vagrant environment, visit localhost:5000 in a browser
* To modify instruments, click on the "Login" link and login to Google+. 

#### Built With
Python 2.7

#### Authors
Joey Berger