# House price prediction tool

A house price prediction tool for predicting house prices from existing or new data.

## Summary

A house price prediction tool for predicting house prices from past data using linear regression. House price data can be existing or fetched from the internet.

## Background

This project originated from a course exercise and developing that into further to create a useful program that uses artificial intelligence methods to make predictions and fetches data from the internet for those methods to use. The goal is to learn how to use the tools in practical real life situations.

In the first version the program uses data from a csv file as the learning data. In the file each line represents data for one house. Then user can input data of the house they want to make prediction of or use example data.

Example data found in the code and csv-file have been found from a property selling website during august 2022. They are shown here only for example purposes.

## How is it used?

Before running the program you have to install required libraries. You can find the requirements in requirements-file or install with ``pip install -r requirements.txt``. To install all requirements including development requirements use command ``pip install -r requirements-dev.txt``.

You can run the program on command line with ``python house_price_prediction_tool.py`` from the project's main directory. The program asks for data to use in the prediction. Choose the option you want to use.

## What next?

Develop the program further and add more features to it.
* Get data automatically from the internet using Robot Framework.
* Use a database instead of a csv-file.

## Acknowledgments

* Original inspiration from exercises in the Building AI -course.
* Do not use code, images, data etc. from others without permission.
