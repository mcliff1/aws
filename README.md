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

contains some serverless code
* ref:  building a sls dev environment - setting up credential


