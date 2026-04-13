# iGrafx KNIME Mining Extension

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/igrafx-mining-sdk.svg)](https://pypi.python.org/pypi/igrafx-mining-sdk/)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/igrafx/KNIME-Mining-connector?color=orange)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/igrafx/KNIME-Mining-connector/blob/main/LICENSE)
[![GitHub forks](https://badgen.net/github/forks/igrafx/KNIME-Mining-connector)](https://github.com/igrafx/KNIME-Mining-connector/forks)
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

Extensions are provided "as is" without any support from iGrafx. iGrafx may, in its sole discretion, choose to provide support for an extension.

### Key Features:

- **Effortless Integration**: Easily incorporate this connector into your Knime environment to streamline data transfer to the iGrafx platform.

- **User-Friendly Credentials Input**: With a straightforward interface, users can input their credentials and file information without any hassle.

### Prerequisites:

- **iGrafx Account**: To maximize the benefits of this connector, ensure you have an active iGrafx account. If you don't have one, please contact us to set up your account.
- **Please make sure you have the 5.5 version of Knime as the latest release works with that version.**

For a step-by-step guide on setting up and using the iGrafx KNIME Mining Connector, refer to the detailed tutorial in the [howto.md](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/howto.md) file.

Empower your Knime workflows with seamless data transmission to the iGrafx Mining Platform – explore the potential of the iGrafx KNIME Mining Connector today!

## Installing the iGrafx Extension

**Please make sure you have KNIME Analytics Platform 5.5 or later.**

There are two ways to install the extension.

> **Important for developers:** If you previously configured KNIME for local development (with the `-Dknime.python.extension.config=` line in `knime.ini`), you must comment out or remove that line and restart KNIME before installing from a release. Otherwise KNIME will load the extension twice, causing conflicts or duplicate nodes.

### Method 1: Install from a downloaded release (Recommended)

1. Go to the [Releases page](https://github.com/igrafx/KNIME-Mining-connector/releases) on GitHub.
2. Under the latest release, download the **knime-extension-release.zip** file.
3. Open KNIME. Go to **Help > Install New Software**.
4. Click **Add > Archive...**, browse to the downloaded zip file, give it a name (e.g., "iGrafx Extension"), and click **OK**.
5. Select the iGrafx extension from the list and click **Finish**.
6. Accept the trust dialog, then restart KNIME.

### Method 2: Install from the update site URL

1. Open KNIME. Go to **Help > Install New Software**.
2. Click **Add** and enter:
   - **Name:** iGrafx Extension
   - **Location:** `https://igrafx.github.io/KNIME-Mining-connector/<version>/` (replace `<version>` with the release tag, e.g., `v1.4.0`)
3. Select the iGrafx extension from the list and click **Finish**.
4. Accept the trust dialog, then restart KNIME.

After restarting:
- **Verify install:** Go to **Help > About KNIME > Installation Details > Installed Software** and confirm the iGrafx extension is listed. If it is not, the installation did not complete — try reinstalling.
- **Verify nodes:** Type **iGrafx** in the **Node Repository** search bar. The iGrafx nodes should appear.

For detailed installation instructions with screenshots, refer to the [howto.md](https://github.com/igrafx/KNIME-Mining-connector/blob/dev/howto.md#installing-the-igrafx-extension) file.

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

