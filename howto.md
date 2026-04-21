# How to use the extension

This document encompasses the installation and basic uses of the **iGrafx KNIME Mining Extension**.

The **iGrafx KNIME Mining Extension** is an open-source application seamlessly integrated with Knime to effortlessly transmit data to the iGrafx Mining Platform.

It is powered by the [iGrafx P360 Live Mining SDK](https://github.com/igrafx/mining-python-sdk) and rooted in Python.
 
This connector simplifies the data transfer process, eliminating complexity and enhancing your workflow.

To maximize the benefits of this extension, ensure you have an active iGrafx account. If you don't have one, please contact us to set up your account.

**Please make sure you have the 5.5 version of Knime as the latest release works with that version.**


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
20. [Configuring KNIME for Local Development](#configuring-knime-for-local-development)
21. [Testing the Extension Locally](#testing-the-extension-locally)
22. [Updating Dependencies](#updating-dependencies)
23. [Further Documentation](#further-documentation)

## Installing the iGrafx Extension

There are two ways to install the **iGrafx Extension** in KNIME. Choose the method that works best for you.

> **Important for developers:** If you previously configured KNIME for local development (with the `-Dknime.python.extension.config=` line in `knime.ini`), you must comment out or remove that line and restart KNIME before installing from a release. Otherwise KNIME will load the extension twice, causing conflicts or duplicate nodes.

### Method 1: Install from a downloaded release (Recommended)

This method uses a release archive downloaded from GitHub.

1. Go to the [Releases page](https://github.com/igrafx/KNIME-Mining-connector/releases) on GitHub.
2. Under the latest release, download the **knime-extension-release.zip** file.
3. Open KNIME. Click on the **settings** icon in the top right of the window.

   ![settings_icon](/icons/settings_icon.png)

4. Click on the **arrow** next to the **Install/Update** section, then go to **Available Software Sites**.
5. Click the **Add** button. In the window that pops up, click **Archive...** and browse to the `knime-extension-release.zip` file you downloaded. Give it a name (e.g., "iGrafx Extension") and click **OK**.
6. Click **Apply and Close**.
7. Go to the top right of the KNIME window and click the small *i* icon.

   ![info_icon](/icons/info_icon.png)

8. Scroll down to **Install Extensions** and click the **Install Extensions** button.

   ![install_extensions_button](/icons/install_extensions_button.png)

9. In the search bar, type **iGrafx**. Tick the box for the iGrafx extension and click **Finish**.

   ![igx_extension](/icons/igx_extension.png)

10. A trust dialog will appear. Tick **Always trust all content**, then click **Yes I accept the risk**, and finally **Trust Selected**.
11. Wait for the installation to finish, then restart KNIME.

### Method 2: Install from the update site URL

This method uses a URL that KNIME checks for updates automatically. The URL always points to the latest release — KNIME will detect new versions and prompt you to update.

1. Open KNIME. Click on the **settings** icon in the top right of the window.

   ![settings_icon](/icons/settings_icon.png)

2. Click on the **arrow** next to the **Install/Update** section, then go to **Available Software Sites**.
3. Click the **Add** button. In the window that pops up, enter the following:
   - **Name:** iGrafx Extension
   - **Location:** `https://igrafx.github.io/KNIME-Mining-connector/`
4. Click **Add**, then **Apply and Close**.
5. Go to **Help > Install New Software**.
6. In the **Work with** dropdown, select **iGrafx Extension** (the site you just added).
7. The iGrafx extension should appear in the list — tick the checkbox for it.
8. Click **Next**, then **Finish**.
9. A trust dialog will appear. Tick **Always trust all content**, click **Yes I accept the risk**, then **Trust Selected**.
10. Wait for the installation to finish, then restart KNIME.

> **Note:** If you wish for KNIME to automatically check for updates, go to **File > Preferences > Install/Update > Automatic Update** and enable automatic update checking. KNIME will notify you whenever a new release is published.

> **Important:** The URL always serves the latest release only. If you need a specific older version, use Method 1 (download the zip from the GitHub Releases page).

### After installation

After restarting KNIME:

1. **Verify the extension is installed:** Go to **Help > About KNIME Analytics Platform > Installation Details > Installed Software**. The iGrafx extension should be listed there. If it is not, the installation did not complete successfully — try reinstalling.
2. **Verify the nodes are available:** Go to the **Node Repository** panel and type **iGrafx** in the search bar. The iGrafx nodes should appear. If they don't, click on **More Advanced Nodes** to expand the results.

![nodes_repo](/icons/node_repo.png)

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

![flow_variable](/icons/flow_variable.png)

In the next sections of this document, each node will be thoroughly explained.

## Using the iGrafx API Connection Node

The iGrafx Mining API Connection Node is the Node that will allow you to connect to the API and use it through the SDK.
Note that this node is **mandatory** as it allows you to establish a connection with the API.

To use this node, double-click on it. The following window will pop up.

![component_parameters](/icons/igx_connection_config.png)

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

![url-projectID](/icons/url-projectID.png)

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

![igrafx_workflow](/icons/igx_wf.png)

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

If you are a developer and wish to contribute to the project, please follow the steps below. The development workflow uses [Pixi](https://pixi.sh) for environment management, which handles all Python dependencies including the iGrafx SDK automatically.

## Requirements

Before getting started, make sure you have the following installed:

- **KNIME Analytics Platform 5.5+** — [Download here](https://www.knime.com/downloads)
- **Pixi** — the package manager used for this project. [Install Pixi](https://pixi.sh)
- **Git** — [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Additionally, you must install the **KNIME Python Extension Development (Labs)** plugin in KNIME:

1. Open KNIME and go to **Help > Install New Software**
2. In the "Work with" dropdown, select **KNIME Analytics Platform 5.5 Update Site**
3. Search for **"Python Extension Development"**
4. Install **KNIME Python Extension Development (Labs)**
5. Restart KNIME

## Getting Started

### Cloning the Repository

Open a terminal and clone the repository:

```shell
git clone https://github.com/igrafx/KNIME-Mining-connector.git
cd KNIME-Mining-connector
```

### Installing the Environment

Run the following command to create the Python environment with all dependencies (including the iGrafx SDK, knime-extension, and knime-python-base):

```shell
pixi install
```

This creates the environment at `.pixi/envs/default`. All dependencies are defined in `pixi.toml` and locked in `pixi.lock`.

### Project Structure

After cloning, the repository has the following structure:

```
.
├── knime.yml                     # Extension metadata (name, version, module path)
├── pixi.toml                     # Python environment and dependency definitions
├── pixi.lock                     # Locked dependency versions
├── config.yml                    # Binds the extension to KNIME (local dev only)
├── LICENSE.TXT
├── README.md
├── howto.md
├── src/
│   └── igrafx_knime_extension.py # Python definitions of all extension nodes
├── icons/                        # Node icons
├── .github/workflows/            # CI/CD workflows (release, linting)
└── .pixi/envs/default/           # Python environment (created by pixi install)
```

Key files:
- **`knime.yml`** — extension metadata (name, group ID, version, module path)
- **`pixi.toml`** — all conda and PyPI dependencies, including the iGrafx SDK version
- **`config.yml`** — maps the extension to its Python environment for local KNIME development
- **`src/igrafx_knime_extension.py`** — the Python module containing all node definitions

## Configuring KNIME for Local Development

### Editing config.yml

Open `config.yml` and update the paths to match your local setup:

```yaml
org.igx.igrafx_extension:
  src: C:/Users/<YourName>/Path/to/KNIME-Mining-connector
  conda_env_path: C:/Users/<YourName>/Path/to/KNIME-Mining-connector/.pixi/envs/default
  debug_mode: true
  python_path:
    - C:/Users/<YourName>/Path/to/KNIME-Mining-connector/src
```

- **`src`** — path to the repository root (where `knime.yml` is located)
- **`conda_env_path`** — path to the pixi environment at `.pixi/envs/default`
- **`debug_mode`** — set to `true` during development so that changes to `execute` and `configure` methods are reflected immediately without restarting KNIME
- **`python_path`** — path to the `src` directory containing the extension module

**Please use forward slashes `/` in all paths, including on Windows.**

### Registering with KNIME

You need to tell KNIME where your `config.yml` is located. There are two methods:

**Method 1 (Automated):**

```shell
pixi run register-debug-in-knime
```

This locates your KNIME installation, backs up `knime.ini`, and appends the config path automatically.

**Method 2 (Manual):**

Edit the `knime.ini` file in your KNIME installation directory and append the following line at the end:

```
-Dknime.python.extension.config=C:/Users/<YourName>/Path/to/KNIME-Mining-connector/config.yml
```

The `knime.ini` file is located at:
- **Windows/Linux:** `<knime-installation-directory>/knime.ini`
- **macOS:** right-click the KNIME application in Finder, select **Show Package Contents**, then navigate to **Contents/Eclipse/knime.ini**

The file can be edited with any plain text editor (Notepad, TextEdit, gedit, etc.).

## Testing the Extension Locally

1. **Restart KNIME** after configuring `config.yml` and `knime.ini`.
2. In the **Node Repository** panel on the left, search for **"iGrafx"**. The iGrafx nodes should appear.
3. Drag nodes into a workflow to test them.

### Debug Mode

With `debug_mode: true` in `config.yml`:
- Changes to `execute` and `configure` methods in `igrafx_knime_extension.py` are reflected **immediately** when re-executing a node — no KNIME restart needed.
- Other changes (adding new nodes, modifying node descriptions) **require a KNIME restart**.

### Checking Logs

If something isn't working, check the KNIME log for errors:
- Go to **View > Open KNIME Log**
- Look for Python-related errors or stack traces

### Common Issues

| Problem | Cause | Fix |
|---------|-------|-----|
| "Missing node extensions" dialog on workflow load | **KNIME Python Extension Development (Labs)** plugin not installed | Install it via **Help > Install New Software** |
| Nodes don't appear in Node Repository | `config.yml` paths are incorrect or `knime.ini` is missing the config line | Double-check all paths use forward slashes and point to the correct directories |
| Python import errors in KNIME log | Environment not set up correctly | Run `pixi install` and verify with `pixi run python -c "import igrafx_mining_sdk"` |
| Project path added as a "Software Site" error | Repository path was added under **Install/Update > Available Software Sites** instead of via `knime.ini` | Remove it from Available Software Sites; use the `knime.ini` config line instead |

## Updating Dependencies

The project includes a Claude Code skill to automate dependency updates. It checks the latest SDK version on PyPI, verifies compatibility with the KNIME environment, and validates the changes.

To use it:

1. Open a terminal in the repository root and launch Claude Code:
   ```shell
   claude
   ```
2. Run the skill:
   ```
   /update-dependencies
   ```

To update dependencies manually:

1. Check the latest SDK version on [PyPI](https://pypi.org/project/igrafx-mining-sdk/).
2. Update the version constraints in `pixi.toml` (both `[pypi-dependencies]` and `[dependencies]` sections).
3. Regenerate the lockfile and install:
   ```shell
   pixi lock
   pixi install
   ```
4. Verify the SDK loads correctly:
   ```shell
   pixi run python -c "import igrafx_mining_sdk; print(igrafx_mining_sdk.__version__)"
   ```

> **Important:** `knime-python-base` (a conda package on the KNIME channel) hard-pins transitive dependencies like `pandas` to exact versions. Any SDK update must have dependency ranges that accept these pinned versions. If the latest SDK version is incompatible, the SDK must relax its constraints before it can be used here.

## Further Documentation

In this section, documentation can be found for further reading.

Support is available at the following address: [support@igrafx.com](mailto:support@igrafx.com)


* [iGrafx Help](https://www.help.logpickr.com/en/welcome/)
* [iGrafx SDK](https://github.com/igrafx/mining-python-sdk)
* [Knime Python Extension Documentation](https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html#introduction)