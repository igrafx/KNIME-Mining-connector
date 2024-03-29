import logging
import knime.extension as knext
import igrafx_mining_sdk as igx
import tempfile
import requests as req

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

        file_structure = igx.FileStructure(charset="UTF-8", file_type=igx.FileType.csv)

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
