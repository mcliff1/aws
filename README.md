# AWS
Collection of AWS Cloud resources

The *cfn-ec2workstation.json* Cloud Formation template will build out a Serverless workstation with NodeJS, NPM, SLS, and REACT frameworks install. You MUST define the parameters **myKeyPair** (name of your SSH Key to access the instance), and optionally **stage** (dev or prod) and **myDomain** (if you have a hosted domain will set a convenience URL *bot-{stage}.{domainname}*) 

<code>
aws cloudformation create-stack --stack-name <stackName> --template-body file://cfn-ec2workstation.json --parameters ParameterKey=myKeyPair
</code>

## Serverless

Frameworks with API Gateway/Lambda
* simpleservice - builds a generic Lambda function and API gateway for POST to /; logs and echos both the event and context objects
* urlshortener - service to take a link, create a short-link and store in DynamoDB
* linklist - provides a framework for serverless list of links with comments uses Cognito, CloudFront, DynamoDB
* staticweb - provides framework to host S3 content behind a provided domainname
* slsweb - provides framework for serverless web (with Route 53, CloudFront, ...)

contains some serverless code
* ref:  building a sls dev environment - setting up credential

**SLSWEB**
----
This project implements a Stack that will deploy a fully functional serverless website. Builds evertyhing in _us-east-1_ region (CloudFront ACM certs must be there).


To fully deploy this (we assume we have some GIT Repo or code base to deploy as web content)  Building this I set my content in *https://github.com/mcliff1/acg-react*

Steps to build
1 create a serverless workstation (if you don't have one)
From AWS CLI
`aws cloudformation create-stack --stack-name <stackName> --template-body file://cfn-ec2workstation.json --parameters ParameterKey=myKeyPair`
From AWS Console - use `cfn-ec2workstation.json` requires a KeyPair, optionally can add a domainname to set a convenince URL _sls-{region}.{domainname}_

1 Check out this Git Repository and change into the <code>slsweb</code> directory
1 **TODO** enter required configuration
   * domainname
   
1 Run `sls deploy` and it will deploy entire stack


