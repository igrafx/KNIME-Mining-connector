import logging
import os

import knime.extension as knext
import igrafx_mining_sdk as igx
import tempfile
import requests as req
import xml.etree.ElementTree as ET
import pandas as pd
import xml.dom.minidom

LOGGER = logging.getLogger(__name__)


igx_category = knext.category(
    path="/community",
    level_id="igrafx_extension",
    name="iGrafx Mining Extension",
    description="The iGrafx Mining Extension for Knime.",
    icon="icons/igx_logo.png",
)

@knext.node(name="iGrafx Mining API Connection", node_type=knext.NodeType.OTHER, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxAPINode:
    """Node to connect to the iGrafx Mining API.
    The iGrafx Mining API Connection node serves as the gateway to establish a seamless connection with the iGrafx Mining API. By providing vital credentials such as the Workgroup ID, Workgroup Private Key, API URL, and Authentication URL, this node enables users to access and utilize the iGrafx API and SDK functionalities within the KNIME environment.

    Key features of the iGrafx Mining API Connection node include:

    1. Authentication Configuration: Input fields for Workgroup ID, Workgroup Private Key, API URL, and Authentication URL, allowing users to securely authenticate their access to the iGrafx Mining API.

    2. Seamless Integration: Facilitates the integration of iGrafx API and SDK capabilities directly into KNIME workflows, ensuring efficient data transfer and interaction with the iGrafx Mining platform.

    3. Essential Connectivity: An essential prerequisite for leveraging iGrafx API features within KNIME, enabling users to perform various operations, such as data retrieval, analysis, and interaction with iGrafx Mining resources.

    The iGrafx Mining API Connection node acts as a foundational element, empowering users to harness the full potential of the iGrafx Mining API and SDK functionalities within the KNIME analytics platform, enabling seamless data flow and interaction with iGrafx resources.

    """

    # Define parameters for iGrafx Mining API connection
    workgroup_id = knext.StringParameter("Workgroup ID", "The ID of the workgroup You are working with.")
    workgroup_key = knext.StringParameter("Workgroup Key", "The Private Key of the workgroup you are working with.")
    api_url = knext.StringParameter("API URL", "The URL of the iGrafx Mining API platform you are using.")
    auth_url = knext.StringParameter("Authentication URL", "The authentication URL of the iGrafx Mining platform.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Connecting to iGrafx Mining API")

    def execute(self, exec_context, input_data):
        # Get the input data and convert to Pandas DataFrame
        input_df = input_data.to_pandas()

        # Get authentication variables from flow variables
        w_id = self.workgroup_id
        w_key = self.workgroup_key
        api_url = self.api_url
        auth_url = self.auth_url

        # Establish connection by creating a Workgroup Object
        wg = igx.Workgroup(w_id, w_key, api_url, auth_url)

        # Define flow variables
        exec_context.flow_variables["wg_id"] = self.workgroup_id
        exec_context.flow_variables["wg_key"] = self.workgroup_key
        exec_context.flow_variables["api_url"] = self.api_url
        exec_context.flow_variables["auth_url"] = self.auth_url

        # Return input data as output
        return input_data

@knext.node(name="iGrafx Mining Project Creation", node_type=knext.NodeType.OTHER, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxProjectCreationNode:
    """Node to create an iGrafx Mining  roject.
    The iGrafx Mining Project Creation node in KNIME facilitates the seamless creation of projects within your iGrafx Workgroup. By utilizing this node, users can efficiently generate new projects by providing  a project name and description.

    Key Features:

    - Effortless Project Setup: Streamline the process of creating projects in your iGrafx Workgroup directly within KNIME.

    - Customizable Project Details: Specify a unique project name and description, tailoring each project to its intended purpose or scope.

    - Enhanced Workflow Control: Enable efficient management of projects by initiating them directly from your KNIME workflow.

    With this node, users gain the ability to integrate project creation tasks seamlessly into their KNIME workflows, ensuring smoother project initiation and management within the iGrafx environment.
    """

    # Define parameters for project creation
    project_name = knext.StringParameter("Project Name", "The name of the project you want to create.")
    project_description = knext.StringParameter("Project Description", "The description of the project you want to create.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Creating iGrafx Mining Project")
        

    def execute(self, exec_context, input_data):

        # Retrieve project name and description from flow variables
        project_name = self.project_name
        project_description = self.project_description
        
        # Establish connection by creating a Workgroup Object
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Create the project
        new_project_id = wg.create_project(project_name, project_description).id

        # Set project ID in flow variables
        exec_context.flow_variables["new_project_id"] = new_project_id

        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining Column Mapping Status", node_type=knext.NodeType.SINK, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the node.")
class ColumnMappingStatusNode:
    """Node to check if a column mapping exists in the project.
    The Mining Column Mapping Status node plays a pivotal role in assessing the presence or absence of a column mapping within a specified project within the iGrafx Workgroup environment.

    Key Features:

    - Mapping Assessment: This node verifies the existence of a column mapping within the specified project.

    - Boolean Output: Outputs a Boolean status, indicating whether a column mapping is present (True) or absent (False) in the designated project.

    - Validation Functionality: Allows users to confirm the availability of column mapping, assisting in decision-making for subsequent actions or processes within the workflow.

    By providing a clear status regarding the existence of column mapping in the specified project, the Column Mapping Status node empowers users to make informed decisions based on the presence or absence of the column mapping within the iGrafx Workgroup project.
    """

    # Define parameters for column mapping assessment
    given_project_id = knext.StringParameter("Project ID", "The ID of the project you want to check the column mapping.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Checking Column Mapping Status")

    def execute(self, exec_context, input_data):

        # Get Workgroup object from the previous node
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Retrieve project ID from flow variables
        if not self.given_project_id:
            project_id = exec_context.flow_variables["new_project_id"]
        else:
            # If the project ID was manually set, it will be prioritized over the flow variable project ID
            project_id = self.given_project_id
            exec_context.flow_variables["new_project_id"] = project_id

        # Use project ID from String Configuration
        my_project = wg.project_from_id(project_id)

        # Check if column mapping exists in the project
        column_mapping_exists = my_project.column_mapping_exists
        exec_context.flow_variables["column_mapping_exists"] = column_mapping_exists 

        # Raise an error if column mapping doesn't exist
        if not column_mapping_exists:
            raise TypeError("Column Mapping doesn't exist")

        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining File Upload", node_type=knext.NodeType.MANIPULATOR, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxFileUploadNode:
    """Node to upload a CSV file to the iGrafx Mining platform.
    The iGrafx Mining File Upload node serves as a pivotal tool within the KNIME environment, enabling users to seamlessly upload files to the iGrafx Mining platform. By providing essential parameters such as the Project ID, Column Mapping in JSON format, and the Workgroup Object, users can establish a secure connection to the iGrafx Mining API and transfer files efficiently.

    Key Features:

    - Efficient File Upload: Simplifies the process of uploading files to the iGrafx Mining platform directly from KNIME, ensuring a streamlined workflow.

    - Project ID Integration: Allows users to specify the target project by providing the unique Project ID, ensuring that the uploaded files are associated with the correct project.

    - Column Mapping Support: Accommodates the transmission of column mapping details in JSON format, facilitating structured and organized data transfer.
    
    - Workgroup Object Connectivity: Establishes a secure connection to the iGrafx Mining API by utilizing the Workgroup Object, ensuring authentication and access permissions.

    This node empowers users to seamlessly integrate file upload functionalities into their KNIME workflows, enabling efficient data transfer and synchronization with the iGrafx Mining platform. By leveraging this node, users can ensure the accurate and secure uploading of files while maintaining structured data organization within the iGrafx ecosystem.
    """
    # Define parameters for file upload
    column_dict = knext.StringParameter("Column Mapping", "The column mapping of the file you want to upload in JSON format.",)
    given_project_id = knext.StringParameter("Project ID", "The ID of the project you want to upload the file to.")
    chunk_size = knext.IntParameter("Number of Rows per Chunk", "The number of rows to process at a time", 100000, min_value=0)


    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Uploading file to iGrafx")

    def execute(self, exec_context, input_data):

        column_dict = self.column_dict

        # Get Workgroup object from the previous node
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Get DataFrame from input table
        df = input_data.to_pandas()

        # Retrieve the number of rows per chunk
        chunk_size = self.chunk_size

        # Retrieve project ID from flow variables or manually set if provided
        if not self.given_project_id:
            project_id = exec_context.flow_variables["new_project_id"]
        else:
            project_id = self.given_project_id
            exec_context.flow_variables["new_project_id"] = project_id

        if not project_id:
            raise ValueError("No project ID was given")
        
        my_project = wg.project_from_id(project_id)

        file_structure = igx.FileStructure(file_type=igx.FileType.csv)

        column_mapping = igx.ColumnMapping.from_json(column_dict)

        my_project.add_column_mapping(file_structure, column_mapping)


        # Process each chunk and upload the corresponding file
        for i in range(0, len(df), chunk_size):
            # Convert the chunk DataFrame to a CSV string
            chunk_df = df.iloc[i:i + chunk_size]

            # Convert the chunk DataFrame to a CSV string
            csv_data = chunk_df.to_csv(index=False)

            # Create a temporary file and write the CSV data to it
            temp_csv_file = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
            temp_csv_file_path = temp_csv_file.name

            # Write the CSV data to the temporary file
            with open(temp_csv_file_path, 'w') as csv_file:
                csv_file.write(csv_data)

            # Add the file
            my_project.add_file(temp_csv_file_path)

            temp_csv_file.close() #Make sure the temp file is closed to be deleted

            exec_context.flow_variables["chunk_size"] = chunk_size

        # Return input data as output
        return input_data


@knext.node(name="iGrafx SAP Data Fetcher", node_type=knext.NodeType.SOURCE, icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.output_table(name="SAP Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxSAPNode:
    """Node to fetch SAP data from the iGrafx Mining platform.

    The iGrafx SAP Data Fetcher node allows users to fetch detailed information about specific
    SAP data. Users can provide the parameters such as the SAP API URL, the authorization token and the cookie, which will be used to connect to the SAP API and retrieve the data.
    Additionally, users can specify the Start Date and End Date to filter the data within the specified
    date range.
    This node can then directly be connected to other iGrafx nodes for further processing and uploading to the iGrafx platform.

    Key Features:

    - **Data Processing**: The node processes the data by cleaning, filtering, and converting it into a table format.
    - **CSRF Token Handling**: Automatically handles CSRF token fetching and cookie management for API authentication.
    - **XML Generation**: Automatically generates the necessary XML payloads for selection and description to interact with the SAP API, eliminating the need to manually input XML files.

    This node returns a table containing the fetched data. This table is retrieved in XML format, then cleaned and converted into a structured table.
    It facilitates easy data processing and uploading to the iGrafx platform by using the other nodes.

    Please contact us in order to get access to the SAP extension.

    """

    start_date = knext.StringParameter("Start Date", "The date from when you want to retrieve information.",)
    end_date = knext.StringParameter("End Date", "The date until when you want to retrieve information.")
    sap_api_url = knext.StringParameter("SAP API URL", "The URL of the SAP API to be used for data fetching.")
    authorization = knext.StringParameter("Authorization", "The authorization token to be used for authentication.")
    auth_cookie = knext.StringParameter("Cookie", "The cookie to be used for authentication.")

    def configure(self, configure_context):
        # Set warning during configuration
        configure_context.set_warning("Getting SAP Data")

    def execute(self, exec_context):

        start_date = self.start_date
        end_date = self.end_date
        sap_api_url = self.sap_api_url
        authorization = self.authorization
        auth_cookie = self.auth_cookie

        payload = {}
        headers = {
            'X-CSRF-TOKEN': 'fetch',
            'Authorization': authorization,
            'Cookie': auth_cookie
        }

        response = req.request("GET", sap_api_url, headers=headers, data=payload, verify=False)

        # Access the CSRF token from the response's headers
        csrf_token = response.headers.get('x-csrf-token')
        cookie = "SAP_SESSIONID_ER6_800=" + response.cookies.get('SAP_SESSIONID_ER6_800') + "; path=/"

        # Print the CSRF token and the Cookie
        print(f"CSRF Token: {csrf_token}\nCookie: {cookie}")
        print(response)

        # Create the root element of the selection XML
        selection_root_xml = ET.Element("Selection")

        # Create and append FromDate element
        from_date_element = ET.SubElement(selection_root_xml, "FromDate")
        from_date_element.text = start_date

        # Create and append ToDate element
        to_date_element = ET.SubElement(selection_root_xml, "ToDate")
        to_date_element.text = end_date

        # Create and append ReadData element with attributes
        read_data_element = ET.SubElement(selection_root_xml, "ReadData")
        read_data_element.set("change_events", "X")
        read_data_element.set("messages", "")
        read_data_element.set("document_details", "")

        # Convert the XML tree to a string
        selection_xml = ET.tostring(selection_root_xml, encoding='utf-8', method='xml').decode()

        # Create the root element of the description XML
        description_root = ET.Element("Process")

        # Add child elements to the root
        ET.SubElement(description_root, "ID").text = "O2C"
        ET.SubElement(description_root, "Product").text = "ERP"

        # Create the Entities element
        entities_element = ET.SubElement(description_root, "Entities")

        identifiers_element = ET.SubElement(entities_element, "Identifiers")
        ET.SubElement(identifiers_element, "Type").text = "DomVal"
        ET.SubElement(identifiers_element, "Domain").text = "VBTYP"

        leading_entities_element = ET.SubElement(entities_element, "LeadingEntities")
        ET.SubElement(leading_entities_element, "EntityID").text = "B"
        ET.SubElement(leading_entities_element, "EntityID").text = "C"

        # Create ProcessStepsDescr element
        process_steps_element = ET.SubElement(description_root, "ProcessStepsDescr")

        status_element = ET.SubElement(process_steps_element, "Status", default='X')
        data_tables_element = ET.SubElement(status_element, "DataTables")
        data_table_vbuk_element = ET.SubElement(data_tables_element, "DataTable", id='VBUK')
        fields_vbuk_element = ET.SubElement(data_table_vbuk_element, "Fields")
        ET.SubElement(fields_vbuk_element, "Field", id='GBSTK')

        messages_element = ET.SubElement(process_steps_element, "Messages", default='X')
        data_table_nast_element = ET.SubElement(messages_element, "DataTable", id='NAST')
        fields_nast_element = ET.SubElement(data_table_nast_element, "Fields")
        ET.SubElement(fields_nast_element, "Field", id='KAPPL', dom_val_from='TNAPR-KAPPL')
        ET.SubElement(fields_nast_element, "Field", id='OBJKY', source='VBELN')
        ET.SubElement(fields_nast_element, "Field", id='KSCHL', semantic='message_type', dom_val_from='TNAPR-KSCHL')
        ET.SubElement(fields_nast_element, "Field", id='SPRAS')
        ET.SubElement(fields_nast_element, "Field", id='PARNR')
        ET.SubElement(fields_nast_element, "Field", id='USNAM', semantic='user')
        ET.SubElement(fields_nast_element, "Field", id='PARVW', dom_val_from='VBPA-PARVW')
        ET.SubElement(fields_nast_element, "Field", id='ERDAT', semantic='crea_timestamp-date')
        ET.SubElement(fields_nast_element, "Field", id='ERUHR', semantic='crea_timestamp-time')

        # Create ProcessSteps element
        process_steps_element = ET.SubElement(process_steps_element, "ProcessSteps")

        for entity_id, header_table, item_table, change_object_class, kappl_value in [
            ("B", "VBAK", "VBAP", "VERKBELEG", "V1"),
            ("C", "VBAK", "VBAP", "VERKBELEG", "V1"),
            ("J", "LIKP", "LIPS", "LIEFERUNG", "V2"),
            ("M", "VBRK", "VBRP", "FAKTBELEG", "V2")
        ]:
            process_step = ET.SubElement(process_steps_element, "ProcessStep")
            ET.SubElement(process_step, "EntityID").text = entity_id

            executables_element = ET.SubElement(process_step, "Executables")
            for action, mod_type in [("01", "create"), ("02", "change")]:
                executable = ET.SubElement(executables_element, "Executable", mod_type=mod_type)
                ET.SubElement(executable, "Type").text = "TRAN"
                ET.SubElement(executable, "ID").text = f"VA{action}"
                ET.SubElement(executable, "Event").text = "Create" if action == "01" else "Change"

            ET.SubElement(process_step, "HeaderDataTable").text = header_table
            ET.SubElement(process_step, "ItemDataTable").text = item_table
            ET.SubElement(process_step, "ChangeObjectClass").text = change_object_class

            messages_step = ET.SubElement(process_step, "Messages")
            data_table_nast_step = ET.SubElement(messages_step, "DataTable", id='NAST')
            fields_nast_step = ET.SubElement(data_table_nast_step, "Fields")
            ET.SubElement(fields_nast_step, "Field", id='KAPPL').text = kappl_value

        # Create ProcessFlow element
        process_flow_element = ET.SubElement(description_root, "ProcessFlow")
        data_table_vbfa = ET.SubElement(process_flow_element, "DataTable", id='VBFA')
        ET.SubElement(data_table_vbfa, "PredecessorEntity").text = "VBTYP_V"
        ET.SubElement(data_table_vbfa, "SuccessorEntity").text = "VBTYP_N"
        ET.SubElement(data_table_vbfa, "PredecessorHeaderKey").text = "VBELV"
        ET.SubElement(data_table_vbfa, "SuccessorHeaderKey").text = "VBELN"
        ET.SubElement(data_table_vbfa, "PredecessorItemKey").text = "POSNV"
        ET.SubElement(data_table_vbfa, "SuccessorItemKey").text = "POSNN"

        # Create DataTables element
        data_tables_element = ET.SubElement(description_root, "DataTables")

        for id_value, header_table, fields_info in [
            ('VBUK', 'X', [{'id': 'VBELN', 'header_key': 'X'}, {'id': 'GBSTK', 'read_value_texts': 'X'}]),
            ('VBAK', '', [
                {'id': 'VBELN', 'header_key': 'X'}, {'id': 'VBTYP', 'entity_id': 'X'},
                {'id': 'UPD_TMSTMP', 'semantic': 'change_timestamp'},
                {'id': 'ERDAT', 'semantic': 'crea_timestamp-date'}, {'id': 'ERZET', 'semantic': 'crea_timestamp-time'},
                {'id': 'ERNAM', 'semantic': 'crea_user'}, {'id': 'AUART', 'read_value_texts': 'X'}, {'id': 'AUDAT'}
            ]),
            ('VBAP', '', [
                {'id': 'VBELN', 'header_key': 'X'}, {'id': 'POSNR', 'item_key': 'X'}, {'id': 'MATNR'}, {'id': 'MATKL'},
                {'id': 'MEINS'}, {'id': 'NETPR'}, {'id': 'NETWR'}, {'id': 'SMENG'},
                {'id': 'ERDAT', 'semantic': 'crea_timestamp-date'},
                {'id': 'ERZET', 'semantic': 'crea_timestamp-time'}, {'id': 'ERNAM', 'semantic': 'crea_user'}
            ]),
            ('VBRK', '', [
                {'id': 'VBELN', 'header_key': 'X'}, {'id': 'VBTYP', 'entity_id': 'X'}, {'id': 'AEDAT'},
                {'id': 'ERDAT', 'semantic': 'crea_timestamp-date'}, {'id': 'ERZET', 'semantic': 'crea_timestamp-time'},
                {'id': 'ERNAM', 'semantic': 'crea_user'}, {'id': 'FKDAT'}, {'id': 'FKART', 'read_value_texts': 'X'}
            ]),
            ('VBRP', '', [
                {'id': 'VBELN', 'header_key': 'X'}, {'id': 'POSNR', 'item_key': 'X'}, {'id': 'NETWR'}, {'id': 'FKIMG'},
                {'id': 'VRKME'}, {'id': 'MATNR'}, {'id': 'MATKL'}, {'id': 'ERDAT', 'semantic': 'crea_timestamp-date'},
                {'id': 'ERZET', 'semantic': 'crea_timestamp-time'}, {'id': 'ERNAM', 'semantic': 'crea_user'}
            ]),
            ('LIKP', '', [
                {'id': 'VBELN', 'header_key': 'X'}, {'id': 'VBTYP', 'entity_id': 'X'}, {'id': 'AEDAT'},
                {'id': 'ERDAT', 'semantic': 'crea_timestamp-date'}, {'id': 'ERZET', 'semantic': 'crea_timestamp-time'},
                {'id': 'ERNAM', 'semantic': 'crea_user'}, {'id': 'LFDAT'}, {'id': 'LFART', 'read_value_texts': 'X'}
            ]),
            ('LIPS', '', [
                {'id': 'VBELN', 'header_key': 'X'}, {'id': 'POSNR', 'item_key': 'X'}, {'id': 'MATKL'},
                {'id': 'LFIMG'}, {'id': 'VRKME'}, {'id': 'NETPR'}, {'id': 'NETWR'}, {'id': 'MATNR'},
                {'id': 'ERDAT', 'semantic': 'crea_timestamp-date'}, {'id': 'ERZET', 'semantic': 'crea_timestamp-time'},
                {'id': 'ERNAM', 'semantic': 'crea_user'}
            ])
        ]:
            data_table = ET.SubElement(data_tables_element, "DataTable", id=id_value)
            if header_table:
                data_table.set("header_table", header_table)
            fields = ET.SubElement(data_table, "Fields")
            for field_info in fields_info:
                ET.SubElement(fields, "Field", field_info)

        # Convert the tree to a string
        description_xml = ET.tostring(description_root, encoding='utf-8').decode('utf-8')

        # Selection and Description XML have been generated

        # Send the XMls to the SAP API and retrieve the response:
        payload = {}
        files = {
            'selection': ('selection.xml', selection_xml, 'application/xml'),
            'description': ('description.xml', description_xml, 'application/xml')
        }
        headers2 = {
            'X-CSRF-TOKEN': csrf_token,
            'Cookie': cookie
        }

        # The response of the Post request:
        response = req.request("POST", sap_api_url, headers=headers2, data=payload, files=files, verify=False)

        print(f"The response is: {response.text}")

        # Parse the XML Response file
        xml_tree = ET.ElementTree(ET.fromstring(response.text))

        # Retrieve the root element of the XML document.
        root = xml_tree.getroot()

        # Create an empty DataFrame with the desired columns
        columns = ['Case ID', 'Entity ID', 'Entity Name']
        df = pd.DataFrame(columns=columns)

        # Find all XML elements with the tag name 'Case' that are children of the 'Cases'
        case_elements = root.findall('Cases/Case')

        # Iterate over Case elements
        for case_element in case_elements:
            case_id = case_element.attrib['id']

            doc_group_elements = case_element.findall('DocGroup')

            # Iterate over DocGroup elements
            for doc_group_element in doc_group_elements:
                entity_element = doc_group_element.find('Entity')
                document_element = doc_group_element.find('Document')

                entity_id = entity_element.attrib['id'] if entity_element is not None else ""
                entity_name = entity_element.text if entity_element is not None else ""
                document_id = document_element.attrib['id'] if document_element is not None else ""

                event_elements = doc_group_element.findall('.//Header/Events/Event')

                # Check if there are any Event elements
                if not event_elements:
                    # Append a row without Event information
                    df = df.append({
                        'Case ID': case_id,
                        'Entity ID': entity_id,
                        'Entity Name': entity_name,
                        'Document ID': document_id
                    }, ignore_index=True)

                # Iterate over Event elements
                for event_element in event_elements:
                    event_type = event_element.attrib['type']
                    event_ts = event_element.attrib['ts']

                    task_name = f"{event_type} {entity_name}"

                    # Append a new row to the DataFrame
                    df = df.append({'Case ID': case_id,
                                    'Entity ID': entity_id,
                                    'Entity Name': entity_name,
                                    'Document ID': document_id,
                                    }, ignore_index=True)
                    df['Task Name'] = task_name
                    df['Event Type'] = event_type
                    df['Timestamp'] = event_ts

        if 'Timestamp' in df.columns:
            # Execute the line only if 'Timestamp' column exists
            df['Timestamp'] = df['Timestamp'].str.replace(" CET", "")
            # df = df.loc[(df['Timestamp'] >= start_date) & (df['Timestamp'] <= end_date)]

        knime_df = knext.Table.from_pandas(df)

        return knime_df
