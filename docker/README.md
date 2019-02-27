# Build Image

This image was designed to be able to bootstrap this GIT into an AWS runtime

### References
[docker entrypoint vs cmd](https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/)


## Usage

Assume this is built as 'mcliff/aws'

`docker run --rm mcliff/aws:1.0.0`


To run locally without anything
`docker build -t local .`
`docker run local`



## Steps to Build

This was built on an EC2 instance set up that has docker installed.

- Build the image (and tag) `docker build -t mcliff1/aws .`
- `docker build -t mcliff/aws .`

These steps created a **latest** tag;  repeated with `:0.0.1` appended to the end for a **v0.0.1** tag as well, that is what other build scripts should reference



