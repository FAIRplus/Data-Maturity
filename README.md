This repo contains a working version of a the iPC DREAM challenge website based on Jekyll and [Just The Docs](https://github.com/pmarsceill/just-the-docs) theme. It is hosted on GitHub pages and althought it is already available at https://inab.github.io/ipc-dream-challenge/ it may change or go down without previous notice as it's still work in progress.

## Installation

If you want to contribute to the website we recommend you install [docker](https://docs.docker.com/engine/install/) and [Docker Compose (**Note:** use version 1.x)](https://docs.docker.com/compose/install/) and use the latter to build and deploy the website locally as follows:

    $ docker-compose up

This start a jekyll server that makes the content available at http://0.0.0.0:4000/.

As you make modifications to your theme and to your content, your site will regenerate and you should see the changes in the browser after a refresh, just like normal.

## Just the Docs documentation

Refer to the [Just the Docs documentation](https://pmarsceill.github.io/just-the-docs/) for usage and customisation information.

## Contributing

If you want to add content please create a new branch from this one. Include your name on the branch name, e.g. `just-the-docs-laura` so that it is easier to know who is the branch author. When you are ready to merge your changes open a pull request against this branch.

## License

The theme is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
