# How to clean JFrog Artifactory's from unused docker images

## Description
Docker is stored in layers, and each layer has its own checksum value stored. Just like with any other artifact, Artifactory will store the layers based on this value, causing layers to be shared by different deployments; not only between different tags, but also between different images. That means that deleting a layer based on their last download date might cause issues cleaning up. Let's say you are using the REST API or AQL to find old Docker images based on the least used, so you run a query to find all artifacts not downloaded since 3 months ago. If you then delete those artifacts you might still have images that have not been used in a long time, and that are now incomplete. This is because some of the layers might still be used by other tags or images, so those layers did not get deleted. On that line we also want to make it clear that if you delete a layer from one image, it will not be fully deleted as long as other images are referencing it, so what we have to focus on is deleting that image as a whole.

## Resolution
So how to cleanup Docker? We search based on the manifest.json file, which is what will be changed only when that specific image/tag are downloaded/used.

For example the following Python script would look for all manifest.json files that are 60 days old or more and delete the entire image. Be careful when running the script as it will delete files, make sure to test first.

## How to run it locally
   ```Shell
   docker run --rm -e JFROGUSERNAME='xxx' -e JFROGPASSWORD='yyy' -e JFROGLIMIT='"60d"' jfrogcleaner
   ```