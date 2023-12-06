build_bundler:
	docker buildx build --platform linux/amd64,linux/arm64 -t  ghcr.io/igrafx/knimebundle_builder:1.0.0 --rm -f ./igrafx_extension/build/Dockerfile-bundlebuilder --push . 

build:
	docker run -v //$(shell pwd)/igrafx_extension/igrafx_knime_extension:/extension -v //$(shell pwd)/igrafx_extension/releases/5.1:/release
