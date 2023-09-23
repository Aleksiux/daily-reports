# RelyITS Python test exercise

This is an initial git repository used as a part of interview for a Python developer role in RelyITS.

## Sample data

Files that should be used in exercise:

* [POSLogV6.0.0.xsd](POSLogV6.0.0.xsd) XSD schema
* [Test XML files](receipts) (*feel free to generate more test files, based on XSD schema*)

## Aim of the exercise

The goal is to give an opportunity to an interviewer to show one's skills in following fields:

* Code design & development
* Usage of various development tools
* Ability to use good coding practices
* Creativity
* Error handling

## Task background scenario

### Hypothetical situation

You are responsible for the service that produces various daily reports. The customer has asked you to create a new
nightly report that summarizes company's sales data throughout the day.

### Architectural design flow

* The service receives multiple XML files that are stored in a directory by another service
* All data from XML files must be stored to a database tables
* The service must generate a comma-separated (CSV) file consisting of aggregated data read from database

### Development requirements

The service must have the following functionality, consisting of **two** component scripts.

#### First component script

* Be able to read the directory full of files
* Correctly parse XML files
* Store gathered XML data to a database

#### Second component script

* Read data from database
* Aggregate data **grouped by store**
* Provide a final CSV file

### Final CSV report explanation

| CSV field name | Field name in XML file                                    | Description                                      |
|----------------|-----------------------------------------------------------|--------------------------------------------------|
| Date           |                                                           | Today’s date                                     |
| StoreID        | UnitID                                                    | Internal ID of the Store                         |
| TotalItems     | RetailTransaction\LineItem\Sale\Quantity                  | Amount of items sold                             |
| TotalAmount    | RetailTransaction\Total[TotalType=”TransactionNetAmount”] | Total amount paid in the receipt                 |
| TotalReceipts  |                                                           | Total amount of receipts received from the store |

## Task requirements

### Mandatory criteria

* Clone this repository
* Create a GitHub repository and push the required files
    * **two** python scripts
        * Python version is not specified, can be chosen to interviewer's comfort
    * **SQL database schema** to recreate tables used in this task
        * Database to use: MySQL or MariaDB
    * **README.md** file for clear task explanation and installation instructions

### Additional bonuses

* Object-Oriented Programming (OOP) knowledge
* Virtual environment setup
* Code testing
* Logging

# Point of Contact

If an interviewer has any questions or concerns, one should not hesitate and ask directly. Such questions are highly
appreciated and welcomed. 🙂

Contact person:

* Martynas Degutis, [martynas.degutis@relyits.se](mailto:martynas.degutis@relyits.se)