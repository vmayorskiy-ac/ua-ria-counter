#!/bin/bash

TAG=1.4-whiner

git tag -d $TAG
git push --delete origin $TAG
git tag $TAG
git push origin $TAG

