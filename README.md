# iGrafx KNIME Mining Extension

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/igrafx/KNIME-Mining-connector?color=orange)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/igrafx/KNIME-Mining-connector/blob/main/LICENSE)
[![GitHub forks](https://badgen.net/github/forks/igrafx/mining-python-sdk)](https://github.com/igrafx/KNIME-Mining-connector/forks)
![GitHub issues](https://img.shields.io/github/issues/igrafx/KNIME-Mining-connector?color=)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/igrafx/KNIME-Mining-connector?color=purple)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/igrafx/KNIME-Mining-connector?color=pink)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

***
## Introduction

Welcome to the **iGrafx KNIME Mining Extension** – an open-source application seamlessly integrated with Knime to effortlessly transmit data to the iGrafx Mining Platform.

Powered by the [iGrafx P360 Live Mining SDK](https://github.com/igrafx/mining-python-sdk) and rooted in Python, this connector simplifies the data transfer process, eliminating complexity and enhancing your workflow.

### Key Features:

- **Effortless Integration**: Easily incorporate this connector into your Knime environment to streamline data transfer to the iGrafx platform.

- **User-Friendly Credentials Input**: With a straightforward interface, users can input their credentials and file information without any hassle.

### Prerequisites:

- **iGrafx Account**: To maximize the benefits of this connector, ensure you have an active iGrafx account. If you don't have one, please contact us to set up your account.

For a step-by-step guide on setting up and using the iGrafx KNIME Mining Connector, refer to the detailed tutorial in the [howto.md](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/howto.md) file.

Empower your Knime workflows with seamless data transmission to the iGrafx Mining Platform – explore the potential of the iGrafx KNIME Mining Connector today!

## Installing the iGrafx Extension

To install the **iGrafx Extension** on Knime, open Knime.

Click on the **settings** icon in the top right of the window.

![settings_icon](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/settings_icon.png)

Then, click on the **arrow** next to the **Install/Update** section.

Go to the **Available Software sites** section and click the add button.

![Available_Software](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/images/available_software_5.2.png)

In the window that pops up, make sure the information is as follows:

- Name: iGrafx Extension
- Location: https://raw.githubusercontent.com/igrafx/KNIME-Mining-connector/master/igrafx_extension/releases/5.1

Copy and paste the location in the respective input.

![location](https://github.com/igrafx/KNIME-Mining-connector/blob/master/images/location3.png)

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

If it is not installed this will cause issues with the extension, and you will not be able to use the extension.
Please run ``sudo xcodebuild -license`` from within a Terminal window to review and agree to the **Xcode and Apple SDKs license**.

Congratulations! You can now refer to other sections for details on how to use the nodes.

If you are a developer wishing to contribute, please refer to [this](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/howto.md#using-the-igrafx-mining-knime-extension-as-a-developer) section instead.

You can directly refer to the example if [needed](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/howto.md#the-igrafx-mining-extension-example).

## Documentation

For comprehensive documentation, refer to the [howto.md](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/howto.md) file.

Follow the step-by-step instructions provided in the documentation to seamlessly integrate and explore the capabilities of the component.


## Contributing

We welcome pull requests. If you plan on making major changes, please open an issue first to discuss your proposed modifications. 

For detailed guidelines on contributing, please refer to the [CONTRIBUTING.md](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/CONTRIBUTING.md) file.

## Support

For assistance, reach out to our support team at [support@igrafx.com](mailto:support@igrafx.com).

## Notice

Your feedback and contributions are valuable to us. Feel free to actively participate in enhancing the project.

## License

This Knime iGrafx Extension is licensed under the MIT License. See the [LICENSE](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/LICENSE) file for more details.

