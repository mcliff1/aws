# AWS Resources
Collection of Amazon Web Services Cloud resources and Utilities

### Contents
* [SLS workstation](#workstation)
* [VPC](#vpc)

## Cloud Formation

These templates are based natively in Cloud Formation, each on should have a clearly defined **Parameters** section and **Outputs** section.

#### Workstation
<table width="100%">
<tr><th><a href="#">ec2-slsworkstation.json</a></th></tr>
<tr><td>
The <i>cfn-ec2workstation.json</i> Cloud Formation template will build out a Serverless workstation with NodeJS, NPM, SLS, and REACT frameworks install.


<code>
aws cloudformation create-stack --stack-name <stackName> --template-body file://cfn-ec2workstation.json --parameters ParameterKey=myKeyPair
</code>
<h6>Create Details</h6>
<h6>Parameters</h6>
<ol>
<li>myKeyPair</li>
<li>myDomain (optional)</li>
</ol>
<h6>Outputs</h6>
<h6>Public S3 Url</h6>
<ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>

</td></tr>
</table>







#### VPC
<table width="100%">
<tr><th><a href="https://github.com/mcliff1/aws/blob/master/vpc.json">vpc.json</a></th></tr>
<tr><td>
The *vpc.json* Cloud Formation template will build out a VPC with private and public subnets. This provides outputs for subnet and security information that other scripts may leverage. This provides the basis for other templates.

<h6>Create Details</h6>
<h6>Parameters</h6>
<ol>
<li>myDomain (optional)</li>
</ol>
<h6>Outputs</h6>
<ul>
<li><i>{StackName}-VpcId</i></li>
<li><i>{StackName}-PublicSubnet1Id</i></li>
</ul>
<h6>Public S3 Url</h6>
<ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>
<h6>TODO</h6>
set up [VPC end points](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-endpoints.html)
</td></tr>
</table>




#### Bastion
<table width="100%">
<tr><th><a href="https://github.com/mcliff1/aws/blob/master/bastion.json">bastion.json</a></th></tr>
<tr><td>
The <i>bastion.json</i> Cloud Formation template will build create a bastion host on a VPC from the template.

<h6>Create Details</h6>
<h6>Requires</h6>
[VPC.json](#vpc)
<h6>Parameters</h6>
<ol>
<li>VPC Stack Name</li>
<li>myDomain (optional)</li>
</ol>
<h6>Outputs</h6>
<h6>Public S3 Url</h6>
<ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>
<h6>TODO</h6>
<ul>
<li>setup EIP (it's free as long as VM is running)</li>
</ul>
</td></tr>
</table>


#### RDS Postgres
<table width="100%">
<tr><th><a href="#">rds-postgres.json</a></th></tr>
<tr><td>
The *rds-postgres.json* Cloud Formation template will build create a PostgreSQL instance in the VPC.

<h6>Create Details</h6>
<h6>Parameters</h6>
<ol>
</ol>
<h6>Outputs</h6>
<h6>Public S3 Url</h6>
<ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>

</td></tr>
</table>





## Serverless
[back to top](#aws_resources)
These use the <a href="https://serverless.com">Serverless</a> framework, which is designed to provide abstraction to the underlying Cloud provider (AWS in our case).


Frameworks with API Gateway/Lambda
* simpleservice - builds a generic Lambda function and API gateway for POST to /; logs and echos both the event and context objects
* urlshortener - service to take a link, create a short-link and store in DynamoDB
* linklist - provides a framework for serverless list of links with comments uses Cognito, CloudFront, DynamoDB
* staticweb - provides framework to host S3 content behind a provided domainname
* slsweb - provides framework for serverless web (with Route 53, CloudFront, ...)
* restitemapi - a REST API for a generic item

contains some serverless code
* ref:  building a sls dev environment - setting up credential


<table width="100%">
<tr><th><a href="#simpleservice">Simple Service</a></th></tr>
<tr><td>
Creates a Lambda function that is generic.
<h6>Create Details</h6>
<h6>Parameters</h6>
<ol>
</ol>
<h6>Outputs</h6>
<h6>Public S3 Url</h6>
<ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>


</td></tr>
</table>


<table width="100%">
<tr><th><a href="#restitemapi">Item REST API</a></th></tr>
<tr><td>
Creates RESTful endpoint for **item** object, which is a generic *JSON* object.  The key is **ItemKey**, this will automatically be generated if not present.

<a href="https://restdb.io/docs/rest-api#restdb">ref</a>

<h6>API</h6>
<ol>
<li>*GET /item[/{ItemKey}]* - retrieve</li>
<li>*POST /item* - create</li>
<li>*PUT /item/{ItemKey}* - update</li>
<li>*DELETE /item/{ItemKey}* - delete</li>
</ol>

<h6>Create Details</h6>
Creates REST API, appropriate lambda function, and DynamoDB backend.
<h6>Parameters</h6>
<ol>
<li>Domain Name (optional)</li>
</ol>
<h6>Outputs</h6>
<ol>
<li>REST End-Point</li>
<li>DynamoDB Table</li>
</ol>

<h6>Public S3 Url</h6>
<ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>
<h6>TODO</h6>
Add identity stuff (URL signing)
Make the term *item* generic


</td></tr>
</table>



<table width="100%">
<tr><th><a href="#slsweb">SLSWEB</a></th></tr>
<tr><td>
<p>
This project implements a Stack that will deploy a fully functional serverless website. Builds evertyhing in _us-east-1_ region (CloudFront ACM certs must be there).
</p>

<h6>Create Details</h6>

create a serverless workstation (if you don't have one) From AWS CLI
`aws cloudformation create-stack --stack-name <stackName> --template-body file://cfn-ec2workstation.json --parameters ParameterKey=myKeyPair`

1 2 From AWS Console - use `cfn-ec2workstation.json` requires a KeyPair, optionally can add a domainname to set a convenince URL _sls-{region}.{domainname}_


Steps to build


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


<h6>Parameters</h6>
<ol>
</ol>

<h6>Outputs</h6>
<h6>Public S3 Url</h6>
<ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>

<h6>TODO</h6>
Current State (as of 4/30); added fix to set content-type on s3 upload (this was causeing index.html to be downloaded);   needed to manually add the S3 trigger to the Lambda function (some access issues still);  need to manually run the CodeBuild after deploy is completed.


To fully deploy this (we assume we have some GIT Repo or code base to deploy as web content)  Building this I set my content in *https://github.com/mcliff1/acg-react*


Next Steps -
   have SNS Topic message get sent after the build is complete

Start flushing out changes to the REACT side of the app
</td></tr>
</table>
