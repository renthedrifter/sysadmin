#!/bin/bash

# Ask user for the directory to hash.
#
echo What directory to you want to hash? 

read directory

md5sum $directory/*
