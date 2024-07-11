import logging
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


@knext.node(name="iGrafx Mining API Connection",
            node_type=knext.NodeType.OTHER,
            icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxAPINode:
    """Node to connect to the iGrafx Mining API.
    The iGrafx Mining API Connection node serves as the gateway to establish a seamless
    connection with the iGrafx Mining API.
    By providing vital credentials such as the Workgroup ID, Workgroup Private Key, API URL, and Authentication URL,
     this node enables users to access and utilize the iGrafx API and SDK functionalities within the KNIME environment.

    Key features of the iGrafx Mining API Connection node include:

    1. Authentication Configuration: Input fields for Workgroup ID, Workgroup Private Key, API URL,
    and Authentication URL, allowing users to securely authenticate their access to the iGrafx Mining API.

    2. Seamless Integration: Facilitates the integration of iGrafx API and SDK capabilities directly into
     KNIME workflows, ensuring efficient data transfer and interaction with the iGrafx Mining platform.

    3. Essential Connectivity: An essential prerequisite for leveraging iGrafx API features within KNIME,
    enabling users to perform various operations, such as data retrieval, analysis,
     and interaction with iGrafx Mining resources.

    The iGrafx Mining API Connection node acts as a foundational element,
    empowering users to harness the full potential of the iGrafx Mining API and SDK functionalities within the
    KNIME analytics platform, enabling seamless data flow and interaction with iGrafx resources.

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
        # Get authentication variables from flow variables
        w_id = self.workgroup_id
        w_key = self.workgroup_key
        api_url = self.api_url
        auth_url = self.auth_url

        # Establish connection by creating a Workgroup Object
        wg = igx.Workgroup(w_id, w_key, api_url, auth_url)

        # Define flow variables
        exec_context.flow_variables["wg_id"] = w_id
        exec_context.flow_variables["wg_key"] = w_key
        exec_context.flow_variables["api_url"] = api_url
        exec_context.flow_variables["auth_url"] = auth_url

        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining Project Creation",
            node_type=knext.NodeType.OTHER,
            icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxProjectCreationNode:
    """Node to create an iGrafx Mining  Project.
    The iGrafx Mining Project Creation node in KNIME facilitates the seamless creation of projects within your
    iGrafx Workgroup. By utilizing this node,
    users can efficiently generate new projects by providing a project name and an optional description.

    Key Features:

    - Effortless Project Setup: Streamline the process of creating projects in your iGrafx Workgroup directly within
    KNIME.

    - Customizable Project Details: Specify a unique project name and description, tailoring each project to its
    intended purpose or scope.

    - Enhanced Workflow Control: Enable efficient management of projects by initiating them directly from your
    KNIME workflow.

    With this node, users gain the ability to integrate project creation tasks seamlessly into their KNIME workflows,
     ensuring smoother project initiation and management within the iGrafx environment.
    """

    # Define parameters for project creation
    project_name = knext.StringParameter("Project Name",
                                         "The name of the project you want to create.")
    project_description = knext.StringParameter("Project Description",
                                                "The description of the project you want to create. "
                                                "The description is optional.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Creating iGrafx Mining Project")

    def execute(self, exec_context, input_data):
        # Retrieve project name and description from flow variables
        project_name = self.project_name
        project_description = self.project_description

        if 'column_mapping' in exec_context.flow_variables:
            column_mapping = exec_context.flow_variables["column_mapping"]
        else:
            column_mapping = None

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


@knext.node(name="iGrafx Mining Column Mapping Status",
            node_type=knext.NodeType.OTHER,
            icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class ColumnMappingStatusNode:
    """Node to check if a column mapping exists in the project.
    The Mining Column Mapping Status node plays a pivotal role in assessing the presence or absence
    of a column mapping within a specified project within the iGrafx Workgroup environment.

    Key Features:

    - Mapping Assessment: This node verifies the existence of a column mapping within the specified project.

    - Boolean Output: Outputs a Boolean status, indicating whether a column mapping is present (True) or absent (False)
    in the designated project.

    - Validation Functionality: Allows users to confirm the availability of column mapping, assisting
    in decision-making for subsequent actions or processes within the workflow.

    By providing a clear status regarding the existence of column mapping in the specified project,
    the Column Mapping Status node empowers users to make informed decisions based on the presence or
    absence of the column mapping within the iGrafx Workgroup project.
    """

    # Define parameters for column mapping assessment
    given_project_id = knext.StringParameter("Project ID",
                                             "The ID of the project you want to check the column mapping.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Checking Column Mapping Status")

    def execute(self, exec_context, input_data):
        # Get Workgroup object from the previous node to establish connection
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Retrieve project ID from flow variables or manually set if provided
        if not self.given_project_id:
            if 'new_project_id' not in exec_context.flow_variables:
                raise ValueError("No project ID was given as a parameter or fetched from flow variables.")
            else:
                project_id = exec_context.flow_variables["new_project_id"]
        else:
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


@knext.node(name="iGrafx Mining File Upload", node_type=knext.NodeType.MANIPULATOR, icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxFileUploadNode:
    """Node to upload a CSV file to the iGrafx Mining platform.
    The iGrafx Mining File Upload node serves as a pivotal tool within the KNIME environment,
    enabling users to seamlessly upload files to the iGrafx Mining platform.
    By providing essential parameters such as the Project ID, Column Mapping in JSON format, and the Workgroup Object,
     users can establish a secure connection to the iGrafx Mining API and transfer files efficiently.

    Key Features:

    - Efficient File Upload: Simplifies the process of uploading files to the iGrafx Mining platform directly
    from KNIME, ensuring a streamlined workflow.

    - Project ID Integration: Allows users to specify the target project by providing the unique Project ID,
    ensuring that the uploaded files are associated with the correct project.

    - Column Mapping Support: Accommodates the transmission of column mapping details in JSON format,
    facilitating structured and organized data transfer.

    - Workgroup Object Connectivity: Establishes a secure connection to the iGrafx Mining API by utilizing
    the Workgroup Object, ensuring authentication and access permissions.

    This node empowers users to seamlessly integrate file upload functionalities into their KNIME workflows,
    enabling efficient data transfer and synchronization with the iGrafx Mining platform. By leveraging this node,
    users can ensure the accurate and secure uploading of files while
    maintaining structured data organization within the iGrafx ecosystem.
    """

    column_dict = knext.StringParameter("Column Mapping",
                                        "The column mapping of the file you want to upload in JSON format.")
    given_project_id = knext.StringParameter("Project ID",
                                             "The ID of the project you want to upload the file to.")
    chunk_size = knext.IntParameter("Number of Rows per Chunk",
                                    "The number of rows to process at a time. The default value is 100,000.",
                                    100000,
                                    min_value=0)

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Uploading file to iGrafx")

    def execute(self, exec_context, input_data):

        column_dict = self.column_dict
        chunk_size = self.chunk_size

        # Get Workgroup object from the previous node
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Get DataFrame from input table
        df = input_data.to_pandas()

        # Retrieve project ID from flow variables or manually set if provided
        if not self.given_project_id:
            if 'new_project_id' not in exec_context.flow_variables:
                raise ValueError("No project ID was given as a parameter or fetched from flow variables.")
            else:
                project_id = exec_context.flow_variables["new_project_id"]
        else:
            project_id = self.given_project_id
            exec_context.flow_variables["new_project_id"] = project_id

        my_project = wg.project_from_id(project_id)

        if not self.column_dict:
            if 'column_mapping' not in exec_context.flow_variables:
                raise ValueError("No column mapping was given as a parameter or fetched from flow variables.")
            else:
                column_mapping = exec_context.flow_variables["column_mapping"]
        else:
            column_mapping = self.column_dict
            exec_context.flow_variables["column_mapping"] = column_mapping

        file_structure = igx.FileStructure(charset="UTF-8", file_type=igx.FileType.csv)

        column_mapping = igx.ColumnMapping.from_json(column_mapping)

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
            with open(temp_csv_file_path, 'w', encoding=file_structure.charset) as csv_file:
                csv_file.write(csv_data)

            # Add the file
            my_project.add_file(temp_csv_file_path)

            # Make sure the temp file is closed to be deleted
            temp_csv_file.close()

        exec_context.flow_variables["chunk_size"] = chunk_size

        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining Project Deletion", node_type=knext.NodeType.OTHER, icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxProjectDeletionNode:
    """Node to delete a project in the iGrafx Mining API.
    The iGrafx Mining Project Deletion node allows users to delete a project via the iGrafx Mining API.
    By providing the Project ID, this node sends a request to delete the specified project.

    Key Features:

    - Project Deletion: Deletes the specified project from the iGrafx Mining API.

    - Secure Operation: Requires the Project ID for authorization, ensuring that only authorized users can
    delete projects.
    Furthermore, a project ID must be entered in the node, else the project will not be deleted.

    - Workflow Integration: Seamlessly integrates with KNIME workflows, allowing users to include project deletion
    as part of their data processing pipelines.

    The iGrafx Mining Project Deletion node provides a straightforward way to delete projects,
    offering users flexibility and control over their iGrafx Mining API operations.
    """

    # Project ID to be deleted
    given_project_id = knext.StringParameter("Project ID",
                                             "The ID of the project you want to delete.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Deleting iGrafx Mining Project")

    def execute(self, exec_context, input_data):
        # Check if project ID is given
        project_id = self.given_project_id

        if not project_id:
            raise ValueError("No Project ID provided. Make sure to provide the Project ID for deletion.")

        # Establish connection by creating a Workgroup Object
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Delete the project
        response_project_delete = wg.project_from_id(project_id).delete_project()

        if not response_project_delete.ok:
            raise ValueError(f"Project deletion failed. Status code: {response_project_delete.status_code}, "
                             f"Reason: {response_project_delete.text}")
        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining Project Mapping Info Fetcher", node_type=knext.NodeType.SOURCE,
            icon_path="icons/igx_logo.png", category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxMappingInfoNode:
    """Node to fetch mapping information from the iGrafx Mining API.

    The iGrafx Mining Mapping Info Fetcher node connects to the iGrafx Mining API, enabling users to retrieve mapping
    information for a specified project.
    By providing the Project ID, this node establishes a connection with the iGrafx API and
    fetches details about metrics and dimensions.

    Key Features:

    1. Project Mapping Details: Fetches mapping information, including metrics and dimensions, for the specified
    project.
    It returns the Name, Aggregation, and the database's column name, to name a few, for each dimension and metric.

    2. Seamless Integration: Integrates iGrafx API capabilities directly into KNIME workflows, allowing efficient data
    retrieval and interaction with iGrafx Mining resources.

    3. Dynamic Configuration: Allows users to dynamically provide the Project ID as a parameter or use a predefined
    ID from the flow variables.

    The iGrafx Mapping Info Fetcher node facilitates the retrieval of essential mapping information, providing users
    with insights into metrics and dimensions associated with a specific project.

    """

    # Define the project ID for the project you want to retrieve mapping information
    given_project_id = knext.StringParameter("Project ID",
                                             "The ID of the project for which you "
                                             "want to retrieve mapping information.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Getting Mapping Information")

    def execute(self, exec_context, input_data):

        # Get Workgroup object from the previous node
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Retrieve project ID from flow variables or manually set if provided
        if not self.given_project_id:
            if 'new_project_id' not in exec_context.flow_variables:
                raise ValueError("No project ID was given as a parameter or fetched from flow variables.")
            else:
                project_id = exec_context.flow_variables["new_project_id"]
        else:
            project_id = self.given_project_id
            exec_context.flow_variables["new_project_id"] = project_id

        # Use project ID from String Configuration
        my_project = wg.project_from_id(project_id)

        # Get Mapping Infos of the project
        mapping_infos = my_project.get_mapping_infos()  # returns a json
        exec_context.flow_variables["mapping_infos"] = str(mapping_infos)

        # Raise an error if mapping infos don't exist
        if not mapping_infos:
            raise TypeError("Mapping Infos do not exist")

        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining Project Variant Fetcher", node_type=knext.NodeType.SOURCE,
            icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxProjectVariantNode:
    """Node to fetch project variants via the iGrafx Mining API.

    The iGrafx Mining Project Variant Fetcher node connects to the iGrafx Mining API, allowing users to
    retrieve information about project variants. By specifying the Project ID, users can establish a
    connection with the iGrafx API and retrieve details about project variants, such as names,
    IDs, number of occurrences and associated information.

    Key Features:

    - Dynamic Configuration: Users can dynamically provide the Project ID as a parameter or use a predefined ID from
      flow variables.
    - Pagination Support: The node supports pagination, allowing users to specify the page index and a limit for
    fetching project variants.
    - Search Functionality: Users can filter project variants by name using the optional search query parameter.
    - Seamless Integration: Integrates iGrafx API capabilities directly into KNIME workflows, facilitating efficient
      data retrieval and interaction with iGrafx Mining resources.

    This node empowers users to seamlessly integrate project variant information into their KNIME workflows, enabling
    efficient data access and synchronization with the iGrafx Mining platform.
    """
    # Define parameters to get project variants
    given_project_id = knext.StringParameter("Project ID",
                                             "The ID of the project for which you want to get the variant information.")
    page_index = knext.IntParameter("Page Index",
                                    "The page index for pagination.", )
    limit = knext.IntParameter("Limit",
                               "The maximum number of items to return per page.")
    search = knext.StringParameter("Search Query",
                                   "The search query to filter variants by name (optional).")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Getting Project Variants")

    def execute(self, exec_context, input_data):
        # Fetch project variants using the provided parameters
        page_index_value = self.page_index
        limit_value = self.limit
        search_value = self.search

        # Get Workgroup object from the previous node
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Retrieve project ID from flow variables or manually set if provided
        if not self.given_project_id:
            if 'new_project_id' not in exec_context.flow_variables:
                raise ValueError("No project ID was given as a parameter or fetched from flow variables.")
            else:
                project_id = exec_context.flow_variables["new_project_id"]
        else:
            project_id = self.given_project_id
            exec_context.flow_variables["new_project_id"] = project_id

        my_project = wg.project_from_id(project_id)
        variants_data = my_project.get_project_variants(page_index=page_index_value, limit=limit_value,
                                                        search=search_value)  # returns a json
        exec_context.flow_variables["variants_data"] = str(variants_data)

        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining Completed Cases", node_type=knext.NodeType.SOURCE, icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Output Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
class iGrafxCompletedCasesNode:
    """Node to fetch completed cases for a specified project.

    The iGrafx Mining Completed Cases node connects to the iGrafx Mining API, enabling users to retrieve
    information about completed cases for a specified project. By providing the Project ID and optional search criteria,
    users can establish a connection with the iGrafx API and fetch details about completed cases.

    Key Features:

    - Dynamic Configuration: Users can dynamically provide the Project ID as a parameter or use a predefined ID from
      flow variables.
    - Pagination Support: The node supports pagination, allowing users to specify the page index and limit for fetching
      completed cases.
    - Search Functionality: Users can filter completed cases by case ID using the optional search query parameter.
    - Error Handling: The node includes error handling for scenarios where there is no END CASE rule set or when
      unexpected exceptions occur.

    This node empowers users to seamlessly integrate completed case information into their KNIME workflows, enabling
    efficient data access and synchronization with the iGrafx Mining platform.
    """
    # Define parameters to get project variants
    given_project_id = knext.StringParameter("Project ID",
                                             "The ID of the project you want to retrieve completed cases for.")
    page_index = knext.IntParameter("Page Index",
                                    "The page index for pagination.", )
    limit = knext.IntParameter("Limit",
                               "The maximum number of items to return per page.")
    search_case_id = knext.StringParameter("Search Query",
                                           "The search query to filter cases by ID (optional).")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Getting Completed cases")

    def execute(self, exec_context, input_data):
        # Fetch completed cases using the provided parameters
        page_index_value = self.page_index
        limit_value = self.limit
        search_value = self.search_case_id

        # Get Workgroup object from the previous node
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Retrieve project ID from flow variables or manually set if provided
        if not self.given_project_id:
            if 'new_project_id' not in exec_context.flow_variables:
                raise ValueError("No project ID was given as a parameter or fetched from flow variables.")
            else:
                project_id = exec_context.flow_variables["new_project_id"]
        else:
            project_id = self.given_project_id
            exec_context.flow_variables["new_project_id"] = project_id

        my_project = wg.project_from_id(project_id)

        try:
            completed_cases_data = my_project.get_project_completed_cases(page_index=page_index_value,
                                                                          limit=limit_value,
                                                                          search_case_id=search_value)
            exec_context.flow_variables["completed_cases_data"] = str(completed_cases_data)

        except req.exceptions.JSONDecodeError as je:
            exec_context.flow_variables["completed_cases_data"] = str(je)
            raise ValueError(f"There is no END CASE rule set or there is over filtering being done: {je}")

        except Exception as e:
            # Handle any other unexpected exception
            exec_context.flow_variables["completed_cases_data"] = str(e)
            raise ValueError(f"Unexpected exception: {e}")

        # Return input data as output
        return input_data


@knext.node(name="iGrafx Mining Project Data", node_type=knext.NodeType.SOURCE, icon_path="icons/igx_logo.png",
            category=igx_category)
@knext.input_table(name="Input Table",
                   description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
@knext.output_table(name="Original Table",
                    description="A Table Output that provides data (CSV or other) out of the node.")
@knext.output_table(name="Project Data",
                    description="A Table Output that provides data of the project.")
class iGrafxProjectDataNode:
    """Node to retrieve project data from the iGrafx Mining platform.

    The iGrafx Project Data node connects to the iGrafx Mining API, allowing users to fetch information about a specific
    project. Users can dynamically provide the Project ID as a parameter or use a predefined ID from flow variables.

    Key Features:

    - Dynamic Configuration: Users can dynamically provide the Project ID as a parameter or use a predefined ID from
      flow variables.
    - Data Processing: This node processes the project data. It cleans it, filters it and converts it into a table.

    This node facilitates efficient integration of project data into KNIME workflows, enabling users to synchronize with
    the iGrafx Mining platform seamlessly.
    """
    # Define parameters to get project data
    given_project_id = knext.StringParameter("Project ID",
                                             "The ID of the project you want to retrieve data for.")

    def configure(self, configure_context, input_schema):
        # Set warning during configuration
        configure_context.set_warning("Getting Project Data")

    def execute(self, exec_context, input_data):

        # Get Workgroup object from the previous node
        wg = igx.Workgroup(
            exec_context.flow_variables["wg_id"],
            exec_context.flow_variables["wg_key"],
            exec_context.flow_variables["api_url"],
            exec_context.flow_variables["auth_url"]
        )

        # Retrieve project ID from flow variables or manually set if provided
        if not self.given_project_id:
            if 'new_project_id' not in exec_context.flow_variables:
                raise ValueError("No project ID was given as a parameter or fetched from flow variables.")
            else:
                project_id = exec_context.flow_variables["new_project_id"]
        else:
            project_id = self.given_project_id
            exec_context.flow_variables["new_project_id"] = project_id

        my_project = wg.project_from_id(project_id)

        mapping_infos = my_project.get_mapping_infos()

        # Create a dictionary mapping database column names from mapping infos to their corresponding names
        # We get the database column names and names of the metrics and dimensions
        # which will then be replaced in the dataframe
        column_name_mapping_infos = {item['databaseColumnName']: item['name'] for category in mapping_infos.values()
                                     for item in category}

        # Get and Load the dataframe of the datasource
        df = my_project.nodes_datasource.load_dataframe()

        # Rename the columns based on the mapping
        df = df.rename(columns=column_name_mapping_infos)

        # Check and replace the column name if it matches the pattern "case_+databasecolumnname"
        df.rename(columns=lambda col: f"{column_name_mapping_infos[col[5:]]} (case)" if col.startswith("case_") and col[5:] in column_name_mapping_infos else col, inplace=True)

        # Filter columns based on the condition
        columns_to_keep = [col for col in df.columns if all(keyword not in col for keyword in
                                                            ["loop_path", "graphkey", "processkey",
                                                             "ingestion_timestamp", "linkedToStart", "linkedToEnd"])]

        # Create a new DataFrame with the selected columns
        filtered_df = df[columns_to_keep]

        # Convert the filtered DataFrame to a KNIME Table
        knime_df = knext.Table.from_pandas(filtered_df)

        # Return input data as output
        return input_data, knime_df

    @knext.node(name="iGrafx Mining Column Mapping Fetcher", node_type=knext.NodeType.SOURCE,
                icon_path="icons/igx_logo.png", category=igx_category)
    @knext.input_table(name="Input Table",
                       description="A Table Input that allows users to provide or feed data (CSV or other) into the node.")
    @knext.output_table(name="Output Table",
                        description="A Table Output that provides data (CSV or other) out of the node.")
    class iGrafxColumnMappingFetcherNode:
        """Node to fetch column mapping information from the iGrafx Mining API.

        The iGrafx Mining Column Mapping Fetcher node connects to the iGrafx Mining API, enabling users to retrieve
        column mapping information for a specified project.
        By providing the Project ID, this node establishes a connection with the iGrafx API and fetches details about
        column mappings.

        Key Features:

        1. Column Mapping Details: Fetches column mapping information for the specified project.
        It returns the Name, Aggregation, Index, among others, for each column.

        2. Seamless Integration: Integrates iGrafx API capabilities directly into KNIME workflows, allowing efficient data
        retrieval and interaction with iGrafx Mining resources.

        3. Dynamic Configuration: Allows users to dynamically provide the Project ID as a parameter or use a predefined
        ID from the flow variables.

        The iGrafx Column Mapping Fetcher node facilitates the retrieval of essential column mapping information,
        providing users with insights into the structure and organization of data associated with a specific project.

        """

        # Define the project ID for the project you want to retrieve column mapping
        given_project_id = knext.StringParameter("Project ID",
                                                 "The ID of the project for which you want to retrieve column mapping.")

        def configure(self, configure_context, input_schema):
            # Set warning during configuration
            configure_context.set_warning("Retrieving Column Mapping")

        def execute(self, exec_context, input_data):

            # Get Workgroup object from the previous node
            wg = igx.Workgroup(
                exec_context.flow_variables["wg_id"],
                exec_context.flow_variables["wg_key"],
                exec_context.flow_variables["api_url"],
                exec_context.flow_variables["auth_url"]
            )

            # Retrieve project ID from flow variables or manually set if provided
            if not self.given_project_id:
                if 'new_project_id' not in exec_context.flow_variables:
                    raise ValueError("No project ID was given as a parameter or fetched from flow variables.")
                else:
                    project_id = exec_context.flow_variables["new_project_id"]
            else:
                project_id = self.given_project_id
                exec_context.flow_variables["new_project_id"] = project_id

            # Use project ID from String Configuration
            my_project = wg.project_from_id(project_id)

            # Get Column Mapping of the project
            retrieved_column_mapping = my_project.get_column_mapping()  # returns a json
            exec_context.flow_variables["column_mapping"] = str(retrieved_column_mapping)

            # Raise an error if column mapping infos don't exist
            if not retrieved_column_mapping:
                raise TypeError("Column Mapping does not exist")

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
    auth_username = knext.StringParameter("Authorization Username", "The authorization username to be used for authentication.")
    auth_pwd = knext.StringParameter("Authorization Password", "The authorization password to be used for authentication.")

    def configure(self, configure_context):
        # Set warning during configuration
        configure_context.set_warning("Getting SAP Data")

    def execute(self, exec_context):

        start_date = self.start_date
        end_date = self.end_date
        sap_api_url = self.sap_api_url
        auth_username = self.auth_username
        auth_pwd = self.auth_pwd

        headers = {
            'X-CSRF-TOKEN': 'fetch',
        }

        session = req.Session()
        print(session)
        session.auth = (auth_username, auth_pwd)
        print(session.auth)
        auth_response = session.post(url=sap_api_url, verify=False)
        print(f"Auth Response: {auth_response.status_code} {auth_response.reason}")
        response = session.get(url=sap_api_url, headers=headers, verify=False)
        #should return authentication  token then use token to call routes
        #https://stackoverflow.com/questions/44020439/session-auth-in-python

        print(headers)
        print(response)

        # Access the CSRF token from the response's headers
        csrf_token = response.headers.get('x-csrf-token')
        print(f"CSRF Token: {csrf_token}\n")

        # Print the CSRF token and the Cookie
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

        # Create ProcessSteps elements
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
        }

        # The response of the Post request:
        response = session.post(sap_api_url, headers=headers2, files=files, verify=False)

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
