.ONESHELL:
VERSION=5.2

#Doc for bundling: https://docs.knime.com/latest/pure_python_node_extensions_guide/index.html#extension-bundling

ifeq ($(OS),Windows_NT)
# Windows commands
install-builder:
	call conda activate base && conda create -y -n knime-ext-bundling -c knime -c conda-forge knime-extension-bundling=$(VERSION)

build:
	rmdir /s /q .\igrafx_extension\releases
	call conda activate && call conda activate knime-ext-bundling && build_python_extension.bat .\igrafx_extension\igrafx_knime_extension .\igrafx_extension\releases && conda deactivate
else
# macOS commands
install-builder:
	source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate base ; conda create -y -n knime-ext-bundling -c knime -c conda-forge knime-extension-bundling=$(VERSION)

build:
	rm -rf ./igrafx_extension/releases
	source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate knime-ext-bundling ; build_python_extension.py ./igrafx_extension/igrafx_knime_extension ./igrafx_extension/releases ; conda deactivate

endif
