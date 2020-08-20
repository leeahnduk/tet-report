# tetreport
This application helps to build basic report for Tetration cluster.

## Table of contents
* [Installation](#Installation)
* [Screenshots](#screenshots)
* [How to Use](#UserGuide)
* [Show Commands](#Show)
* [Create Commands](#Create)
* [Setup Commands](#Setup)
* [Clean Commands](#Clean)
* [Others Commands](#Others)
* [Steps to run](#Steps)
* [Feedback and Author](#Feedback)

## Installation

From sources

Download the sources from [Github](https://github.com/leeahnduk/tet-report.git), extract and execute the following commands

```
$ pip3 install -r requirements.txt

```

## Screenshots
![Example screenshot](https://github.com/leeahnduk/tet-report/blob/master/tet-report.jpg)
![Vulerabilities report screenshot](https://github.com/leeahnduk/tet-report/blob/master/tet-vul.jpg)

## UserGuide
How to use this application:
To access to the cluster you need to get the API Credentials with the following permissions
* `sensor_management` - option: SW sensor management: API to configure and monitor status of SW sensors
* `hw_sensor_management` - option: HW sensor management: API to configure and monitor status of HW sensors
* `flow_inventory_query` - option: Flow and inventory search: API to query flows and inventory items in Tetration cluster
* `user_role_scope_management` - option: Users, roles and scope management: API for root scope owners to read/add/modify/remove users, roles and scopes
* `app_policy_management` - option: 
 Applications and policy management: API to manage applications and enforce policies

Download the api_credentials.json locally and have it ready to get the information required for the setup.

A quick look for the help will list the current available options.
To start the script, just use: `python3 tet-report.py --url https://tet-cluster-ip --credential api_credentials.json`
```

Object support:
  * workloads       Build report about all workloads or detail about a specific workload
  * flows           Build top flow report in a specific timerange
  * apps            Build application report into xlsx format


```

Each subcommand has its own help that list the options available.

```
You can use -h, help, h, ? to get help and options
```

## Report
```
tetcli #  report workloads all 
Report all installed workloads in your cluster in all scopes

tetcli #  report workloads detail
Detail Report about a specific workload 

tetcli #  report workloads stats
Detail Workload communication report from time (t0) to time(t1) 

tetcli #  report workloads software 
Detail Installed Software Packages report for a specific workload

tetcli #  report workloads vulnerabilities ?
Detail Vulnerable Software Packages report for a specific workload or all workloads that match a CVE Score query. Sub: workload or all

tetcli #  report workloads vulnerabilities all
Detail Vulnerable Software Packages report for all workloads that match a CVE score query.

tetcli #  report workloads vulnerabilities workload
Detail Vulnerable Software Packages report for a specific workload.

tetcli #  report workloads processes ?
Detail Running processes report for a specific workload. Sub command: summary or all

tetcli #  report workloads processes summary
Summary Running processes report for a specific workload.

tetcli #  report workloads processes all
Detail all Running processes report for a specific workload.

tetcli #  report apps ?
Build application report into xlsx format. Sub command: conversation or policies

tetcli #  report apps conv
Download conversation report into xlsx format for a specific application.

tetcli #  report apps pol
Build detail application policies report into xlsx format.

tetcli #  report flows ?
Build top flow report in a specific timerange. Sub command: inventory or top

tetcli #  report flows inv
Detail flow communication report about a subnet in a VRF from time (t0) to time(t1).

tetcli #  report flows top ?
Top Talkers/Destination/Service report in excel for a scope from time (t0) to time(t1). Sub command: talkers, servers, sports, dports

tetcli #  report flows top talkers
Top Talkers report in excel for a scope from time (t0) to time(t1).

tetcli #  report flows top dest
Top Destination report in excel for a scope from time (t0) to time(t1).

tetcli #  report flows top sport
Top source Service report in excel for a scope from time (t0) to time(t1). 

tetcli #  report flows top dport
Top Destination Service report in excel for a scope from time (t0) to time(t1). Sub command: talkers, servers, sports, dports


```

## Steps

Step 1: Issue `$ pip3 install -r requirements.txt` to install all required packages.

Step 2: Run the apps: `python3 tet-report.py --url https://tet-cluster-ip --credential api_credentials.json`

Step 3: Test if you can successfully query the cluster from the command line
```
tetcli #  report wl vul all
Which CVE Score you want to query your inventory (from 0 to 10): 8
Processing vulnerabilities data ........  
```

## Feedback
Any feedback can send to me: Le Anh Duc (leeahnduk@yahoo.com or anhdle@cisco.com)
