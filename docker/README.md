# Build Image

This image was designed to be able to bootstrap this GIT into an AWS runtime

## Usage

Assume this is built as 'mcliff/awsbuild'

`docker run --rm mcliff/awsbuild:1.0.0`

## Steps to Build

This was built on an EC2 instance set up that has docker installed.

- Build the image (and tag) `docker build -t foundation .`
- `docker build -t foundation .`

These steps created a **latest** tag;  repeated with `:v0.0.1` appended to the end for a **v0.0.1** tag as well, that is what other build scripts should reference



