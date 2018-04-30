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


Current State (as of 4/30); added fix to set content-type on s3 upload (this was causeing index.html to be downloaded);   needed to manually add the S3 trigger to the Lambda function (some access issues still);  need to manually run the CodeBuild after deploy is completed.


To fully deploy this (we assume we have some GIT Repo or code base to deploy as web content)  Building this I set my content in *https://github.com/mcliff1/acg-react*

Steps to build

1 create a serverless workstation (if you don't have one)
From AWS CLI
1 1 `aws cloudformation create-stack --stack-name <stackName> --template-body file://cfn-ec2workstation.json --parameters ParameterKey=myKeyPair`
1 2 From AWS Console - use `cfn-ec2workstation.json` requires a KeyPair, optionally can add a domainname to set a convenince URL _sls-{region}.{domainname}_

1 Check out this Git Repository and change into the <code>slsweb</code> directory
1 **TODO** enter required configuration otherwise you will get errors about SSLCert being unknown.
   * domainname
**TODO** have the git repository <code>https://github.com/mcliff1/acg-react</code> hard coded in the CodeBuild configuration
   
1. Run `sls deploy --domainname <domain>` and it will deploy entire stack
1. Run Code Build (from CLI?) aws codebuild ....


Work Process,   once we make an update to the Git repository, then run the CodeBuild process.
Alternatives
 * Use CodePipeline to watch the github source
 * add plug-in to github with AWS credentials to trigger CodeBuild on push


Next Steps - 
   have SNS Topic message get sent after the build is complete

Start flushing out changes to the REACT side of the app

