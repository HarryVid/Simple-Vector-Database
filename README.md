# Simple Vector Database Example for RAG!

This repository contains a very simple setup of a vector database which can then be used for RAG by LLMs to improve the quality of the output. A full-fledged version of this app is in the works and is coming soon in the form of a Philosophy Bot.

## Project Overview

The project is designed to meet the following key requirements:

- Input PDF document. This example only supports PDFs.
- Convert the PDF into chunks.
- Convert the chunks into embeddings.
- Store the embeddings in a database.
- Enter a query to fetch similar content for the pdf.

## Getting Started

To set up the project locally, follow these steps:

1. Clone this repository to your local machine.
2. Run the provided script `./run.sh` to start the program locally. Make this an executable with chmod. sudo privileges not required.
3. Since this is the example the query needs to be edited in the `pdf_processor.py`. You can change the pdf and the query to match your requirements.

## Project Structure

The project structure is organized as follows:

- `pdf_processor.py`: Contains the main file.
- `requirements.txt`: File listing project dependencies.

## Usage

Once the application is running, follow these steps to use it:

1. Change the pdf file as per your requirements.
2. Update the query in the Python file to fit your needs.
3. Run the docker container to view the output along with the fetched data.

## Notes
1. A stoic philosophy text is taken as an example but the PDF contents can be anything matching any requirements.
2. A GPU could be used for the embedding models but currently, there is no GPU support here as this is just a simple example but could be added and is recommended for bigger projects.
3. Currently this example project only supports a single PDF, but could be easily extended to support multiple PDF documents.
