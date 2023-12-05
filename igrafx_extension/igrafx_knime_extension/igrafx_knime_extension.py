import logging
import knime.extension as knext
import pandas as pd
import igrafx_mining_sdk as igx
import tempfile
import time

LOGGER = logging.getLogger(__name__)


igx_category = knext.category(
    path="/community",
    level_id="igrafx_extension",
    name="iGrafx Extension",
    description="The iGrafx Extension for Knime.",
    icon="icons/igx_logo.png",
)

@knext.node(name="iGrafx API Connection", node_type=knext.NodeType.OTHER, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the component.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the component.")
class iGrafxAPINode:
    """Node to connect to the iGrafx API.
    The iGrafx API Connection component serves as the gateway to establish a seamless connection with the iGrafx API. By providing vital credentials such as the Workgroup ID, Workgroup Private Key, API URL, and Authentication URL, this component enables users to access and utilize the iGrafx API and SDK functionalities within the KNIME environment.

    Key features of the iGrafx API Connection component include:

    1. Authentication Configuration: Input fields for Workgroup ID, Workgroup Private Key, API URL, and Authentication URL, allowing users to securely authenticate their access to the iGrafx API.

    2. Seamless Integration: Facilitates the integration of iGrafx API and SDK capabilities directly into KNIME workflows, ensuring efficient data transfer and interaction with the iGrafx platform.

    3. Essential Connectivity: An essential prerequisite for leveraging iGrafx API features within KNIME, enabling users to perform various operations, such as data retrieval, analysis, and interaction with iGrafx resources.

    The iGrafx API Connection component acts as a foundational element, empowering users to harness the full potential of the iGrafx API and SDK functionalities within the KNIME analytics platform, enabling seamless data flow and interaction with iGrafx resources.

    """

    # Define parameters for iGrafx API connection
    workgroup_id = knext.StringParameter("Workgroup ID", "The ID of the workgroup You are working with.")
    workgroup_key = knext.StringParameter("Workgroup Key", "The Private Key of the workgroup you are working with.")
    api_url = knext.StringParameter("API URL", "The URL of the iGrafx API platform you are using.")
    auth_url = knext.StringParameter("Authentication URL", "The authentication URL of the iGrafx platform.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Connecting to iGrafx API")

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

@knext.node(name="iGrafx Project Creation", node_type=knext.NodeType.OTHER, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the component.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the component.")
class iGrafxProjectCreationNode:
    """Node to create an iGrafx project.
    The iGrafx Project Creation component in KNIME facilitates the seamless creation of projects within your iGrafx Workgroup. By utilizing this component, users can efficiently generate new projects by providing  a project name and description.

    Key Features:

    - Effortless Project Setup: Streamline the process of creating projects in your iGrafx Workgroup directly within KNIME.

    - Customizable Project Details: Specify a unique project name and description, tailoring each project to its intended purpose or scope.

    - Enhanced Workflow Control: Enable efficient management of projects by initiating them directly from your KNIME workflow.

    With this component, users gain the ability to integrate project creation tasks seamlessly into their KNIME workflows, ensuring smoother project initiation and management within the iGrafx environment.
    """

    # Define parameters for project creation
    project_name = knext.StringParameter("Project Name", "The name of the project you want to create.")
    project_description = knext.StringParameter("Project Description", "The description of the project you want to create.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Creating iGrafx Project")
        

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


@knext.node(name="iGrafx Column Mapping Status", node_type=knext.NodeType.SINK, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the component.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the component.")
class ColumnMappingStatusNode:
    """Node to check if a column mapping exists in the project.
    The Column Mapping Status component plays a pivotal role in assessing the presence or absence of a column mapping within a specified project within the iGrafx Workgroup environment.

    Key Features:

    - Mapping Assessment: This component verifies the existence of a column mapping within the specified project.

    - Boolean Output: Outputs a Boolean status, indicating whether a column mapping is present (True) or absent (False) in the designated project.

    - Validation Functionality: Allows users to confirm the availability of column mapping, assisting in decision-making for subsequent actions or processes within the workflow.

    By providing a clear status regarding the existence of column mapping in the specified project, the Column Mapping Status component empowers users to make informed decisions based on the presence or absence of the column mapping within the iGrafx Workgroup project.
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


@knext.node(name="iGrafx File Upload", node_type=knext.NodeType.MANIPULATOR, icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table", description="A Table Input that allows users to provide or feed data (CSV or other) into the component.")
@knext.output_table(name="Output Table", description="A Table Output that provides data (CSV or other) out of the component.")
class iGrafxFileUploadNode:
    """Node to upload a CSV file to the iGrafx platform.
    The Mining File Upload component serves as a pivotal tool within the KNIME environment, enabling users to seamlessly upload files to the iGrafx platform. By providing essential parameters such as the Project ID, Column Mapping in JSON format, and the Workgroup Object, users can establish a secure connection to the iGrafx API and transfer files efficiently.

    Key Features:

    - Efficient File Upload: Simplifies the process of uploading files to the iGrafx platform directly from KNIME, ensuring a streamlined workflow.

    - Project ID Integration: Allows users to specify the target project by providing the unique Project ID, ensuring that the uploaded files are associated with the correct project.

    - Column Mapping Support: Accommodates the transmission of column mapping details in JSON format, facilitating structured and organized data transfer.
    
    - Workgroup Object Connectivity: Establishes a secure connection to the iGrafx API by utilizing the Workgroup Object, ensuring authentication and access permissions.

    This component empowers users to seamlessly integrate file upload functionalities into their KNIME workflows, enabling efficient data transfer and synchronization with the iGrafx platform. By leveraging this component, users can ensure the accurate and secure uploading of files while maintaining structured data organization within the iGrafx ecosystem.
    """
    # Define parameters for file upload
    column_dict = knext.StringParameter("Column Mapping", "The column mapping of the file you want to upload in JSON format.")
    given_project_id = knext.StringParameter("Project ID", "The ID of the project you want to upload the file to.")
    chunk_size = knext.IntParameter("Number of Rows per Chunk", "The number of rows to process at a time", 500, min_value=0)


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

        my_project.reset()
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

            # Wait for the upload to complete
            time.sleep(180)

            exec_context.flow_variables["chunk_size"] = chunk_size

        # Return input data as output
        return input_data
