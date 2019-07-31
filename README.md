# KisanMill
KisanMill is a platform for the farmers , customers and students where farmers can sell their product directly to the customers by eliminating the process of the middle man. They can also contact government to submit the sample of the zero day attack of the diseases on the crops and much more. The people can create services for the farmers like cold storage , combines and farmers can contact them by comparing their price and location. Students can help the farmers directly from the portal.


KisanMill is an open source project for farmers , students ,customers built with [Python][2.7] using the [Django Web Framework][1.11].

The project has eight basic apps from which six are almost completed :

* Administrator       ( Admin panel to handle the queries and monitor the platform. )
* Accounts            (Handle Authentication part of the whole App. )
* Bond                ( A bond is to get the investment , facilities for a particular product. )
* Customercorner      ( App to create/update all the categories and products. )
* Core                ( Handle authentication of the Application. )
* Expertcorner        ( Connect local universities students with the farmers. )
* Shop                ( App to list all the services , auctions , biddings. )
* UFS                 ( Urgent Feedback System. )

## Administrator App
Admin section to maintain the queries from farmers through ufs app and can see all the bidding made by farmers and customers.

> 1. **Main Admin page and all of its options.**

![alt text](docs/snapshots/admin/1_main_administrator_page.png)
---

> 2. **Adding new product for the farmers in the panel.**

![alt text](docs/snapshots/admin/2_list_of_all_products_from_admin_panel.png)
---

> 3. **Complaint list Inbox in the Admin Account  / Reports Submitted by the Farmers on the affected crops.**

![alt text](docs/snapshots/admin/3_compaint_list_inbox.png)
---

> 4. **Zero day disease sample submitted by the farmers on the Application.**

![alt text](docs/snapshots/admin/4_disease_report.png)
---

## Accounts App
Not implemented yet

## Bond App
Join the farmers with investors on the basis of the their requirements like investment and requirements.

> 1. **Creating an new bond farmer.**

![alt text](docs/snapshots/bond/1_creating_a_new_bond.png)

---

> 2. **List of all bonds b/w the farmers and the investors.**

![alt text](docs/snapshots/bond/2_list_all_bonds_between_people.png)
---


## Customercorner App
The customers can see all products , add products , see categories.

## Core App
Core app is used to handle the authentication system of the platform. It is also used to maintain the user list on the platform

> 1. **Category choosing page before login.**

![alt text](docs/snapshots/core/1_category_login.png)
---

> 2. **Login Page.**

![alt text](docs/snapshots/core/2_login_page.png)
---



## Expert Corner App
Expertcorner App is used by the students,teachers and researchers to interact with the farmers. Find a cure for the solution.


## Shop App
Shop is the most important app where all the features will be present.

The list of all features which are present in the Application are as follow :


> 1. **Landing Page 1.**

![alt text](docs/snapshots/shop/1_landing_page_1.png)
---

> 2. **Landing Page 2.**

![alt text](docs/snapshots/shop/2_landing_page_2.png)
---

> 3. **Landing Page 3.**

![alt text](docs/snapshots/shop/3_landing_page_3.png)
---

> 4. **Creating a new service for farmer.**

![alt text](docs/snapshots/shop/4_creating_a_new_services_for_the_farmers.png)
---


> 6. **List of all services made by the vendor.**

![alt text](docs/snapshots/shop/5_list_of_all_services_for_the_farmers.png)
---

> 6. **Details of a service for the farmer provided by the vendor.**

![alt text](docs/snapshots/shop/6_details_of_a_service_for_the_farmer_provided_by_the_vendor.png)
---

> 7. **Details of another service for the farmer provided by the vendor.**

![alt text](docs/snapshots/shop/7_detail_of_another_service_for_the_farmer_provided_by_the_vendor.png)
---

> 8. **Creating auction for the crops (by farmer).**

![alt text](docs/snapshots/shop/8_creating_auction_for_the_crop_by_farmer.png)
---

> 9. **List of all Auction of a farmer.**

![alt text](docs/snapshots/shop/9_list_of_all_auction_of_a_farmer.png)
---


> 10. **Detail of biddings on a crop.**

![alt text](docs/snapshots/shop/10_details_of_a_bidding_on_auction_of_crops.png)
---

> 11. **Customer bidding on the crop.**

![alt text](docs/snapshots/shop/11_customer_bidding_on_the_product.png)
---

> 12. **List of all auctions for the customer to bid.**

![alt text](docs/snapshots/shop/12_list_of_all_auction_for_bidding_by_customer.png)
---

## UFS App
Urgent feedback system provided to the farmers to direct contact to the government agencies to submit the sample of the zero day attack on the crops.
They can tell about the attack and upload images of the attack so that it will help agencies to detect the new diseases.

>  Feedback form to submit the crop diseases and its images
![alt text](docs/snapshots/ufs/giving_feedback_for_the_disease_to_the_organizations.png)
---

## Technology Stack

- Python 2.7 / 3.5
- Django > 1.11
- Twitter Bootstrap 3
- jQuery 2
- javascript

## Installation Guide

navigate to the directory Code by cloning project using

>> git clone https://github.com/pr0jects27/kisanmill.git

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
