# AWS Resources
Collection of Amazon Web Services Cloud resources and Utilities

### Contents
* [Cloud Formation](#Cloud_Formation)
* [VPC](#vpc)
* [References](#references)

## Cloud Formation

These templates are based natively in Cloud Formation, each on should have a clearly defined **Parameters** section and **Outputs** section.
* [ec2-slsworkstation.json](#SLS_Workstation) - creates EC2 REACT/SLS Dev workstation in the selected VPC and Subnet
* [vpc.json](#VPC) - creates a VPC in the region imported into with public and private subnets in 3 availability zones
* [bastion.json](#Bastion) - adds a bastion host (uses vpc.json)
* [rds-snapshot.json](#RDS_Snapshot) - restores a RDS database from snapshot (uses vpc.json)
* [rds-postgres.json](#RDS_Postgres) - creates a new RDS PostgreSQL database (uses vpc.json)


#### SLS Workstation
<table width="100%">
<tr><th><a href="#">ec2-slsworkstation.json</a></th></tr>
<tr><td>
The <i>cfn-ec2workstation.json</i> Cloud Formation template will build out a Serverless workstation with NodeJS, NPM, SLS, and REACT frameworks install.


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
<li>VPC Stack Name - referenced by other stacks</li>
<li>Project - used to Tag associated resources</li>
<li>VPC Subnet IPv4 CIDR range</li>
<li>Public Subnet 1 IPv4 CIDR range</li>
<li>Public Subnet 2 IPv4 CIDR range</li>
<li>Public Subnet 3 IPv4 CIDR range</li>
<li>Private Subnet 1 IPv4 CIDR range</li>
<li>Private Subnet 2 IPv4 CIDR range</li>
<li>Private Subnet 3 IPv4 CIDR range</li>
</ol>
<h6>Outputs</h6>
<ul>
<li><i>{StackName}-VpcId</i></li>
<li><i>{StackName}-PublicSubnet1Id</i></li>
<li><i>{StackName}-PublicSubnet2Id</i></li>
<li><i>{StackName}-PublicSubnet3Id</i></li>
<li><i>{StackName}-PrivateSubnet1Id</i></li>
<li><i>{StackName}-PrivateSubnet2Id</i></li>
<li><i>{StackName}-PrivateSubnet3Id</i></li>
<li><i>{StackName}-TopicArn</i> SNS topic that can be used for events in this VPC</li>
</ul>
<h6>TODO</h6>
set up [VPC end points](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-endpoints.html); also what kind of termination protection/monitoring framework
</td></tr>
</table>




#### Bastion
<table width="100%">
<tr><th><a href="https://github.com/mcliff1/aws/blob/master/bastion.json">bastion.json</a></th></tr>
<tr><td>
The <i>bastion.json</i> Cloud Formation template will build create a bastion host on a VPC from the template.

<h6>Create Details</h6>
Creates EC2 instance and security group, the new security group allows connectivity from outside the VPC, the instance also gets the security group that allows internal access to all resources (private and public) in the specified VPC.

<h6>Requires</h6>
[VPC.json](#vpc)
<h6>Parameters</h6>
<ol>
<li>Stack Name - referenced by other stacks</li>
<li>Project - used to Tag associated resources</li>
<li>VPC StackName</i> - from <a href="#VPC">VPC</a> stack</li>
<li>Network to allow SSH access from</li>
<li>Key Pair to use for SSH access</li>
<li>Update Route53 -<b>TODO not implemented</b></li>
<li>Instance Type</li>
</ol>
<h6>Outputs</h6>
<h6>TODO</h6>
<ul>
<li>setup EIP (it's free as long as VM is running)</li>
<li>rename export name of internal access security group</li>
<li>add the DNS update</li>
</ul>
</td></tr>
</table>


#### RDS Snapshot
<table width="100%">
<tr><th><a href="#">rds-snapshot.json</a></th></tr>
<tr><td>
The *rds-snapshot.json* Cloud Formation template will build create a RDS instance in the VPC, from a snapshot.

<h6>Create Details</h6>
Can restore any RDS DB instance

<h6>Parameters</h6>
<ol>
<li>Stack Name - referenced by other stacks</li>
<li>Project - used to Tag associated resources</li>
<li>VPC StackName</i> - from <a href="#VPC">VPC</a> stack</li>
<li>ARN of the snapshot</li>
<li>Update Route53 -<b>TODO not implemented</b></li>
<li>Instance Type</li>
<li>AutoMinorVersionUpgrade</li>
<li>MultiAvailabilityZone</li>
<li>TcpPort</li>
</ol>
<h6>Outputs</h6>
<ol>
<li><i>{StackName}-DbId</i></li>
<li><i>{StackName}-DbHost</i></li>
<li><i>{StackName}-DbPort</i></li>
</ol>
</td></tr>
</table>




#### RDS Postgres
<table width="100%">
<tr><th><a href="#">rds-postgres.json</a></th></tr>
<tr><td>
The *rds-postgres.json* Cloud Formation template will build create a PostgreSQL instance in the VPC.

<h6>Create Details</h6>
Builds a new RDS PostgreSQL database in the Private Subnets of the VPC.

<h6>Parameters</h6>
<ol>
<li>Stack Name - referenced by other stacks</li>
<li>Project - used to Tag associated resources</li>
<li>VPC StackName</i> - from <a href="#VPC">VPC</a> stack</li>
<li>Update Route53 -<b>TODO not implemented</b></li>
<li>Instance Type</li>
<li>AllocatedStorage</li>
<li>AutoMinorVersionUpgrade</li>
<li>MultiAvailabilityZone</li>
<li>DbName</li>
<li>DbUser</li>
<li>DbPassword</li>
<li>MultiAvailabilityZone</li>
<li>DbVersion</li>
<li>TcpPort</li>
</ol>
<h6>Outputs</h6>

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


## References
[back to top](#contents)

* [AWS Bastion Host](https://docs.aws.amazon.com/quickstart/latest/linux-bastion/architecture.html)
