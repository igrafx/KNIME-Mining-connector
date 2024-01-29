.ONESHELL:
VERSION=5.1

#https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html#extension-bundling

ifeq ($(OS),Windows_NT)
# Windows commands
install-builder:
	call conda activate base && call conda create -n knime-ext-bundling -c knime -c conda-forge knime-extension-bundling=5.1.0

build:
	rmdir /s /q .\igrafx_extension\releases\$(VERSION)
	call conda activate base && call conda activate knime-ext-bundling && build_python_extension.bat .\igrafx_extension\igrafx_knime_extension .\igrafx_extension\releases\$(VERSION) && conda deactivate
else
# macOS commands
install-builder:
	source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate ; conda create -n knime-ext-bundling -c knime -c conda-forge knime-extension-bundling=5.1.0

build:
	rm -rf ./igrafx_extension/releases/$(VERSION)
	source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate knime-ext-bundling ; build_python_extension.py ./igrafx_extension/igrafx_knime_extension ./igrafx_extension/releases/$(VERSION) ; conda deactivate
endif
