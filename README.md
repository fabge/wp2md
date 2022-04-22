# Title



[![CI](https://github.com/outerbounds/wp2md/actions/workflows/main.yml/badge.svg)](https://github.com/outerbounds/wp2md/actions/workflows/main.yml)

# wp2md

> Convert Wordpress Posts To Markdown

## Install

`pip install wp2md`

## Usage

`wp2md` is a simple command line tool.

```python
!wp2md -h
```

    usage: wp2md [-h] [--baseurl BASEURL] [--dest_path DEST_PATH]
                 [--dest_file DEST_FILE]
                 id
    
    Convert A wordpress post into markdown file with front matter.
    
    positional arguments:
      id
    
    optional arguments:
      -h, --help             show this help message and exit
      --baseurl BASEURL      the baseurl that corresponds to the wp api (default:
                             https://outerbounds.com/wp-json/wp/v2/posts)
      --dest_path DEST_PATH  The path to save the markdown file to (default: .)
      --dest_file DEST_FILE  Optional, if not given defaults to the slug indicated
                             in wordpress


## Example

To convert a wordpress post to markdown, you will have to have to have two pieces of information:

1. The url for the api.  This is `<your_site>/wp-json/v2/posts`, for example `https://outerbounds.com/wp-json/wp/v2/posts`.  Note: _This is [the api route to retrieve a single WP post](https://developer.wordpress.org/rest-api/reference/posts/#retrieve-a-post)._

2. The `post id` you wish to convert to markdown. The post id can be extracted from wordpress edit url, for example the id for `https://outerbounds.com/wp-admin/post.php?post=220&action=edit` is `220`.

For example, we can generate the markdown for the notebooks card post, which has an id of `220` as follows:

```python
!wp2md 220
```

    Writing: notebooks-in-production-with-metaflow.md


The generated markdown looks like this:

```python
!cat notebooks-in-production-with-metaflow.md
```

    ---
    title: "Notebooks In Production With Metaflow"
    date: "2022-02-09T22:59:06"
    image: "https://outerbounds.com/wp-content/uploads/2022/02/Screen-Shot-2022-02-09-at-12.45.20-pm-1024x525.png"
    slug: "notebooks-in-production-with-metaflow"
    ---
    
    
    By Hamel Husain
    
    
    *Learn how to use notebooks in production ML workflows with a new Metaflow feature*
    
    
    When building production-ready machine learning systems, it is critical to monitor the health and performance of those systems with reports and visualizations. Furthermore, allowing for rapid debugging and interactive introspection is critical when workflows fail or do unexpected things. Jupyter notebooks have often been a preferred tool of data scientists for these tasks of visualization, exploration, debugging, and rapid iteration.  Ironically, many production systems do not integrate appropriately with notebooks, which can significantly frustrate progress on these tasks.
    
    
    Indeed, in the field of data science tooling, one of the most [hotly-contested](https://mlops.community/jupyter-notebooks-in-production/) questions is whether notebooks are suitable for production use. We believe that tools should strive to meet data scientists where they are instead of forcing them to adapt approaches from other disciplines not suited to their needs. This is why we are excited to introduce **Notebook Cards**, which allow data scientists to use notebooks for visualizing and debugging production workflows and help to bridge the MLOps divide between prototype and production. This allows data scientists to safely use notebooks for parts of their production workflows, without having to refactor code to conform to a different development environment. 
    
    
    With notebook cards, Metaflow orchestrates notebook execution in a reproducible manner without compromising the integrity of your workflows.
    
    
    ![](https://lh4.googleusercontent.com/-8XLZezB4E7s64BQcu-KTZO0VWh4VyKXpNhVwzSqPSgrAC_3qu62OZ-fleSr5mGRqPYTcEm5ed_ZKx8o6W0o2JIQea1kCemhuX5cZMMZRRtumGi0yf0mIp3DJWvDzKGpUR9GP8ug)A card rendered directly from a Jupyter Notebook in the [Metaflow GUI](https://netflixtechblog.com/open-sourcing-a-monitoring-gui-for-metaflow-75ff465f0d60).
    
    ### From notebooks to production machine learning
    
    
    [Metaflow](https://docs.metaflow.org/) is an ergonomic Python framework created at Netflix for building production ML systems. The data team at Netflix is also famous [for notebook innovation](https://netflixtechblog.com/notebook-innovation-591ee3221233) in data science workflows.  This notebook innovation was revolutionary because it provided mechanisms to integrate notebooks into production data science workflows by providing the [following features](https://netflixtechblog.com/scheduling-notebooks-348e6c14cfd6):
    
    
    ![](https://lh5.googleusercontent.com/SANnJj9aVoAToY6DbwTWkSZzfifaLw5EFziI9xKmG5-66Fh3kCyNeSLJmfkYVVr0dDaSX4xYRImOQT5U4KfvxSndEk2C1mpXPX12tIwFSDR86KTTBWu1ryLGT01HWrvtYU3qfVA1)
    There are many ways to use notebooks in production-ready ML applications, ranging from using notebooks as a complete [software development environment](https://nbdev.fast.ai/) to using notebooks as [reporting, visualization, and debugging tools](https://netflixtechblog.com/scheduling-notebooks-348e6c14cfd6), and [these are key questions in the MLOps space](https://outerbounds.com/blog/mlops-vs-devops/).  The features demonstrated in this post focus on the latter but do not preclude the former.  We think notebooks are great reporting and visualization tools because:
    
    
    * Notebooks allow data scientists to use tools they are very familiar with, including very mature visualization libraries to create visualizations that are appropriate for the problem at hand, allowing for faster iteration.
    * There is no need to push data into another system like Looker or Tableau for multi-stakeholder consumption.
    * You can author interactive visualizations with tools like Altair and Bokeh.
    * Notebooks can also offer a convenient debugging environment for your Metaflow workflows, as you can [use notebooks to interactively inspect the result of your workflows](https://docs.metaflow.org/metaflow/debugging#inspecting-data-with-a-notebook).
    
    
    **This is why we created the** [**notebook card**](https://github.com/outerbounds/metaflow-card-notebook)**, a** [**Metaflow card**](https://outerbounds.com/blog/integrating-pythonic-visual-reports-into-ml-pipelines/) **that allows you to**:
    
    
    * Access data from any step in your DAG so you can visualize it or otherwise use it to generate reports in a notebook.
    * Inject custom parameters into your notebook for execution.
    * Ensure that notebook outputs are reproducible.
    * Keep the resulting notebooks versioned and organized automatically.
    * Isolate notebook-based reporting from the other business logic, making sure that errors in the notebook cannot cause the workflow to fail.
    * Render your notebooks as reports or model cards that can be embedded in various apps.  Notebook Cards generated from a flow are shareable directly from the [Metaflow GUI](https://netflixtechblog.com/open-sourcing-a-monitoring-gui-for-metaflow-75ff465f0d60).
    * Run notebook(s) programmatically in your Metaflow DAGs. With the notebook card, you can automatically inject notebooks with the run\_id, flow\_name, and task\_id so that users can debug workflows immediately upon a failure in your workflow.
    
    
    Additionally, you can use all of the features of Metaflow to manage the execution of notebooks, for example:
    
    
    * [Managing dependencies](https://docs.metaflow.org/metaflow/dependencies) (e.g., @conda)
    * [Requesting compute](https://docs.metaflow.org/metaflow/scaling) (e.g., @resources)
    * [Parallel execution](https://docs.metaflow.org/metaflow/basics#foreach) (e.g., foreach)
    
    
    Crucially, this feature works equally on a laptop during prototyping as well as when deployed to [a cloud-based production environment](https://docs.metaflow.org/going-to-production-with-metaflow/scheduling-metaflow-flows). Traditionally notebooks have been hard to deploy into production, necessitating a separate solution for prototyping and production, causing unnecessary busywork for the data scientist.  
    
    
    Notebook cards allow you to use notebooks as reporting, visualization, and debugging tools. For example, let’s say that you wanted to visualize model performance metrics, feature importance, hyperparameter tuning, and partial dependence plots in your notebook. You can do so! Note that these are just examples of many different visualizations you could build:
    
    
    ![](https://lh6.googleusercontent.com/y5Qfu8F8MWrOtR7693B9JKraTXNKQQeRMNArTJ2_6vqaJb54YDkGEZ1bM67s4sXWwtzwSRKHSU0g6U04iaywfWKZy7MSIrdtB7QVSgqMJTyxYAmbNwxlzaneIxDK6vtPe0PBlWj3)
    The above visualizations were created in a notebook and refreshed with data specific for the pipeline run. The [project’s README](https://github.com/outerbounds/metaflow-card-notebook) has instructions on how to do this.
    
    
    Also note that this is model framework-agnostic and so will work with all types of ML models, whether they be scikit-learn, TensorFlow, PyTorch, or XGBoost.
    
    
    ### How to use notebook cards
    
    
    You can get started with Notebook cards by installing them with pip:
    
    
    
    ```
    pip install metaflow-card-notebook
    ```
    
    Afterward, you need to decorate the appropriate step with @card(type=’notebook’) and assign the nb\_options\_dict variable to the path of the notebook as illustrated in the toy example below:
    
    
    
    ```
    from metaflow import step, current, FlowSpec, card
    from mymodel import train_model
    
    class NBFlow(FlowSpec):
        "A toy example of using the notebook card."
    
        @step
        def start(self):
            # Train a model, save the results in `model_results`
            self.model_results = train_model(...)
            self.next(self.end)
    
        @card(type='notebook')
        @step
        def end(self):
            # eval_model.ipynb can read `self.model_results`
            self.nb_options_dict = dict(input_path='eval_model.ipynb')
    
    if __name__ == '__main__':
        NBFlow()
    
    ```
    
    *This is a toy example of notebook cards.  You can see real examples in the* [*GitHub repo*](https://github.com/outerbounds/metaflow-card-notebook)*.*
    
    
    If you are using the [Metaflow GUI](https://netflixtechblog.com/open-sourcing-a-monitoring-gui-for-metaflow-75ff465f0d60),  you can view a card under the appropriate step(s) in a run (see the above example visualizing model performance metrics). Alternatively, you can view the rendered notebook card locally with the command:
    
    
    
    ```
    python flow.py card view <step name>
    ```
    
    Notebook cards are built on [Metaflow Cards](https://docs.metaflow.org/metaflow/visualizing-results), a general-purpose SDK that allows you to build visual artifacts of your flows.  Notebook cards use [Papermill](https://papermill.readthedocs.io/en/latest/index.html) to programmatically run notebooks as well as inject parameters into the notebook necessary to access data for a Flow.  To enable this behavior, you just need to create a notebook with the cell tag “parameters”.  At runtime, Papermill injects parameters as a new cell as illustrated below:
    
    
    ![](https://lh5.googleusercontent.com/Ug0gWo_tjvED_lw_EAbaEMsvxMz4ByiJxaxY3EJKV4iUyfu_NJjL1zeG_2lzl4EM-EkMNgUsbOPioaLFIpegwN-BfxgPSH8EZy5xtY9Y5Bc3bObvIgFha9noCxzmX5ZJjnBYSSqN)
    With these parameters, we can retrieve data from our flow.  In our example, we saved our training results from our model to self.model\_results in the start step of our flow.  We can use Metaflow’s Task object to retrieve this data as follows:
    
    
    ![](https://lh5.googleusercontent.com/BzBxut9lbxwn-SjuPqu7E3d3SvUhA4QJPCLT52VZd5yW8SwnGjderrGPI425L1Dr8OqO8YT1Kvw4mFB0A6KYUDo64P-JfZhrKsk53m9RdsDFJvrg68wzi3bFg-XZAu6B3FjU1yy8)
    One useful aspect of this workflow is that rendered notebooks can be run after the Flow completes from top-to-bottom.  This is useful for both iterating on Flow dashboards or debugging, as all the information you need to inspect a flow is provided for you.  For a complete walkthrough as well as how you can customize the behavior of notebook cards, [see the project’s README](https://github.com/outerbounds/metaflow-card-notebook).
    
    
    ### Get involved with notebooks in production
    
    
    We recommend visiting the [documentation](https://github.com/outerbounds/metaflow-card-notebook) for this project and studying the [examples](https://github.com/outerbounds/metaflow-card-notebook/tree/main/examples).  Notebook cards are not the only kind of card that we offer.  To understand Metaflow cards more generally, see [this overview](https://docs.metaflow.org/metaflow/visualizing-results).   Furthermore, you can even [create custom card templates](https://docs.metaflow.org/metaflow/visualizing-results/advanced-shareable-cards-with-card-templates) for the community.
    
    
    We would love to see what you create.  Please share your cards, questions, and feedback with us in the [Metaflow Community Slack Channel](http://slack.outerbounds.co), where there are over 900 data scientists and engineers. Lastly, this feature is only the tip of the iceberg of the features we plan to bring to data scientists everywhere.  Sounds interesting?  Come [work with us](https://outerbounds.com/workwithus/).
    
    

