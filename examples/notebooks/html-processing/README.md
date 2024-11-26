# Using Data Prep Kit to Process HTML files

## Step-1: Setup Python Env

See [project README](../../../README.md#create-a-virtual-environment).

Here is a quick setup guide

```bash
conda create -n dpk-html-processing-py311  python=3.11

conda activate dpk-html-processing-py311
```

If on linux do this

```bash
conda install -y gcc_linux-64
conda install -y gxx_linux-64
```

Install modules

```bash
pip install -r requirements.txt 
```


## Step-2: Crawl a website

This step will crawl a site and download HTML files in `output/1-html2parquet` directory

[1_crawl_site.ipynb](1_crawl_site.ipynb)

or use `wget`

`wget --recursive --level=1  --adjust-extension https://thealliance.ai/`

## Step-3: Process HTML files

We will process downloaded HTML files and extract the text as markdown.  The output will be saved in `output/2-markdown` directory

[2_extract_text_from_html.ipynb](2_extract_text_from_html.ipynb)

## Step-4: Save data into DB

We will save the extracted text (markdown) into a vector database (Milvus)

[3_save_to_vector_db.ipynb](3_save_to_vector_db.ipynb)

## Step-5: Query documents

### 5.1 - Setup `.env` file with API Token

For this step, we will be using Replicate API service.  We need a Replicate API token for this step.

Follow these steps:

- Get a **free** account at [replicate](https://replicate.com/home)
- Use this [invite](https://replicate.com/invites/a8717bfe-2f3d-4a52-88ed-1356231cdf03) to add some credit  💰  to your Replicate account!
- Create an API token on Replicate dashboard

Once you have an API token, add it to the project like this:

- Copy the file `env.sample.txt` into `.env`  (note the dot in the beginning of the filename)
- Add your token to `REPLICATE_API_TOKEN` in the .env file.

### 5.2 - Query

Query documents using LLM

[4_query.ipynb](4_query.ipynb)