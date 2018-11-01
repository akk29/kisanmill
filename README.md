# KisanMill
KisanMill is a platform for the farmers , customers and students where farmers can sell their product directly to the customers by eliminating the process of the middle man. They can also contact government to submit the sample of the zero day attack of the diseases on the crops and much more. The people can create services for the farmers like cold storage , combines and farmers can contact them by comparing their price and location. Students can help the farmers directly from the portal.


KisanMill is an open source project for farmers , students ,customers built with [Python][2.7] using the [Django Web Framework][1.11].

The project has eight basic apps from which six are almost completed :

* Administrator       ( Admin panel to handle the queries and monitor the platform. )
* Accounts
* Bond                ( A bond is to get the investment , facilities for a particular product. )
* Customercorner      ( App to create/update all the categories and products. )
* Core                ( Handle authentication of the Application. )
* Expertcorner        ( Connect local universities students with the farmers. )
* Shop                ( App to list all the services , auctions , biddings. )
* UFS                 ( Urgent Feedback System. )

## Administrator App
Admin section to maintain the queries from farmers through ufs app and can see all the bidding made by farmers and customers.

- Main Admin page and all of its options
![alt text](https://github.com/hackath0n/kisanmill/blob/master/docs/snapshots/main_administrator_page.png)

- Adding new product for the farmers in the panel.
![alt text](https://github.com/hackath0n/kisanmill/blob/master/docs/snapshots/adding_new_product_from_admin_panel.png)

- Complaint list Inbox in the Admin Account  / Reports Submitted by the Farmers on the affected crops
![alt text](https://github.com/hackath0n/kisanmill/blob/master/docs/snapshots/compaint_list_inbox.png)

- Zero day disease sample submitted by the farmers on the Application.
![alt text](https://github.com/hackath0n/kisanmill/blob/master/docs/snapshots/disease_report.png)

## Accounts App
Not implemented yet

## Bond App
Join the farmers with investors on the basis of the their requirements like investment and requirements.


## Customercorner App
The customers can see all products , add products , see categories.

## Core App
Core app is used to handle the authentication system of the platform. It is also used to maintain the user list on the platform

## Expert Corner App
Expertcorner App is used by the students,teachers and researchers to interact with the farmers. Find a cure for the solution.


## Shop App
Shop is the most important app where all the features will be present.

The list of all features which are present in the Application are as follow :

* Create an auction.
* Check all the bidding on the auction.
* Urgent feedback system.
* Create a new service.
* List all services provided to the farmers.
* Create a new bond.
* List all bonds.

## Expertcorner App
Not implemented yet (but it will join the local students with the farmers so that they can help the farmers.)

## UFS App
Urgent feedback system provided to the farmers to direct contact to the government agencies to submit the sample of the zero day attack on the crops.
They can tell about the attack and upload images of the attack so that it will help agencies to detect the new diseases.

- Feedback form to submit the crop diseases and its images
![alt text](https://github.com/hackath0n/kisanmill/blob/master/docs/snapshots/giving_feedback_for_the_disease_to_the_organizations.png)

## Technology Stack

- Python 2.7 / 3.5
- Django > 1.11
- Twitter Bootstrap 3
- jQuery 2
- javascript

## Installation Guide

navigate to the directory Code by cloning project using

>> git clone https://github.com/hackath0n27/kisanmill.git

navigate to the directory kisanmill and Code

>> cd kisanmill
>> cd code

Install the base packages for the proper functioning of the project

>> pip install -r requirements.txt


## Demo

After Installation and setup navigate to the directory
open command line in the same directory

>> python manage.py runserver

To see the website follow : http://127.0.0.1:8000
