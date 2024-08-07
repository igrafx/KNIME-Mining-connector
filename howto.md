# How to use the extension

This document encompasses the installation and basic uses of the **iGrafx KNIME Mining Extension**.

The **iGrafx KNIME Mining Extension** is an open-source application seamlessly integrated with Knime to effortlessly transmit data to the iGrafx Mining Platform.

It is powered by the [iGrafx P360 Live Mining SDK](https://github.com/igrafx/mining-python-sdk) and rooted in Python.
 
This connector simplifies the data transfer process, eliminating complexity and enhancing your workflow.

To maximize the benefits of this extension, ensure you have an active iGrafx account. If you don't have one, please contact us to set up your account.

**Please make sure you have the 5.2 version of Knime as the latest release works with that version.**


***

## Table of Contents

1. [Installing the iGrafx Extension](#installing-the-igrafx-extension)
2. [Using the iGrafx KNIME Mining Extension](#using-the-igrafx-knime-mining-extension)
3. [Using the iGrafx API Connection Node](#using-the-igrafx-api-connection-node)
4. [Using the Project Creation Node](#using-the-project-creation-node)
5. [Using the iGrafx Column Mapping Status Node](#using-the-igrafx-column-mapping-status-node)
6. [Using the iGrafx File Upload Node](#using-the-igrafx-file-upload-node)
7. [The iGrafx Mining Project Data Node](#the-igrafx-mining-project-data-node)
8. [The iGrafx Mining Completed Cases Node](#the-igrafx-mining-completed-cases-node)
9. [The iGrafx Mining Project Variant Fetcher Node](#the-igrafx-mining-project-variant-fetcher-node)
10. [The iGrafx Mining Project Mapping Info Fetcher Node](#the-igrafx-mining-project-mapping-info-fetcher-node)
11. [The iGrafx Mining Project Deletion Node](#the-igrafx-mining-project-deletion-node)
12. [The iGrafx Mining Column Mapping Fetcher Node](#the-igrafx-mining-column-mapping-fetcher-node)
13. [The iGrafx SAP Data fetcher](#using-the-igrafx-sap-data-fetcher)
14. [The iGrafx Mining Project Files Info Fetcher Node](#the-igrafx-mining-project-files-info-fetcher-node)
15. [The iGrafx Mining File Info Fetcher Node](#the-igrafx-mining-file-info-fetcher-node)
16. [The iGrafx Mining Extension Example](#the-igrafx-mining-extension-example)
17. [Using the iGrafx Mining Knime Extension as a developer](#using-the-igrafx-mining-knime-extension-as-a-developer)
18. [Requirements](#requirements)
19. [Getting Started](#getting-started)
20. [Using the iGrafx Knime Extension locally](#using-the-igrafx-knime-extension-locally)
21. [Further Documentation](#further-documentation)

## Installing the iGrafx Extension
To install the **iGrafx Extension** on Knime as a user, open Knime. 

Click on the **settings** icon in the top right of the window.

![settings_icon](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/settings_icon.png)

Then, click on the **arrow** next to the **Install/Update** section.

Go to the **Available Software sites** section and click the add button.

![Available_Software](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/available_software_5.2.png)

In the window that pops up, make sure the information are as follows:

- Name: iGrafx Extension
- Location: https://raw.githubusercontent.com/igrafx/KNIME-Mining-connector/master/igrafx_extension/releases

Copy and paste the location in the respective input. 

**5.2 is the latest Knime version and the build will work with that version.**

![location2](https://github.com/igrafx/KNIME-Mining-connector/blob/master/images/location3.png)

Click on **Add**, the **Apply and Close**.

Please note that if you wish for Knime to automatically look for updates of your extensions,
go to the **Automatic update** section and check the following:

![update](https://github.com/igrafx/KNIME-Mining-connector/blob/master/images/auto_update.png)



Go to the top right, you will find a small *i* icon . 

![info_icon](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/info_icon.png)

Click on it then scroll down to **Install Extensions**. Then, click on the **Install Extensions** button.

![install_extensions_button](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/install_extensions_button.png)

A **window** will pop up. In the search bar, you can search for **iGrafx**. 
Tick the box of the corresponding extension and click on **Finish**.
It may take some time to install.

![igx_extension](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/igx_extension.png)

Another window will pop up during the installation, asking if you trust the extension:

![Trust_window](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/trusted.png)

Tick the **Always trust all content** box. Then, on the next window that pops up, click on **Yes I accept the risk**.
You can now click on **Trust Selected**. Wait for the installation to finish.
Don't restart the platform just yet.

You can now restart Knime.

After reopening Knime, you can go to the **Node Repository** and type **iGrafx** in the search bar.
Then, click on **More Advanced Nodes**. The iGrafx nodes should be there.

![nodes_repo](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/node_repo.png)

**For macOS users** please install **XCode**. If it is not installed this will cause issues with the extension, and you will not be able to use the extension.
Please run ``sudo xcodebuild -license`` from within a Terminal window to review and agree to the **Xcode and Apple SDKs license**.

Congratulations! You can now refer to other sections for details on how to use the nodes.
If you are already familiar with the extension, you can skip to the [example](https://github.com/igrafx/KNIME-Mining-connector/blob/master/howto.md#the-igrafx-mining-extension-example)

If you are a developer wishing to contribute, please refer to [this](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/howto.md#using-the-igrafx-mining-knime-extension-as-a-developer) section instead.

## Using the iGrafx KNIME Mining Extension

There are several nodes in the iGrafx extension.

You will find:
- An **iGrafx Mining API Connection** Node
- An **iGrafx Mining Project Creation** Node
- An **iGrafx Mining Column Mapping Status** Node
- An **iGrafx Mining File Upload** Node

When executing a node, you will notice 3 circles underneath the nodes. If the circle is green,
it means that the node has successfully been executed. Contrariwise, if it is red, it has failed.
If it is yellow, it means it is configured.

Each node has flow variables which are produced when it is executed. To see them, go to the **flow variable** tab

![flow_variable](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/flow_variable.png)

In the next sections of this document, each node will be thoroughly explained.

## Using the iGrafx API Connection Node

The iGrafx Mining API Connection Node is the Node that will allow you to connect to the API and use it through the SDK.
Note that this node is **mandatory** as it allows you to establish a connection with the API.

To use this node, double-click on it. The following window will pop up.

![component_parameters](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/igx_connection_config.png)

You then have to fill in your **Workgroup ID** and **Secret Key**, **Authentication URL** and **API URL**. To get this information, open up the **Process Explorer 360**, and go to your workgroup settings. In the settings page, go to the **Public API** tab. There, you should see your workgroup's ID and secret key. These are the values that will be used by the SDK to log in to the iGrafx P360 Live Mining API.

![settings](https://github.com/igrafx/mining-python-sdk/blob/dev/imgs/settings.PNG)

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable |                        Meaning                         |         Description |
|:--------------|:------------------------------------------------------:|--------------------:|
| auth_url      |     The authentication URL of the iGrafx platform.     |  Authentication URL |
| api_url       |   The URL of the iGrafx API platform you are using.    |             API URL | 
| wg_key        | The Private Key of the workgroup you are working with. |       Workgroup Key |
| wg_id         |     The ID of the workgroup You are working with.      |        Workgroup ID |

The flow variables are automatically passed to other iGrafx nodes.

## Using the Project Creation Node

The iGrafx Mining Project Creation node is an optional node that allows you to create a project in a workgroup.

To use it, double-click on the node and enter the **name** you want to give your project and its **description**.

Note that the **description** is optional.

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable  |                        Meaning                         |        Description |
|:---------------|:------------------------------------------------------:|-------------------:|
| auth_url       |     The authentication URL of the iGrafx platform.     | Authentication URL |
| api_url        |   The URL of the iGrafx API platform you are using.    |            API URL | 
| wg_key         | The Private Key of the workgroup you are working with. |      Workgroup Key |
| wg_id          |     The ID of the workgroup You are working with.      |       Workgroup ID |
| new_project_id |          The ID of the newly created project.          |     New Project ID |

The new **project ID**  can then be used in the **Column Mapping Status** node for instance.
You can also use this new ID in the **File Upload** node if you wish to upload the file to a new project.

Please note that the flow variables of each node vary depending on the order they are in.

## Using the iGrafx Column Mapping Status Node

The Column Mapping Status node allows you to check if a column mapping exists.
A column mapping is a list of columns describing a document(.CSV, .XLSX, .XLS).

Further documentation on the column mapping and file structure can be found [here](https://github.com/igrafx/mining-python-sdk/blob/dev/howto.md#sending-data).

To use the node, you can either place the node after the **iGrafx Project Creation** node or the **iGrafx File Upload** node
to automatically get the project ID, or you can manually set it by double-clicking on the node.
Please note that if you set the project ID by double-clicking the node, it is prioritized over the project ID connection.

If the Column Mapping Status node is green, it means that a column mapping exists for this project.
If there are other nodes connected after this one, they will also pass as the column mapping exists.

If on the other hand, it is red, that means that the column mapping does not exist and has to be defined.
You can define a column mapping in the **File Upload** node.
If there are other nodes connected after this one, they will not be executed as the column mapping does not exist.

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable         |                            Meaning                             |           Description |
|:----------------------|:--------------------------------------------------------------:|----------------------:|
| auth_url              |         The authentication URL of the iGrafx platform.         |    Authentication URL |
| api_url               |       The URL of the iGrafx API platform you are using.        |               API URL | 
| wg_key                |     The Private Key of the workgroup you are working with.     |         Workgroup Key |
| wg_id                 |         The ID of the workgroup You are working with.          |          Workgroup ID |
| new_project_id        |              The ID of the newly created project.              |        New Project ID |
| column_mapping_exists | A boolean indicating whether ot not the column mapping exists. | Column Mapping Status |


If the `column_mapping_exists` flow variable is **True**, then the column mapping exists,
else it does not.

## Using the iGrafx File Upload Node

The iGrafx Mining File Upload Node is the node that will allow you to upload you file by simply entering a [column mapping](https://github.com/igrafx/mining-python-sdk/blob/dev/howto.md#sending-data), a Project ID and a chunk size value.
A column mapping is a list of columns describing a document(.CSV, .XLSX, .XLS).


**Please make sure that you are using ``UTF-8`` for the data you are planning to send, else it will result in an error.**

To use the node, double-click on it and , enter the column mapping of the file you wish to upload.
This has to be done in a JSON format. 
In this JSON, for each column, there is a column number (for instance *"col1"*).
It is then followed by the column's name, its index number and the column type.
For date columns, you have to set a format.

Beneath, you can find an example of what is expected.

```json
{       "col1": {"name": "case_id", "columnIndex": "0", "columnType":   "CASE_ID"},         
        "col2": {"name": "activity", "columnIndex": "1", "columnType": "TASK_NAME"},         
        "col3": {"name": "start_date", "columnIndex": "2", "columnType": "TIME", "format": "yyyy-MM-dd HH:mm:ss.SSSSSS"},         
        "col4": {"name": "end_date", "columnIndex": "3", "columnType": "TIME", "format": "yyyy-MM-dd HH:mm:ss.SSSSSS"}         }
```

You can also add `DIMENSION` and `METRIC` columns. For instance:
````json
{"col5": {"name": "Price", "columnIndex": "4", "columnType": "METRIC", "isCaseScope": false, 
        "groupedTasksAggregation": "SUM", "aggregation": "SUM", "unit": "unit"}}
````

More information about File Structures, Columns and column mappings can be found [here](https://github.com/igrafx/mining-python-sdk/blob/dev/howto.md#sending-data).

You must also input your **Project ID**. It can be found in the URL, when you are in the project. Or you can get it with the Project Creator node output.

![url-projectID](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/url-projectID.png)

Finally, the **number of rows in each sent chunk** must be set (chunk size). 
This means that for every file that is sent, it will be cut in the chunk size value, processed and sent to the platform.
Depending on the number of rows in your file it is important to set this value.
A good value to set it to is a 100 000, for instance.

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable                 |                              Meaning                               |                Description |
|:------------------------------|:------------------------------------------------------------------:|---------------------------:|
| auth_url                      |           The authentication URL of the iGrafx platform.           |         Authentication URL |
| api_url                       |         The URL of the iGrafx API platform you are using.          |                    API URL | 
| wg_key                        |       The Private Key of the workgroup you are working with.       |              Workgroup Key |
| wg_id                         |           The ID of the workgroup You are working with.            |               Workgroup ID |
| new_project_id                |                The ID of the newly created project.                |             New Project ID |
| column_mapping_exists         |   A boolean indicating whether ot not the column mapping exists.   |      Column Mapping Status |
| chunk_size                    |              The number of rows to process at a time               |   Number of Rows per Chunk |
| uploaded_files_info           | Information on the uploaded file(s) such as the ID, name or status | Uploaded files Information |

With the ``uploaded_files_info`` flow variable, you will be able to access information about the added file.
If several files are added then their information will also be returned in the list.

## The iGrafx Mining Project Data Node

The iGrafx Mining Project Data Node is a node that can be used to retrieve data about a specific project. 
This information is based on the node datasource. It is fetched, cleaned, filtered and returned.
It returns information such as the **case ID**, the **task ID**, corresponding **vertex IDs** and much more.

To use it, double-click on the **iGrafx Mining Project Data** node. Make sure there is an iGrafx API Connection node active first.
Enter the ID of the project for which you wish to retrieve data and execute it.

It will return two tables: the **Original Table** and a table containing the **Project's Data**.

This node takes a table as input and outputs 2 tables.

Here are the **flow variables** of this node:

| Flow variable         |                            Meaning                             |              Description |
|:----------------------|:--------------------------------------------------------------:|-------------------------:|
| auth_url              |         The authentication URL of the iGrafx platform.         |       Authentication URL |
| api_url               |       The URL of the iGrafx API platform you are using.        |                  API URL | 
| wg_key                |     The Private Key of the workgroup you are working with.     |            Workgroup Key |
| wg_id                 |         The ID of the workgroup You are working with.          |             Workgroup ID |
| new_project_id        |              The ID of the newly created project.              |           New Project ID |


While using this node, the flow variables will not be modified, it will simply take those of the latter node.
Only the **Project Data** table is added.

## The iGrafx Mining Completed Cases Node

The iGrafx Mining Completed Cases Node is a node that fetches completed cases for a specific project.

To use it, double-click on the **iGrafx Mining Completed Cases** node. Enter 
the **ID** of the project for which you wish to retrieve completed cases. 
Then, enter the page index for **pagination**.
You must also set a **limit** which represents the maximum number of items to return per page.
Optionally, you may enter a case ID in the **search query** to filter the results by case ID.

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable        |                        Meaning                         |              Description |
|:---------------------|:------------------------------------------------------:|-------------------------:|
| auth_url             |     The authentication URL of the iGrafx platform.     |       Authentication URL |
| api_url              |   The URL of the iGrafx API platform you are using.    |                  API URL | 
| wg_key               | The Private Key of the workgroup you are working with. |            Workgroup Key |
| wg_id                |     The ID of the workgroup You are working with.      |             Workgroup ID |
| new_project_id       |          The ID of the newly created project.          |           New Project ID |
| completed_cases_data |            The case IDs of completed cases             |          Completed Cases |


The complete cases data can be found in the flow variables. It is called `completed_cases_data`.

If you are met with the error: `There is no END CASE rule set or there is overfiltering being done`, it means that there is no **Business Rule** set for the project.
You can set one by going to the projects settings.

## The iGrafx Mining Project Variant Fetcher Node

The iGrafx Mining Project Variant Fetcher node is a node that allows users to retrieve information about project variants.
By specifying the Project ID, users can establish a connection with the iGrafx API and retrieve details about project variants,
such as names, IDs, number of occurrences and associated information.

To use it, double-click the **iGrafx Mining Project Variant Fetcher** node. 
Set the **project ID** of the project for which you want to get variant information.
You must also set the **page index** for pagination, 
the **limit** (representing the maximum number of items per page) and optionally, you can set a string in the search query. 
It represents the search query to filter the variants by name.

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable  |                        Meaning                         |        Description |
|:---------------|:------------------------------------------------------:|-------------------:|
| auth_url       |     The authentication URL of the iGrafx platform.     | Authentication URL |
| api_url        |   The URL of the iGrafx API platform you are using.    |            API URL | 
| wg_key         | The Private Key of the workgroup you are working with. |      Workgroup Key |
| wg_id          |     The ID of the workgroup You are working with.      |       Workgroup ID |
| new_project_id |          The ID of the newly created project.          |     New Project ID |
| variants_data  |             Information about the variants             |     Variants Cases |

When the node is successfully executed, for each variant, it will return its ID, name,and number of occurrences under the flow variable `variants_data`. 

## The iGrafx Mining Project Mapping Info Fetcher Node

**The iGrafx Mining Project Mapping Info Fetcher** node is a node that returns the **mapping information** of a project.
It returns the Name, Aggregation, and the database's column name, to name a few, for each dimension and metric.

To use it, double-click **The iGrafx Mining Project Mapping Info Fetcher** node and set the **project ID** of the project
for which you want to retrieve mapping information.

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable  |                        Meaning                         |        Description |
|:---------------|:------------------------------------------------------:|-------------------:|
| auth_url       |     The authentication URL of the iGrafx platform.     | Authentication URL |
| api_url        |   The URL of the iGrafx API platform you are using.    |            API URL | 
| wg_key         | The Private Key of the workgroup you are working with. |      Workgroup Key |
| wg_id          |     The ID of the workgroup You are working with.      |       Workgroup ID |
| new_project_id |          The ID of the newly created project.          |     New Project ID |
| mapping_infos  |      Mapping information for a specified project       |      Mapping Infos |

When the node is successfully executed, it will return the `mapping_infos` of the given project. 

## The iGrafx Mining Project Deletion Node

**The iGrafx Mining Project Deletion** Node is a node that allows you to delete a project by giving its ID.

To use it, double-click on it and enter the project ID of the project you wish to delete. 
After executing, if the node becomes green, that means the project has been deleted.

Flow variables are not modified with this node.

## The iGrafx Mining Column Mapping Fetcher Node

**The iGrafx Mining Column Mapping Fetcher** node is a node that returns the **Column Mapping** of a project.
It returns the information of each column such as the column's name, its index, the format of the date to name a few.

To use it, double-click **iGrafx Mining Column Mapping Fetcher** node and set the **project ID** of the project
for which you want to retrieve the column mapping.

This node takes a table as input and outputs a table.

Here are the **flow variables** of this node:

| Flow variable  |                        Meaning                         |        Description |
|:---------------|:------------------------------------------------------:|-------------------:|
| auth_url       |     The authentication URL of the iGrafx platform.     | Authentication URL |
| api_url        |   The URL of the iGrafx API platform you are using.    |            API URL | 
| wg_key         | The Private Key of the workgroup you are working with. |      Workgroup Key |
| wg_id          |     The ID of the workgroup You are working with.      |       Workgroup ID |
| new_project_id |          The ID of the newly created project.          |     New Project ID |
| column_mapping  |         Column Mapping for a specified project         |     Column Mapping |

When the node is successfully executed, it will return the `column_mapping` of the given project. 

Note that when retrieved, the column mapping can be reused to add files.
 

## Using the iGrafx SAP Data fetcher

The **iGrafx SAP Data Fetcher Node** allows users to retrieve data from an SAP API. It generates Selection and Description XML files, which are then used in a POST request to fetch the desired data. This data is subsequently cleaned, processed, and converted into a table for further use.

**Note**: The node currently handles only Order to Cash processes.

To use the node :

1. Double-click the **iGrafx SAP Data Fetcher** node. 
2. Specify the **Start Date** and **End Date**. The node will return Case IDs that fall within these dates. 
3. Enter the **SAP API URL**, **authorization username**, and **password** to connect to the SAP API. This enables the node to make the necessary requests to retrieve the data.

The node does not take any inputs. All necessary information is either generated within the node or provided by the user through parameters.

The node provides a single output, the **SAP Table**. This table can be connected to other iGrafx nodes for uploading to the iGrafx Mining Platform for further analysis.

No **flow variables** are returned with this node.

When the node is successfully executed it will return the `SAP Table`.

For assistance with using the SAP extension, please contact us at [support@igrafx.com](mailto:support@igrafx.com).


## The iGrafx Mining Project Files Info Fetcher Node

The iGrafx Mining Project Files Info Fetcher node is a node that allows users to retrieve metadata information for all files in a specified project.
By specifying the Project ID, Page Index, Limit and Sort Order users can establish a connection with the iGrafx API and retrieve details about project files,
such as names, statuses, creation dates, and ingestion statuses.

To use the **iGrafx Mining Project Files Info Fetcher** node, follow these steps:

1. Double-click the **iGrafx Mining Project Files Info Fetcher** node.
2. Set the **Project ID** of the project for which you want to get file information.
3. Set the **Page Index** for pagination.
4. Set the **Limit**, representing the maximum number of items to return per page.
5. Set the **Sort Order** (ASC or DESC) to determine the order of the results.

This node takes a table as input, allowing users to provide or feed data (CSV or other) into the node.
It then outputs a table, providing data (CSV or other) out of the node.

The following **flow variables** are available for this node:

| Flow variable     |                        Meaning                         |        Description |
|:------------------|:------------------------------------------------------:|-------------------:|
| auth_url          |     The authentication URL of the iGrafx platform.     | Authentication URL |
| api_url           |   The URL of the iGrafx API platform you are using.    |            API URL | 
| wg_key            | The Private Key of the workgroup you are working with. |      Workgroup Key |
| wg_id             |     The ID of the workgroup you are working with.      |       Workgroup ID |
| new_project_id    |          The ID of the project.                        |       Project ID   |
| project_files_info| Information about the files in the project             | Project Files Info |

When the node is successfully executed, it retrieves and returns metadata information for all files in the specified project under the flow variable `project_files_info`. This includes details such as:

- File ID
- File name
- File status
- Creation date
- Ingestion status

## The iGrafx Mining File Info Fetcher Node

The iGrafx Mining File Info Fetcher node is a node that allows users to retrieve metadata information for a specific file in a specified project.
By specifying the Project ID and File ID, users can establish a connection with the iGrafx API and retrieve details about a specific file,
such as its name, status, creation date, and ingestion status.

Note that neither the Project ID nor File ID *have* to be specified. They can be retrieved from other nodes,
for instance the **iGrafx Mining File Upload Node**, by simply connecting them.

To use the **iGrafx Mining File Info Fetcher** node, follow these steps:

1. Double-click the **iGrafx Mining File Info Fetcher** node.
2. Set the **Project ID** of the project for which you want to get file information.(Optional)
3. Set the **File ID** of the file for which you want to get information.(Optional)

This node takes a table as input, allowing users to provide or feed data (CSV or other) into the node.
It then outputs 2 tables. One providing the original data (CSV or other) out of the node.
And the other, named **File Info Table**, providing a table containing the file IDs and their respective information.
These tables can then be reused for further processing.

The following **flow variables** are available for this node:

| Flow variable               |                               Meaning                               |                Description |
|:----------------------------|:-------------------------------------------------------------------:|---------------------------:|
| auth_url                    |           The authentication URL of the iGrafx platform.            |         Authentication URL |
| api_url                     |          The URL of the iGrafx API platform you are using.          |                    API URL | 
| wg_key                      |       The Private Key of the workgroup you are working with.        |              Workgroup Key |
| wg_id                       |            The ID of the workgroup you are working with.            |               Workgroup ID |
| new_project_id              |                       The ID of the project.                        |                 Project ID |
| uploaded_files_info         | Information on the uploaded file(s) such as the ID, name or status  | Uploaded files Information |

When the node is successfully executed, it retrieves and returns metadata information for the specified file in the project in the Table ``File Info Table``. 
This includes details such as:

- File ID
- File name
- File status
- Creation date
- Ingestion status
- And more...

## The iGrafx Mining Extension Example

Go to Knime and import the workflow called ``igrafx_extension_example.knwf``.

When the workflow is imported, you should see all iGrafx Extension nodes.

![igrafx_workflow](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/igx_wf.png)

To start using them, look for a **File Reader Node**. Please note that you may use other nodes as long as the output is a table.
Here we use the File Reader Node as an Example.
With this node, you will be able to select the file you wish to upload to the iGrafx platform.
You can try it with the [100_fake_cases.csv](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/igrafx_extension/100_fake_cases.csv) file.

You can then connect it to any node you wish to try, fill in the information by double-clicking the node and execute the nodes.

Set your credentials on the iGrafx Mining API Connection node.

Note that the column mapping for the **100_fake_cases.csv** file is as follows:
````json
{
   "col1":{
      "name":"case_id",
      "columnIndex":"0",
      "columnType":"CASE_ID"
   },
   "col2":{
      "name":"activity",
      "columnIndex":"1",
      "columnType":"TASK_NAME"
   },
   "col3":{
      "name":"start_date",
      "columnIndex":"2",
      "columnType":"TIME",
      "format":"yyyy-MM-dd HH:mm:ss.SSSSSS"
   },
   "col4":{
      "name":"end_date",
      "columnIndex":"3",
      "columnType":"TIME",
      "format":"yyyy-MM-dd HH:mm:ss.SSSSSS"
   }
}
````
You can now execute all the nodes.

Once all connected nodes are green, the execution is done.


## Using the iGrafx Mining Knime Extension as a developer
If you are a developer and wish to contribute to the project, please follow the steps below, as they are relatively different from the ones a client would follow.


## Requirements

Note that the iGrafx P360 Live Mining SDK is also required and that its installation is explained further in the document.

### Download Knime

This extension works with Knime. Please Download Knime to be able to use it.
You can find the download link [here](https://www.knime.com/downloads).

### Download Anaconda

To be able to use Python in Knime, Anaconda must be installed, otherwise Python nodes will not be accessible, and it will be impossible to use the iGrafx Knime Mining Connector.

You can download Anaconda [here](https://www.anaconda.com/download).

## Getting started

After having downloaded Knime and Anaconda, open Knime. In the top right, you will find a small *i* icon. 

![info_icon](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/info_icon.png)

Click on it then scroll down to **Install Extensions**. Then, click on the **Install Extensions** button.

![install_extensions_button](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/install_extensions_button.png)


A **window** will pop up. In the search bar, you can search for **Python integration**. Tick the following boxes, corresponding to the necessary extensions and click on **Finish**.

![python_integration_extensions](https://github.com/igrafx/KNIME-Mining-connector/blob/master/images/python__ext_install.png)

When that is done, configure the KNIME Python Integration. To do so, click on the **settings** icon in the top right of the window.

![settings_icon](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/settings_icon.png)

When clicking on it, you will see a section called **Conda**. 
Go to that section and browse for your **Conda Installation Directory**. 
When the correct path is entered, the conda version will appear underneath. The path may look like this: `C:\Users\Your Name\AppData\Local\anaconda3`.
**Please note that the path to your Anaconda3 may differ depending on how and where you installed it.** 

![conda_path](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/conda_path.png)

## Using the iGrafx Knime Extension locally
### Cloning the iGrafx KNIME Mining Extension
You are going to need the ``git`` command for this section. 
If you do not have git, please follow the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).


Once everything is Python is integrated in Knime, the first thing to do is to clone the repository.
To do so create a new folder. Open a terminal and type the following command:
```shell
cd C:\Users\Your\Path\to\New\folder 
```
After having executed the command, do the following command.
```shell
git clone https://github.com/igrafx/KNIME-Mining-connector.git
```

Doing this will clone the iGrafx KNIME Mining Connector GitHub repository to the new folder you have created. This simply means that the project was copied from GitHub to your new folder. 

### Checking the Project Structure

In the ``igrafx_extension`` folder, you should see the following file structure:

.

├── igrafx_knime_extension

│   ├── icons

│   │   └── icon.png

│   │   └── igx_logo.png

│   │── knime.yml

│   │── LICENSE.TXT

│   └── igrafx_knime_extension.py

├── config.yml

├── my_conda_env.yml

├── iGrafx_Extension_Example.knwf

└── README.md

Please make sure the structure you have matches the one above.

The ``igrafx_knime_extension`` will be your new extension. In it, you will find several elements:

 - The ``icons`` folder contain the node icons.
 - The ``knime.yml``, which contains important metadata about your extension, such as the name, the version, the licence, etc...
 - The ``igrafx_knime_extension.py``, which contains Python definitions of the nodes of the extension.
 - The ``config.yml``, just outside the folder, which contains the information that binds the extension and the corresponding conda/Python environment with KNIME Analytics Platform.

### Creating a new Conda Python environment
We need to **create an environment** containing the [knime-python-base meta package](https://anaconda.org/knime/knime-python-base)
and the node development API [knime-extension](https://anaconda.org/knime/knime-extension).

To do this, open **Anaconda prompt** and copy the following command:
```shell
conda create -n <Your Environment Name> python=3.10.11 knime-python-base=5.2 knime-extension=5.2 -c knime -c conda-forge
```
Python 3.10 is the minimum requirement to be able to use the iGrafx SDK.

If you would like to install the packages into an environment that already exists you can run the following command from within that environment:
````shell
conda install knime-python-base=5.2 knime-extension=5.2 -c knime -c conda-forge
````
Please note that you must append both the ``knime`` and ``conda-forge`` channels to the commands to install the ``mandatory packages``.
To install ``additional packages``, for your specific use case, it is better to use the ``conda-forge`` channel.
````shell
conda install -c conda-forge <additional_pkg_name>
````

### Adding the iGrafx SDK package to the Conda environment
We must now install the SDK package so that we are able to communicate with the platform.
Please note that the SDK version must match the platform version to ensure that all functionalities will work.

To do so, open **Anaconda prompt**.

When the terminal is opened, enter the following command:
```bash
conda activate <Your Environment Name>
```
Doing this will activate the environment you created above, and you will then be able to install the package.
Finally, you can install **the latest** the iGrafx SDK with the following command:
```bash
pip install igrafx-mining-sdk
```
This command will install the SDK and all the required dependencies. 
To avoid issues and conflicts please make sure to download the latest version of the SDK.

If you need to install a specific version of the SDK, use the following command:
  ```shell
  pip install igrafx-mining-sdk==<Your Version>
  ```
For instance:
  ```shell
  pip install igrafx-mining-sdk==2.31.4
  ```
You can go to the [PyPi page](https://pypi.org/project/igrafx-mining-sdk/2.25.0/) of the SDK to check the different versions. You can also to the SDK's [GitHub page](https://github.com/igrafx/mining-python-sdk) if you need additional information about the SDK.

### Setting up the Conda Environment in Knime
This section is to set up the Conda environment in Knime.

Open Knime and go to the `Settings`. Go to the `Python` tab. Make sure you are in the `Python` tab and not the ``Python (Legacy)`` tab.
Indeed, Python 2 is not used here, so it isn't necessary.

Under `Python environment configuration`, check `Conda`.

![environment configuration](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/python_image_6.png)

Under `Python 3`, select the Knime environment you created above.

It is possible that `Pyarrow` and `Numpy` packages are in conflict. 
That is because the **iGrafx SDK Package** was installed with **pip**.
If so, to fix this, they must be reinstalled with conda.

![conflicts](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/conflicts.png)

Note that these conflicts can differ, and you should follow the following instructions no matter the package.

First, check the version of both packages with the following commands. If you are on MACOS or Linux, replace `findstr` with `grep`:
````shell
conda list | findstr pyarrow
````

````shell
conda list | findstr numpy
````

They will return you something like this, respectively:
````shell
pyarrow                   9.0.0           py39hca4e8af_45_cpu    conda-forge
````

````shell
numpy                     1.21.6           py39h6331f09_0    conda-forge
````

The problematic packages will not have `conda-forge` written, but they will have something else.

Then reinstall the packages with the following commands using the versions that were found with the commands above:
````shell
conda install -c conda-forge numpy=<Version that was found>
````
````shell
conda install -c conda-forge pyarrow=<Version that was found>
````
For instance: 
````shell
conda install -c conda-forge numpy=1.21.6 
````
````shell
conda install -c conda-forge pyarrow=9.0.0
````
If there are other packages that are problematic, **use the same commands but change the name of the package**.

Afterward, restart Knime. Go to the **Python Tab** in **Settings**.
Reselect the correct environment. If the Python Version is shown, the environment has been set successfully!

### Editing the necessary files
Some paths in certain files need modifying so that Knime can detect the Python extension locally.

First, open the `config.yml` file. it looks like this:
````yaml
org.igx.igrafx_extension: # {group_id}.{name} from the knime.yml
  src: C:/Users/Path/to/igrafx_extension/igrafx_knime_extension # Path to folder containing the extension files
  conda_env_path:  C:/Users/Path/to/anaconda/python/environment # Path to the Python environment to use
  debug_mode: false # Optional line, if set to true, it will always use the latest changes of execute/configure, when that method is used within the KNIME Analytics Platform
````

Replace the `src` field as to specify the path to the `igrafx_knime_extension` folder.
For instance, it could look like ``C:/Users/iGrafx/igrafx_extension/igrafx_knime_extension``.

**Please double-check the paths as the most common errors stem from incorrect paths.**

Similarly, the ``conda_env_path`` field should specify the path to the conda/Python environment created earlier.
To get this path, run the following command in your Terminal/Anaconda Prompt,
and copy the path displayed next to the appropriate environment.
````shell
conda env list
````
The ``debug_mode`` is an optional field, which, if set to ``true``, 
will tell **KNIME Analytics Platform** to use the latest changes in the Python node code.

Furthermore, we need to let Knime know where the ``config.yml`` is in order to allow it to use our extension
and its Python environment. 
To do this, you need to edit the ``knime.ini`` of your Knime Platform installation,
which is located at ``<path-to-Knime>/knime.ini``.

Append the following line to the end, 
and modify it to have the correct path to the ``config.yml``:
````shell
-Dknime.python.extension.config=<path/to/your/config.yml>
````

**Please note that the forward slash ``/`` has to be used on all OS, including Windows.**

**On macOS**,  to locate ``knime.ini``, open **Finder** and navigate to your
installed Applications. Next, **right-click** the KNIME application, select **Show
Package Contents** in the menu, and navigate to **Contents → Eclipse**.

The ``knime.ini`` file can be edited with any plaintext editor, such as **Notepad** (Windows),
**TextEdit** (macOS) or **gedit** (Linux).


You can now relaunch Knime. If you type ``iGrafx`` in the node Repository, you should find the iGrafx nodes. 


Congratulations! The extension has been installed locally. You can now use the iGrafx nodes.



## Further Documentation

In this section, documentation can be found for further reading.

Support is available at the following address: [support@igrafx.com](mailto:support@igrafx.com)


* [iGrafx Help](https://www.help.logpickr.com/en/welcome/)
* [iGrafx SDK](https://github.com/igrafx/mining-python-sdk)
* [Knime Python Extension Documentation](https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html#introduction)