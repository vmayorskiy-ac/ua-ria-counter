#!/bin/bash

TAG=1.0

git tag -d $TAG
git push --delete origin $TAG
git tag $TAG
git push origin $TAG

