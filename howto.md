# How to use the extension

This document encompasses the installation and basic uses of the **iGrafx KNIME Mining Connector**.

The **iGrafx KNIME Mining Extension** is an open-source application seamlessly integrated with Knime to effortlessly transmit data to the iGrafx Mining Platform.

It is powered by the [iGrafx P360 Live Mining SDK](https://github.com/igrafx/mining-python-sdk) and rooted in Python.
 
This connector simplifies the data transfer process, eliminating complexity and enhancing your workflow.

To maximize the benefits of this extension, ensure you have an active iGrafx account. If you don't have one, please contact us to set up your account.

***

## Table of Contents

1. [Requirements](#requirements)
2. [Getting Started](#getting-started)
3. [Adding the iGrafx SDK package](#adding-the-igrafx-sdk-package)
4. [Cloning the iGrafx KNIME Mining Connector](#cloning-the-igrafx-knime-mining-connector)
5. [Using the iGrafx KNIME Mining Connector](#using-the-igrafx-knime-mining-connector)

## Requirements

Note that the iGrafx P360 Live Mining SDK is also required and that its installation is explained further in the document.

### Download Knime

This component works with Knime. Please Download Knime to be able to use it.
You can find the download link [here](https://www.knime.com/downloads).

### Download Anaconda

To be able to use Python in Knime, Anaconda must be installed, otherwise Python nodes will not be accessible and it will be impossible to use the iGrafx Knime Mining Connector.

You can download Anaconda [here](https://www.anaconda.com/download).

## Getting started

After having downloaded Knime and Anaconda, open Knime. In the top right, you will find a small *i* icon . 

![info_icon](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/info_icon.png)

Click on it then scroll down to **Install Extensions**. Then, click on the **Install Extensions** button.

![install_extensions_button](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/install_extensions_button.png)


A **window** will pop up. In the search bar, you can search for **Python integration**. Tick the box of the corresponding extension and click on **Finish**.

![python_integration](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/python_integration.png)

When that is done, configure the KNIME Python Integration. To do so, click on the **settings** icon in the top right of the window.

![settings_icon](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/settings_icon.png)

When clicking on it you will see a section called **Conda**. Go to that section and browse for your **Conda Installation Directory**. When the correct path is entered, the conda version will appear underneath. The path may look like this: `C:\Users\Your Name\AppData\Local\anaconda3`.

![conda_path](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/conda_path.png)

Afterwards, go to the **Python** section. Under **Python environment configuration** select **Conda**.

We must create a new environment. To do so, under *Python 3 (Default)*, select the **New Environment** button. It will automatically be named `py3_knime`. You can now click on the **Create new Environment** button. It may take some time as it is installing all necessary dependencies that are required.

![python_image_6](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/python_image_6.png)

## Adding the iGrafx SDK package
We must now install the SDK package so that we are able to communicate with the platform.
Please note that the SDK version must match the platform version to ensure that all functionalities will work.

To do so, press the windows button on your keyboard and type in **Anaconda prompt**.

When the terminal is opened, enter the following command:
```bash
conda activate py3_knime
```
Doing this will activate the environment you created above and you will then be able to install the package.
Finally, you can install **the latest** the iGrafx SDK with the following command:
```bash
pip install igrafx-mining-sdk
```
This command will install the SDK and all the required dependencies.

If you need to install a specific version of the SDK, use the following command:
  ```shell
  pip install igrafx-mining-sdk==<Your Version>
  ```
For instance:
  ```shell
  pip install igrafx-mining-sdk==2.25.0
  ```
You can go to the [PyPi page](https://pypi.org/project/igrafx-mining-sdk/2.25.0/) of the SDK to check the different versions. You can also to the SDk's [Github page](https://github.com/igrafx/mining-python-sdk) if you need additional information about the SDK.



## Cloning the iGrafx KNIME Mining Connector

Once everything is setup, the first thing to do is to clone the repository.
To do so create a new folder. Open a terminal and type the following command:
```shell
cd C:\Users\Your\Path\to\New\folder 
```
After having executed the command, do the following command.
```shell
git clone https://github.com/igrafx/KNIME-Mining-connector.git
```

Doing this will clone the iGrafx KNIME Mining Connector Github repository to the new folder you have created. This simply means that the project was copied from Github to your new folder. 

Afterwards, you can open the iGrafx KNIME Mining Connector in Knime from the **Local Space** and use it. 

## Using the iGrafx KNIME Mining Connector

When first opening the project in Knime, you will notice several nodes and components.
There is:
- A **File Reader** node
- A **Chunk Loop Start**
- An **API Connection** component
- A **Project Creator** component
- A **Column Mapping Status** component
- A **File Upload** component
- A **Loop End** node

When executing a node, you will notice a 3 circles underneath the nodes. If the circle is green,
it means that the node has successfully been executed. Contrariwise, if it is red, it has failed.


In the next sections of this document, end node will be thoroughly explained.

## Using the File Reader node

The **File Reader** node provides the functionality to browse for a specific data file path and read its contents. While the node automatically detects the file format, it's recommended to double-check for accuracy.

To utilize this node, simply double-click on it. In the input location section, click the browse button to navigate and select the desired data file for reading.

| Node Input      | Node Output |   Symbol    |
|:----------------|:-----------:|:-----------:|
| No input        | File Table  | Black Arrow | 

Above, you can see a table of the inputs and outputs of this node.
As you can see, it only outputs the table that you gave.

Furthermore, by **hovering on the triangle of the arrow output**, you can see information about the table.

## Using the Chunk Loop Start

The **Chunk Loop Start** node is used to split a large dataset into smaller, manageable chunks or segments for processing.
This node is particularly useful when dealing with large volumes of data that might not fit into memory all at once or when performing operations that need to be executed in smaller batches.

The **Chunk Loop Start** node generates chunks or segments of data based on a defined size or number of rows specified by the user. 
It creates a loop that iterates over these chunks, allowing you to perform operations within the loop. 

To use this node, double click on it, then set the number of **rows per chunk** that you desire.

The output of the **Chunk Loop Start** node includes these segmented chunks of the input data, which can then be processed within the loop using subsequent nodes. Additionally, after processing each chunk, the loop continues until all the data has been processed, providing a way to efficiently handle large datasets in a step-by-step manner.

| Node Input |  Node Output  |   Symbol    |
|:-----------|:-------------:|:-----------:|
| File Table | Chunked Input | Black Arrow | 

If you hover over the triangle of the input and the output, you will notice the number of columns may have changed depending on how you set the node.

## Using the API Connection Component

The API Connection component is the component that will allow you to connect to the API and use it through the SDK.
Note that this node is **mandatory** as it allows you to establish a connection with the API.

To use this component, double click on it. The following window will pop up.

![component_parameters](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/component_parameters.png)

You then have to fill in your **Workgroup ID** and **Secret Key**, **Authentication URL** and **API URL**. To get this information, open up the **Process Explorer 360**, and go to your workgroup settings. In the settings page, go to the **Public API** tab. There, you should see your workgroup's ID and secret key. These are the values that will be used by the SDK to log in to the iGrafx P360 Live Mining API.

![settings](https://github.com/igrafx/mining-python-sdk/blob/dev/imgs/settings.PNG)

Here are the inputs and outputs table for this component:

| Node Input    |   Node Output    |   Symbol    |
|:--------------|:----------------:|:-----------:|
| Chunked Table |  Chunked Table   | Black Arrow | 
| ------------- | Workgroup Object | Blue Square | 

The Workgroup Object output plays a crucial role as it provides essential information for other nodes to establish connections with the API.
You can hover on the blue square to see the object.

## Using the Project Creator Component

The Project Creator component is an optional component that allows you to create a project in a workgroup.

To use it, double click on the node and enter the **name** you want to give your project and its **description**.

Here are the inputs and outputs table for this component:

| Node Input       |      Node Output      |   Symbol    |
|:-----------------|:---------------------:|:-----------:|
| Chunked Table    |     Chunked Table     | Black Arrow | 
| Workgroup Object |   Workgroup Object    | Blue Square | 
 | ---------------  | New Project ID String | Blue Square | 

The new **project ID** output can then be used in the **Column Mapping Status** node for instance.
You can also use this new ID in the **File Upload** node if you wish to upload the file to a new project.


## Using the Column Mapping Status Component

The Column Mapping Status component allows you to check if a column mapping exists.

To use it, you can either place the node after the **Project Creator** component or the **File Upload** component
to automatically get the project ID, or you can manually set it by double clicking on the node.
Please note that if you set the project ID by double clicking the node, it is prioritized over the project ID connection.

If the Column Mapping Status component is green, it means that a column mapping exists for this project.
If there are other nodes connected after this one, they will also pass as the column mapping exists.

If on the other hand, it is red, that means that the column mapping does not exist and has to be defined.
You can define a column mapping in the **File Upload** component.
If there are other nodes connected after this one, they will not be executed as the column mapping does not exist.

Here are the inputs and outputs table for this component:

| Node Input        |      Node Output      |   Symbol    |
|:------------------|:---------------------:|:-----------:|
| Chunked Table     |     Chunked Table     | Black Arrow | 
| Workgroup Object  |   Workgroup Object    | Blue Square | 
| Project ID String |   Project ID String   | Blue Square | 
| ----------------- | Column Mapping Status | Blue Square |

If you hover over the blue square of the Column Mapping Status output, uyou will see a boolean value. If it is written **True**, then the column mapping exists,
else it does not.

## Using the File Upload Component

The File Upload Component is the component that will allow you to upload you file by simply entering a column mapping and a Project ID.

To use it, double click on it and enter the  column mapping of the file you wish to upload.
This has to be done in a JSON format. 
In this JSON, for each column, there is a column number (for instance *"col1"*).
It is then followed by the column's name, its index number and the column type.
For date columns, you have to set a format. 

Beneath, you can find an example of what is expected.

```JSON
{       "col1": {"name": "case_id", "columnIndex": "0", "columnType":   "CASE_ID"},         
        "col2": {"name": "activity", "columnIndex": "1", "columnType": "TASK_NAME"},         
        "col3": {"name": "start_date", "columnIndex": "2", "columnType": "TIME", "format": "yyyy-MM-dd HH:mm:ss.SSSSSS"},         
        "col4": {"name": "end_date", "columnIndex": "3", "columnType": "TIME", "format": "yyyy-MM-dd HH:mm:ss.SSSSSS"}         }
```

More information about Columns and column mappings can be found [here](https://github.com/igrafx/mining-python-sdk/wiki/5.-Sending-Data#column-mapping).

Finally, you must input your **Project ID**. It can be found in the URL, when you are in the project. Or you can get it with the Project Creator node output.

![url-projectID](https://github.com/igrafx/KNIME-Mining-connector/blob/main/images/url-projectID.png)

Here are the inputs and outputs table for this component:

| Node Input        |      Node Output      |   Symbol    |
|:------------------|:---------------------:|:-----------:|
| Chunked Table     |     Chunked Table     | Black Arrow | 
| Workgroup Object  |   Workgroup Object    | Blue Square | 
| ----------------- |   Project ID String   | Blue Square |

## Using the Loop End node

The **Loop End** node marks the end of a loop that was initiated by a loop start node (**Chunk Loop Start**). Its primary function is to finalize the loop execution and gather the results or data generated within the loop's iterations.

Once the loop starts, subsequent nodes within the loop perform operations iteratively. The **Loop End** node collects the output data or results generated during each iteration of the loop and aggregates them into a single output port.

After the completion of the loop iterations, the **Loop End** node outputs the aggregated data or results, which can then be further processed or utilized by subsequent nodes outside the loop. It essentially consolidates the outputs generated during the loop iterations into a single dataset or result, providing a way to continue the workflow beyond the loop's execution.

Here are the inputs and outputs table for this node:

| Node Input        |      Node Output      |   Symbol    |
|:------------------|:---------------------:|:-----------:|
| Chunked Table     |     Chunked Table     | Black Arrow | 
