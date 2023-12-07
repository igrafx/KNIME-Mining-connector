VERSION=5.1


#1 - Create before a personal token at https://github.com/settings/tokens 
#2 - login to ghcr.io with your new token 
#    echo mytoken | docker login ghcr.io -u myusername --password-stdin
build_bundler:
	docker buildx build --platform linux/amd64,linux/arm64 -t  ghcr.io/igrafx/knimebundle_builder:1.0.0 --build-arg VERSION=$(VERSION) --rm -f ./igrafx_extension/build/Dockerfile-bundlebuilder --push . 

build:
	rm -rf ./igrafx_extension/releases/5.1
	docker run -v //$(shell pwd)/igrafx_extension:/extension -v //$(shell pwd)/igrafx_extension/releases/5.1:/release ghcr.io/igrafx/knimebundle_builder:1.0.0

