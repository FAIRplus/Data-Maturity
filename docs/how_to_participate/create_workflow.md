---
layout: default
title: Create a workflow
parent: How to Participate
nav_order: 4
---

# Create a workflow

You’re probably here because you want to take your models and put them into a functional workflow so that the workflow 
takes care of running the models. If so, you have come to the right place. 

### A practical example

The goal of this tutorial is to introduce you to the concepts of Nextflow workflows so you 
can create a new workflow by yourself. The process of creating a workflow will be simple, the workflow will only contain
one container, and you will use an existing Nextflow workflow as a template. This existing workflow was developed for the
integration of the [COSIFER](https://github.com/PhosphorylatedRabbits/cosifer) tool into the [VRE](https://vre.ipc-project.bsc.es/openvre/home/) 
and is in the [iPC Workflows for VRE](https://github.com/inab/ipc_workflows/tree/main/cosifer/nextflow) repository.

### Prerequisites

This tutorial assumes that you have [Nextflow](https://www.nextflow.io), [docker](https://docs.docker.com/get-docker/), 
[git](https://git-scm.com/downloads) installed; and your model as a Docker container.

## Nextflow setup

### Clone a GitHub repository

Let's start by setting up a folder to work with, so you can use version control. You must create a clone in your local 
machine of the [iPC-project-H2020](https://github.com/iPC-project-H2020) repository using the next command:

```bash
git clone https://github.com/iPC-project-H2020/dream-challenge.git
```

Next, you need to create a new folder for your workflow within the repository. Our recommendation is to put your model's
name as the name of the folder.

### Files

Every Nextflow workflow requires two main files.

- **nextflow.nf**:
  - The nextflow.nf file contains the main workflow that calls your model script.
  - It doesn't have to be called nextflow.nf, but it is a standard practice to do so.
- **nextflow.config**:
  - The nextflow.config file contains default parameters to use in the nextflow.nf.

Executing the next command will create the `nextflow.nf` and `nextflow.config` files in the folder you specified.

```bash
touch nextflow.nf nextflow.config
```

Make sure you created the files in your folder:

```bash
ls 
nextflow.nf nextflow.config
```

In the next section, you will modify the configuration file provided as a template according to the parameters needed 
for your model to run.

## Nextflow config file

Now, you know that the Nextflow config file is `nextflow.config`. In this section, you will set some default global 
parameters for the workflow: params, manifest and docker; but if you want to add more, follow this [link](https://www.nextflow.io/docs/latest/config.html#config-scopes).

First, copy the following [example](https://github.com/inab/ipc_workflows/blob/main/cosifer/nextflow/nextflow.config) 
into the `nextflow.config` file:

```bash
manifest {
  name = 'COSIFER - COnSensus Interaction Network InFErence Workflow'
  homePage = 'https://github.com/inab/ipc_workflows/tree/main/cosifer/nextflow'
  defaultBranch = 'master'
  mainScript = 'nextflow.nf'
  nextflowVersion = '>=19.10.0'
}

params {
  data_matrix = "${baseDir}/test/data_matrix.csv"
  outputsDir = "${baseDir}/test/results/"
  index_col = ""
  hallmark_gene_sets_file = ""
  sep = "\t"
  samples_on_rows = ""
}

docker {
  runOptions='-u $(id -u):$(id -g)'
  enabled = true
}
```

To adapt the `nextlfow.config` file to your needs, you have to modify the `manifest` and `params` parameters. The 
`docker` parameter does not need to be modified. Some indications are:

- `manifest`: the manifest configuration allows you to define certain required metadata information when publishing 
your workflow to *GitHub*, *Bitbucket*, or *Gitlab*, or when running your workflow. And in this case, you need to 
modify:
  - `name`: the project short name.
  - `homePage`: the project home page URL (e.g. *https://github.com/iPC-project-H2020/dream-challenge/{your-folder-name}*)
  - `defaultBranch`: the Git repository default branch (e.g. main)
  - `mainScript`: the project main script (e.g. nextflow.nf)
- `params`: the params configuration allows you to define parameters to be used in the workflow, usually input and 
output values. To do so, replace and add the parameters needed to run your model from a command line.

In the next section, you will modify the workflow file provided as a template according to the parameters you just 
specified in the configuration file, needed for your model to run.

## Nextflow workflow

The Nextflow workflow file is `nextflow.nf`, and by following the steps below you can create a new workflow and use it 
to run your model with it.

- **Step 1:** [Integrating params from config file](#params).`
- **Step 2:** [Modify the channel](#channel).
- **Step 3:** [Modify the process](#process).
- **Step 4:** [Publish the workflow](#publish).
- **Step 5:** [Execute the workflow](../execute_workflow).

To start, copy the following [example](https://github.com/inab/ipc_workflows/blob/main/cosifer/nextflow/nextflow.nf)
into the `nextflow.nf` file:

```bash
#!/usr/bin/env nextflow

data_matrix = file(params.data_matrix)
outdir = file(params.outputsDir)
result = outdir.mkdirs()
println result ? "Created directory $outdir" : "Cannot create output directory: $outdir"

separator = params.sep
index_col = params.index_col
gmt_filepath = file(params.hallmark_gene_sets_file != '' ? params.hallmark_gene_sets_file : '.empty.')
samples_on_rows = params.samples_on_rows

// We are telling we want the result in this specific subdirectory
// of the outdir
// When empty string is no subdir
cosifer_input = Channel.of([data_matrix,outdir,''])

process cosifer {
  container "tsenit/cosifer:b4d5af45d2fc54b6bff2a9153a8e9054e560302e"

  publishDir "${destdir}", saveAs: { filename -> (destsubdir!='' ? "${destsubdir}/" : '') + filename.minus('resdir/') }

  input:
    tuple matrix, destdir, val(destsubdir) from cosifer_input
    file gmt_filepath
    val separator
    val index_col
    val samples_on_rows

  output:
    path "resdir/**" into cosifer_output

  """
  cosifer -i "${matrix}" "--sep=${separator}" ${index_col!='' ? '--index ' + index_col : ''}  ${gmt_filepath.name != '.empty.' ? '--gmt_filepath ' + gmt_filepath : ''} -o "resdir" ${samples_on_rows ? '--samples_on_rows' : ''}
  """
}

cosifer_output.subscribe{ result -> println "Output:" + result.name }
```

### Step 1. Integrating params from config file <a name="params"></a>

The input and output parameters you defined in the configuration file (`nextflow.config`) must be mentioned on the 
Nextflow workflow file. In the configuration file, you defined and gave values to these parameters and here you only 
need to import them. 

The following code shows how it is imported the parameters in the workflow file in the example:

```bash
data_matrix = file(params.data_matrix)
outdir = file(params.outputsDir)
result = outdir.mkdirs()
println result ? "Created directory $outdir" : "Cannot create output directory: $outdir"

separator = params.sep
index_col = params.index_col
gmt_filepath = file(params.hallmark_gene_sets_file != '' ? params.hallmark_gene_sets_file : '.empty.')
samples_on_rows = params.samples_on_rows
```

**TO CHANGE**: modify, delete, and add the parameters as you defined them in the configuration file.

### Step 2. Modify the channel <a name="channel"></a>

It turns out that Nextflow entries are intrinsically linked to Nextflow channels because the entries are connected 
between channels and processes. 

The example uses the `of` method which allows you to create a channel that broadcasts any sequence of values that are 
specified as parameters to the method, which in this case, are an input file and an output directory. See below:

```bash
// We are telling we want the result in this specific subdirectory
// of the outdir
// When empty string is no subdir
cosifer_input = Channel.of([data_matrix,outdir,''])
```

**TO CHANGE**: rename the channel name and then specify the input or output parameters for your model needs as 
parameters of the channel.

### Step 3. Modify the process <a name="process"></a>

A Nextflow process typically contains four definition blocks, respectively: directives (e.g. container), inputs, 
outputs, and the command line of the script to be executed (between the """"). The syntax is defined as follows:

```bash
process <name> {
  
  [ directives ]
  
  input:
    <input qualifier> <input name> from <channel name>
    <input qualifier> <input name> # optional attribute
  
  output:
    <output qualifier> <output name>
  
  """
  command line of the script to be executed
  """
  
}
```

To adapt the `process` to your needs using the example, first, rename the process and replace the container with your 
own container of the model. Then, modify the process `input`, `output`, and `command line` as follows:

  - **input**: the input defines from which channel the process will receive the input values. In the example, the 
channel is `cosifer_input`, and the input definition starts with an input qualifier (type of data to be received) 
followed by more than one input name from the channel. Additionally, **OPTIONAL** inputs like `gmt_filepath`, can be
specified as a continuation of the input values passed from the channel as we can see in the example:

  ```bash
  input:
    tuple matrix, destdir, val(destsubdir) from cosifer_input
    file gmt_filepath
    val separator
    val index_col
    val samples_on_rows
  ```

**TO CHANGE**: modify the input block to your needs with the name of your channel, that you changed in [step 2](#channel). 
More information and input qualifiers are available [here](https://www.nextflow.io/docs/latest/process.html#inputs). 

  - **output**: the output defines the channel used by the process to send out the results produced. The output 
definitions start with an output qualifier and the output name, followed by `into` and the channel over which the output 
will be sent. In the example, the output named `cosifer_output` is sent to a directory.

````bash
output:
  path "resdir/**" into cosifer_output
````

**TO CHANGE**: rename the output name and adapt the output block to your needs. You can see all the output qualifiers 
available [here](https://www.nextflow.io/docs/latest/process.html#outputs).

  - **command line**: the command line of the script from your model to be executed is interpreted by Nextflow as a 
Bash script by default; but you are not limited, you can use any language you want (e.g. Python, R, Perl, etc.), or 
even mix them. In the example, to run the `cosifer` script is used the following command line:

```bash
cosifer -i "${matrix}" "--sep=${separator}" ${index_col!='' ? '--index ' + index_col : ''}  ${gmt_filepath.name != '.empty.' ? '--gmt_filepath ' + gmt_filepath : ''} -o "resdir" ${samples_on_rows ? '--samples_on_rows' : ''}
````

**TO CHANGE**: add the command line to run your script of the model, passing the input values needed, defined in 
previous steps as parameters.

### Step 4. Publish the workflow <a name="publish"></a>

TBD

