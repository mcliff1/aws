# Kaggle Tools for AWS

this folder contains tools to support running Kaggle environments in AWS.


We have

- Stack to create an EBS Volume that will store the users data;
  - creates volume
  - creates launch template for generic AMI to build environment with kaggle python docker image (mounts the volume)

Reference for the [Kaggle/Python](https://github.com/Kaggle/docker-python) Docker ImageId


  #### Kaggle Project Stack
  <table width="100%">
  <tr><th><a href="#">ec2-kaggle.json</a></th></tr>
  <tr><td>
  The <i>ec2-kaggle.json</i> Template builds
  a EBS volume to store the user data accross EC2 instances,
  a EC2 Launch Template to be able to use any type of instances,
  and supporing roles and security groups.

  <h6>Create Details</h6>
  <h6>Parameters</h6>
  <ol>
  <li>myKeyPair</li>
  <li>myDomain (optional)</li>
  <li>VPC</li>
  </ol>
  <h6>Outputs</h6>
  <h6>Public S3 Url</h6>
  <ol><li>https://s3.amazonaws.com/mcliff/cliffconsulting.com/</li></ol>

  </td></tr>
  </table>
